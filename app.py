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

# 3. CSS 주입 (가로 배치 강제 및 디자인 최적화)
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    * { font-family: 'Pretendard', sans-serif !important; box-sizing: border-box; }
    html, body, [data-testid="stAppViewContainer"] { background-color: #FFFEF5 !important; }
    #MainMenu, footer, header { visibility: hidden; }

    [data-testid="stMainBlockContainer"] { padding: 2rem 1rem !important; }

    .main-card {
        background: white; padding: 40px 20px; border-radius: 40px;
        box-shadow: 0 15px 35px rgba(253, 224, 71, 0.15); margin-bottom: 30px;
        border: 1px solid #ddd; text-align: center;
    }
    .question-text { font-size: 22px; font-weight: 800; color: #334155; line-height: 1.4; word-break: keep-all; }

    /* 모바일에서도 버튼 가로 정렬 유지 */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 10px !important;
    }
    div[data-testid="column"] { width: 50% !important; flex: 1 1 auto !important; }

    div.stButton > button {
        width: 100% !important;
        height: 65px !important;
        border-radius: 50px !important;
        border: none !important;
        background-color: #eee !important;
        color: #333 !important;
        font-size: 16px !important;
        font-weight: 700 !important;
    }
    div.stButton > button:hover { background-color: #475569 !important; color: #fff !important; }

    @media (max-width: 430px) {
        div.stButton > button { font-size: 14px !important; height: 60px !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# 4. 세션 초기화
if 'step' not in st.session_state: st.session_state.step = 0
if 'scores' not in st.session_state: st.session_state.scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}

# 5. 헤더
st.markdown("<p style='text-align: center; color: #76A1BE; font-weight: 800; letter-spacing: 2px;'>UX/UI CONSULTING</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-weight: 800;'>📝 내 서비스 자가진단하기</h1>", unsafe_allow_html=True)

# 6. 메인 로직
if st.session_state.step < len(diagnostics):
    curr = st.session_state.step
    st.progress(curr / len(diagnostics))
    st.write(f"<p style='text-align: right;'>{curr + 1} / {len(diagnostics)}</p>", unsafe_allow_html=True)
    st.markdown(f'<div class="main-card"><p class="question-text">{diagnostics[curr]["q"]}</p></div>', unsafe_allow_html=True)

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
    # 7. 결과 화면 로직
    s = st.session_state.scores

    def get_persona(s):
        total = sum(s.values())
        if total >= 11: return "스마트 가이드 돌고래", "모두에게 친절한 지능형 서비스", "최고의 접근성입니다!"
        if s['V'] <= 1: return "눈 가린 코끼리", "시각적 장벽이 높은 거대 서비스", "시각 요소 개선이 시급합니다."
        if s['C'] <= 1: return "잠자는 거북이", "조작이 답답한 미로형 서비스", "사용자 동선 재설계가 필요합니다."
        if s['F'] <= 1: return "까칠한 고슴도치", "피드백이 불친절한 예민한 서비스", "오류 안내를 강화하세요."
        return "과묵한 진돗개", "기본은 하지만 센스가 부족한 서비스", "UX 디테일 보완이 권장됩니다."

    # 함수 호출하여 변수 할당
    p_name, p_sub, p_desc = get_persona(s)

    st.markdown(f'''
        <div class="main-card">
            <h2 style="color:#1E293B;">{p_name}</h2>
            <h4 style="color:#475569;">{p_sub}</h4>
            <p style="color:#64748B;">{p_desc}</p>
        </div>
    ''', unsafe_allow_html=True)
    
    st.subheader("📊 영역별 상세 지표")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("시각", f"{s['V']}/3")
    c2.metric("조작", f"{s['C']}/3")
    c3.metric("반응", f"{s['F']}/3")
    c4.metric("보편", f"{s['I']}/3")
    
    st.write("---")
    
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        if st.button("문의하기", key="final_contact"):
            st.success("접수되었습니다!")
    with res_col2:
        if st.button("다시 하기", key="final_restart"):
            st.session_state.step = 0
            st.session_state.scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}
            st.rerun()
