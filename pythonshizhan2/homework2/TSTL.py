# -*- coding: utf-8 -*-
# @Time  :2020/10/25 9:04 下午
# @Author : caohe
# @File :TSTL.py
'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。



'''
#定义一个天山童姥类 ，类名为TongLao
class TongLao:
    #构造函数，属性有血量，武力值（通过传入的参数得到）
    #my_hp,my_power,emeny_hp,emenmy_power分别代表我的血量，我的武力值，敌人血量，敌人武力值
    def __init__(self,my_hp,my_power,emeny_hp,emenmy_power):
        self.my_hp=int(my_hp)
        self.my_power=int(my_power)
        self.emeny_hp=int(emeny_hp)
        self.emeny_power=int(emenmy_power)
    #see_people方法，需要传入一个name参数
    def  see_people(self,name):
        self.name=name
    #如果传入”WYZ”（无崖子），则打印，“师弟！！！！”
        if self.name == 'WYZ':
            print("师弟！！！！")
        #如果传入“李秋水”，打印“师弟是我的！”
        elif self.name == "LQS":
            print("师弟是我的！")
        #如果传入“丁春秋”，打印“叛徒！我杀了你”
        elif self.name == "DCQ":
            print("叛徒！我杀了你")
        else:
            print("我不认识你")
         #fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
    def  fight_zms(self):
        #调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power
        self.my_power=self.my_power *10
        self.my_hp=self.my_hp/2
        #我的最终血量
        my_final_hp=self.my_hp-self.emeny_power
        #敌人的最终血量
        emeny_final_hp=self.emeny_hp-self.my_power
        #打印我的血量
        print(f"我的血量是{my_final_hp}")
        #打印敌人血量
        print(f"敌人血量是{emeny_final_hp}")
        #如果我的最终血量>敌人的血量，则我赢了
        if my_final_hp >= emeny_final_hp:
            print('我赢了')
        #否则，敌人赢了
        else:
            print("敌人赢了")

# TL=TongLao("100","100","100","100")
# TL.see_people("DCQ")
# TL.fight_zms()
