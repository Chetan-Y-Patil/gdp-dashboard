import streamlit as st

# Page Configuration
st.set_page_config(page_title="Chetan Patil - Resume", layout="centered")

# Header
st.title("👨‍🎓 Chetan Patil")
st.subheader("Final Year B.Tech Student | R. C. Patel Institute of Technology")

# Personal Details
st.markdown("""
- 🎓 **CGPA**: `8.0`
- 🏫 **Diploma**: Government Polytechnic, Nandurbar  
  - **Branch**: Computer Technology  
  - **Percentage**: `85%`
""")

# Skills
st.markdown("## 🛠️ Skills")
st.markdown("""
- 💻 Java
- 🐍 Python
- 🌐 HTML
- 🎨 CSS
""")

# Resume Download Button
st.markdown("## 📄 Download My Resume")
try:
    with open("chetan_resume.pdf", "rb") as file:
        st.download_button(
            label="📥 Download Resume (PDF)",
            data=file,
            file_name="Chetan_Patil_Resume.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.error("❌ Resume file not found! Please make sure `chetan_resume.pdf` is in the app folder.")

# Footer
st.markdown("---")
st.markdown("📧 _Want to connect? Let’s build something amazing!_")
