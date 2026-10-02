from langchain_openai import OpenAIEmbeddings

def get_embedding():
    """Create the open AI embedding Model."""
    
    return OpenAIEmbeddings(
        model="text-embedding-3-small"
    )