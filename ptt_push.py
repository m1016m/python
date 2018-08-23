import telnetlib
import sys
import time

host = 'ptt.cc'
user = 'Your PTT ID'
password = 'Your PTT Password'



def login(host, user ,password) :
    global telnet
    telnet = telnetlib.Telnet(host)
    time.sleep(1)
    content = telnet.read_very_eager().decode('big5','ignore')
    if "系統過載" in content :
        print ("系統過載, 請稍後再來")
        sys.exit(0)
        

    if "請輸入代號" in content:
        print ("輸入帳號中...")
        telnet.write(user + "\r\n" )
        time.sleep(1)
        print ("輸入密碼中...")
        telnet.write(password + "\r\n")
        time.sleep(1)
        content = telnet.read_very_eager().decode('big5','ignore')
        if "密碼不對" in content:
           print ("密碼不對或無此帳號。程式結束")
           sys.exit()
           content = telnet.read_very_eager().decode('big5','ignore')
        if "您想刪除其他重複登入" in content:
           print ('刪除其他重複登入的連線....')
           telnet.write("y\r\n")
           time.sleep(8)
           content = telnet.read_very_eager().decode('big5','ignore')
        if "請按任意鍵繼續" in content:
           print ("資訊頁面，按任意鍵繼續...")
           telnet.write("\r\n" )
           time.sleep(2)
           content = telnet.read_very_eager().decode('big5','ignore')
        if "您要刪除以上錯誤嘗試" in content:
           print ("刪除以上錯誤嘗試...")
           telnet.write("y\r\n")
           time.sleep(2)
           content = telnet.read_very_eager().decode('big5','ignore')
        if "您有一篇文章尚未完成" in content:
           print ('刪除尚未完成的文章....')
           # 放棄尚未編輯完的文章
           telnet.write("q\r\n")   
           time.sleep(2)   
           content = telnet.read_very_eager().decode('big5','ignore')
        print ("----------------------------------------------")
        print ("------------------ 登入完成 ------------------")
        print ("----------------------------------------------")
        
    else:
        print ("沒有可輸入帳號的欄位，網站可能掛了")

def disconnect() :
     print ("登出中...")
     # q = 上一頁，直到回到首頁為止，g = 離開，再見
     telnet.write("qqqqqqqqqg\r\ny\r\n" )
     time.sleep(3)
     #content = telnet.read_very_eager().decode('big5','ignore')
     #print content
     print ("----------------------------------------------")
     print ("------------------ 登出完成 ------------------")
     print ("----------------------------------------------")
     telnet.close()

def post(board, push, index, tag) :
        list_AID = [] 
        # s 進入要發文的看板
        telnet.write('s')
        telnet.write(board + '\r\n')
        time.sleep(1)       
        telnet.write("q") ;                            
        time.sleep(1)
        reset_count = 0;         
    
        while 1 : 
           print ('機器人推文中...')
           if(reset_count == index):
              reset_count = 0 
              print ('刷新文章...')
              telnet.write('$') ; # "$" = End = 到最末頁

           telnet.write('Q') #查詢文章資訊
           time.sleep(1)
           contentdata = telnet.read_very_eager().decode('big5','ignore')
           if( u'文章代碼(AID)' in contentdata): 
              start = contentdata.find(u'文章代碼(AID):')
              position = start + len('文章代碼(AID):')
              AID_data = contentdata[position:position + 20]
              removedata = AID_data.find('(')
              AID = AID_data[:removedata]
              #print 'AID:',AID
              if (AID not in list_AID and u'特殊文章，無價格記錄' not in contentdata ):
                 list_AID.append(AID)
                 telnet.write('\r\nX')   # "X" = 推文
                 time.sleep(1)              
                 content = telnet.read_very_eager().decode('big5','ignore')   
                 while ( '本板禁止快速連續推文' in content) :  
                        print  ('本板禁止快速連續推文')                
                        telnet.write('X')  
                        time.sleep(1) 
                        telnet.write('X')  
                        time.sleep(1)
                        content = telnet.read_very_eager().decode('big5','ignore')  
                                                    
                 if ('您覺得這篇文章' in content):
                    telnet.write( (tag + push +'\r\ny\r\n').encode('big5') ) #tag = 1(推) or(噓) 2 or 3(註解)                  
                 else:
                    telnet.write( (push+'\r\ny\r\n').encode('big5') )     
                 print ('推文成功')                    
                 reset_count += 1          
              else:
                 telnet.write('\r\n') 
                 if (AID  in list_AID  ):   
                    reset_count = index
           else: 
               telnet.write('\r\n') 
           content ,contentdata = '',''
           telnet.write('p') # 'p' = 方向鍵的上
           
        print ("----------------------------------------------")
        print ('自動推文完成...')
        print ("----------------------------------------------")
 

def main():
    login(host, user ,password)    

    #python PttAutoPush.py [版名] [內容] [標題數] [推文tag]
    #python PttAutoPush.py gossiping 別再發文了，趕快出門運動吧  10 1
    board, push, index, tag = sys.argv[1],sys.argv[2].decode(sys.getfilesystemencoding()),int(sys.argv[3]),sys.argv[4]
    post(board, push, index, tag)
    #disconnect();
       

if __name__=="__main__" :
   main()
