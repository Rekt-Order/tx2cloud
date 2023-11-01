from flask import Flask, render_template, request, send_file
import io  # このインポートを追加
import mailsub
import Wcloud

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        nouns = mailsub.extract_nouns_from_text(text)
        img = Wcloud.generate_wordcloud_image(nouns)
        return send_file(io.BytesIO(img), mimetype='image/png', as_attachment=True, download_name='wordcloud.png')
    return render_template('index.html')  # これは基本的な入力フォームを持つHTMLを想定しています。

if __name__ == '__main__':
    app.run()
