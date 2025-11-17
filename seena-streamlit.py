import streamlit as st
from PIL import Image

st.set_page_config(page_title="Seena Mohajeran", layout="wide")

# ----------------------
# HERO SECTION
# ----------------------
st.title("Hi, I'm Seena 👋")
st.subheader("Machine Learning Engineer | Medical Device R&D | Vision & Multimodal AI")
st.write(
    """
I'm an ML Engineer with experience building software and AI systems for medical devices, multimodal models, and real-time perception.  
My work spans applied machine learning, computer vision, embedded systems, and full‑stack R&D tooling.
"""
)

st.markdown("---")

# ----------------------
# ABOUT ME
# ----------------------
st.header("About Me")
st.write(
    """
I’m currently pursuing my **M.S. in Machine Learning & Data Science at USC**, where I focus on multimodal learning, large models, and applied AI.  
Previously, I spent two years at **Applied Medical**, engineering internal tools used across R&D labs for electrosurgical devices.

Outside of engineering: I’m a **2nd‑degree Taekwondo black belt**, MMA enthusiast, and I love cameras, fitness, and cooking.
"""
)

st.markdown("---")

# ----------------------
# SKILLS VISUAL
# ----------------------
st.header("Skills")

skills = {
    "Languages": ["Python", "C++", "SQL", "R", "MATLAB", "JavaScript", "C"],
    "Frameworks": ["PyTorch", "Scikit‑learn", "OpenCV", "TensorFlow", "Streamlit"],
    "Expertise": ["Machine Learning", "Computer Vision", "Time Series", "ETL Pipelines", "Data Analysis"],
    "Tools": ["Git", "CMake", "Qt", "Bazel", "Conan", "Jupyter"]
}

cols = st.columns(2)
for i, (cat, items) in enumerate(skills.items()):
    with cols[i % 2]:
        st.markdown(f"### {cat}")
        for item in items:
            st.markdown(f"- {item}")

st.markdown("---")

# ----------------------
# PROJECTS
# ----------------------
st.header("Projects")

with st.container():
    st.subheader("🔵 High‑Dimensional Embedding for Language‑Aligned Perception (2025)")
    st.write(
        "A Vision Transformer–LLM hybrid generating step‑by‑step visual reconstruction programs. Studied embedding dimensionality for causal & procedural reasoning."
    )

with st.container():
    st.subheader("🟣 Noisy Rubik’s Cube Solver (2024)")
    st.write(
        "Neural solver using a modified Adam optimizer with probabilistic priors. Reduced cube‑solution turns by **19%** compared to classic Adam."
    )

with st.container():
    st.subheader("🟢 YOLO Object Detection Analysis (2023)")
    st.write(
        "Benchmarked YOLO architectures and hardware pipelines. Published at CoDIT 2024 via Intelligent Computing Lab."
    )

with st.container():
    st.subheader("🟡 Human Activity Recognition via Multisensor Fusion (2025)")
    st.write(
        "Built a PyTorch model for classifying movements through motion‑sensor fusion. Compared classical ML with RNN architectures."
    )

st.markdown("---")

# ----------------------
# EXPERIENCE
# ----------------------
st.header("Experience")
with st.expander("Applied Medical — Software Engineer, R&D (2022–2024)"):
    st.write(
        """
- Developed a full‑stack Qt + C++ USB communication application used across electrosurgical R&D labs.  
- Engineered an automated Python/C++ ETL pipeline for medical‑device D‑Forms → boosted lab productivity by **25%**.  
- Built a proprietary script‑decompiler reducing reverse‑engineering workflow time by **70%**.
"""
    )

st.markdown("---")

# ----------------------
# RESEARCH
# ----------------------
st.header("Research & Publications")

st.write("**CoDIT 2024** — YOLO performance trade‑off analysis")
st.write("**SCURR/NCUR 2022–2023** — CV‑based drone waypoint navigation")
st.write("**Neural Optimizer Modification** — Noisy Rubik’s Cube solver (2024)")

st.markdown("---")

# ----------------------
# CONTACT
# ----------------------
st.header("Contact")
cols = st.columns(3)
cols[0].markdown("📧 **Email:** smohajer@usc.edu")
cols[1].markdown("🔗 [LinkedIn](https://linkedin.com/in/seenamohajeran)")
cols[2].markdown("💻 [GitHub](https://github.com/Seena-02)")

st.caption("© 2025 Seena Mohajeran — Personal Website")
