# robot_arm.py
# --------------------------------------------------------------
# 3‑D 로봇 팔 시뮬레이션 (VPython)
#   - Base, Shoulder, Elbow 3개 관절
#   - 관절 각도 제한 로직 포함
#   - 간단한 “로봇 팔 댄스” 예제
# --------------------------------------------------------------

from vpython import canvas, vector, cylinder, sphere, rate, color, scene

# ------------------------------------------------------------------
# 1️⃣ 전역 설정
# ------------------------------------------------------------------
scene = canvas(title='KION Labs 로봇 팔 실습',
                width=800, height=600,
                background=color.white)

# 관절 각도(라디안) 초기값
base_angle    = 0.0          # Y축 회전
shoulder_angle = 0.0         # X축 앞뒤
elbow_angle   = 0.0          # X축 앞뒤

# ------------------------------------------------------------------
# 2️⃣ 로봇 팔 파라미터
# ------------------------------------------------------------------
BASE_HEIGHT   = 0.2
ARM_LENGTH    = 1.0
ELBOW_LENGTH  = 0.8
JOINT_RADIUS  = 0.07

# ------------------------------------------------------------------
# 3️⃣ 제한 각도 (학생이 실수하기 쉬운 부분)
#   - 각도는 라디안 단위이며, 파이(π) 기준으로 제한합니다.
# ------------------------------------------------------------------
BASE_MIN,    BASE_MAX    = -3.14, 3.14      # -180° ~ +180°
SHOULDER_MIN, SHOULDER_MAX = -1.57, 1.57    # -90°  ~ +90°
ELBOW_MIN,    ELBOW_MAX    = 0.0, 2.36      #   0°  ~ +135° (펴진 상태)

def clamp(val, lo, hi):
    """값을 lo~hi 구간 안으로 강제 제한"""
    return max(lo, min(hi, val))

# ------------------------------------------------------------------
# 4️⃣ 부품 생성 (시각화용)
# ------------------------------------------------------------------
# Base (지면 위 원통)
base = cylinder(pos=vector(0,0,0), axis=vector(0,BASE_HEIGHT,0),
                radius=0.2, color=color.gray(0.5))

# Joint spheres (시각적 구분)
joint_base    = sphere(pos=base.pos + vector(0,BASE_HEIGHT,0),
                       radius=JOINT_RADIUS, color=color.red)
joint_shoulder = sphere(pos=vector(0,BASE_HEIGHT,0),
                        radius=JOINT_RADIUS, color=color.green)
joint_elbow    = sphere(pos=vector(0,BASE_HEIGHT,0),
                        radius=JOINT_RADIUS, color=color.blue)

# Arm segments (cylinder)
upper_arm = cylinder(radius=0.05, color=color.orange)
forearm   = cylinder(radius=0.05, color=color.cyan)

# ------------------------------------------------------------------
# 5️⃣ 로봇 팔 업데이트 함수
# ------------------------------------------------------------------
def update_arm():
    """현재 관절 각도에 따라 3‑D 모델을 재배치"""
    # 1) Base 회전 (Y축)
    base_rot = vector(0, base_angle, 0)

    # Base joint 위치
    joint_base.pos = base.pos + vector(0, BASE_HEIGHT, 0)

    # 2) Shoulder 회전 (X축) – Base 회전 적용 후
    shoulder_dir = vector(0, 1, 0).rotate(angle=base_angle, axis=vector(0,1,0))
    shoulder_dir = shoulder_dir.rotate(angle=shoulder_angle, axis=vector(1,0,0))

    joint_shoulder.pos = joint_base.pos + shoulder_dir * 0.0   # 실제 위치는 같은 좌표

    # Upper arm
    upper_arm.pos = joint_base.pos
    upper_arm.axis = shoulder_dir * ARM_LENGTH

    # 3) Elbow 회전 (X축) – shoulder 방향을 기준으로 회전
    elbow_dir = shoulder_dir.rotate(angle=elbow_angle, axis=vector(1,0,0))

    joint_elbow.pos = upper_arm.pos + upper_arm.axis

    # Forearm
    forearm.pos = joint_elbow.pos
    forearm.axis = elbow_dir * ELBOW_LENGTH

# ------------------------------------------------------------------
# 6️⃣ 기본 댄스 루틴 (1분 이내)
# ------------------------------------------------------------------
def dance_demo():
    """학생들이 따라 할 수 있는 간단한 움직임 시퀀스"""
    import math
    steps = [
        (0,         0,          0),            # 초기 자세
        (0.5,       0.6,        0),            # Shoulder 올리기
        (0.5,       0.6,        1.0),          # Elbow 굽히기
        (-0.5,      -0.6,       0.5),          # 반대쪽으로 회전 + 어깨 내리기
        (0,         0,          0),            # 원점 복귀
    ]

    for base_t, sh_t, el_t in steps:
        # 제한 범위 안으로 강제 clamp
        global base_angle, shoulder_angle, elbow_angle
        base_angle     = clamp(base_t, BASE_MIN, BASE_MAX)
        shoulder_angle = clamp(sh_t, SHOULDER_MIN, SHOULDER_MAX)
        elbow_angle    = clamp(el_t, ELBOW_MIN, ELBOW_MAX)

        # 부드러운 움직임: 60 FPS (rate(60))
        for _ in range(30):          # 대략 0.5 s (30 frame)
            rate(60)
            update_arm()

# ------------------------------------------------------------------
# 7️⃣ 메인 루프 – 즉시 실행 혹은 함수 호출
# ------------------------------------------------------------------
if __name__ == '__main__':
    # 초기 포즈 표시
    update_arm()
    # 학생이 직접 관절 각도를 바꾸고 싶다면 아래 코드를 수정
    # 예시: base_angle = math.pi/4; shoulder_angle = 0.5; elbow_angle = 1.0; update_arm()
    # -----------------
    # 바로 댄스 시연
    dance_demo()
    # 시뮬레이션이 자동 종료되지 않도록 대기
    while True:
        rate(30)
