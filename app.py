import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------
# 앱 제목 및 설명
# -------------------------------------
st.title("🏠 제로에너지 하우스 시뮬레이터")
st.write("가정의 에너지 소비를 분석하고, 다양한 절전 기술을 적용하여 전기요금을 절감할 수 있는 방법을 시뮬레이션합니다.")

# -------------------------------------
# 가전제품 기본 소비 전력 사전 (W 단위)
# -------------------------------------
device_power = {
    "냉장고": 150,
    "세탁기": 500,
    "TV": 100,
    "에어컨": 1500,
    "컴퓨터": 300,
    "전자레인지": 1000
}

# -------------------------------------
# 사용자 입력: 가전제품 선택 및 사용 시간
# -------------------------------------
st.subheader("1️⃣ 가전제품 사용 정보 입력")

device = st.selectbox("사용하는 가전제품을 선택하세요:", list(device_power.keys()))
hours_per_day = st.slider("하루 사용 시간 (시간 단위)", 0.0, 24.0, 1.0, step=0.5)

# -------------------------------------
# 절전 기술 적용 여부 선택
# -------------------------------------
st.subheader("2️⃣ 절전 기술 적용 여부")

led_lighting = st.checkbox("LED 조명 사용 중인가요?", value=False)
inverter_appliance = st.checkbox("인버터 냉장고 사용 중인가요?", value=False)

# -------------------------------------
# 전기요금 계산
# -------------------------------------
unit_price = 130  # 원/kWh

# 기본 소비 전력 불러오기
power_w = device_power[device]

# 절전 기술 적용
if led_lighting:
    power_w *= 0.9  # 소비 전력 10% 절감
if inverter_appliance:
    power_w *= 0.8  # 소비 전력 20% 절감

# W → kW 단위로 변환
power_kw = power_w / 1000

# 하루 및 한 달 전력량 계산
daily_energy = power_kw * hours_per_day
monthly_energy = daily_energy * 30
monthly_cost = monthly_energy * unit_price

# -------------------------------------
# 결과 출력
# -------------------------------------
st.subheader("💰 예상 전기요금")

st.write(f"📌 전자제품: **{device}**")
st.write(f"🔋 하루 사용 전력: **{daily_energy:.2f} kWh**")
st.write(f"📅 한 달 사용 전력: **{monthly_energy:.2f} kWh**")
st.write(f"💸 예상 전기요금: **{monthly_cost:,.0f} 원**")

# 절전 기술 적용 메시지
if led_lighting or inverter_appliance:
    st.success("✅ 절전 기술이 적용되어 소비 전력이 감소했습니다!")

# -------------------------------------
# 결과 시각화
# -------------------------------------
st.subheader("📊 전기요금 절감 효과 시각화")

labels = ['기본 소비 전력', '절전 기술 적용 후']
sizes = [device_power[device], power_w]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # 원형 그래프 유지
st.pyplot(plt)
