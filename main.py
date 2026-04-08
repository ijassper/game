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
      # 배경 이미지 코드
      [data-testid="stAppViewContainer"] {{
        background: url(data:image/jpeg;base64,{b64});
        background-size: 100% 100%;
        background-repeat: no-repeat;
        background-position: center;
        backgorund-attachment: fixed;
      }}
      # 버튼에 배경이미지 넣는 코드
      button[kind="secondary"] {{
            background-image: url(data:image/jpeg;base64,{b64_sponge});
            background-size: cover;
            width: 300px;
                      
      }}
      </style>
      """,
      unsafe_allow_html=True
    )
with open("sponge.jpg", "rb") as f:
    b64_sponge = base64.b64encode(f.read()).decode()

# 배경 이미지 함수 호출
set_background('bg_spongebob.jpg')

if 'game_started' not in st.session_state:
  st.session_state.game_started = False
  
# st.markdown("<h1 style='text-align: center; color: white;'>멈추기게임</h1>", unsafe_allow_html=True)

# 게임영역 3등분
col1, col2 = st.columns([3, 1])

with col2:

  if st.button(" ", key="sponge_btn"):
    st.session_state.game_started = True
    num = rd.random()
    if num < 0.25:
      st.error("멈춰!!")
    else:
      st.success("통과!!")
