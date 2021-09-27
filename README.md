# Jieba_Extra_tag
 這次分享的是結疤(Jieba) <br> 
 因為期末專題需要做餐廳的關鍵字標籤 <br> 
 所以開始研究這個套件 <br> 
 這邊我就不講太多<br> 
 流程很簡單<br> 

# 句子/文章/長篇小說等等 都可以分析關鍵字

請使用 jieba_extra_tag.py這個版本 <br> 
old_jieba.py 是我之前想到甚麼寫甚麼出來的噁心怪物 <br> 
裡面雜亂無章 單純給我做一個紀錄用<br> 

# 使用方式

把所有文件丟到同一個檔案夾 <br> 
在執行即可 <br> 
如果有其他想嘗試判斷的文件 <br> 
就把他替換掉 <br> 

# 使用方式:<br>  **analyse_res = jieba.analyse.extract_tags(row, topK=3, allowPOS='ag')** 

(row, topK=3, allowPOS='ag') <br>
analyse_res 是變數名 請自己設定 <br>
row -> 這是要判別的資料 <br> 
topk  -> 這是權重 數字N 就是會顯示前面N個關鍵詞 <br> 
allowPOS --> 詞類選擇 可複數設定 <br> 
