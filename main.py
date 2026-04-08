import random as rd
import streamlit as st
import base64

def set_background(main_bg):
  #if 'bg_set' not in st.session_state:
  with open(main_bg,"rb") as f:
    data = f.read()
  b64 = base64.b64encode(data).decode()
  
  st.markdown(
      f"""
      <style>
      [data-testid="stAppViewContainer"] {{
        background: url(data:image/jpeg;base64,{b64});
        background-size: 100% 100%;
        background-repeat: no-repeat;
        background-position: center;
        backgorund-attachment: fixed;
      }}
      </style>
      """,
      unsafe_allow_html=True
    )
#    st.session_state.bg_set = True

# 배경 이미지 함수 호출
set_background('bg_spongebob.jpg')

st.markdown("<h1 style='text-align: center; color: white;'>멈추기게임</h1>", unsafe_allow_html=True)

# 게임영역 3등분
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
#  with open("bg_spongebob.jpg","rb") as f:
#    img_data = base64.b64encode(f.read()).decode()
  st.image("sponge.jpg")

#  if st.button(f'<img src="data:image/jpeg;base64,{img_data}" width="300">', use_container_with=True):
  if st.button("게임시작"):
    num = rd.random()
    if num < 0.25:
      st.error("멈춰!!")
    else:
      st.success("통과!!")
