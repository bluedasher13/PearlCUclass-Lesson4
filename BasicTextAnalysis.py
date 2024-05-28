# 匯入正則表達式模組
import re

# 指定要分析的文本檔案路徑
file_path = r"LV2/TextAnalysis/text_file.txt"
# 創建一個文本檔案相關類別的實例（模式"r"為唯讀），並指定給file這個變數後續可以操作指定的文本檔案
file = open(file_path, "r")
# 讀取文本內容，並用text這個變數接收回傳的內容字串
text = file.read()

############# 開始進行文本分析 #############
# 使用正則表達式進行句子拆分，考慮了.!?作為句子的結束標點，並計算句子數量
num_sentences = len(re.split("[.!?]", text))

############# 開始計算詞頻 #############
# 使用正則表達式找出所有的單詞，並轉換為小寫
words = re.findall(r"\w+", text.lower())
# 建立空列表用於接下來儲存單詞及其出現次數
words_freq = []
# 使用 set 去除words重複的元素
unique_words = set(words)
# 用迴圈對每個唯一單詞進行計算
for word in unique_words:
    # 計算目前單詞在原始單詞列表中的出現次數
    count = words.count(word)
    # 將該單詞及其出現次數作為列表添加到 words_freq 列表中
    words_freq.append([word, count])
############# 結束計算詞頻 #############

# 計算單詞數量
num_words = len(words)

# 顯示單詞數量統計
print(f"字數統計：{num_words} 個字")
# 顯示句子數量統計
print(f"句數統計：{num_sentences} 句")
# 顯示詞頻統計
print(f"詞頻統計：")
for word_freq in words_freq:
    print(f"{word_freq[0]} 出現 {word_freq[1]} 次")
############# 文本分析結束 #############

# 在分析結束後需記得關閉和釋放開啟的檔案資源
file.close()
