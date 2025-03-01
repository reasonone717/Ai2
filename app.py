import streamlit as st

# 제목 설정
st.title("AI 주가 예측 앱")

# 간단한 설명
st.write("이 앱은 주가 예측을 위한 AI 모델을 기반으로 작동합니다.")

# 입력 필드 추가
user_input = st.text_input("종목 코드를 입력하세요:", "")

# 버튼 추가
if st.button("예측 시작"):
    st.write(f"'{user_input}' 종목에 대한 예측을 진행 중입니다... 🚀")

st.write("데이터 분석 및 시각화 기능은 차후 업데이트 예정입니다!")

