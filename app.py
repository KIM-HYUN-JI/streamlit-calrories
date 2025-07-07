import streamlit as st

st.title("🍱 하루 칼로리 계산기")

sex = st.radio("성별을 선택하세요:", ["남자", "여자"])
age = st.number_input("나이", min_value=10, max_value=100, value=25)
height = st.number_input("키 (cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("체중 (kg)", min_value=30, max_value=200, value=65)

activity_levels = {
    "아주 낮음 (거의 활동 없음)": 1.2,
    "가벼움 (가벼운 활동)": 1.375,
    "중간 (주 3~5일 운동)": 1.55,
    "높음 (매일 운동)": 1.725,
    "매우 높음 (하드 트레이닝)": 1.9
}
activity = st.selectbox("활동 수준", list(activity_levels.keys()))
activity_factor = activity_levels[activity]

if sex == "남자":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

tdee = bmr * activity_factor

st.subheader("결과")
st.write(f"👉 기초대사량 (BMR): **{bmr:.0f} kcal**")
st.write(f"👉 하루 유지 칼로리 (TDEE): **{tdee:.0f} kcal**")
st.write(f"🔹 다이어트용: {tdee - 500:.0f} ~ {tdee - 300:.0f} kcal/day")
st.write(f"🔹 벌크업용: {tdee + 300:.0f} ~ {tdee + 500:.0f} kcal/day")
