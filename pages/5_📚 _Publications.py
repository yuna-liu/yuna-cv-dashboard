import streamlit as st
from streamlit_timeline import timeline
import pandas as pd

st.set_page_config(layout="wide", page_icon="📚")

# Use markdown instead of st.title to save space
st.markdown("## 📚 Yuna's Research Publications Timeline")

# Put the title and the scholar link side-by-side using columns
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("### Research Publications")
with col2:
    st.markdown(
        "[🔗 Full Google Scholar Profile](https://scholar.google.com/citations?user=U4i_QG8AAAAJ&hl=en)",
        unsafe_allow_html=True,
    )

# Load CSV
df = pd.read_csv("data/citations.csv")

# Journal logos
journal_covers = {
    "Borsa Istanbul Review": "https://ars.els-cdn.com/content/image/X22148450.jpg",
    "Economics Letters": "https://ars.els-cdn.com/content/image/X01651765.jpg",
    "Nordic Journal of Business": "http://njb.fi/wp-content/uploads/2015/03/Textlogo.jpg",
    "Digitala Vetenskapliga Arkivet": "https://www.umu.se/Static/img/umu-logo-left-neg-EN.svg"
}

# Build events
events = []
for _, row in df.iterrows():
    title = row["Title"]
    journal = row["Publication"]
    year = int(row["Year"])
    link = row.get("link", "")

    description = f"Published in <i>{journal}</i>."
    if pd.notna(link) and link.strip() != "":
        description += f'<br><a href="{link.strip()}" target="_blank">🔗 View Publication</a>'

    event = {
        "start_date": {"year": str(year), "month": "01", "day": "01"},
        "text": {"headline": title, "text": description}
    }

    if journal in journal_covers:
        event["media"] = {
            "url": journal_covers[journal],
            "caption": journal
        }

    events.append(event)

# Timeline data structure
timeline_data = {
    "title": {
        "text": {
            "headline": "",
            "text": ""
        }
    },
    "events": events
}

# Display timeline
timeline(timeline_data, height=700)  # Slightly reduced height for better fit
