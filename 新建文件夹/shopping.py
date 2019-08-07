#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
项目二
需求：
    用户名，密码和余额存放于文件中，格式为：Albert|Albert123|3000
    启动程序后：
        已注册用户===>先登录===>登录成功===>读取用户余额===>开始购物
                登录过程中，用户密码输入超过三次则退出程序，
                并将用户名添加到黑名单，再次启动程序登录该用户名，提示用户禁止登录
        未注册用户===>先注册===>注册成功===>输入用户工资，即为用户余额===>开始购物
                注册过程中，用户密码输入两次一样才可以注册
    允许用户根据商品编号购买商品，比如：
    1  iPhone
    2  macbook
    3  bike
    用户选择商品后，检测余额是否够，够就直接扣款，修改文件中用户余额，不够就提醒可随时退出，
    退出时，打印已购买商品和余额。
"""      
import os

def login():  # 登录
    with open('users.txt',mode='r',encoding='utf-8') as f1:
        data = f1.readlines()
        user_pwd_dict = {}
        for i in data:
            user_pwd_dict[i.split('|')[0]] = user_pwd_dict.split('|')[1]
            
    flag = True      
    while flag:
        count = 1
        name = input("请输入用户名： ")
        pwd = input("请输入密码： ")
        for user in user_pwd_dict:
            if (name in user_pwd_dict) and (pwd == user_pwd_dict[name]):
                print("登录成功！")
                return True,name
            elif name not in user_pwd_dict:
                print("请先注册！")
            elif pwd != user_pwd_dict[name]:
                print("密码输入错误，请重新输入！")
                count += 1
        if count == 3 :
            print("登录超过三次加入黑名单！")
            with open('blacklist.txt', 'a',encoding='utf-8') as f2:
                f2.write('\n',name)                
            return None

def signup():
    name = input("请输入用户名: ")
    salary = int(input("请输入用户工资："))
    pwd1 = input("请输入密码: ")
    pwd2 = input("请再次输入密码: ")
    if pwd1 != pwd2:
        print("密码有误，请重新输入")
        break
    elif pwd1 == pwd2:
        print("注册成功！")
    new_data="|".join([name,pwd1,salary])
    with open('users.txt',mode='a',encoding='utf-8') as f1:
        f1.write('\n',new_data) # 写入文件
    return True,name


goods_dic = {
    'iPhone':8000,
    'macBook':10000,
    'lenovo':6000,
    'bike':2500,    
}

shopping_dic = {}
print("欢迎购物！".center(50,'-'))
while True:
    print("登录请选择1\n注册请选择2\n")
    choice = input("Make your choice:")
    if choice == '1':
        login()
    elif choice == '2':
        signup()
        
    while True:
        print("商品信息".center(50,'-'))
        for key,value in goods_dic.items():
            print(key,value)      
        goods = input("请输入商品名称： ")
        num = int(input("请输入购买个数： "))
        money = goods_dic[goods]*num
        with open('users.txt',mode='r',encoding='utf-8') as f1:
                for i in f1:
                    i1=i.split("|",3)
                    if i1[0] == name:
                        account = i1[2]        
        if money > account:
            print("余额不足，请充值！")
            break
        elif:
            print("购买成功！")
            shopping_dic[goods] = list()
            shopping_dic[goods].extend([goods_dic[goods],num])
            account = account - money
            print("已购{},单价{}元，数量{},余额{}元".format(goods,shopping_dic[goods][0],shopping_dic[goods][1],account))
            with open('users.txt',mode='r',encoding='utf-8' ) as f2,                open('users1.txt',mode='w',encoding='utf-8') as f3:
                for i in f2:
                    j=i.split("|",3)
                    if j[0] == name:
                        j[2] = account
                    i2="|".join(j)
                    f3.write(i2)
            os.remove('users.txt')
            os.rename('users1.txt','users.txt')

        while True:
            flag = input("继续购买输入c,退出输入q.")
            if flag == "c":
                continue
            else flag == "q":
                break
print("欢迎下次再来！".center(50,'-'))

