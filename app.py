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
        font-size: 34px;
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

  /* ★ 모바일 레이아웃 강제 교정 (최종) ★ */
    @media (max-width: 768px) {
        /* 1. 질문 텍스트 및 카드 최적화 */
        .question-text {
            font-size: 24px !important; 
            line-height: 1.4 !important;
            word-break: keep-all;
        }
        .main-card { padding: 30px 15px !important; }

        /* 2. 버튼 가로 정렬 강제 (기존 그리드 무력화) */
        div[data-testid="stHorizontalBlock"]:has(div.stButton) {
            display: flex !important;
            flex-direction: row !important; /* 가로 유지 */
            flex-wrap: nowrap !important; /* 절대 줄바꿈 금지 */
            justify-content: center !important;
            width: 100% !important;
            gap: 10px !important;
        }

        /* 버튼을 감싸는 각 컬럼 요소 강제 확장 */
        div[data-testid="stHorizontalBlock"]:has(div.stButton) > div[data-testid="column"] {
            width: 50% !important; /* 정확히 절반 */
            flex: 1 1 0% !important;
            min-width: 0 !important;
        }

        div.stButton > button {
            width: 100% !important; /* 부모 너비 꽉 채우기 */
            height: 60px !important;
            font-size: 15px !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        /* 3. 결과창 지표(Metric) 2x2 그리드 강제 */
        div[data-testid="stHorizontalBlock"]:has(div[data-testid="stMetricSimple"]) {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: wrap !important; /* 2개씩 끊기 위해 줄바꿈 허용 */
            justify-content: space-between !important;
            width: 100% !important;
            gap: 10px !important;
        }

        /* Metric 각 컬럼을 50% 미만으로 설정하여 한 줄에 2개씩 오도록 유도 */
        div[data-testid="stHorizontalBlock"]:has(div[data-testid="stMetricSimple"]) > div[data-testid="column"] {
            width: calc(50% - 10px) !important;
            flex: 1 1 calc(50% - 10px) !important;
            min-width: 140px !important;
            background: #ffffff !important;
            border-radius: 15px !important;
            border: 1px solid #eee !important;
            padding: 10px 0 !important;
        }

        /* Metric 내부 레이아웃 중앙 정렬 */
        [data-testid="stMetricSimple"] {
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
        }
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
st.markdown("<h1 style='text-align: center; font-weight: 800; margin-top: 10px; margin-bottom: 40px;'>내 서비스 자가진단하기 📝</h1>", unsafe_allow_html=True)

# 6. 메인 로직
if st.session_state.step < len(diagnostics):
    total_q = len(diagnostics)
    current_q_idx = st.session_state.step
    progress_val = current_q_idx / total_q
    st.progress(progress_val)
    st.write(f"<p style='text-align: right; color: #64748B;'>{current_q_idx + 1} / {total_q}</p>", unsafe_allow_html=True)

    q_text = diagnostics[current_q_idx]['q']
    st.markdown(f"""
        <div class="main-card">
            <p class="question-text">{q_text}</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("네, 준수합니다", key=f"yes_{current_q_idx}"):
            st.session_state.scores[diagnostics[current_q_idx]['type']] += 1
            st.session_state.step += 1
            st.rerun()
    with col2:
        if st.button("아니요, 부족합니다", key=f"no_{current_q_idx}"):
            st.session_state.step += 1
            st.rerun()

else:
    s = st.session_state.scores
    
    def get_persona(s):
        total = sum(s.values())
        if total >= 11: return "스마트 가이드 돌고래", "모두에게 친절한 지능형 서비스", "최고의 접근성입니다! 전문가의 디테일 한 스푼만 더하면 완벽합니다."
        if s['V'] <= 1: return "눈 가린 코끼리", "시각적 장벽이 높은 거대 서비스", "시각 요소 개선이 시급합니다. 고령층 이탈률이 매우 높을 것으로 보입니다."
        if s['C'] <= 1: return "잠자는 거북이", "조작이 답답한 미로형 서비스", "사용자 동선 재설계가 필요합니다. 터치 및 키보드 조작성을 높여주세요."
        if s['F'] <= 1: return "까칠한 고슴도치", "피드백이 불친절한 예민한 서비스", "오류 안내와 상태 피드백을 강화하여 사용자 심리적 불안을 해소하세요."
        return "과묵한 진돗개", "기본은 하지만 센스가 부족한 서비스", "기능은 작동하지만, 사용자 배려를 위한 UX 디테일 보완이 권장됩니다."

    p_name, p_sub, p_desc = get_persona(s)

    st.markdown(f"""
        <div class="main-card">
            <p class="persona-title">{p_name}</p>
            <h3>{p_sub}</h3>
            <p style="font-size: 18px; color: #475569;">{p_desc}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📊 영역별 상세 지표")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("시각 배려", f"{s['V']}/3")
    col2.metric("조작 편의", f"{s['C']}/3")
    col3.metric("반응/알림", f"{s['F']}/3")
    col4.metric("보편 설계", f"{s['I']}/3")
    
    st.write("---")
    
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        if st.button("전문 컨설팅 문의하기", key="final_contact"):
            st.success("📩 요청이 접수되었습니다! 곧 연락드릴게요.")
    with res_col2:
        if st.button("다시 테스트하기", key="final_restart"):
            st.session_state.step = 0
            st.session_state.scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}
            st.rerun()
