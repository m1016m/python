1.將所需檔案上傳至Google Drive（我的是keras-yolo3-master） 
2.新建或上傳ipnb檔案，並用Colaboratory開啟（我這裡新建是"授權程式碼.ipynb"）
 
注：Colaboratory現在已全面支援python2和python3兩個版本，新建預設為python2，無GPU加速，點選左上角“修改”——》“筆記本設定”→更改“執行時型別”選擇python版本，並在“硬體加速器”中選擇是否使用GPU加速。
 
3.在notebook中執行下方程式碼進行授權繫結（拷貝如下程式碼）
# 授權繫結Google Drive
!apt-get install -y -qq software-properties-common python-software-properties module-init-tools
!add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null
!apt-get update -qq 2>&1 > /dev/null
!apt-get -y install -qq google-drive-ocamlfuse fuse
from google.colab import auth
auth.authenticate_user()
from oauth2client.client import GoogleCredentials
creds = GoogleCredentials.get_application_default()
import getpass
!google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret} < /dev/null 2>&1 | grep URL
vcode = getpass.getpass()
!echo {vcode} | google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret}
注：執行完，過一會兒會要求兩次點進連結登陸google賬號並完成相關授權，複製授權碼，回車即可

# 授權繫結Google Drive
!apt-get install -y -qq software-properties-common python-software-properties module-init-tools
!add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null
!apt-get update -qq 2>&1 > /dev/null
!apt-get -y install -qq google-drive-ocamlfuse fuse
from google.colab import auth
auth.authenticate_user()
from oauth2client.client import GoogleCredentials
creds = GoogleCredentials.get_application_default()
import getpass
!google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret} < /dev/null 2>&1 | grep URL
vcode = getpass.getpass()
!echo {vcode} | google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret}
注：執行完，過一會兒會要求兩次點進連結登陸google賬號並完成相關授權，複製授權碼，回車即可
 
出現以下提示，算是完成授權：
 
4. 指定工作目錄
在指定之前先用!ls命令檢視一下雲端自動分配的預設檔案目錄，雲端預設的檔案根目錄是datalab
 
執行下方程式碼，指定檔案根目錄：
# 指定Google Drive雲端硬碟的根目錄，名為drive
!mkdir -p drive
!google-drive-ocamlfuse drive
指定完之後，再用!ls命令檢視繫結的檔案根目錄，根目錄變為drive，即咱們使用的雲端硬碟：
 
5. 指定當前工作資料夾（這裡我指定的是我上傳的資料夾，即keras-yolo3-master）
# 指定當前的工作目錄
import os

# 此處為google drive中的檔案路徑,drive為之前指定的工作根目錄，要加上
os.chdir("drive/GoogleAI/keras-yolo3-master") 
再次用!ls檢視當前的檔案目錄：
 
6.執行python檔案
!python yolo.py
7. 總結：
需要注意的是，Colaboratory是完全基於雲端執行的，每次登陸操作，後臺分配的機子都是隨機的，所以如果notebook執行需要額外的檔案，那麼在執行之前都要將檔案先上傳至Google Drive，然後對Colaboratory指定所需的工作目錄。
以下是每次繫結都需要執行的所有程式碼，現總結如下：
#執行python檔案之前需要先安裝各種依賴以及進行授權
#看見連結之後，點選它，複製驗證碼並貼上到文字框裡
#授權完成後，就可以掛載Google Drive了
!apt-get install -y -qq software-properties-common python-software-properties module-init-tools
!add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null
!apt-get update -qq 2>&1 > /dev/null
!apt-get -y install -qq google-drive-ocamlfuse fuse
from google.colab import auth
auth.authenticate_user()
from oauth2client.client import GoogleCredentials
creds = GoogleCredentials.get_application_default()
import getpass
!google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret} < /dev/null 2>&1 | grep URL
vcode = getpass.getpass()
!echo {vcode} | google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret}


# 掛載Google driver，指定Google Drive雲端硬碟的根目錄，名為drive
!mkdir -p drive
!google-drive-ocamlfuse drive


# 指定當前的工作目錄
# 此處為google drive中的檔案路徑,drive為之前指定的工作根目錄，要加上
import os
os.chdir("drive/GoogleAI/keras-yolo3-master")

# 檢視檔案目錄，是否包含所需的檔案
!ls

#執行工作目錄下的python檔案
!python yolo.py

確認GPU運行正常
import tensorflow as tf
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))

上傳和下載檔案
from google.colab import files
uploaded = files.upload()

files.download('WestWorld.png')
安裝package
Keras
!pip install -q keras
import keras

PyTorch
from os import path
from wheel.pep425tags import get_abbr_impl, get_impl_ver, get_abi_tag
platform = '{}{}-{}'.format(get_abbr_impl(), get_impl_ver(), get_abi_tag())
accelerator = 'cu80' if path.exists('/opt/bin/nvidia-smi') else 'cpu'
!pip install -q http://download.pytorch.org/whl/{accelerator}/torch-0.3.0.post4-{platform}-linux_x86_64.whl torchvision
import torch
或!pip3 install torch torchvision

MxNet
!apt install libnvrtc8.0
!pip install mxnet-cu80
import mxnet as mx

OpenCV
!apt-get -qq install -y libsm6 libxext6 && pip install -q -U opencv-python
import cv2

XGBoost
!pip install -q xgboost==0.4a30
import xgboost

GraphViz
!apt-get -qq install -y graphviz && pip install -q pydot
import pydot

!ls可以查看目前所在資料夾的目錄，若要查看特定資料夾之目錄可以用!ls <資料夾路徑>

而大部分Linux中用到的terminal指令(mv, rm, wget,apt-get…etc)，只需要在前面加上!就可以直接在cell中運行，如這裡展示用來下載網路檔案的wget指令，用後綴-P指定存放路徑，下圖為下載我GitHub上的一張圖到Drive中，Drive便會即時顯示這份檔案。
 

