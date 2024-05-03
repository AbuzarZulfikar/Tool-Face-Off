
from trulens_eval import Tru
from trulens_eval.tru_custom_app import instrument
tru = Tru()
# tru.reset_database()

from trulens_eval import Feedback, Select
from trulens_eval.feedback import Groundedness
#from trulens_eval.feedback.provider.openai import fOpenAI
from trulens_eval.feedback.provider.openai import OpenAI as fOpenAI
from trulens_eval import TruCustomApp
import numpy as np

# import streamlit as st
import time
from openai import OpenAI

#import testTruLens
# openai_apikey = "sk-proj-WLI8hLo4RSkmgPNvfEVAT3BlbkFJxwUY3cV2iMNF4OhxrCXe"


openai_apikey = "sk-proj-3ViR5ld74PUm7rFgqqPlT3BlbkFJiYtY2ysxbqHMS1GSJHrU"
#client = OpenAI(api_key=openai_apikey, default_headers={"OpenAI-Beta": "assistants=v1"})

provider = fOpenAI(api_key=openai_apikey)

grounded = Groundedness(groundedness_provider=provider)

    # Define a groundedness feedback function
f_groundedness = (
    Feedback(grounded.groundedness_measure_with_cot_reasons, name = "Groundedness")
    .on(Select.RecordCalls.retrieve_and_generate.rets.collect())
    .on_output()
    #  .on(Select.RecordCalls.retrieve_and_generate.rets[1])
    #  .on(Select.RecordCalls.retrieve_and_generate.rets[0])
    .aggregate(grounded.grounded_statements_aggregator)
)

# Question/answer relevance between overall question and answer.
f_answer_relevance = (
    Feedback(provider.relevance_with_cot_reasons, name = "Answer Relevance")
    .on(Select.RecordCalls.retrieve_and_generate.args.query)
    .on_output()
    # .on(Select.RecordCalls.retrieve_and_generate.rets[0])
)

# Question/statement relevance between question and each context chunk.
f_context_relevance = (
    Feedback(provider.context_relevance_with_cot_reasons, name = "Context Relevance")
    .on(Select.RecordCalls.retrieve_and_generate.args.query)
    # .on(Select.RecordCalls.retrieve_and_generate.rets[1])
    .on(Select.RecordCalls.retrieve_and_generate.rets.collect())
    .aggregate(np.mean)
)



class RAG_with_OpenAI_Assistant:
    def __init__(self):
        client = OpenAI(api_key=openai_apikey)
        self.client = client
        # upload the file\
        file = self.client.files.create(
        file=open("data/Q_A.txt", "rb"),
        purpose='assistants'
        )

        # create the assistant with access to a retrieval tool
        assistant = client.beta.assistants.create(
            name="Mental_Health_Bot",
            instructions="You are an assistant that answers questions about mental health advice.",
            tools=[{"type": "retrieval"}],
            model="gpt-3.5-turbo-1106",
            file_ids=[file.id]
        )
        
        self.assistant = assistant

   
    @instrument
    def retrieve_and_generate(self, query: str) -> str:
        """
        Retrieve relevant text by creating and running a thread with the OpenAI assistant.
        """

        self.thread = self.client.beta.threads.create()           
        self.message =  self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=query
        )

        run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id,
            instructions="Please answer the queries with health practitioner bot. Just give general health advice."
        )

                # Wait for the run to complete
                
        while run.status in ['queued', 'in_progress', 'cancelling']:
            time.sleep(1)
            run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id,
                run_id=run.id
            )

        if run.status == 'completed':
            messages = self.client.beta.threads.messages.list(
                    thread_id=self.thread.id
                )
               
            response = messages.data[0].content[0].text.value
            #quote = messages.data[0].content[0].text.annotations[0].file_citation.quote
        else:
            response = "Unable to retrieve information at this time."

        return response#, quote
    
   

if __name__ == "__main__":
    rag = RAG_with_OpenAI_Assistant()

    
    tru_rag = TruCustomApp(rag,
        app_id = 'Mental Health Bot Using OpenAI Assistant RAG',
        feedbacks = [f_groundedness, f_answer_relevance])#, f_context_relevance])

    with tru_rag:
        result = rag.retrieve_and_generate("I am stressed")

    #from trulens_eval import Tru
    tru.get_leaderboard(app_ids=["Mental Health Bot Using OpenAI Assistant RAG"])
    tru.run_dashboard()