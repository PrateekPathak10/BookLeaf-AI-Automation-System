import streamlit as st
import requests

st.title("BookLeaf AI Support Assistant")

email = st.text_input("Registered Email")

query = st.text_area("Ask your query")

if st.button("Submit"):

    payload = {
        "query": query,
        "email": email
    }

    response = requests.post(
        "http://127.0.0.1:8000/query",
        json=payload
    )

    result = response.json()
    

    st.success(result["response"])

    st.write(
        f"Confidence Score: {result['confidence']}"
    )

    if result["escalated"]:
        st.warning("Escalated to Human Agent")