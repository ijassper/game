import random as rd
import streamlit as st

# CSS 코들을 이용해 배경색 설정
page_bg_color = """
<style>
[data-testid="stAppViewContainer"]{
background-color: #f0f8ff;
}
"""
st.markdown(page_bg_color, unsafe_allow_html=True)
st.title("멈추기 게임")

if st.button("게임시작"):
  num = rd.random()
  if num < 0.25:
    st.error("멈춰!!")
  else:
    st.success("통과!!")
