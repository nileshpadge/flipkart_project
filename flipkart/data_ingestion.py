from langchain_astradb import AstraDBVectorStore
#from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings


import os
from flipkart.data_converter import dataconverter
from dotenv import load_dotenv
load_dotenv()




GROQ_API_KEY=os.getenv("GROQ_API_KEY")
ASTRA_DB_API_ENDPOINT=os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE=os.getenv("ASTRA_DB_KEYSPACE")
HF_TOKEN = os.getenv("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")

embeddings= HuggingFaceEmbeddings(model_name="BAAI/bge-base-en-v1.5",model_kwargs={"token": HF_TOKEN})
import os
from langchain_community.embeddings import HuggingFaceEmbeddings

# Set your HF token
#HF_TOKEN = "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"

# embeddings = HuggingFaceEmbeddings(
#     model_name="BAAI/bge-base-en-v1.5",
#     model_kwargs={"use_auth_token": HF_TOKEN}
# )




def data_ingestion(status):

    vector_store = AstraDBVectorStore(
        embedding=embeddings,
        collection_name = "flipkart_status",
        api_endpoint = ASTRA_DB_API_ENDPOINT,
        token = ASTRA_DB_APPLICATION_TOKEN,
        namespace = ASTRA_DB_KEYSPACE 
    )



    storage = status

    if storage is None:
        docs = dataconverter()
        insert_ids = vector_store.add_documents(docs)
    
    else:
        return vector_store
    return vector_store, insert_ids

if __name__ == "__main__":

    vector_store, insert_ids = data_ingestion(None)
    print(f"\n Inserted {len(insert_ids)} documents.")
    results = vector_store.similarity_search("give me laptop list ?")
    for res in results:
        print(f"\n {res.page_content} [{res.metadata}]")