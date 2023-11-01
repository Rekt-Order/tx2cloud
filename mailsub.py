import MeCab
import os

def extract_nouns_from_text(input_text):
    # MeCabのインスタンスを作成
    m = MeCab.Tagger()

    # テキストを行に分割
    subjects = input_text.splitlines()

    # 除外する文字や文字列のリスト
    exclusions = ['お', 'や', 'ご', ',', '.', '!', '?', '[', ']', ':', '-', 'co', 'jp']

    # 各行を形態素解析し、名詞のみを取得、指定された文字や文字列を除外
    noun_results = []
    for subject in subjects:
        nodes = m.parse(subject).splitlines()
        nouns = []
        for node in nodes:
            columns = node.split("\t")
            if len(columns) > 3 and "名詞" in columns[3]:  # 品詞情報が「名詞」を含む場合のみ抽出
                word = columns[0]
                # 除外リストに含まれていない単語のみを追加
                if word not in exclusions:
                    nouns.append(word)
        noun_results.append(",".join(nouns))

    return "\n".join(noun_results)
