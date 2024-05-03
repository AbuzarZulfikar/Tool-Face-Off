from openai import OpenAI
import streamlit as st
import time

openai_apikey = "sk-proj-sxtS1qXeZTM4y70MsRmBT3BlbkFJoyHj9Y7SS8xUmFMURhyb"

#client = openai
#from openai import OpenAI

client = OpenAI(api_key=openai_apikey, default_headers={"OpenAI-Beta": "assistants=v1"})

file = client.files.create(
file=open("data/testPages.pdf","rb"),
purpose="assistants"
)

print("file id: " + file.id)
#For version v1
assistant = client.beta.assistants.create(
  name="Mental Health Bot",
  instructions="you are a health practitioner bot that just give general health advice.",
  tools=[{"type": "retrieval"}],
  model="gpt-3.5-turbo-1106",
  file_ids=[file.id]
)

# "attachments": [
#         { "file_id": message_file.id, "tools": [{"type": "file_search"}] }
#       ],


#use in V2 assistant api
#vector_store = client.beta.vector_stores.create(name="General Advice")
# vector_store = client.beta.vector_stores.create(
#   name="General Advice",
#   file_ids=[file.id]
# )

#For version V2
# assistant = client.beta.assistants.create(
#   name="Mental Health Bot",
#   description="you are a health practitioner bot that just give general health advice.",
#   model="gpt-3.5-turbo",
#   tools=[{"type": "file_search"}],
#   tool_resources={
#       "file_search": {
#       "vector_store_ids": [vector_store.id]
#     },
#     # "file_search": {
#     #   "file_ids": file.id
#     # }
#   }
# )



if "start_chat" not in st.session_state:
    st.session_state.start_chat = False
if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

st.set_page_config(page_title="Mental Health Bot", page_icon=":speech_balloon:")

#openai.api_key = "sk-insert Your OpenAI API Key"

if st.sidebar.button("Start Chat"):
    st.session_state.start_chat = True
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id

st.title("Mental Health Chatbot")
st.write("I am a Mental Health Bot")

if st.button("Exit Chat"):
    st.session_state.messages = []  # Clear the chat history
    st.session_state.start_chat = False  # Reset the chat state
    st.session_state.thread_id = None

if st.session_state.start_chat:
    if "openai_model" not in st.session_state:
        st.session_state.openai_model = "gpt-3.5-turbo-1106"
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("User:"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        client.beta.threads.messages.create(
                thread_id=st.session_state.thread_id,
                role="user",
                content=prompt
                #file_ids=[file.id]
            #    attachments: [{ "file_id": message_file.id, "tools": [{"type": "file_search"}] }],
            )
        
        run = client.beta.threads.runs.create(
            thread_id=st.session_state.thread_id,
            assistant_id=assistant.id,
            instructions="Please answer the queries with health practitioner bot. Just give general health advice."
        )

        while run.status in ['queued', 'in_progress', 'cancelling']:   #!= 'completed':
            time.sleep(1)
            run = client.beta.threads.runs.retrieve(
                thread_id=st.session_state.thread_id,
                run_id=run.id
            )
        messages = client.beta.threads.messages.list(
            thread_id=st.session_state.thread_id
        )

        # Process and display assistant messages
        assistant_messages_for_run = [
            message for message in messages 
            if message.run_id == run.id and message.role == "assistant"
        ]
        for message in assistant_messages_for_run:
            st.session_state.messages.append({"role": "assistant", "content": message.content[0].text.value})
            with st.chat_message("assistant"):
                st.markdown(message.content[0].text.value)

else:
    st.write("Click 'Start Chat' to begin.")
