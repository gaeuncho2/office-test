import streamlit as st

# 1. 페이지 설정 및 기본 테마
st.set_page_config(page_title="UX Health Check | 전문 진단 서비스", page_icon="🔍", layout="centered")

# 2. 고퀄리티 에이전시 스타일 CSS 주입
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    /* 전체 배경 및 폰트 */
    html, body, [class*="css"] {
        font-family: 'Pretendard', sans-serif;
        background-color: #F8FAFC;
        color: #1E293B;
    }

    /* 스트림릿 기본 요소 숨기기 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 메인 카드 컨테이너 */
    .main-card {
        background: white;
        padding: 50px 40px;
        border-radius: 30px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.05);
        margin-bottom: 30px;
        border: 1px solid #F1F5F9;
        text-align: center;
    }

    /* 질문 텍스트 스타일 */
    .question-text {
        font-size: 28px;
        font-weight: 700;
        color: #0F172A;
        line-height: 1.5;
        margin-bottom: 10px;
    }

    /* 버튼 스타일 개조 */
    div.stButton > button {
        width: 100%;
        height: 70px;
        border-radius: 20px;
        border: 1px solid #E2E8F0;
        background-color: white;
        color: #475569;
        font-size: 20px;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        border-color: #10B981;
        color: #10B981;
        background-color: #F0FDF4;
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(16, 185, 129, 0.1);
    }

    /* 프로그래스 바 */
    .stProgress > div > div > div > div {
        background-color: #10B981;
    }

    /* 결과 박스 */
    .result-box {
        background: #F8FAFC;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #10B981;
        margin-top: 20px;
    }

    .persona-title {
        font-size: 32px;
        font-weight: 800;
        color: #10B981;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 세션 상태 초기화
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}

# 4. 진단 문항 데이터 (4개 축 x 3문항 = 12문항)
# V:시각, C:조작, F:피드백, I:인지적포용
diagnostics
