import streamlit as st
import qdrant_client
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import Qdrant
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

embeddings = CohereEmbeddings(model="embed-english-light-v3.0",cohere_api_key="HgZpQb9mGtu3BmkG9AtMQVhT9kRW9VHSqSXk2kqP")
llm = ChatGroq(temperature=0.5, groq_api_key="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", model_name="llama3-70b-8192")

from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    url="https://1ab5e976-8980-472c-878b-4730a4e34d0c.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="YNm0FNkIrd_brOMMtX0x_S40YxUYbVEQgWDr05UY2X2lBahcX8Lr3g",
)


vectorstore = Qdrant(
        client=qdrant_client,
        collection_name="raga-docs",
        embeddings=embeddings
    )


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs[:2])

def qa(query, context):
    prompt = f"""
    You are an expert assistant with access to the RAGA AI documentation. A user has asked the following question:

    "{query}"

    Based on the following context from the RAGA AI documentation:

    {context}

    If the query is not related to Raga docs context given or Is the context relevant to the query above? if not then respond with "I cannot help you with this query". The must strictly come from the context 

    If you have the answer in the context then:

    Please provide a detailed, accurate, and step-by-step answer to the user's question. If the answer requires code, include the necessary code snippets. List points and steps as needed to give a comprehensive and precise response.

    Ensure that your answer is based solely on the provided context. If the information is not available in the context, respond with "The information you requested is not available in the provided context."

    Do not include unnecessary statements like based on the context. The response should be concise yet contain all information like Code, points, steps.

    Answer:
    """
    
    response = llm.invoke(prompt)
    return response.content

# Streamlit App
st.title('Chat with Raga.ai Docs')

query = st.text_input('Enter your query:')
if query:
    found_docs = vectorstore.similarity_search(query)
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in found_docs[:2])
    context = format_docs(found_docs)

    response = qa(query,context)

    st.markdown(f"### Response:\n{response}")
