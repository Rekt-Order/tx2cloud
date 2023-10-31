from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io

def generate_wordcloud_image(input_text):
    # ワードクラウドの設定
    wordcloud = WordCloud(
        background_color="white",
        width=800,
        height=600,
        max_words=200,
        max_font_size=100,
        font_path="C:\\Users\\ns9999\\python\\DelaGothicOne-Regular.ttf",
        colormap="tab10",
        stopwords=set(),
        contour_width=3,
        contour_color="steelblue"
    )

    # ワードクラウドを生成
    wordcloud.generate(input_text)

    # 画像をバイト形式で保存
    img_bytes = io.BytesIO()
    wordcloud.to_image().save(img_bytes, format='PNG')
    return img_bytes.getvalue()
