# ベースとなるイメージを指定
FROM python:3.8-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコンテナにコピー
COPY requirements.txt ./
COPY app.py ./
COPY Wcloud.py ./
COPY mailsub.py ./
# その他の必要なファイルやディレクトリもコピーしてください

# 依存関係のインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションの起動コマンドを指定
CMD ["python", "app.py"]
