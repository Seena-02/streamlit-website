import streamlit as st

st.set_page_config(page_title="Seena Mohajeran", layout="wide")

# ----------------------
# HERO SECTION
# ----------------------
# Uncomment below if you have a profile image (place it in same directory as app.py)
# from PIL import Image
# import base64
# from io import BytesIO
# 
# def get_circular_image(image_path, size=150):
#     img = Image.open(image_path).convert("RGBA")
#     img = img.resize((size, size), Image.LANCZOS)
#     mask = Image.new("L", (size, size), 0)
#     from PIL import ImageDraw
#     draw = ImageDraw.Draw(mask)
#     draw.ellipse((0, 0, size, size), fill=255)
#     img.putalpha(mask)
#     buffered = BytesIO()
#     img.save(buffered, format="PNG")
#     return base64.b64encode(buffered.getvalue()).decode()
# 
# col1, col2 = st.columns([1, 4])
# with col1:
#     img_base64 = get_circular_image("profile.jpg")
#     st.markdown(f'<img src="data:image/png;base64,{img_base64}" style="border-radius:50%;">', unsafe_allow_html=True)
# with col2:
#     st.title("Hi, I'm Seena 👋")
#     st.subheader("ML Engineer | MLOps | Medical Device R&D | Vision & Multimodal AI")

st.title("Hi, I'm Seena 👋")
st.subheader("ML Engineer | MLOps | Medical Device R&D | Vision & Multimodal AI")

st.write(
    """
I'm an ML Engineer with experience building production AI systems, MLOps pipelines, and software for medical devices.  
My work spans applied machine learning, computer vision, model serving infrastructure, and full-stack R&D tooling.
"""
)

col1, col2, col3, col4 = st.columns(4)
col1.markdown("📧 [smohajer@usc.edu](mailto:smohajer@usc.edu)")
col2.markdown("🔗 [LinkedIn](https://linkedin.com/in/seenamohajeran)")
col3.markdown("💻 [GitHub](https://github.com/Seena-02)")
col4.markdown("📍 Irvine, CA")

st.markdown("---")

# ----------------------
# ABOUT ME
# ----------------------
st.header("About Me")
st.write(
    """
I'm currently pursuing my **M.S. in Machine Learning & Data Science at USC** (GPA: 3.8), focusing on multimodal learning, 
large models, and production ML systems. Previously, I spent over two years at **Applied Medical**, engineering internal 
tools used across R&D labs for electrosurgical medical devices.

I'm passionate about bridging the gap between ML research and production—building systems that are not just accurate, 
but deployable, monitored, and maintainable.

Outside of engineering: I'm a **2nd-degree Taekwondo black belt** and former tournament coach, MMA enthusiast, 
and I enjoy fitness, strength training, and culinary arts.
"""
)

st.markdown("---")

# ----------------------
# SKILLS
# ----------------------
st.header("Skills")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Languages")
    st.write("Python, SQL, C, C++, R, MATLAB, HTML/CSS, JavaScript")
    
    st.markdown("### ML & Data Science")
    st.write("PyTorch, TensorFlow, Scikit-learn, NumPy, Pandas, OpenCV")
    
    st.markdown("### Algorithms & Methods")
    st.write("SVM, K-means, Naive Bayes, Bayesian Networks, Nearest Neighbors, Time Series Modeling, A/B Testing")

with col2:
    st.markdown("### MLOps & Infrastructure")
    st.write("Docker, FastAPI, MLflow, Prometheus, Grafana, CI/CD, GitHub Actions, Model Serving, Monitoring & Observability")
    
    st.markdown("### Tools & Platforms")
    st.write("Git, MySQL, Qt, CMake, Conan, Bazel, Jupyter, Streamlit, Google Colab, LaTeX, Linux")
    
    st.markdown("### Knowledge Areas")
    st.write("OOP, OOSD, Software Design Specs (SDS), Software Requirements Specs (SRS), Code Versioning, Data Analysis")

st.markdown("---")

# ----------------------
# EXPERIENCE
# ----------------------
st.header("Experience")

with st.expander("🏥 Applied Medical — Software Engineer Intern, R&D (May 2022 – Aug 2024)", expanded=True):
    st.markdown("**Rancho Santa Margarita, CA**")
    
    st.markdown("#### Voyant Debug Utility")
    st.write(
        """
Spearheaded and maintained a **C++ Qt full-stack application** with three years of prior development—designed to 
communicate and handle USB bulk transactions for Voyant (electrosurgical generator product line) using libusb. 
Deployed in medical device production laboratories and used throughout the product development lifecycle including 
assembly, testing, and validation. **Reduced bugs by 30%**, added quality-of-life updates and customer-requested features. 
Maintained SRS and SDS documentation for internal development and testing workflows.
"""
    )
    
    st.markdown("#### Voyant MedForm Extractor")
    st.write(
        """
Developed an automated **ETL pipeline** with Python (NumPy, Pandas, PyPDF2) and C++ to extract, parse, convert, 
and store D-Forms (PDFs, CSVs, and proprietary text files) from Voyant generators' mass storage onto networked systems. 
Streamlined data management and ensured regulatory compliance, **increasing lab productivity by 25%** and 
**improving data processing speed by 30%** during the product development lifecycle.
"""
    )
    
    st.markdown("#### Voyant Script Decompiler")
    st.write(
        """
Developed an internal automated decompilation tool in Python (NumPy, Pandas) to convert proprietary compiled 
medical device script files (SDB format) into human-readable DSF format. By automating tokenization in SDB CSV files, 
the tool eliminated manual reverse engineering, **saving 70% of workflow time** for testing teams.
"""
    )

