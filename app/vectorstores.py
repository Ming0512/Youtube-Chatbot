from pathlib import Path
from langchain_chroma import Chroma
from app.embeddings import get_embedding

VECTORSTORE_DIR = Path("chroma_db")

def create_vectorstore(documents, video_id:str):
    """Create Vectorstores for one YouTube Video."""
    
    embeddings = get_embedding()
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name=f"Video_{video_id}",
        persist_directory=str(VECTORSTORE_DIR)
    )
    return vectorstore