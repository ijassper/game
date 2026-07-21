# ── app.py (수정본) ──
import streamlit as st
import subprocess, os, time
import threading
import requests

st.title("KION Labs Robot Arm (Streamlit)")

script_path = os.path.join(os.path.dirname(__file__), "robot_arm.py")

# ngrok 실행 (먼저 pip install pyngrok)
def start_ngrok():
    from pyngrok import ngrok
    ngrok.set_auth_token("YOUR_NGROK_AUTHTOKEN")   # ngrok 계정 토큰
    tunnel = ngrok.connect(8080, "http")
    return tunnel.public_url

# 백그라운드 VPython 서버
process = subprocess.Popen(["python", script_path],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)

# ngrok 터널 확보 (최초 2초 대기)
public_url = start_ngrok()
time.sleep(2)

st.components.v1.html(
    f"""<iframe src="{public_url}" width="800" height="600"
            style="border:none;"></iframe>""",
    height=610,
)

if st.button("Stop Simulation"):
    process.terminate()
    st.success("Simulation stopped.")
