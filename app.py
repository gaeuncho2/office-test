import streamlit as st

# 1. 페이지 설정 (최상단)
st.set_page_config(page_title="UX Health Check", page_icon="🔍", layout="centered")

# 2. 진단 데이터 정의
diagnostics = [
    {"q": "배경과 텍스트가 잘 구분되며 저시력자도 읽기 편한가요?", "type": "V"},
    {"q": "모든 입력 폼에 무엇을 적어야 하는지 명확한 레이블이 있나요?", "type": "I"},
    {"q": "중요한 버튼의 크기가 조작 오작동을 방지할 만큼 충분히 큰가요?", "type": "C"},
    {"q": "로딩이나 데이터 처리 중 사용자가 기다려야 함을 시각적으로 알리나요?", "type": "F"},
    {"q": "키보드나 전용 패드만으로 모든 메뉴 이동이 가능한가요?", "type": "C"},
    {"q": "전문 용어 대신 누구나 이해하기 쉬운 보편적인 단어를 사용하나요?", "type": "I"},
    {"q": "이미지에 대한 대체 텍스트가 스크린 리더용으로 제공되고 있나요?", "type": "V"},
    {"q": "오류 메시지는 구체적이고 해결 방법을 함께 제시하나요?", "type": "F"},
    {"q": "페이지의 구조가 일관되어 다음 행동을 예측하기 쉬운가요?", "type": "I"},
    {"q": "색상만으로 정보를 전달하지 않고 아이콘이나 텍스트를 병기하나요?", "type": "V"},
    {"q": "결제나 전송 전, 마지막으로 확인하거나 취소할 수 있는 기회를 주나요?", "type": "C"},
    {"q": "제한 시간이 있는 경우, 사용자가 시간을 연장할 수 있는 옵션이 있나요?", "type": "F"}
]

# 3. 아기자기한 에이전시 스타일 CSS 주입 (반응형 보완)
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    
    /* 전체 공통 설정 */
    * {font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif !important;}
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #FFFEF5 !important;
        color: #1E293B;
    }

    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}

    /* 메인 카드 컨테이너 */
    .main-card {
        background: white;
        padding: 40px 30px;
        border-radius: 40px;
        box-shadow: 0 15px 35px rgba(253, 224, 71, 0.15);
        margin-bottom: 20px;
        border: 1px solid #ddd;
        text-align: center;
    }

    /* 질문 텍스트 스타일 (PC 기준) */
    .question-text {
        font-size: 50px;
        font-weight: 800;
        color: #334155;
        line-height: 1.4;
        word-break: keep-all;
    }

    /* 버튼 레이아웃 정렬 (PC) */
    div[data-testid="stHorizontalBlock"]:has(div.stButton) {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        gap: 0px !important;
    }

    div[data-testid="stHorizontalBlock"]:has(div.stButton) > div {
        flex: none !important;
        width: auto !important;
    }

    /* 버튼 기본 스타일 */
    div.stButton > button {
        width: 250px !important;
        height: 65px;
        border-radius: 50px;
        border: none;
        background-color: #eee !important;
        color: #333 !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin: 10px !important;
    }

    div.stButton > button:hover, div.stButton > button:focus {
        background-color: #475569 !important;
        color: #fff !important;
        font-weight: 900 !important;
        text-decoration: underline;
        transform: scale(1.05);
    }

    /* Metric 결과창 방어 */
    div[data-testid="stHorizontalBlock"]:has(div[data-testid="stMetricSimple"]) {
        display: flex !important;
        justify-content: space-between !important;
        width: 100% !important;
    }

    .stProgress > div > div > div > div {
        background-color: #4ADE80;
        border: 1px solid #555555;
    }
    
    .persona-title {
        font-size: 36px;
        font-weight: 900;
        background: linear-gradient(to right, #EAB308, #22C55E);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    /* ★ 모바일 반응형 핵심 수정 ★ */
    @media (max-width: 768px) {
        .question-text {
            font-size: 28px !important; /* 모바일에서는 폰트 크기 대폭 축소 */
            line-height: 1.3 !important;
        }
        
        .main-card {
            padding: 30px 15px !important;
            border-radius: 25px !important;
        }

        /* 모바일에서 버튼 세로 정렬 */
        div[data-testid="stHorizontalBlock"]:has(div.stButton) {
            flex-direction: column !important;
        }

        div.stButton > button {
            width: 100% !important; /* 버튼 너비 가득 채우기 */
            max-width: 300px;
            margin: 5px 0 !important;
        }

        /* 결과창 Metric 2열 배치 */
        div[data-testid="stHorizontalBlock"]:has(div[data-testid="stMetricSimple"]) > div {
            min-width: 45% !important;
        }
        
        h1 { font-size: 30px !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# 4. 세션 상태 초기화
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}

# 5. 헤더 섹션
st.markdown("<p style='text-align: center; color: #76A1BE; font-weight: 800; letter-spacing: 2px; margin-bottom: 0;'>UX/UI CONSULTING</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-weight: 800; margin-top: 10px; margin-bottom: 40px;'>내 서비스 자가진단하기 📝</h1>", unsafe_allow_html=True
