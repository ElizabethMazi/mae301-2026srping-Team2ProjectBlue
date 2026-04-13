import streamlit as st

st.title("Project Blue AI Assistant")

query = st.text_input("Ask a question about development:")

if query:
    from scripts.retrieve import search
    from scripts.generate import generate_answer

    docs = search(query)
    answer = generate_answer(query, docs)

    st.write(answer)

    st.subheader("Sources")
    for d in docs:
        st.write(f"{d['source']} ({d['id']})")
