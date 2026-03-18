import random as rd
import streamlit as st

st.tilte("Stop Game")

if st.button("Game Start"):
  num = rd.random()
  if num < 0.1:
    st.error("STOP")
  else:
    st.success("PASS")
