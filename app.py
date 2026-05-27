import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="UX Health Check", page_icon="🔍", layout="centered")

# 2. 진단 데이터 (기존과 동일)
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

# 3. 핵심 CSS 수정 (가로 꽉 참 & 모바일 정렬 유지)
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    * { font-family: 'Pretendard', sans-serif !important; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFEF5 !important; overflow-x: hidden; }
    #MainMenu, footer, header { visibility: hidden; }

    /* 메인 카드 */
    .main-card {
        background: white; padding: 40px 20px; border-radius: 40px;
        box-shadow: 0 15px 35px rgba(253, 224, 71, 0.15); margin-bottom: 30px;
        border: 1px solid #ddd; text-align: center;
    }
    .question-text { font-size: 22px; font-weight: 800; color: #334155; line-height: 1.5; word-break: keep-all; }

    /* ★ 가로 정렬 & 꽉 차게 만드는 핵심 로직 ★ */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important; /* 모바일에서도 무조건 가로 */
        flex-wrap: nowrap !important;
        gap: 10px !important; /* 버튼 사이 간격 */
        width: 100% !important;
    }

    div[data-testid="column"] {
        flex: 1 1 50% !important; /* 각 컬럼이 정확히 절반 차지 */
        min-width: 0 !important;
    }

    /* 버튼 스타일 */
    div.stButton > button {
        width: 100% !important; /* 컬럼 너비에 꽉 차게 */
        height: 65px;
        border-radius: 50px;
        border: none;
        background-color: #eee;
        color: #333;
        font-size: 16px;
        font-weight: 700;
        margin: 0 !important;
        padding: 0 !important;
    }

    div.stButton > button:hover {
        background-color: #475569;
        color: #fff;
    }

    /* 모바일 전용 미세 조정 (390px 근처) */
    @media (max-width: 768px) {
        .main-card { padding: 30px 15px !important; }
        .question-text { font-size: 18px !important; }
        div.stButton > button {
            height: 60px !important;
            font-size: 14px !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# 4. 세션 초기화 (기존과 동일)
if 'step' not in st.session_state: st.session_state.step = 0
if 'scores' not in st.session_state: st.session_state.scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}

# 5. 헤더
st.markdown("<p style='text-align: center; color: #76A1BE; font-weight: 800; letter-spacing: 2px; margin-top:20px;'>UX/UI CONSULTING</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-weight: 800; margin-bottom:30px;'>📝 내 서비스 자가진단</h1>", unsafe_allow_html=True)

# 6. 메인 로직
if st.session_state.step < len(diagnostics):
    curr = st.session_state.step
    st.progress(curr / len(diagnostics))
    st.write(f"<p style='text-align: right; margin-bottom: 5px; font-weight:bold;'>{curr + 1} / {len(diagnostics)}</p>", unsafe_allow_html=True)

    st.markdown(f'<div class="main-card"><p class="question-text">{diagnostics[curr]["q"]}</p></div>', unsafe_allow_html=True)

    # st.columns에 gap을 주어 버튼 사이 여백 조절
    col1, col2 = st.columns(2)
    with col1:
        if st.button("네, 준수합니다", key=f"y_{curr}"):
            st.session_state.scores[diagnostics[curr]['type']] += 1
            st.session_state.step += 1
            st.rerun()
    with col2:
        if st.button("아니요, 부족합니다", key=f"n_{curr}"):
            st.session_state.step += 1
            st.rerun()
else:
    # 결과 화면 (생략 없이 유지)
    s = st.session_state.scores
    def get_persona(s):
        total = sum(s.values())
        if total >= 11: return "스마트 가이드 돌고래", "모두에게 친절한 지능형 서비스"
        return "과묵한 진돗개", "기본은 하지만 센스가 부족한 서비스"

    p_name, p_sub = get_persona(s)
    st.markdown(f'<div class="main-card"><p style="font-size:28px; font-weight:900;">{p_name}</p><h3>{p_sub}</h3></div>', unsafe_allow_html=True)
    
    st.subheader("📊 영역별 상세 지표")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("시각", f"{s['V']}/3")
    c2.metric("조작", f"{s['C']}/3")
    c3.metric("반응", f"{s['F']}/3")
    c4.metric("보편", f"{s['I']}/3")
    
    st.write("---")
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.button("문의하기", key="final_contact", use_container_width=True)
    with res_col2:
        if st.button("다시 하기", key="final_restart", use_container_width=True):
            st.session_state.step = 0
            st.session_state.scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}
            st.rerun()
