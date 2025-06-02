import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Meet Yuna Liu – A Structured Mind for an Unstructured World! 👋")

st.sidebar.success("Select an aspect above.")

st.markdown("""
This dashboard consists of several pages, each highlighting an important aspect of my professional journey:

- 💼 **Work Experience** — Explore my career milestones and roles.  
- 🎓 **Education** — Details about my academic background.  
- 🎖️ **Certifications** — Professional certificates I earned.  
- ❄️ **Chatbot Demo** — Interactive demo showcasing AI chatbot capabilities I developed developed as part of a GenAI project.  
- 📚 **Publications** — A timeline view of my research publications.

Use the sidebar to navigate between pages. Enjoy exploring! 😊
""")

st.markdown("---")
st.caption("Created with ❤️ by Yuna Liu")
