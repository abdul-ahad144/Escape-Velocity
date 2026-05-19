import streamlit as st
import streamlit.components.v1 as components

# --------------------------------
# PAGE
# --------------------------------
st.set_page_config(page_title="Escape Velocity Visualisation", layout="wide")

st.title("🌍 Escape Velocity Visualisation")

st.write("""
Earth ki gravity se bahar nikalne ke liye object ko minimum speed chahiye hoti hai.
Usko Escape Velocity kehte hain.
""")

# --------------------------------
# SLIDERS
# --------------------------------
mass = st.sidebar.slider("Ball Mass (kg)", 1, 100, 10)

velocity = st.sidebar.slider("Launch Velocity (km/s)", 1.0, 15.0, 5.0)

# --------------------------------
# ESCAPE VELOCITY
# --------------------------------
escape_velocity = 11.2

st.latex(r"v_e = \sqrt{\frac{2GM}{R}}")

st.subheader(f"Earth Escape Velocity = {escape_velocity} km/s")

st.subheader(f"Current Velocity = {velocity} km/s")

# --------------------------------
# STATUS
# --------------------------------
if velocity < escape_velocity:
    status = "❌ Ball Falls Back To Earth"
else:
    status = "🚀 Ball Escapes Earth Gravity"

st.success(status)

# --------------------------------
# ANIMATION SPEED
# --------------------------------
animation_speed = max(2, 12 - velocity)

# --------------------------------
# ESCAPE HEIGHT
# --------------------------------
if velocity < escape_velocity:
    top_position = "35%"
else:
    top_position = "-120px"

# --------------------------------
# HTML
# --------------------------------
html_code = f"""
<!DOCTYPE html>
<html>

<head>

<style>

body {{
    margin:0;
    overflow:hidden;
}}

.container {{
    position:relative;
    width:100%;
    height:500px;
    background:black;
    overflow:hidden;
    border-radius:20px;
}}

.earth {{
    position:absolute;
    bottom:-180px;
    left:50%;
    transform:translateX(-50%);
    width:500px;
    height:500px;
    background:radial-gradient(circle, #2ecc71, #145a32);
    border-radius:50%;
}}

.ball {{
    position:absolute;
    bottom:140px;
    left:50%;
    transform:translateX(-50%);
    font-size:50px;

    animation: launch {animation_speed}s linear forwards;
}}

@keyframes launch {{

    from {{
        bottom:140px;
    }}

    to {{
        bottom:{top_position};
    }}
}}

.stars {{
    position:absolute;
    width:100%;
    height:100%;
    background-image:
        radial-gradient(white 1px, transparent 1px);
    background-size:50px 50px;
}}

.text {{
    position:absolute;
    top:20px;
    left:20px;
    color:white;
    font-size:28px;
    font-family:Arial;
}}

</style>

</head>

<body>

<div class="container">

    <div class="stars"></div>

    <div class="text">
        Escape Velocity = 11.2 km/s
    </div>

    <div class="earth"></div>

    <div class="ball">⚽</div>

</div>

</body>

</html>
"""

# --------------------------------
# SHOW COMPONENT
# --------------------------------
components.html(html_code, height=520)

# --------------------------------
# EXPLANATION
# --------------------------------
st.write("## Explanation")

st.write(f"""
- Ball Mass = {mass} kg
- Launch Velocity = {velocity} km/s
- Earth Escape Velocity = 11.2 km/s

### Physics Logic

If:
- Velocity < 11.2 km/s  
→ gravity ball ko wapas kheench legi

If:
- Velocity ≥ 11.2 km/s  
→ ball Earth gravity se escape kar jayegi
""")

# --------------------------------
# SUPER IMPORTANT
# --------------------------------
st.error("""
SUPER-IMPORTANT:

Escape Velocity does NOT depend on object mass.

It depends on:
- Planet mass
- Planet radius
- Gravity
""")
