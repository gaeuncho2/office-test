import streamlit as st

# 1. 스타일 및 폰트 설정 (컨설팅 회사 느낌)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3.5em; font-weight: bold; }
    h1 { color: #1E3A8A; } /* 신뢰감을 주는 네이비 */
    </style>
    """, unsafe_allow_html=True)

if 'ux_scores' not in st.session_state:
    st.session_state.ux_scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}
if 'step' not in st.session_state:
    st.session_state.step = 0

# 진단 문항 (UX/UI 전문가 관점)
diagnostics = [
    {"q": "주요 버튼의 크기가 손가락으로 누르기에 충분히 큰가요?", "type": "C"},
    {"q": "저시력 사용자를 위해 배경과 글자의 대비가 명확한가요?", "type": "V"},
    {"q": "오류 발생 시, 무엇이 잘못되었는지 쉬운 언어로 설명해주나요?", "type": "F"},
    {"q": "처음 사용하는 고령자도 1분 안에 결제 단계까지 갈 수 있나요?", "type": "I"},
    {"q": "로딩 중이거나 처리가 완료되었을 때 시각적/청각적 신호를 주나요?", "type": "F"},
    {"q": "화면의 폰트 크기를 사용자가 조절할 수 있나요?", "type": "V"}
]

st.title("🔍 우리 서비스 UX/UI 건강검진")
st.write("---")

if st.session_state.step < len(diagnostics):
    q_item = diagnostics[st.session_state.step]
    st.subheader(f"Q{st.session_state.step + 1}. {q_item['q']}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("네, 아주 잘 되어 있어요"):
            st.session_state.ux_scores[q_item['type']] += 2
            st.session_state.step += 1
            st.rerun()
    with col2:
        if st.button("아니요, 개선이 필요해요"):
            st.session_state.step += 1
            st.rerun()

else:
    # 결과 로직 (점수가 낮을수록 컨설팅 필요도가 높은 페르소나 노출)
    total_v = st.session_state.ux_scores['V']
    total_c = st.session_state.ux_scores['C']
    
    st.balloons()
    st.header("진단 리포트 요약")
    
    if total_v <= 1:
        st.error("### 🐘 당신의 서비스는 '눈 가린 코끼리'")
        st.write("콘텐츠는 풍부하지만, 접근성(시각적 배려)이 부족해 많은 사용자가 장벽을 느끼고 있습니다.")
    elif total_c <= 1:
        st.warning("### 🐢 당신의 서비스는 '잠자는 거북이'")
        st.write("조작 반응이 느리거나 버튼 배치가 비효율적입니다. 사용자 이탈률이 높을 수 있습니다.")
    else:
        st.success("### 🏆 당신의 서비스는 '스마트 가이드 돌고래'")
        st.write("기본적인 접근성이 훌륭합니다! 더 세밀한 고도화 전략을 추천드립니다.")

    st.write("---")
    st.subheader("💡 전문 컨설턴트의 한 줄 제안")
    st.info("현재 진단 결과, '조작 편의성' 영역이 가장 취약합니다. 고령층 사용자를 위한 터치 가이드 개선이 시급해 보입니다.")
    
    # 마케팅 연결 버튼
    if st.button("상세 컨설팅 제안서 요청하기 (무료)"):
        st.write("📩 담당자 메일로 제안서 양식을 보냈습니다. (예시)")

    if st.button("다시 진단하기"):
        st.session_state.step = 0
        st.session_state.ux_scores = {'V': 0, 'C': 0, 'F': 0, 'I': 0}
        st.rerun()
