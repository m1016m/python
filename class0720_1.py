from sklearn import datasets 
from sklearn.model_selection import train_test_split # 引入 train_test_split 套件
iris = datasets.load_iris()

# X_train: 訓練集資料特徵, y_train: 訓練集分類target, X_test: 測試集資料特徵, y_test: 測試集分類target
X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, random_state=0)

print(X_train[:5], '\n', y_train[:5]) # 印出前五筆資料