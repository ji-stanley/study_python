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

current_layer = menu
exit_flag = False
parent_layers = []

while not exit_flag:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:continue
    if choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == "b":
        if parent_layers:
            current_layer = parent_layers.pop()
    elif choice == "q":
        exit_flag = True
    else:
        print("no data")
