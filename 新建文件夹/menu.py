#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
项目一
要求：打印三级菜单如：汽车、种类、品牌、型号，可自由发挥
可返回上一级
可随时退出程序
"""
menu = {
    '护肤': {
        '精华水':{
            '黛珂': {},
            '悦木之源': {},
        },
        '面霜': {
            '科颜氏': {},
            '资生堂': {},
        },
        '防晒霜':{
            '兰蔻防':{},
            '庭润紫苏':{}         
        }
    },
    '彩妆': {
        '口红': {
            '迪奥': {},
            '纪梵希': {},
        },
        '粉底液': {
            '雅诗兰黛': {},
            '乔治阿玛尼': {},
        }
    },
    '香氛': {
        '女士': {
            '香奈儿': {},
            '圣罗兰': {},
        },
        '男士': {
            '宝格丽': {},
            '爱马仕': {},
        }
    }
}
current_layer = menu
parent_layer = []
tag = True
while tag:
    print("欢迎您选购".center(40, '-'))
    for key in current_layer:
        print(key)
    choice = input('请输入您的选择(b-返回上一级，k-返回初始界面，q-退出程序)：').strip()
    if len(choice) == 0 :continue
    if choice in current_layer:
        parent_layer.append(current_layer)
        current_layer = current_layer[choice]  # 改成子层

    elif choice == 'b':  # 子层变父层
        current_layer = parent_layer.pop()
        
    elif choice == 'k':  # 返回初始界面
        current_layer = menu
    
    elif choice == 'q':  # 退出程序
        tag = False
        print("您已退出。")      
        
    else:
        print('输入格式错误！')

