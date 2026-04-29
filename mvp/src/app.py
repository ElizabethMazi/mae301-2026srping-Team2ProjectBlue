print("APP STARTING")

import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    /* Force same radius everywhere */
    .stTextInput,
    .stTextInput > div,
    .stTextInput > div > div,
    div[data-baseweb="input"],
    div[data-baseweb="input"] > div {
        border-radius: 11px !important;
    

    /* Your input box */
    div[data-baseweb="input"] > div {
        background-color: #AB9E91;
        border: 1px solid #8F857A;
        border-radius: 10px !important;
    }

    /* Text */
    .stTextInput input {
        color: #2B2B2B !important;
    }

    /* Placeholder */
    .stTextInput input::placeholder {
        color: #4A4541 !important;
    }

    /* Focus state */
    .stTextInput:focus-within div[data-baseweb="input"] > div {
        border: 1px solid #312129 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Pima County Home-buyer Assistant")
st.markdown(
"""
This AI assistant helps home buyers understand how future developments in Pima County may shape neighborhood growth, livability, and long-term value.

Use it to get clearer insight into the area you wish to call home!

Explore topics like:
- Planned infrastructure and road expansions  
- Zoning changes and growth areas  
- Long-term neighborhood development  
- General home-buying considerations like schools, safety, and local conditions *(when information is available)*
"""
)

query = st.text_input(
    "What would you like to know?",
    placeholder='Try asking: Are there major projects planned nearby?'
    )

if query:
    from src.retrieve import search
    from src.generate import generate_answer

    docs = search(query)
    answer = generate_answer(query, docs)

    st.write(answer)

    st.subheader("Sources")

    seen_sources = set()

    for d in docs:
        source = d["source"]
        if source not in seen_sources:
            st.write(source)
            seen_sources.add(source)
