import streamlit as st

# 페이지 스타일링
st.set_page_config(page_title="오피스 사바나 테스트", page_icon="🐾")

# 세션 상태 관리
if 'scores' not in st.session_state:
    st.session_state.scores = {'speed': 0, 'temp': 0, 'view': 0}
if 'page' not in st.session_state:
    st.session_state.page = 0

# 질문지 데이터
questions = [
    {"q": "급한 업무가 쏟아질 때 나의 스타일은?", "a": "폭풍 같은 속도로 일단 쳐낸다", "b": "차분하게 우선순위를 분석한다", "type": "speed"},
    {"q": "팀원의 실수를 발견했을 때 나는?", "a": "냉철하게 원인을 파악하고 피드백한다", "b": "상대가 민망하지 않게 조심스레 말한다", "type": "temp"},
    {"q": "내가 더 자신 있는 업무 분야는?", "a": "꼼꼼한 서류 작업과 데이터 검증", "b": "창의적인 아이디어와 기획안 구상", "type": "view"},
    {"q": "회의가 길어질 때 드는 생각은?", "a": "빨리 결정하고 가서 일하고 싶다", "b": "조금 더 다각도로 논의해보고 싶다", "type": "speed"},
    {"q": "동료가 고민 상담을 요청한다면?", "a": "현실적인 해결책을 제시해준다", "b": "충분히 공감하고 위로해준다", "type": "temp"},
    {"q": "보고서를 작성할 때 나의 강점은?", "a": "빈틈없는 상세 실행 계획", "b": "설득력 있는 전체 비전 제시", "type": "view"}
]

# 결과 데이터 상세화
results = {
    "STD": {"animal": "매 🦅", "nick": "냉철한 조준 사수", "good": "빠른 실행력, 완벽한 디테일", "bad": "가끔은 주변을 기다려주세요", "match": "평화로운 코끼리 🐘"},
    "STB": {"animal": "사자 🦁", "nick": "정글의 통치자", "good": "결단력 있는 리더십, 시원한 추진력", "bad": "디테일을 챙겨줄 파트너가 필요해요", "match": "섬세한 다람쥐 🐿️"},
    "SFD": {"animal": "보더콜리 🐕", "nick": "만능 해결사", "good": "높은 효율과 동료를 챙기는 따뜻함", "bad": "혼자 너무 많은 짐을 지려 해요", "match": "조용한 미어캣 🦦"},
    "SFB": {"animal": "돌고래 🐬", "nick": "긍정 시너지 메이커", "good": "분위기 메이커, 열정적인 소통", "bad": "가끔은 집중의 시간이 필요해요", "match": "북극곰 🐻‍❄️"},
    "FTD": {"animal": "미어캣 🦦", "nick": "오피스 파수꾼", "good": "엄청난 정보력, 리스크 파악 능력", "bad": "결정이 조금 늦어질 수 있어요", "match": "만능 보더콜리 🐕"},
    "FTB": {"animal": "북극곰 🐻‍❄️", "nick": "묵직한 중재자", "good": "신중한 판단, 갈등 없는 협업", "bad": "표현을 조금 더 과감하게 해보세요", "match": "해맑은 돌고래 🐬"},
    "FFD": {"animal": "다람쥐 🐿️", "nick": "섬세한 서포터", "good": "꼼꼼한 뒷정리, 동료들의 수호천사", "bad": "거절을 어려워하는 게 고민!", "match": "결단력 사자 🦁"},
    "FFB": {"animal": "코끼리 🐘", "nick": "마음 넓은 전략가", "good": "비전 제시, 든든한 멘토 스타일", "bad": "실무의 디테일을 놓치지 마세요", "match": "냉철한 매 🦅"}
}

st.title("🐾 오피스 사바나 생존 테스트")

if st.session_state.page < len(questions):
    item = questions[st.session_state.page]
    st.write(f"### {item['q']}")
    
    if st.button(item['a'], key=f"a{st.session_state.page}"):
        st.session_state.scores[item['type']] += 1
        st.session_state.page += 1
        st.rerun()
        
    if st.button(item['b'], key=f"b{st.session_state.page}"):
        st.session_state.page += 1
        st.rerun()
else:
    res_key = ("S" if st.session_state.scores['speed'] >= 1 else "F") + \
              ("T" if st.session_state.scores['temp'] >= 1 else "F") + \
              ("D" if st.session_state.scores['view'] >= 1 else "B")
    
    res = results[res_key]
    st.balloons()
    st.success("🎉 분석 완료!")
    st.header(f"당신은 {res['animal']} [{res['nick']}]")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**💪 장점**\n\n{res['good']}")
    with col2:
        st.warning(f"**⚠️ 보완점**\n\n{res['bad']}")
        
    st.subheader(f"🤝 환상의 짝꿍: {res['match']}")
    
    if st.button("다시 하기"):
        st.session_state.clear()
        st.rerun()
