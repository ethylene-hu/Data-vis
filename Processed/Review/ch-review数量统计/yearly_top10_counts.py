
import json
import sys

#inert1——success
from matplotlib import rcParams
# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False   # 解决负号显示问题
# 设置标准输出编码为utf-8，解决中文乱码问题
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

import json

# 每年评论最多的用户排行榜
yearly_top_users = {
    "2005": {"n-lBS02-3yvlY5Q91mmwDA": 171, "3MYdpmHeNwC6FquRWi3YOg": 60, "iUeZhkI0OK0BisakOkb3pQ": 51},
    "2006": {"gfQqQYI5_hCAGEHlHXIz2Q": 137, "TDXV6AC5PYOZEyN9eeODfA": 107, "nnImk681KaRqUVHlSfZjGQ": 78},
    "2007": {"0yYCMhDWCEIVUyZLzDWwqQ": 316, "5aVByErCyBwi-cnx_iEJmg": 305, "6O0MxTs3Pzzj5cXSHgYmrw": 264},
    "2008": {"bnVzSHI48lEHPaEzZNIqJg": 413, "758g6NGLp9deCbvowz62Ww": 407, "6s-g2vFu12OemhiK3FJuOQ": 371},
    "2009": {"_BcWyKQL16ndpBdggh2kNA": 407, "0Igx-a1wAstiBDerGxXk2A": 284, "ABy_uGiyQ7zlndwnodvFaw": 263},
    "2010": {"f9lq4KAus-xCsmJmjXeKVw": 381, "ztVQFPr9khc_TjsBny-3rA": 335, "0MJ5sKX5uq7Ma5hbl4l3BQ": 330},
    "2011": {"1HM81n6n4iPIFU5d2Lokhw": 292, "_BcWyKQL16ndpBdggh2kNA": 291, "z9uf9-0uX5Jh8-4Y5l2PQg": 272},
    "2012": {"1HM81n6n4iPIFU5d2Lokhw": 413, "ouODopBKF3AqfCkuQEnrDg": 406, "pou3BbKsIozfH50rxmnMew": 279},
    "2013": {"zYFGMy1_thjMnvQLX6JNBw": 331, "_BcWyKQL16ndpBdggh2kNA": 316, "AaJ9d4OrFmgc4S_U2QiSZg": 309},
    "2014": {"EQpFHqGT9Tk6YSwORTtwpg": 287, "AaJ9d4OrFmgc4S_U2QiSZg": 280, "Um5bfs5DH6eizgjH3xZsvg": 256},
    "2015": {"vYMvOTL31e0KbTo9Hd0tjg": 343, "lMY8NBPyzlPbbu-KBYfD9A": 317, "Um5bfs5DH6eizgjH3xZsvg": 300},
    "2016": {"B1OVDsstzC_RaESmtd1oWQ": 355, "Xw7ZjaGfr0WNVt6s_5KZfA": 345, "fr1Hz2acAb3OaL3l6DyKNg": 282},
    "2017": {"qcf3A5mtPntTmmSfADo6tg": 302, "uQY03sjjoHSBGb0bIUR9Vw": 253, "PnwOegp7RXfMeNAyO9fQhQ": 247},
    "2018": {"wXdbkFZsfDR7utJvbWElyA": 367, "fr1Hz2acAb3OaL3l6DyKNg": 203, "vFd8aBLg1kFcd0kCkoi-xw": 189},
    "2019": {"wXdbkFZsfDR7utJvbWElyA": 400, "HWQNlFjchIN37v-aPJEQDQ": 311, "vFd8aBLg1kFcd0kCkoi-xw": 269},
    "2020": {"Sp2GV7D-_JLZMPQmDanzPQ": 216, "qT1-N9hjbyjMW4Mvq4uU4w": 208, "vmUqcqMjlWoBM6qfmUXgyQ": 201},
    "2021": {"xalgcjscRLNPuyaAeKNThA": 242, "ZDCWEctaQHfJQT1sH_rMmA": 236, "S_VUtqoT9eHYrcb4qTVdIw": 213},
    "2022": {"vjLQ8F8opdDXGyXISRnuYQ": 39, "o1JVYrF_LnDpQwsmPpMSBg": 29, "OPMWWa7j4sD_xuXE8_oDvg": 23}
}

# 保存到文件
with open("yearly_top_users.json", "w", encoding="utf-8") as f:
    json.dump(yearly_top_users, f, ensure_ascii=False, indent=4)

print("统计内容已保存到 yearly_top_users.json 文件中。")


##pic
import json
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False   # 解决负号显示问题

