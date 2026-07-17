from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Initialize the same embedding model you used for ingestion
embedding_func = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load the existing database
vectorstore = Chroma(
    persist_directory="chroma_db", 
    embedding_function=embedding_func
)

# Peek at the database
count = vectorstore._collection.count()
print(f"Number of document chunks in DB: {count}")

# Check what the first chunk looks like
if count > 0:
    results = vectorstore.similarity_search("VMC15", k=1)
    print("\nSample content found in DB:")
    print(results[0].page_content[:500])
else:
    print("\nDatabase is empty! You need to run src/ingest.py again.")