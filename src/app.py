from dotenv import load_dotenv
import streamlit as st
import streamlit_navigation_bar as st_navbar

from langchain_core.messages import HumanMessage, AIMessage
from langchain_cohere import ChatCohere
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser


load_dotenv()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(page_title="ChatBot", page_icon="🤖")
# st_navbar(logo_path="https://huggingface.co/recogna-nlp/bode-7b-alpaca-pt-br/resolve/main/Logo_Bode_LLM_Circle.png", pages=[])

# interface
st.sidebar.markdown(
    """
    <div style="display: flex; align-items: center; justify-content:center; flex-direction: column;">
        <img src="https://huggingface.co/recogna-nlp/bode-7b-alpaca-pt-br/resolve/main/Logo_Bode_LLM_Circle.png" alt="Bode LLM Logo" width="100px">
        <h3 style="color:#9ffec8">ChatBODE</h3>
    </div>""",
    unsafe_allow_html=True,
)

# st.sidebar.page_link("./app.py", label="Conversa 1")
# st.sidebar.page_link("./app.py", label="Conversa 2")
# st.sidebar.page_link("./app.py", label="Conversa 3")
# st.sidebar.page_link("./app.py", label="Conversa 4")

container = st.container(height=500, border=False)


# # get response
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


def stream_response(user_input, chat_history):
    llm = ChatCohere()
    prompt = ChatPromptTemplate.from_template(
        """You are a personal assistant that should help the user with their questions. 
                                              Make sure to keep attention to the chat history: {chat_history}.
                                                Now, the question of the user is {input}"""
    )

    chain = prompt | llm | StrOutputParser()
    return chain.stream({"input": user_input, "chat_history": chat_history})


# # conversation
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        container.chat_message("Human").markdown(message.content)
    else:
        container.chat_message("AI").markdown(message.content)

# # user input & AI answer
user_query = st.chat_input("You: ")  # add a chat input in the screen
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(user_query))

    container.chat_message("Human").markdown(user_query)
    ai_response = container.chat_message("AI").write_stream(
        stream_response(
            user_input=user_query, chat_history=st.session_state.chat_history
        )
    )

    st.session_state.chat_history.append(AIMessage(ai_response))
