from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 定義要生成文字雲的文字
text = "Python is great for data analysis. Python is popular for machine learning."

# 創建 WordCloud 物件
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# 使用 recolor() 來改變文字顏色，這裡將文字顏色改為藍色
wordcloud = wordcloud.recolor(color_func=lambda *args, **kwargs: "blue")

# 顯示 WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 不顯示座標軸
plt.show()
