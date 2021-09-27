import jieba
import jieba.analyse
import csv
from pprint import *
import os
import regex as re
import random
import paddle
# 檔案路徑
path = r'D:\PycharmProjects\CodingLife\Jieba_BDSE20\google_review_csv'
csv_location = os.listdir(path)
# 正則規則
rule = re.compile('[\u4e00-\u9fa5]')

res_review_analyse_list = []
find_tags_sentence = []
heavy_list = []
stop_list = []
paddle_mode_sentence = []

dic = {}


def get_csv_name():

    global index ,res_name

    # 讀取檔案目錄
    for index in csv_location:
        # 檔案路徑+檔名
        csv_name = path + '\\' + index
        # 開啟檔案
        with open(csv_name, 'r', encoding='utf-8') as csv_file:

            # 讀取列
            rows = csv.reader(csv_file)

            for row in rows:

                # 刪除空值(非nan) 原本nan被"NA"替代
                if row[5] == "NA":
                    pass
                # 正則把所有非中文刪除 加入餐廳評論(單餐廳)list
                else:
                    res = re.findall(rule, row[5])
                    res_sentence = ''.join(res)
                    find_tags_sentence.append(res_sentence)
                res_name_pos = row[0]
                res_name = res_name_pos[0:]
        find_tags_sentence.pop(0)

        do_extra_get()


def do_extra_get():

    # 取出評論
    for sentence in find_tags_sentence:

        # 分析 提取關鍵詞
        jieba.analyse.set_stop_words('all_stopwords.txt')
        analyse_res = jieba.analyse.extract_tags(sentence, topK=200, withWeight=True, allowPOS='ag')
        # 詞 , 對應分數 加入分析後的list清單
        for key, score in analyse_res:
            res_review_analyse_list.append([key, score])

    # 轉成字典 方便排序
    res_review_analyse_dic = dict(res_review_analyse_list)
    # 由大到小 排序完成
    res_review_keyword_and_score = sorted(res_review_analyse_dic.items(), key=lambda x: x[1], reverse=True)
    # 放關鍵字
    res_keyword_rank = []
    # 取出餐廳代表關鍵字標籤
    for res_key_word_score_tuple in res_review_keyword_and_score:
        keyword = res_key_word_score_tuple[0]
        res_keyword_rank.append(keyword)

    print('==========')
    print('"' + res_name + '"')
    print( " 這間餐廳的關鍵詞: " + str(res_keyword_rank[0:3]))

get_csv_name()
do_extra_get()

'''
==========
reviews_1.csv
['簡單', '貼心', '愉快', '很好', '舒適', '親切']
==========

==========
reviews_10.csv
['舒適', '優秀', '鮮美', '穩定', '輕切', '驚艷']
==========
'''