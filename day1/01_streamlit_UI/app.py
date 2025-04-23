import streamlit as st
import pandas as pd
import numpy as np
import time

# ページ設定
st.set_page_config(page_title="改善版 Streamlit デモ", layout="wide")

# サイドバーのナビゲーション
page = st.sidebar.radio("表示するセクションを選んでください", 
                        ["ホーム", "インタラクティブUI", "データ表示", "ファイルアップロード", "グラフ表示"])

# ホーム
if page == "ホーム":
    st.title("Streamlit 改善版デモ")
    st.markdown("ようこそ！このアプリでは、Streamlitの様々な機能を体験できます。")
    st.info("左のサイドバーからセクションを選んでください。")

# インタラクティブUI
elif page == "インタラクティブUI":
    st.header("インタラクティブUI")
    
    name = st.text_input("あなたの名前は？", "ゲスト")
    age = st.slider("年齢を選択してください", 0, 100, 25)
    lang = st.selectbox("好きなプログラミング言語は？", ["Python", "JavaScript", "C++", "Rust"])

    if st.button("送信"):
        st.success(f"{name}さん、{age}歳、{lang}が好きなんですね！")

# データ表示
elif page == "データ表示":
    st.header("サンプルデータの表示")
    df = pd.DataFrame({
        '名前': ['田中', '鈴木', '佐藤', '高橋', '伊藤'],
        '年齢': [25, 30, 22, 28, 33],
        '都市': ['東京', '大阪', '福岡', '札幌', '名古屋']
    })
    st.dataframe(df)

# ファイルアップロード
elif page == "ファイルアップロード":
    st.header("CSVファイルアップロード")
    uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("アップロードしたデータ:")
        st.dataframe(df)

# グラフ表示
elif page == "グラフ表示":
    st.header("グラフの表示例")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.line_chart(chart_data)

# フッター
st.divider()
st.caption("Created with ❤️ by AI工学講義用 Streamlitデモ")
