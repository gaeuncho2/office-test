import streamlit as st

st.set_page_config(page_title="사바나 오피스 8가지 유형", page_icon="🐾")

# 세션 상태 초기화 (3개의 점수 축)
if 'speed' not in st.session_state: st.session_state.speed = 0  # 추진력 vs 신중함
if 'temp' not in st.session_state: st.session_state.temp = 0    # 이성 vs 감성
if 'view' not in st.session_state: st.session_state.view = 0    # 디테일 vs 큰그림
if 'page' not in st.session_state: st.session_state.page = 0

# 질문지 (각 축당 2문제씩 총 6문제)
questions = [
    {"q": "새로운 프로젝트가 내려왔을 때 나는?", "a": "일단 바로 실행에 옮긴다", "b": "전체적으로 검토 후 천천히 시작한다", "type": "speed"},
    {"q": "팀원의 실수로 보고서가 엉망이 되었다면?", "a": "잘못된 부분을 조목조목 짚어준다", "b": "팀원의 마음을 먼저 다독여준다", "type": "temp"},
    {"q": "업무를 처리할 때 더 중요하게 생각하는 것은?", "a": "숫자 하나, 오타 하나까지 완벽한 디테일", "b": "전체적인 흐름과 최종 목적(큰 그림)", "type": "view"},
    {"q": "점심 메뉴를 정할 때 나는?", "a": "가장 먼저 메뉴를 제안한다", "b": "다들 결정할 때까지 기다렸다가 따른다", "type": "speed"},
    {"q": "동료가 업무 고민을 털어놓는다면?", "a": "현실적인 대안을 찾아준다", "b": "충분히 들어주며 공감해준다", "type": "temp"},
    {"q": "기획안을 작성할 때 나의 스타일은?", "a": "각 항목의 세부 실행 방안에 집중한다", "b": "이 사업의 비전과 방향성에 집중한다", "type": "view"}
]

# 8가지 결과 데이터
results = {
    "STD": {"animal": "독수리 🦅", "title": "완벽주의 리더", "desc": "빠르고 정확합니다. 빈틈없는 일 처리로 신뢰를 얻어요."},
    "STB": {"animal": "사자 🦁", "title": "결단력 있는 보스", "desc": "시원시원하게 일을 밀어붙이며 큰 성과를 만들어냅니다."},
    "SFD": {"animal": "돌고래 🐬", "title": "다정한 해결사", "desc": "팀의 활력소이자 문제가 생기면 발 벗고 나서는 타입입니다."},
    "SFB": {"animal": "강아지 🐶", "title": "핵인싸 메이커", "desc": "친화력 갑! 긍정적인 에너지로 팀 분위기를 주도합니다."},
    "FTD": {"animal": "거미 🕷️", "title": "치밀한 전략가", "desc": "조용하지만 뒤에서 모든 상황을 파악하고 분석합니다."},
    "FTB": {"animal": "코끼리 🐘", "title": "묵직한 중심점", "desc": "신중하고 이성적이며, 어떤 상황에서도 흔들리지 않습니다."},
    "FFD": {"animal": "다람쥐 🐿️", "title": "섬세한 서포터", "desc": "보이지 않는 곳에서 팀원들을 세심하게 챙기고 돕습니다."},
    "FFB": {"animal": "나무늘보 🦥", "title": "평화로운 공상가", "desc": "여유로운 마음으로 창의적인 아이디어를 제안합니다."}
}

st.title("🐾 사바나 오피스 생존 테스트")

if st.session_state.page < len(questions):
    item = questions[st.session_state.page]
    st.write(f"### {item['q']}")
    
    if st.button(item['a'], key=f"a{st.session_state.page}"):
        if item['type'] == 'speed': st.session_state.speed += 1
        elif item['type'] == 'temp': st.session_state.temp += 1
        else: st.session_state.view += 1
        st.session_state.page += 1
        st.rerun()
        
    if st.button(item['b'], key=f"b{st.session_state.page}"):
        st.session_state.page += 1
        st.rerun()
else:
    # 8가지 조합 계산 (2개 중 1개 이상이면 앞 글자 선택)
    res_key = ("S" if st.session_state.speed >= 1 else "F") + \
              ("T" if st.session_state.temp >= 1 else "F") + \
              ("D" if st.session_state.view >= 1 else "B")
    
    res = results[res_key]
    st.snow()
    st.header(f"당신은 {res['animal']}")
    st.subheader(res['title'])
    st.write(res['desc'])
    
    if st.button("다시 하기"):
        st.session_state.clear()
        st.rerun()
