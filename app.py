import streamlit as st
import requests
from datetime import date

# -------------------------------------
# NASA API 설정
# -------------------------------------
API_KEY = "DEMO_KEY"  # NASA 공식 데모 키
API_URL = "https://api.nasa.gov/planetary/apod"

# 오늘 날짜
today = date.today().isoformat()

# API 요청 파라미터
params = {
    "api_key": API_KEY,
    "date": today
}

# -------------------------------------
# API 호출
# -------------------------------------
response = requests.get(API_URL, params=params)
data = response.json()

# -------------------------------------
# Streamlit 앱 UI
# -------------------------------------
st.title("🚀 NASA 오늘의 우주 사진")
st.write("NASA에서 제공하는 오늘의 천문 사진입니다. 매일매일 우주를 감상해보세요!")

if response.status_code == 200:
    st.subheader(f"📅 날짜: {today}")
    st.markdown(f"### 🌌 {data['title']}")
    st.image(data['url'], caption=data.get('title', ''), use_container_width=True)  # 수정된 부분
    st.write(data.get('explanation', '설명이 없습니다.'))
else:
    st.error("NASA API로부터 데이터를 가져오지 못했습니다.")
    st.write(data)
