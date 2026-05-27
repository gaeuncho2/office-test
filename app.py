import streamlit as st

# 1. 페이지 기본 설정 및 디자인 테마 정의
st.set_page_config(page_title="UX/UI Health Check", page_icon="✨", layout="centered")

# 2. 강력한 CSS 주입 (디자인 컨설팅사 스타일)
st.markdown("""
    <style>
    /* 전체 배경 및 폰트 */
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    html, body, [class*="css"] {
        font-family: 'Pretendard', sans-serif;
        background-color: #F8FAFC;
    }

    /* 스트림릿 기본 헤더/푸터 숨기기 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 메인 카드 컨테이너 */
    .main-card {
        background: white;
        padding: 40px;
        border-radius: 24px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid #E2E8F0;
    }

    /* 질문 텍스트 스타일 */
    .question-text {
        font-size: 26px;
        font-weight: 700;
        color: #0F172A;
        line-height: 1.4;
        margin-bottom: 30px;
    }

    /* 버튼 스타일 개조 */
    div.stButton > button {
        width: 100%;
        height: 60px;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        background-color: white;
        color: #475569;
        font-size: 18px;
        font-weight: 500;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        border-color: #10B981;
        color: #10B981;
        background-color: #F0FDF4;
        transform: translateY(-2px);
    }

    /* 프로그래스 바 스타일 */
    .stProgress > div > div > div > div {
        background-color: #10B981;
    }
    
    /* 결과 강조 박스 */
    .result-box {
        background: #F0FDF4;
        border-left: 5px solid #10B981;
        padding: 20px;
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# 세션 상태 관리
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}

# 문항 데이터
diagnostics = [
    {"q": "시각 장애인을 위한 '이미지 대체 텍스트'가 적절히 제공되고 있나요
