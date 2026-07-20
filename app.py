import streamlit as st

st.title("# 앱 UI 만들기")
name =  st.text_input("nickname")
grade = st.radio("학년", [1,2,3,4,5,6,7,8,9,10,11], horizontal=True)
cls = st.number_input("반", value=1)
level = st.select_slider("난이도", ["쉬움", "보통", "어려움"], value = "보통")
score = st.slider("점수", 0, 100, 50)
text = st.text_area("소감")

if st.button("확인"):
    st.success(f"{name} / {grade}학년 / {cls}반 / {level}")
    st.markdown(f"점수: `{score}`")
    st.info(f"소감: {text}")
