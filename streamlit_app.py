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

# Footer
st.markdown("---")
st.markdown("📧 _Want to connect? Let’s build something amazing!_")

# Optional: Add a download button for resume if you have a PDF
# with open("chetan_resume.pdf", "rb") as file:
#     st.download_button("📄 Download Resume (PDF)", file, "Chetan_Patil_Resume.pdf")
