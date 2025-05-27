import streamlit as st
import requests
from datetime import date, datetime

# -------------------------------------
# NASA API 설정
# -------------------------------------
API_KEY = "DEMO_KEY"  # NASA 공식 데모 키
API_URL = "https://api.nasa.gov/planetary/apod"

# -------------------------------------
# Streamlit 앱 UI
# -------------------------------------
st.title("🚀 NASA 오늘의 우주 사진")
st.write("NASA에서 제공하는 천문 사진을 날짜별로 볼 수 있어요!")

# 날짜 입력 위젯 (최대 오늘 날짜까지 선택 가능)
selected_date = st.date_input(
    "보고 싶은 날짜를 선택하세요:",
    value=date.today(),
    max_value=date.today()
)

# 날짜 문자열로 변환 (API에 맞게)
date_str = selected_date.isoformat()

# API 요청 파라미터
params = {
    "api_key": API_KEY,
    "date": date_str
}

# API 호출
response = requests.get(API_URL, params=params)
data = response.json()

# 결과 출력
if response.status_code == 200:
    st.subheader(f"📅 날짜: {date_str}")
    st.markdown(f"### 🌌 {data['title']}")
    st.image(data['url'], caption=data.get('title', ''), use_container_width=True)
    st.write(data.get('explanation', '설명이 없습니다.'))
else:
    st.error("NASA API로부터 데이터를 가져오지 못했습니다.")
    st.write(data)
