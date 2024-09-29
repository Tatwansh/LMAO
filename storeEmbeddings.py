from src.helper import load_pdf, text_split, allMiniLM_embeddings
from langchain_community.vectorstores import FAISS
import ollama


extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = allMiniLM_embeddings()

# Storing Embeddings in Vector Database: FIASS 
faiss_db = FAISS.from_documents(documents=doc_splits, embedding=embeddings)


""""
# Retrive data from vector store
query = '''What is Text Detection with Random Perturbations?'''

# searching 
search_result = faiss_db.similarity_search(query)
search_result[0].page_content

"""