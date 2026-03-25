import random as rd
import streamlit as st
import base64

def set_background(main_bg):
  with open(main_bg,"rb") as f:
    data = f.read()
  b64 = base64.b64encode(data).decode()

  st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
      background: url(data:image/jpeg;base64,{b64});
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
  )

# 배경 이미지 함수 호출
set_background('bg_spongebob.jpg')

# CSS 코들을 이용해 배경색 설정
page_bg_color = """
<style>
[data-testid="stAppViewContainer"]{
background-color: #87CEFF;
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
