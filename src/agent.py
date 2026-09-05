from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate


DB_PATH = "chroma_db"

def query_agent(question):
 
    embedding_func = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    vectorstore = Chroma(
        persist_directory=DB_PATH, 
        embedding_function=embedding_func
    )
    
   
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    
   
    llm = OllamaLLM(model="llama3") 
    

    prompt = ChatPromptTemplate.from_template("""
    Answer the following question based only on the provided context:
    {context}
    
    Question: {input}
    """)
    
   
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)
    
 
    print("\nThinking...")
    result = retrieval_chain.invoke({"input": question})
    print("\nAI Answer:", result["answer"])

if __name__ == "__main__":
    q = input("Ask a question about the machine: ")
    query_agent(q)
