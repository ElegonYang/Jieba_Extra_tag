import jieba
import jieba.analyse
import csv
import pandas as pd


# 有些評論過長 修改讀取字串最大上限
csv.field_size_limit(500 * 1024 * 1024)


class ExtraTag:
    # 實例化 我們傳的參是csv的檔名
    def __init__(self, csv_name):
        self.csv_name = csv_name
        self.review_list = []
        self.name_list = []
        self.all_res_key_list = []

    # 入口
    def do(self):

        review_row = self.csv_rows()  # 讀取出 csv的內容
        self.do_extra_tag(review_row)  # 以一間餐廳的評論為單位餐廳 執行關鍵字分析
        self.write_to_csv(self.name_list, self.all_res_key_list)  # 寫入CSV

    def csv_rows(self):
        """讀取出 csv的內容"""

        # 打開 CSV 編碼為utf-8 設定換行
        with open('res_review_dict.csv', encoding='utf-8', newline='') as csv_file:
            rows = csv.reader(csv_file)
            for row in rows:
                self.name_list.append(row[0])
                self.review_list.append(row[1])
            # 將讀出來的內容 用字典裝好  name-->對應餐廳名稱 review--> 對應評論
            dict_1 = {'name': self.name_list, 'review': self.review_list}
            # 將字典回傳
            return dict_1

    def do_extra_tag(self, dict_1):
        """以一間餐廳的評論為單位餐廳 執行關鍵字分析"""

        # 讀取每間餐廳評論的list分析  預設單位為取3個最高權重關鍵字
        for row in dict_1['review']:
            analyse_res = jieba.analyse.extract_tags(row, topK=3, allowPOS='ag')
            # 加入所有餐廳關鍵字的list
            self.all_res_key_list.append(analyse_res)
        # 回傳包含所有餐廳關鍵字的list -->  [ [key1-1,key2-1,key3-1] , [key2-1,key3-1,key4-1] ]
        return self.all_res_key_list

    def write_to_csv(self, res_name, res_keys):
        """寫入CSV"""

        info = {
            '餐廳名稱': self.name_list[0:6],
            '關鍵字': self.all_res_key_list[0:6]
        }
        # 用pandas dict to csv方法
        df1 = pd.DataFrame.from_dict(info)
        df1.to_csv('res_key.csv', encoding='utf_8_sig', index=False)




ExtraTag_get = ExtraTag('res_review_dict.csv')


if __name__ == '__main__':
    ExtraTag_get.do()
