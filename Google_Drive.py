from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import sys

'''
ArgumentParser(prog=None, usage=None, description=None, epilog=None)

'''

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()#以父母解析器集创建另一个解析器
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
CLIENT_SECRET_FILE = 'client_secrets.json'
APPLICATION_NAME = 'Drive API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')#os.path.expanduser(path)  #把path中包含的"~"和"~user"转换成用户目录
    credential_dir = os.path.join(home_dir, '.credentials')#把目录和文件名合成一个路径
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)#批准為具有 openid 和 email 作用域的授權API客戶端
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list(
        pageSize=10,fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)
try:
    name = 'ex1.py'  # It's the file which you'll upload
    file = drive.CreateFile()  # Create GoogleDriveFile instance
    file.SetContentFile(name)
    file.Upload()
except :
    print("Unexpected error:", sys.exc_info()[0])

if __name__ == '__main__':
    main()


'''
原來如果一個 python script 是被別的 python script 當成 module 來 import 的話，
那麼這個被 import 的 python script 的 __name__ 就會是那個 python script 的名稱。
而如果這個 python script 是直接被執行的話，__name__ 就會是 __main__。

舉例來說，如果我有一個程式叫做 myModule.py，內容就是一行顯示自己的 __name__:

print '__name__:' + __name__

那麼我直接執行它的話，結果會顯示 __main__:

bash-3.2$ python myModule.py
__name__:__main__

但如果我準備了另一個程式叫做 testModule.py，裡面就這麼一行去 import myModule:

import myModule

然後我去執行 testModule.py 的話，則會顯示 myModule:

bash-3.2$ python testModule.py
__name__:myModule

所以用 __name__ 就可以分辨我的程式是被 import 當成模組還是被直接執行的。
這樣附帶的好處就是如果我寫的程式平常可以被 import 來使用，但有時它自己也可以直接執行。
其它語言的話，可能就要區分 library 跟使用 library 的程式，而 python 的話這兩者的界線就很模糊。
'''