st.markdown("---")

# ----------------------
# PROJECTS
# ----------------------
st.header("Projects")

col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.subheader("🔷 Legal Document RAG System")
        st.caption("Jan 2026 | In Progress")
        st.write(
            """
Building a retrieval-augmented generation system for legal contract analysis using the **CUAD dataset**. 
Implementing custom token-based chunking with tiktoken, sentence-transformer embeddings, and **ChromaDB** for vector storage. 
Planned extensions include hybrid search with reranking, FastAPI backend, and evaluation with RAGAS metrics.
"""
        )
        st.markdown("`RAG` `ChromaDB` `Embeddings` `FastAPI` `NLP`")

    with st.container():
        st.subheader("🟣 Noisy Adam Optimizer")
        st.caption("Dec 2024 | PhD Seminar Course")
        st.write(
            """
Developed a stochastic extension of the Adam optimizer that injects distribution-driven noise 
(Gaussian, Uniform, Laplace, Cauchy) into post-update parameter steps to improve exploration in high-dimensional 
optimization landscapes. Demonstrated smoother convergence and faster training across benchmark tasks.
"""
        )
        st.markdown("`PyTorch` `Optimization` `Research`")

    with st.container():
        st.subheader("🟡 Titan Providence")
        st.caption("Nov 2022 | Published at SCURR 2022 & NCUR 2023")
        st.write(
            """
Developed a real-time CV-based waypoint navigation pipeline on embedded Linux (Raspberry Pi), implementing 
TensorFlow/TFLite models and custom OpenCV preprocessing for onboard autonomy. Performed model quantization, 
profiling, and hardware-aware optimization, **reducing latency and compute footprint by 30%** under limited 
power and memory constraints.
"""
        )
        st.markdown("`Computer Vision` `TensorFlow Lite` `Embedded Systems` `Edge AI`")

with col2:
    with st.container():
        st.subheader("⚙️ MLOps Model Serving Pipeline")
        st.caption("Dec 2025")
        st.write(
            """
Developed a production-grade ML serving pipeline with **FastAPI, Docker, and MLflow** for versioned model deployment. 
Implemented **Prometheus metrics and Grafana dashboards** for real-time monitoring, and CI/CD automation with 
**GitHub Actions** for reproducible deployment workflows.
"""
        )
        st.markdown("`MLOps` `FastAPI` `Docker` `Prometheus` `Grafana` `CI/CD`")

    with st.container():
        st.subheader("🧠 High-Dimensional Embedding for Language-Aligned Perception")
        st.caption("Nov 2025")
        st.write(
            """
Investigated visual-to-sequential reasoning by designing a **ResNet18-GPT2 architecture** with prefix-tuning that 
encodes procedural information from images into language model representations. Systematic ablation studies revealed 
prefix token count controls vision-to-language information flow, with model capacity exhibiting sharp phase transitions.
"""
        )
        st.markdown("`Multimodal AI` `Vision-Language` `PyTorch` `Research`")

st.markdown("---")

# ----------------------
# EDUCATION
# ----------------------
st.header("Education")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎓 University of Southern California")
    st.write("**M.S. in Electrical and Computer Engineering**")
    st.write("Concentration: Machine Learning and Data Science")
    st.write("GPA: 3.8 | Aug 2024 – May 2026")

with col2:
    st.markdown("### 🎓 California State University, Fullerton")
    st.write("**B.S. in Computer Science/Engineering**")
    st.write("GPA: 3.51 | Aug 2020 – May 2024")

st.markdown("---")

# ----------------------
# RESEARCH & PUBLICATIONS
# ----------------------
st.header("Research & Publications")

st.write("📄 **CoDIT 2024** — YOLO object detection performance and hardware trade-off analysis (via Intelligent Computing Lab)")
st.write("📄 **SCURR 2022 & NCUR 2023** — CV-based drone waypoint navigation on embedded systems")
st.write("📄 **Neural Optimizer Research** — Noisy Adam optimizer for improved exploration in high-dimensional spaces")

st.markdown("---")

# ----------------------
# FOOTER
# ----------------------
st.caption("© 2025 Seena Mohajeran — Built with Streamlit")