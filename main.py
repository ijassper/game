import random as rd
import streamlit as st
import base64

def set_background(main_bg):
  if 'bg_set' not in st.session_state:
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
      }}
      </style>
      """,
      unsafe_allow_html=True
    )
    st.session_state.bg_set = True

# 배경 이미지 함수 호출
set_background('bg_spongebob.jpg')

#st.markdown(page_bg_color, unsafe_allow_html=True)
st.title("멈추기 게임")

# 이미지와 버튼을 겹치기 위한 투명 버튼
st.markdown(
      """
      <style>
      .stButton > button {
        width: 300px;
        height: 300px;
        background-color: rgba(0,0,0,0) !important;
        border: none;
        color: rgba(0,0,0,0);        
      }
      </style>
      """,
      unsafe_allow_html=True
    )

# 게임영역 3등분
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    
  st.image("bg_spongebob.jpg")

  if st.button(" "):
    num = rd.random()
    if num < 0.25:
      st.error("멈춰!!")
    else:
      st.success("통과!!")
