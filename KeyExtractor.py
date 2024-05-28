# 匯入 re 模組，用於正則表達式的操作
import re

# 匯入自定義的 StopWord_en 模組
import StopWord_en

# 從Sorting模組中匯入bubble_sort方法，用於排序
from Sorting import bubble_sort


# 移除文本中的停用詞
def remove_stopwords(text):
    # 將輸入的文本以空格分割成單詞列表
    words = text.split()
    # 創建一個空字串，用來串接過濾後的單詞字串
    filtered_words = ""
    for word in words:
        if word.lower() not in StopWord_en.stop_words:
            # 將所有不含在停用詞列表的單詞重新組合成字串
            filtered_words = filtered_words + " " + word
    # 回傳過濾後的單詞字串
    return filtered_words


# 找出文本中出現頻率最高且非停用詞的關鍵詞
def extract_keywords(text):
    # 使用 remove_stopwords 函式去除停用詞
    filtered_text = remove_stopwords(text)

    # 使用正則表達式找出所有的單詞，並轉換為小寫
    words = re.findall(r"\w+", filtered_text.lower())
    # 建立空列表用於接下來儲存單詞及其出現次數
    words_freq = []
    # 使用 set 去除words重複的元素
    unique_words = set(words)
    # 用迴圈對每個唯一單詞進行計算
    for word in unique_words:
        # 將該單詞及其出現次數添加到 words_freq 字典中
        words_freq.append([word, words.count(word)])
    # 使用 Counter 計算單詞出現的頻率
    words_freq_sorted = bubble_sort(words_freq)
    # 取得出現頻率最高的前 5 個詞彙作為關鍵詞
    top_keywords = words_freq_sorted[:5]
    # 返回最常見的關鍵詞列表
    return top_keywords


if __name__ == "__main__":
    # 指定要打開的文件路徑
    file_path = r"LV2/TextAnalysis/text_file.txt"

    with open(file_path, "r") as file:
        # 讀取文件內容
        text = file.read()
        # 使用 extract_keywords 函數提取關鍵詞
        keywords = extract_keywords(text)
        print("提取的關鍵詞:")
        for keyword, frequency in keywords:
            # 輸出提取到的關鍵詞及其頻率
            print(f"{keyword}: {frequency}")
