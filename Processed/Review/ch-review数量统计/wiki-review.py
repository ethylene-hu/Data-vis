
import json
import re
import string
from collections import Counter, defaultdict
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime
import sys

# # 下载必要的nltk数据
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt')


import nltk

# # 指定清华大学镜像源
# nltk.download('stopwords', download_dir='./nltk_data', quiet=True)
# nltk.download('wordnet', download_dir='./nltk_data', quiet=True)
# nltk.download('punkt', download_dir='./nltk_data', quiet=True)

# # 将下载目录添加到 NLTK 搜索路径
# nltk.data.path.append('./nltk_data')

import nltk
import os

import nltk
nltk.download('wordnet', download_dir='A:/1shixu/1/nltk_data')
nltk.download('stopwords', download_dir='A:/1shixu/1/nltk_data')
nltk.download('punkt', download_dir='A:/1shixu/1/nltk_data')

# 文件路径
# REVIEW_FILE = 'yelp_academic_dataset_review.json'
REVIEW_FILE = 'test.json'

# 设置标准输出编码为utf-8，解决中文乱码问题
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

# 1.
def load_reviews():
    """加载评论数据"""
    reviews = []
    try:
        with open(REVIEW_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                reviews.append(json.loads(line))
    except FileNotFoundError:
        print(f"错误: 文件 {REVIEW_FILE} 未找到!")
        exit(1)
    except Exception as e:
        print(f"错误: 读取文件时发生错误: {e}")
        exit(1)
    return reviews

# 2.
def count_reviews_by_year(reviews):
    """统计每年的评论数"""
    year_counts = defaultdict(int)
    for review in reviews:
        year = review['date'][:4]
        year_counts[year] += 1
    # 按年份排序
    sorted_years = sorted(year_counts.items())
    print("\n每年的评论数:")
    for year, count in sorted_years:
        print(f"{year}: {count}")
    return sorted_years

# 3.
def count_interaction_types(reviews):
    """统计有用、有趣及酷的评论及数量"""
    interaction_types = ['useful', 'funny', 'cool']
    interaction_counts = {t: 0 for t in interaction_types}

    for review in reviews:
        for t in interaction_types:
            if review[t] > 0:
                interaction_counts[t] += 1

    print("\n互动类型的评论数量:")
    for t, count in interaction_counts.items():
        print(f"{t}: {count}")
    return interaction_counts

# 4.
def get_top_users_by_year(reviews):
    """每年全部评论用户排行榜"""
    user_reviews_by_year = defaultdict(lambda: defaultdict(int))

    for review in reviews:
        year = review['date'][:4]
        user_id = review['user_id']
        user_reviews_by_year[year][user_id] += 1

    # 为每年找出前10名用户
    top_users_by_year = {}
    for year, user_counts in user_reviews_by_year.items():
        sorted_users = sorted(user_counts.items(), key=lambda x: x[1], reverse=True)
        top_users_by_year[year] = sorted_users[:10]

    print("\n每年评论最多的用户:")
    for year, top_users in sorted(top_users_by_year.items()):
        print(f"\n{year}:")
        for rank, (user_id, count) in enumerate(top_users, 1):
            print(f"{rank}. 用户ID: {user_id}, 评论数: {count}")
    return top_users_by_year


# run
def main():
    """主函数，执行所有分析任务"""
    print("正在加载评论数据...")
    reviews = load_reviews()
    print(f"已加载 {len(reviews)} 条评论")

    # # 1. 统计每年的评论数
    # count_reviews_by_year(reviews)

    # 2. 统计有用、有趣及酷的评论及数量
    # count_interaction_types(reviews)

    # # 3. 每年全部评论用户排行榜
    # get_top_users_by_year(reviews)


if __name__ == "__main__":
    main()