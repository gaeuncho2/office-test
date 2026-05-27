import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="UX Health Check", page_icon="🔍", layout="centered")

# 2. 진단 데이터
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

# 3. CSS (반응형 2열 & 2x2 그리드 강제)
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    * { font-family: 'Pretendard', sans-serif !important; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFEF5 !important; }
    #MainMenu, footer, header { visibility: hidden; }

    .main-card {
        background: white; padding: 40px 20px; border-radius: 40px;
        box-shadow: 0 15px 35px rgba(253, 224, 71, 0.15); margin-bottom: 20px;
        border: 1px solid #ddd; text-align: center;
    }
    .question-text { font-size: 34px; font-weight: 800; color: #334155; line-height: 1.4; }

    /* [결과창 2x2 강제] */
    [data-testid="stHorizontalBlock"] { display: flex !important; flex-wrap: wrap !important; flex-direction: row !important; gap: 10px !important; }
    [data-testid="column"] { flex: 1 1 calc(50% - 10px) !important; min-width: calc(50% - 10px) !important; max-width: 50% !important; }

    /* [커스텀 버튼 스타일] */
    .btn-container { display: flex; justify-content: center; gap: 20px; width: 100%; margin-top: 20px; }
    .custom-btn {
        width: 250px; height: 65px; border-radius: 50px; border: none;
        background-color: #eee; color: #333; font-size: 18px; font-weight: 700;
        text-decoration: none; display: flex; align-items: center; justify-content: center;
        cursor: pointer; transition: 0.3s;
    }
    .custom-btn:hover { background-color: #475569; color: white; }

    @media (max-width: 768px) {
        .question-text { font-size: 22px !important; }
        .btn-container { gap: 10px; padding: 0 10px; }
        .custom-btn { width: 50% !important; height: 60px; font-size: 15px; }
        [data-testid="stMetricSimple"] { background: white; border: 1px solid #eee; border-radius: 15px; padding: 10px 0; }
    }
    </style>
    """, unsafe_allow_html=True)

# 4. 세션 초기화
if 'step' not in st.session_state: st.session_state.step = 0
if 'scores' not in st.session_state: st.session_state.scores = {'V':0, 'C':0, 'F':0, 'I':0}

# 5. 로직
if st.session_state.step < len(diagnostics):
    current_idx = st.session_state.step
    st.progress(current_idx / len(diagnostics))
    
    st.markdown(f'<div class="main-card"><p class="question-text">{diagnostics[current_idx]["q"]}</p></div>', unsafe_allow_html=True)

    # ⚠️ 핵심: st.button 대신 query_params를 이용한 HTML 버튼 구현
    col1, col2 = st.columns(2)
    with col1:
        if st.button("네, 준수합니다", key=f"y_{current_idx}", use_container_width=True):
            st.session_state.scores[diagnostics[current_idx]['type']] += 1
            st.session_state.step += 1
            st.rerun()
    with col2:
        if st.button("아니요, 부족합니다", key=f"n_{current_idx}", use_container_width=True):
            st.session_state.step += 1
            st.rerun()

else:
    # 결과 화면
    s = st.session_state.scores
    st.markdown(f'<div class="main-card"><p class="persona-title">진단 완료!</p><p>{sum(s.values())}점입니다.</p></div>', unsafe_allow_html=True)
    
    st.subheader("📊 영역별 상세 지표")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("시각", f"{s['V']}/3")
    c2.metric("조작", f"{s['C']}/3")
    c3.metric("반응", f"{s['F']}/3")
    c4.metric("보편", f"{s['I']}/3")

    if st.button("다시 하기", use_container_width=True):
        st.session_state.step = 0
        st.session_state.scores = {'V':0, 'C':0, 'F':0, 'I':0}
        st.rerun()
