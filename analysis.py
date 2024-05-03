
import streamlit as st

def welcome():
    st.title("Financial Analysis Chatbot")
    st.write("Welcome to the Financial Analysis Chatbot. Please upload your financial statement to get started.")

def upload_file():
    uploaded_file = st.file_uploader("Upload your financial statement (CSV or Excel)", type=["csv", "pdf"])
    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        return uploaded_file
    else:
        return None

def select_analysis():
    st.subheader("Select the type of analysis")
    analysis_type = st.selectbox("Choose analysis type", ["Horizontal Analysis", "Vertical Analysis", "Ratio Analysis"])
    return analysis_type

def perform_analysis(file, analysis_type):
    # Here you would perform the analysis based on the uploaded file and the selected analysis type
    # You can use libraries like pandas for data manipulation and analysis
    
    # Placeholder for demonstration
    result = f"Performing {analysis_type} on the uploaded file..."
    return result

def app():
    welcome()
    file = upload_file()
    if file:
        analysis_type = select_analysis()
        if st.button("Perform Analysis"):
            result = perform_analysis(file, analysis_type)
            st.subheader("Analysis Result")
            st.write(result)


# import streamlit as st
# import openai
# def app():
#     # st.subheader('Chat now')

#     # st.text_area(label='#',value='Please wait this page is under construction..')

#     st.title("OFIN")

#     # Set your OpenAI API key
#     openai.api_key = "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"

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     if prompt := st.chat_input("What is up?"):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         with st.spinner(text="Assistant is typing..."):
#             response = openai.Completion.create(
#                 engine="text-davinci-002",  # You can change the engine as needed
#                 prompt="\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages]),
#                 temperature=0.7,
#                 max_tokens=150,
#                 stop=["\n"],
#             )
#             assistant_response = response.choices[0].text.strip()

#         st.session_state.messages.append({"role": "assistant", "content": assistant_response})
#         with st.chat_message("assistant"):
#             st.markdown(assistant_response)
