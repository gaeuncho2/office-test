import streamlit as st

# 페이지 설정
st.set_page_config(page_title="사바나 오피스 테스트", page_icon="🦁")

# 세션 상태 초기화
if 'speed_score' not in st.session_state:
    st.session_state.speed_score = 0
if 'temp_score' not in st.session_state:
    st.session_state.temp_score = 0
if 'page' not in st.session_state:
    st.session_state.page = 0

# 질문 데이터
questions = [
    {"q": "Q1. 출근 직후 나는?", "a": "바로 일 시작!", "b": "커피부터 한 잔...", "type": "speed"},
    {"q": "Q2. 회의 중 황당한 의견을 들으면?", "a": "팩트 폭격", "b": "일단 리액션", "type": "temp"},
    {"q": "Q3. 갑작스러운 급한 업무 요청엔?", "a": "폭풍 작업", "b": "차근차근 계획", "type": "speed"},
    {"q": "Q4. 동료가 실수해서 우울해하면?", "a": "해결책 제시", "b": "따뜻한 위로", "type": "temp"}
]

# 결과 데이터
results = {
    "TT": {"animal": "치타", "desc": "성과에 미친 효율 끝판왕! 결론 없는 회의를 가장 싫어해요."},
    "TF": {"animal": "부엉이", "desc": "차분한 팩트 체크기! 데이터와 근거 없이는 움직이지 않아요."},
    "FT": {"animal": "골든 리트리버", "desc": "우리 팀 에너자이저! 추진력도 좋은데 성격까지 밝은 타입."},
    "FF": {"animal": "코알라", "desc": "오피스의 평화주의자! 남의 부탁을 잘 거절 못하는 따뜻한 분이군요."}
}

# UI 구현
st.title("🦁 사바나 오피스 생존 테스트")
st.write("나의 직장 생활 동물 유형은?")

if st.session_state.page < len(questions):
    item = questions[st.session_state.page]
    st.progress((st.session_state.page) / len(questions))
    st.subheader(item['q'])
    
    if st.button(item['a'], key="a"):
        if item['type'] == 'speed': st.session_state.speed_score += 1
        else: st.session_state.temp_score += 1
        st.session_state.page += 1
        st.rerun()
        
    if st.button(item['b'], key="b"):
        # B 선택 시 점수 추가 없음 (이진 분류)
        st.session_state.page += 1
        st.rerun()
else:
    # 결과 도출
    res_speed = "T" if st.session_state.speed_score >= 1 else "F"
    res_temp = "T" if st.session_state.temp_score >= 1 else "F"
    res_key = res_speed + res_temp
    
    st.balloons()
    st.header(f"당신은 '{results[res_key]['animal']}' 유형!")
    st.write(results[res_key]['desc'])
    
    if st.button("다시 하기"):
        st.session_state.page = 0
        st.session_state.speed_score = 0
        st.session_state.temp_score = 0
        st.rerun()