# 完整的用户评论数据
yearly_top_users = {
    "2005": {
        "n-lBS02-3yvlY5Q91mmwDA": 171,
        "3MYdpmHeNwC6FquRWi3YOg": 60,
        "iUeZhkI0OK0BisakOkb3pQ": 51,
        "58yhbFfNHjULDZx0FD-Dvw": 38,
        "_BHTC7nyCBoZcfiiD5cOXg": 37,
        "jTXj5uf5ER5siDnQK_y4aA": 24,
        "3xX-Et9I4Bi4wdRPWJkAFg": 19,
        "-qoyKSF2G3PkR_7XNoJfpQ": 18,
        "DOFamdMaC_hjn9zg3Gs-0w": 16,
        "PO-U11FmTDiqCEqtilFjVQ": 15
    },
    "2006": {
        "gfQqQYI5_hCAGEHlHXIz2Q": 137,
        "TDXV6AC5PYOZEyN9eeODfA": 107,
        "nnImk681KaRqUVHlSfZjGQ": 78,
        "3xX-Et9I4Bi4wdRPWJkAFg": 72,
        "tiLm3eFfpxhwV6O9DEaneQ": 61,
        "Ffa1cXIvFAy8H1sorICaiQ": 50,
        "fnBAgDX4D9mNgQZsjFCoog": 48,
        "6OV_PFTl9RW2FmYQoOsuRQ": 46,
        "_BHTC7nyCBoZcfiiD5cOXg": 45,
        "RBXVFcXR3IjP0CYgmkSmtg": 42
    },
    "2007": {
        "0yYCMhDWCEIVUyZLzDWwqQ": 316,
        "5aVByErCyBwi-cnx_iEJmg": 305,
        "6O0MxTs3Pzzj5cXSHgYmrw": 264,
        "bJ5FtCtZX3ZZacz2_2PJjA": 263,
        "RdJ7Ykelg8w4y5FTmxjT8g": 228,
        "TLcUXi2bn6v4hdB8X-M73w": 218,
        "rjD5JDrDndu0vZvUhnnA7g": 198,
        "kS1MQHYwIfD0462PE61IBw": 175,
        "gpqGjIHlvUKDTttna4wcZQ": 172,
        "6s-g2vFu12OemhiK3FJuOQ": 144
    },
    "2008": {
        "bnVzSHI48lEHPaEzZNIqJg": 413,
        "758g6NGLp9deCbvowz62Ww": 407,
        "6s-g2vFu12OemhiK3FJuOQ": 371,
        "_BcWyKQL16ndpBdggh2kNA": 368,
        "y8aWXOimQ9ZgUgZ6q--nCQ": 325,
        "NyqoJTiKgXi1h7MDJDGbxg": 301,
        "S-P2haI61umZRkGPCWrqfA": 293,
        "RkTfZGAksML93OYzvW4TMQ": 280,
        "hL-p_AOo53wJyYrggzYMVg": 271,
        "Jc2D_Uk4i03E3bmFNp2Smw": 270
    },
    "2009": {
        "_BcWyKQL16ndpBdggh2kNA": 407,
        "0Igx-a1wAstiBDerGxXk2A": 284,
        "ABy_uGiyQ7zlndwnodvFaw": 263,
        "2T8ZGt1RsCrcJEZcRfsylg": 238,
        "KGmDAZI48MtoS_SnSkM0ag": 238,
        "BmCI9_Oxg7018TOxvnUPEg": 223,
        "RgDVC3ZUBqpEe6Y1kPhIpw": 210,
        "f9lq4KAus-xCsmJmjXeKVw": 201,
        "bJ5FtCtZX3ZZacz2_2PJjA": 199,
        "nnwBdqGHIAJQ5QX9lHOtrQ": 187
    },
    "2010": {
        "f9lq4KAus-xCsmJmjXeKVw": 381,
        "ztVQFPr9khc_TjsBny-3rA": 335,
        "0MJ5sKX5uq7Ma5hbl4l3BQ": 330,
        "_BcWyKQL16ndpBdggh2kNA": 313,
        "djxnI8Ux8ZYQJhiOQkrRhA": 288,
        "2T8ZGt1RsCrcJEZcRfsylg": 238,
        "ouODopBKF3AqfCkuQEnrDg": 232,
        "6s-g2vFu12OemhiK3FJuOQ": 225,
        "KDewJBJknfWvQyHHFNbfdg": 194,
        "lYQk0R6sPfo3WeX-l_5BuA": 188
    },
    "2011": {
        "1HM81n6n4iPIFU5d2Lokhw": 292,
        "_BcWyKQL16ndpBdggh2kNA": 291,
        "z9uf9-0uX5Jh8-4Y5l2PQg": 272,
        "Hn8O2RQijYIVLFNF5VPWTA": 268,
        "ET8n-r7glWYqZhuR6GcdNw": 267,
        "Oi1qbcz2m2SnwUeztGYcnQ": 266,
        "W625SoCsKsZyiws3GR1MTg": 261,
        "Vwslifegl59fQVOe5BH1gw": 259,
        "Xw7ZjaGfr0WNVt6s_5KZfA": 258,
        "47oIw-CN1guUKx2_vUdsgw": 243
    },
    "2012": {
        "1HM81n6n4iPIFU5d2Lokhw": 413,
        "ouODopBKF3AqfCkuQEnrDg": 406,
        "pou3BbKsIozfH50rxmnMew": 279,
        "_BcWyKQL16ndpBdggh2kNA": 267,
        "HxyLRaoH9PS09M6R3rV-EQ": 237,
        "F3lu1icxJX5A5tCw-jVpTg": 234,
        "7Na1pUcEv3oF_QTRwZ-2iw": 226,
        "0G-QF457q_0Z_jKqh6xWiA": 219,
        "ET8n-r7glWYqZhuR6GcdNw": 200,
        "bYENop4BuQepBjM1-BI3fA": 198
    },
    "2013": {
        "zYFGMy1_thjMnvQLX6JNBw": 331,
        "_BcWyKQL16ndpBdggh2kNA": 316,
        "AaJ9d4OrFmgc4S_U2QiSZg": 309,
        "Xw7ZjaGfr0WNVt6s_5KZfA": 284,
        "dgGUKdOh2a01OwLw1qgfDw": 283,
        "0Igx-a1wAstiBDerGxXk2A": 250,
        "VL12EhEdT4OWqGq0nIqkzw": 241,
        "0dIvVs3PY64bE3PZF-8V8A": 229,
        "GcdYgbaF75vj7RO6EZhPOQ": 225,
        "2iS1vg5TYpV_iEiNC8osTg": 224
    },
    "2014": {
        "EQpFHqGT9Tk6YSwORTtwpg": 287,
        "AaJ9d4OrFmgc4S_U2QiSZg": 280,
        "Um5bfs5DH6eizgjH3xZsvg": 256,
        "VL12EhEdT4OWqGq0nIqkzw": 233,
        "-G7Zkl1wIWBBmD0KRy_sCw": 222,
        "I2XpWCHAom1JRyHXZQrnfg": 214,
        "vHc-UrI9yfL_pnnc6nJtyQ": 201,
        "3_inIIto4ZaKsuOqEaJazw": 200,
        "0Igx-a1wAstiBDerGxXk2A": 199,
        "huHPQSQgw4kFakc0Vq7TDA": 191
    },
    "2015": {
        "vYMvOTL31e0KbTo9Hd0tjg": 343,
        "lMY8NBPyzlPbbu-KBYfD9A": 317,
        "Um5bfs5DH6eizgjH3xZsvg": 300,
        "I2XpWCHAom1JRyHXZQrnfg": 298,
        "qjfMBIZpQT9DDtw_BWCopQ": 293,
        "fr1Hz2acAb3OaL3l6DyKNg": 248,
        "JI6T6niNLWzks55uON1QDg": 241,
        "kkPgJv6KBFN15caG7NYYlg": 235,
        "iiaWyeXrdiddVVshvv7mzA": 235,
        "d8FwfuFM9SJA3kU_cIQ3aw": 231
    },
    "2016": {
        "B1OVDsstzC_RaESmtd1oWQ": 355,
        "Xw7ZjaGfr0WNVt6s_5KZfA": 345,
        "fr1Hz2acAb3OaL3l6DyKNg": 282,
        "-G7Zkl1wIWBBmD0KRy_sCw": 257,
        "h7p-GuaHFGsiKCF4g6Bjqg": 251,
        "VL12EhEdT4OWqGq0nIqkzw": 241,
        "GcdYgbaF75vj7RO6EZhPOQ": 220,
        "_BcWyKQL16ndpBdggh2kNA": 215,
        "vFZUDAxiFZlEQgkV3VSsBA": 213,
        "PnwOegp7RXfMeNAyO9fQhQ": 212
    },
    "2017": {
        "qcf3A5mtPntTmmSfADo6tg": 302,
        "uQY03sjjoHSBGb0bIUR9Vw": 253,
        "PnwOegp7RXfMeNAyO9fQhQ": 247,
        "GfI-d9mQePFA2PvhAd4WGQ": 238,
        "-kLVfaJytOJY2-QdQoCcNQ": 230,
        "wXdbkFZsfDR7utJvbWElyA": 218,
        "-G7Zkl1wIWBBmD0KRy_sCw": 214,
        "B-s-8VUnuBjGTP3d01jsyw": 213,
        "Xw7ZjaGfr0WNVt6s_5KZfA": 210,
        "gv0coNUFY-fibRwP8IKqPA": 207
    },
    "2018": {
        "wXdbkFZsfDR7utJvbWElyA": 367,
        "fr1Hz2acAb3OaL3l6DyKNg": 203,
        "vFd8aBLg1kFcd0kCkoi-xw": 189,
        "WwulXySQN8t2hwqH_yWurA": 183,
        "gv0coNUFY-fibRwP8IKqPA": 179,
        "4YyJpeAr6jsY0FaIbLiTSQ": 178,
        "-G7Zkl1wIWBBmD0KRy_sCw": 177,
        "8VPCVY70TcE353gRruotWQ": 173,
        "vmUqcqMjlWoBM6qfmUXgyQ": 170,
        "xSlBsTTPtPvwlclBIvAjYw": 166
    },
    "2019": {
        "wXdbkFZsfDR7utJvbWElyA": 400,
        "HWQNlFjchIN37v-aPJEQDQ": 311,
        "vFd8aBLg1kFcd0kCkoi-xw": 269,
        "vmUqcqMjlWoBM6qfmUXgyQ": 252,
        "n-iTQUXN2Y-meUP_YrXGTg": 249,
        "Sp2GV7D-_JLZMPQmDanzPQ": 232,
        "-kLVfaJytOJY2-QdQoCcNQ": 207,
        "r9S0VYrdXJrdhfR7OXj8tA": 192,
        "rWl260C3GTKkCYkPWt6kgA": 185,
        "9nDw3Z1Y-JkXB4Qec3LluQ": 183
    },
    "2020": {
        "Sp2GV7D-_JLZMPQmDanzPQ": 216,
        "qT1-N9hjbyjMW4Mvq4uU4w": 208,
        "vmUqcqMjlWoBM6qfmUXgyQ": 201,
        "AEowRtLGb_AdqFAZ8e6C9A": 185,
        "R9IJ1Byr27n6wXj3QvJ2Lg": 173,
        "fr1Hz2acAb3OaL3l6DyKNg": 167,
        "leMOR7VSm5z-0r60iJ90EA": 155,
        "R7NM7vIyUfSTXvMsw7jNTA": 155,
        "WwulXySQN8t2hwqH_yWurA": 154,
        "nWRDqA-XXdju1jOMnN7QcA": 151
    },
    "2021": {
        "xalgcjscRLNPuyaAeKNThA": 242,
        "ZDCWEctaQHfJQT1sH_rMmA": 236,
        "S_VUtqoT9eHYrcb4qTVdIw": 213,
        "R7NM7vIyUfSTXvMsw7jNTA": 196,
        "R9IJ1Byr27n6wXj3QvJ2Lg": 186,
        "0YI3p9o-ntRgRaPWpfa22Q": 171,
        "A9cXP_K95FRor1qxuUEu2g": 162,
        "D2EQgPgib4kSHKROuPBLAw": 159,
        "L90JF_h-3oy4Q60wTnOuvw": 152,
        "98jv8gu7kAwa2WzIPdw6-w": 151
    },
    "2022": {
        "vjLQ8F8opdDXGyXISRnuYQ": 39,
        "o1JVYrF_LnDpQwsmPpMSBg": 29,
        "OPMWWa7j4sD_xuXE8_oDvg": 23,
        "wxqxIOP9SoqKY3ZxvKchqg": 22,
        "W5ile8ec40snDwWjyuNHzA": 22,
        "S_VUtqoT9eHYrcb4qTVdIw": 20,
        "PLxAUBVOoK45izcTfucJ-g": 19,
        "MB0jD-3_LUktXJPl3kMbzA": 18,
        "k79e_2xLR6C1grGQLWvTng": 18,
        "oR5az_eNCnfN7e49H3ONhg": 18
    }
}

# 提取年份和评论数据
years = list(yearly_top_users.keys())
data_points = [list(yearly_top_users[year].values()) for year in years]

# 计算平均值和去掉极值后的平均值
averages = [np.mean(points) for points in data_points]
trimmed_averages = [np.mean(sorted(points)[1:-1]) if len(points) > 2 else np.mean(points) for points in data_points]

# 绘制散点图
plt.figure(figsize=(12, 6))
for i, points in enumerate(data_points):
    plt.scatter([years[i]] * len(points), points, color="skyblue", label="散点" if i == 0 else "")

# 绘制平均值折线图
plt.plot(years, averages, color="orange", label="平均值折线", marker="o")

# 绘制去掉极值后的平均值折线图
plt.plot(years, trimmed_averages, color="green", label="去掉极值后的平均值折线", marker="o")

# 设置图例和标签
plt.xlabel("年份", fontsize=12)
plt.ylabel("评论数", fontsize=12)
plt.title("每年评论数据散点图及平均值折线图", fontsize=16)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# 保存图片
plt.savefig("yearly_top_users_scatter_trimmed_line.png", dpi=300)
plt.show()

print("统计图片已保存为 yearly_top_users_scatter_trimmed_line.png。")