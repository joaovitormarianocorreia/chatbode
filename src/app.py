from dotenv import load_dotenv
import streamlit as st
import streamlit_navigation_bar as st_navbar

from langchain_core.messages import HumanMessage, AIMessage
from langchain_cohere import ChatCohere
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

load_dotenv()

if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {"Default": []}
    st.session_state.current_chat = "Default"

st.set_page_config(page_title="ChatBot", page_icon="🤖")

# Sidebar for chat session management
st.sidebar.markdown(
    """
    <div style="display: flex; align-items: center; justify-content:center; flex-direction: column;">
        <img src="https://huggingface.co/recogna-nlp/bode-7b-alpaca-pt-br/resolve/main/Logo_Bode_LLM_Circle.png" alt="Bode LLM Logo" width="100px">
        <h3 style="color:#9ffec8">ChatBODE</h3>
    </div>""",
    unsafe_allow_html=True,
)

# Function to create a new chat session
def create_new_chat():
    new_chat_name = st.sidebar.text_input("Nome do Chat", key="new_chat_name")
    if st.sidebar.button("criar novo chat", key="create_chat"):
        if new_chat_name:
            st.session_state.chat_sessions[new_chat_name] = []
            st.session_state.current_chat = new_chat_name

# Display current chat sessions
st.sidebar.markdown("## Chats")
for chat_name in st.session_state.chat_sessions.keys():
    if st.sidebar.button(chat_name, key=f"select_{chat_name}"):
        st.session_state.current_chat = chat_name

create_new_chat()

# Function to get the current chat history
def get_current_chat_history():
    return st.session_state.chat_sessions[st.session_state.current_chat]

# Container for chat messages
container = st.container()

# Function to get response from the bot
def get_response(user_input, chat_history):
    llm = ChatCohere()
    prompt = ChatPromptTemplate.from_template(
        """You are a personal assistant that should help the user with their questions. 
        Make sure to keep attention to the chat history: {chat_history}.
        Now, the question of the user is {input}"""
    )

    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"input": user_input, "chat_history": chat_history})
    return response

# Function to stream response from the bot
def stream_response(user_input, chat_history):
    llm = ChatCohere()
    prompt = ChatPromptTemplate.from_template(
        """You are a personal assistant that should help the user with their questions. 
        Make sure to keep attention to the chat history: {chat_history}.
        Now, the question of the user is {input}"""
    )

    chain = prompt | llm | StrOutputParser()
    return chain.stream({"input": user_input, "chat_history": chat_history})

# Display the current chat history
current_chat_history = get_current_chat_history()
for message in current_chat_history:
    if isinstance(message, HumanMessage):
        container.chat_message("Human").markdown(message.content)
    else:
        container.chat_message("AI").markdown(message.content)

# Handle user input and AI response
user_query = st.chat_input("You: ")  # add a chat input in the screen
if user_query is not None and user_query != "":
    current_chat_history.append(HumanMessage(user_query))

    container.chat_message("Human").markdown(user_query)
    ai_response = container.chat_message("AI").write_stream(
        stream_response(
            user_input=user_query, chat_history=current_chat_history
        )
    )

    current_chat_history.append(AIMessage(ai_response))

# Update the chat history in session state
st.session_state.chat_sessions[st.session_state.current_chat] = current_chat_history
