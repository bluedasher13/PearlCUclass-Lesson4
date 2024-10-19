import jieba
from collections import Counter

# 示例文本
text = "今天是個好日子，我們一起去公園散步吧！天氣真好。"

# 計算字數
char_count = len(text)

# 計算句數
sentence_count = len(text.split('。')) - 1  # 或使用其他標點符號來拆分句子，如'！'、'？'

# 使用 jieba 進行中文分詞
words = jieba.lcut(text)

# 計算詞頻
word_freq = Counter(words)

# 輸出結果
print(f"字數: {char_count}")
print(f"句數: {sentence_count}")
print("詞頻分析:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")