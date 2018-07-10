#設計一個點餐系統,將所點的餐點放入unserved,服務完成將餐點放入served
def kitchen(unserved, served):
    """ 將未服務的餐點轉為已經服務 """
    for x in unserved :
        print "菜單: ", x
    print "廚房處理顧客所點的餐點"

    served.append(x)
    show_unserved_meal(served)
    

def show_unserved_meal(unserved):
    """ 顯示尚未服務的餐點 """
    print "=== 下列是尚未服務的餐點 ==="
    for x in unserved :
         s = unserved.pop()
    """ 顯示已經服務的餐點 """
    if len(s) :#判斷串列為空
        print "end"
        

unserved = ['大麥克', '勁辣雞腿堡', '麥克雞塊']   # 所點餐點
served = []  
