from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_transcript(
    transcript: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 150,
):
    """Splits transcripts into overlapping chunks."""
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    
    return RecursiveCharacterTextSplitter([transcript])