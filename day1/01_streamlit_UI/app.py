import streamlit as st
import pandas as pd
import numpy as np
import time

# ページ設定
st.set_page_config(page_title="改善版 Streamlit デモ", layout="wide")

# サイドバーのナビゲーション
page = st.sidebar.radio("表示するセクションを選んでください", 
                        ["ホーム", "インタラクティブUI", "ファイルアップロード"])

# ホーム
if page == "ホーム":

    st.title("Streamlitの体験")
    st.markdown("このアプリでは、Streamlitの様々な機能を体験できます。")
    st.info("左のサイドバーからセクションを選んでください。")

    st.header("🩺 今日の健康状態チェック")

    with st.form("health_check_form"):
        mood = st.slider("今日の気分は？（1: 最悪 〜 10: 絶好調）", 1, 10, 5)
        sleep_hours = st.number_input("昨夜の睡眠時間（時間）", min_value=0.0, max_value=24.0, value=7.0)
        temperature = st.number_input("今朝の体温（℃）", min_value=35.0, max_value=42.0, value=36.5)
        appetite = st.selectbox("食欲はありますか？", ["ある", "少しある", "あまりない", "全くない"])
        
        submitted = st.form_submit_button("チェックする")

    if submitted:
        st.subheader("📝 チェック結果")
        if temperature >= 37.5:
            st.warning("熱があります。無理せず休みましょう。")
        elif mood <= 3 or appetite in ["あまりない", "全くない"]:
            st.info("体調が良くないかもしれません。しっかり休んでください。")
        else:
            st.success("特に問題なさそうです。今日も元気に過ごしましょう！")

# インタラクティブUI
elif page == "インタラクティブUI":
    st.header("インタラクティブUI")
    
    name = st.text_input("あなたの名前は？", "ゲスト")
    age = st.slider("年齢を選択してください", 0, 100, 25)
    lang = st.selectbox("好きなプログラミング言語は？", ["Python", "JavaScript", "C++", "Rust"])

    if st.button("送信"):
        st.success(f"{name}さん、{age}歳、{lang}が好きなんですね！")

# ファイルアップロード
elif page == "ファイルアップロード":
    st.header("CSVファイルアップロード")
    uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("アップロードしたデータ:")
        st.dataframe(df)

# フッター
st.divider()
st.caption("Created with ❤️ by AI工学講義用 Streamlitデモ")
