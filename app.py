import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="UX Health Check", page_icon="🔍", layout="centered")

# 2. 진단 데이터 (순정 유지)
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

# 3. CSS (우선순위 대폭 강화)
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    * { font-family: 'Pretendard', sans-serif !important; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFEF5 !important; }
    #MainMenu, footer, header { visibility: hidden; }

    .main-card {
        background: white; padding: 40px 30px; border-radius: 40px;
        box-shadow: 0 15px 35px rgba(253, 224, 71, 0.15); margin-bottom: 20px;
        border: 1px solid #ddd; text-align: center;
    }
    .question-text { font-size: 34px; font-weight: 800; color: #334155; line-height: 1.4; }

    /* [PC 레이아웃] 버튼 중앙 */
    div[data-testid="stHorizontalBlock"]:has(div.stButton) {
        display: flex !important; justify-content: center !important; align-items: center !important;
    }
    div[data-testid="stHorizontalBlock"]:has(div.stButton) > div[data-testid="column"] {
        flex: none !important; width: auto !important;
    }

    /* 버튼 스타일 */
    div.stButton > button {
        width: 250px !important; height: 65px; border-radius: 50px; border: none;
        background-color: #eee !important; color: #333 !important;
        font-size: 18px !important; font-weight: 700 !important;
        margin: 10px !important;
    }
    div.stButton > button:hover { background-color: #475569 !important; color: #fff !important; }

    /* ★★★ 모바일 반응형 끝장내기 ★★★ */
    @media (max-width: 768px) {
        .question-text { font-size: 24px !important; }

        /* [핵심] 모든 수평 블록 가로 정렬 강제 */
        div[data-testid="stAppViewContainer"] div[data-testid="stHorizontalBlock"] {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: wrap !important;
            width: 100% !important;
            gap: 10px !important;
        }

        /* [핵심] 컬럼 너비 50% 강제 (지표 2x2 및 버튼 가로 배치 동시 해결) */
        div[data-testid="stAppViewContainer"] div[data-testid="column"] {
            flex: 1 1 calc(50% - 10px) !important;
            min-width: calc(50% - 10px) !important;
            max-width: calc(50% - 5px) !important;
        }

        div.stButton > button {
            width: 100% !important;
            margin: 0 !important;
            font-size: 14px !important;
            height: 60px !important;
        }

        /* Metric 상자 시각화 */
        [data-testid="stMetricSimple"] {
            background: white !important;
            border: 1px solid #eee !important;
            border-radius: 15px !important;
            padding: 10px 0 !important;
            width: 100% !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# 4. 세션 초기화
if 'step' not in st.session_state: st.session_state.step = 0
if 'scores' not in st.session_state: st.session_state.scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}

# 5. 메인 로직
if st.session_state.step < len(diagnostics):
    curr = st.session_state.step
    st.progress(curr / len(diagnostics))
    
    st.markdown(f'<div class="main-card"><p class="question-text">{diagnostics[curr]["q"]}</p></div>', unsafe_allow_html=True)

    # 버튼 가로 배치를 위한 columns
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("네, 준수합니다", key=f"y_{curr}"):
            st.session_state.scores[diagnostics[curr]['type']] += 1
            st.session_state.step += 1
            st.rerun()
    with btn_col2:
        if st.button("아니요, 부족합니다", key=f"n_{curr}"):
            st.session_state.step += 1
            st.rerun()
else:
    # 7. 결과 화면
    s = st.session_state.scores
    st.markdown(f'<div class="main-card"><p class="persona-title">진단 결과</p><h3>분석이 완료되었습니다.</h3></div>', unsafe_allow_html=True)
    
    st.subheader("📊 영역별 상세 지표")
    # ⚠️ 이 columns(4)가 CSS를 통해 모바일에서 2x2로 정렬됩니다.
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    m_col1.metric("시각 배려", f"{s['V']}/3")
    m_col2.metric("조작 편의", f"{s['C']}/3")
    m_col3.metric("반응/알림", f"{s['F']}/3")
    m_col4.metric("보편 설계", f"{s['I']}/3")
    
    st.write("---")
    
    # 하단 버튼 가로 정렬
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        if st.button("전문 컨설팅 문의하기", key="final_contact_btn"):
            st.success("접수 완료!")
    with res_col2:
        if st.button("다시 테스트하기", key="final_restart_btn"):
            st.session_state.step = 0
            st.session_state.scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}
            st.rerun()
