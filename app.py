#chatbot takes prompt - gives response - maintains the conversation 

import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.schema import HumanMessage, AIMessage

load_dotenv()

#open api key playground

st.set_page_config(
    page_title='AI Chatbot',
    layout="centered"
)

st.title("AI Chatbot")
st.subheader("Built with Streamlit Langchain and Groq")

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

if 'conversation' not in st.session_state:    
    llm = ChatGroq(
        model_name = 'llama-3.3-70b-versatile',
        temperature=0.7,
        api_key=os.getenv('GROQ_API_KEY')
        )
    
    memory = ConversationBufferMemory(return_messages=True)

    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory = memory,
        verbose = False
    )

for message in st.session_state.chat_history:
    if isinstance(message,HumanMessage):
        with st.chat_message('user'):
            st.write(message.content)

    else:
        with st.chat_message('assistant'):
            st.write(message.content)    


user_input = st.chat_input("Type your message here...")  

if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message('user'):
        st.write(user_input)

    with st.chat_message('assistant'):
        with st.spinner('Thinking....'):
            response = st.session_state.conversation.predict(input= user_input)
            st.write(response)

    st.session_state.chat_history.append(AIMessage(content=response))

with st.sidebar:
    st.title('options')

    if st.button('Clear chat history'):
        st.session_state.chat_history = []

        memory = ConversationBufferMemory(return_messages=True) 

        llm = ChatGroq(
            model_name = 'llama-3.3-70b-versatile',
            temperature=0.7,
            api_key=os.getenv('GROQ_API_KEY')
            )


        st.session_state.conversation = ConversationChain(

            llm=llm,
            memory = memory,
            verbose = False
        )

        st.rerun()

    st.subheader("About")

    st.markdown(
        '''
        This Chatbot uses: 

        - **Streamlit** for the web interface
        - **Langchain** for conversation management
        - **Groq** language model used 
        - **ConversationBufferMemory** to keep track of all conversations 
  '''  )    



