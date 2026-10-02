def get_retriever(vectorstore, k: int = 4):
    """Create similarity retriever."""
    
    return vectorstore.as_retriever(
        search_kwargs={'k':k}
    )