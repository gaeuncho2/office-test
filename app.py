import streamlit as st

# 1. 페이지 설정 (최상단)
st.set_page_config(page_title="UX Health Check", page_icon="🔍", layout="centered")

# 2. 진단 데이터 정의 (로직보다 먼저 선언되어야 NameError가 나지 않음)
diagnostics = [
    {"q": "배경과 텍스트의 명도 대비가 충분하여 저시력자도 읽기 편한가요?", "type": "V"},
    {"q": "모든 입력 폼에 무엇을 적어야 하는지 명확한 레이블이 있나요?", "type": "I"},
    {"q": "중요한 버튼의 크기가 터치 오작동을 방지할 만큼 충분히 큰가요?", "type": "C"},
    {"q": "로딩이나 데이터 처리 시 사용자가 기다려야 함을 시각적으로 알리나요?", "type": "F"},
    {"q": "키보드나 전용 패드만으로 모든 메뉴 이동이 가능하신가요?", "type": "C"},
    {"q": "전문 용어 대신 누구나 이해하기 쉬운 보편적인 단어를 사용하나요?", "type": "I"},
    {"q": "이미지에 대한 대체 텍스트가 스크린 리더용으로 제공되고 있나요?", "type": "V"},
    {"q": "오류 메시지는 구체적이고 해결 방법을 함께 제시하나요?", "type": "F"},
    {"q": "페이지의 구조가 일관되어 다음 행동을 예측하기 쉬운가요?", "type": "I"},
    {"q": "색상만으로 정보를 전달하지 않고 아이콘이나 텍스트를 병기하나요?", "type": "V"},
    {"q": "결제나 전송 전, 마지막으로 확인하거나 취소할 수 있는 기회를 주나요?", "type": "C"},
    {"q": "제한 시간이 있는 경우, 사용자가 시간을 연장할 수 있는 옵션이 있나요?", "type": "F"}
]

# 3. 에이전시 스타일 CSS 주입
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
    html, body, [class*="css"] { font-family: 'Pretendard', sans-serif; background-color: #F8FAFC; color: #1E293B; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .main-card {
        background: white; padding: 50px 40px; border-radius: 30px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.05); margin-bottom: 30px;
        border: 1px solid #F1F5F9; text-align: center;
    }
    .question-text { font-size: 28px; font-weight: 700; color: #0F172A; line-height: 1.5; margin-bottom: 10px; }
    div.stButton > button {
        width: 100%; height: 70px; border-radius: 20px; border: 1px dashed #E2E8F0;
        background-color: white; color: #bbbbbb; font-size: 25px; font-weight: 600; transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        border-color: #10B981; color: #10B981; text-decoration: black wavy underline; background-color: #F0FDF4;
        transform: translateY(-3px); box-shadow: 0 10px 20px rgba(16, 185, 129, 0.1);
    }
    .stProgress > div > div > div > div { background-color: #10B981; }
    .persona-title { font-size: 32px; font-weight: 800; color: #10B981; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# 4. 세션 상태 초기화
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}

# 5. 헤더 섹션
st.markdown("<p style='text-align: center; color: #10B981; font-weight: 800; letter-spacing: 2px; margin-bottom: 0;'>UX/UI CONSULTING GROUP</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 46px; margin-top: 10px; margin-bottom: 40px;'>서비스 접근성 마스터 진단</h1>", unsafe_allow_html=True)

# 6. 메인 로직 시작
if st.session_state.step < len(diagnostics):
    # 진행률 표시
    total_q = len(diagnostics)
    current_q_idx = st.session_state.step
    progress_val = current_q_idx / total_q
    st.progress(progress_val)
    st.write(f"<p style='text-align: right; color: #64748B;'>{current_q_idx + 1} / {total_q}</p>", unsafe_allow_html=True)

    # 질문 카드 (문자열 리터럴 에러 방지를 위해 변수에 할당)
    q_text = diagnostics[current_q_idx]['q']
    st.markdown(f"""
        <div class="main-card">
            <p class="question-text">{q_text}</p>
        </div>
    """, unsafe_allow_html=True)

    # 선택 버튼
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
    # 7. 결과 화면
    st.balloons()
    s = st.session_state.scores
    
    # 페르소나 매칭 함수
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
            <p style="font-size: 20px; color: #475569;">{p_desc}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 상세 지표
    st.subheader("📊 영역별 상세 지표")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("시각 배려", f"{s['V']}/3")
    col2.metric("조작 편의", f"{s['C']}/3")
    col3.metric("반응/알림", f"{s['F']}/3")
    col4.metric("보편 설계", f"{s['I']}/3")
    
    st.write("---")
    if st.button("무료 컨설팅 제안서 요청하기"):
        st.success("📩 담당자에게 진단 결과가 전송되었습니다. 곧 연락드리겠습니다!")

    if st.button("다시 테스트하기"):
        st.session_state.step = 0
        st.session_state.scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}
        st.rerun()
