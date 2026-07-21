import streamlit as st
import subprocess, os, time

st.title("KION Labs Robot Arm Simulation (Streamlit)")

# VPython 스크립트 경로
script_path = os.path.join(os.path.dirname(__file__), "robot_arm.py")

# 비동기 실행 (stdout/err 은 백그라운드에 두고)
process = subprocess.Popen(
    ["python", script_path],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

# VPython 서버가 열릴 때까지 잠시 대기
time.sleep(2)

# iframe 으로 캔버스 삽입
st.components.v1.html(
    """
    <iframe src="http://localhost:8080/" width="800" height="600"
            style="border:none;"></iframe>
    """,
    height=610,
)

# 시뮬레이션 정지 버튼
if st.button("Stop Simulation"):
    process.terminate()
    st.success("Simulation stopped.")
