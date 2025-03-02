import streamlit as st
import joblib
import numpy as np

# 모델 불러오기
@st.cache_data
def load_model():
    return joblib.load("model.pkl")  # GitHub에 업로드한 model.pkl 파일

model = load_model()

# Streamlit UI
st.title("📈 주식 예측 AI")
st.write("감성 점수를 입력하고 예측을 실행하세요.")

# 감성 점수 입력 필드 추가
sentiment_score = st.number_input("감성 점수 입력 (1~10)", min_value=1, max_value=10, step=1)

# 예측 실행 버튼
if st.button("예측 실행"):
    # 입력값을 모델이 처리할 수 있는 형태로 변환
    input_data = np.array([[sentiment_score]])  # 2차원 배열로 변환
    prediction = model.predict(input_data)  # 예측 실행
    
    # 예측 결과 출력
    st.success(f"🔮 예측 결과: {prediction[0]:.2f}")  # 소수점 2자리까지 표시

