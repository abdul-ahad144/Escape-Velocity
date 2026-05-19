import streamlit as st
import streamlit.components.v1 as components

# --------------------------------
# PAGE
# --------------------------------
st.set_page_config(page_title="Escape Velocity", layout="wide")

st.title("🌍🚀 Escape Velocity Visualisation")

st.write("""
Ball Earth se launch hogi aur space ki taraf jayegi.
Agar velocity kam hui to wapas gir jayegi.
""")

# --------------------------------
# SLIDERS
# --------------------------------
velocity = st.sidebar.slider(
    "Launch Velocity (km/s)",
    1.0,
    15.0,
    8.0
)

# --------------------------------
# ESCAPE VELOCITY
# --------------------------------
escape_velocity = 11.2

st.latex(r"v_e = \sqrt{\frac{2GM}{R}}")

st.subheader(f"Escape Velocity = {escape_velocity} km/s")

st.subheader(f"Current Velocity = {velocity} km/s")

# --------------------------------
# STATUS
# --------------------------------
escaped = velocity >= escape_velocity

if escaped:
    st.success("🚀 Ball Escaped Earth Gravity")
else:
    st.error("🌍 Gravity Pulled Ball Back")

# --------------------------------
# SPEED
# --------------------------------
animation_speed = max(2, 10 - velocity / 2)

# --------------------------------
# MOVEMENT
# --------------------------------
if escaped:
    final_position = "110%"
else:
    final_position = "55%"

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
    background:black;
}}

.container {{
    position:relative;
    width:100%;
    height:600px;
    overflow:hidden;
    border-radius:20px;
    background:black;
}}

.stars {{
    position:absolute;
    width:100%;
    height:100%;
    background-image:
        radial-gradient(white 1px, transparent 1px);
    background-size:60px 60px;
}}

.earth {{
    position:absolute;
    bottom:-300px;
    left:50%;
    transform:translateX(-50%);
    width:700px;
    height:700px;
    border-radius:50%;

    background:
        radial-gradient(circle at 30% 30%, #4caf50, #1565c0);
}}

.ball {{
    position:absolute;
    bottom:170px;
    left:50%;
    transform:translateX(-50%);
    font-size:60px;

    animation: launch {animation_speed}s linear forwards;
}}

@keyframes launch {{

    from {{
        bottom:170px;
    }}

    to {{
        bottom:{final_position};
    }}
}}

.label {{
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

    <div class="label">
        🌍 Earth Escape Velocity = 11.2 km/s
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
components.html(html_code, height=620)

# --------------------------------
# EXPLANATION
# --------------------------------
st.write("## Explanation")

st.write(f"""
### Current Velocity
{velocity} km/s

### Physics Behaviour

If velocity:
- less than 11.2 km/s
→ ball upar jayegi phir gravity niche kheench legi

If velocity:
- greater than or equal to 11.2 km/s
→ ball Earth gravity se escape kar jayegi
""")

# --------------------------------
# SUPER IMPORTANT
# --------------------------------
st.error("""
SUPER-IMPORTANT:

Escape Velocity depends on:
- Planet gravity
- Planet mass
- Planet radius

NOT on object mass.
""")
