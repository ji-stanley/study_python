# __author__: Stanley
# date: 2018/2/28

menu = {
    '北京':{
        '朝阳':{
            '国贸':{
                'CICC':{},
                'HP':{},
                '渣打银行':{},
                'CCTV':{},
            },
            '望京':{
                '陌陌':{},
                '奔驰':{},
                '360':{},
            },
            '三里屯':{
                '优衣库':{},
                'apple':{},
            },
        },
        '昌平':{
            '沙河':{
                'oldboy':{},
                '阿泰包子':{},
            },
            '天通苑':{
                '链家':{},
                '我爱我家':{},
            },
            '回龙观':{},
        },
        '海淀':{
            '五道口':{
                '谷歌': {},
                '网易': {},
                '搜狐': {},
                'Sogo': {},
                '快手': {},
            },
            '中关村':{
                'youku':{},
                'Iqiyi':{},
                '汽车之家':{},
                '新东方':{},
                'QQ':{},
            }
        },
    },
    '上海':{
        '浦东':{
            '陆家嘴':{
                'CICC':{},
                '高盛':{},
                '摩根':{},
            },
            '外滩':{},
        },
        '闵行':{},
        '静安':{},
    },
    '山东':{
        '济南':{},
        '德州':{
            '乐陵':{
                '丁务镇':{},
                '城区':{},
            },
            '平原':{},
        },
        '青岛':{},
    },
}

back_flag = False
exit_flag = False

while not back_flag and not exit_flag:
    for key in menu:
        print(key)
    chioce = input("1>>").strip()
    if chioce == 'q':
        exit_flag = True
    if chioce in menu:
        while not back_flag and not exit_flag:
            for key2 in menu[chioce]:
                print(key2)
            chioce2 = input("2>>:").strip()
            if chioce2 == 'b':
                back_flag = True
            if chioce2 == 'q':
                exit_flag = True
            if chioce2 in menu[chioce]:
                while not back_flag and not exit_flag:
                    for key3 in menu[chioce][chioce2]:
                        print(key3)
                    chioce3 = input("3>>:").strip()
                    if chioce3 == 'b':
                        back_flag=True
                    if chioce3 == "q":
                        exit_flag=True
                    if chioce3 in menu[chioce][chioce2]:
                        while not back_flag and not exit_flag:
                            for key4 in menu[chioce][chioce2][chioce3]:
                                print(key4)
                            chioce4 = input("4>>:").strip()
                            print('last level')
                            if chioce4 == "b":
                                back_flag = True
                            if chioce4 == "q":
                                exit_flag = True
                        else:
                            back_flag = False
                else:
                    back_flag = False
        else:
            back_flag = False
