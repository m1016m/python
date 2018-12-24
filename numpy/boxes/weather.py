from source import daily,weekly
print ('Daily forecast : ',daily.forecast())
print ('Weekily forecast : ')
'''
enumerate()说明
enumerate()是python的内置函数
enumerate在字典上是枚举、列举的意思
对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
enumerate多用于在for循环中得到计数
enumerate()使用
如果对一个列表，既要遍历索引又要遍历元素时，首先可以这样写：
list1 = ["这", "是", "一个", "测试"]
for i in range (len(list1)):
    print i ,list1[i]

上述方法有些累赘，利用enumerate()会更加直接和优美：
list1 = ["这", "是", "一个", "测试"]
for index, item in enumerate(list1):
    print index, item

0 这
1 是
2 一个
3 测试

'''
for number,outlook in enumerate(weekly.forecast()) :
    print (number , outlook)