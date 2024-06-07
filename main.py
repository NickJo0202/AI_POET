from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

import streamlit as st

st.title("인공지능 작가")
subject = st.text_input("소설의 주제를 입력해주세요.")
st.write("소설의 주제 : " + subject)

if st.button("소설 작성"):
    with st.spinner("소설 작성중 ..."):
        result = chat_model.invoke(subject + "에 대한 소설를 써줘")
        st.write(result.content)