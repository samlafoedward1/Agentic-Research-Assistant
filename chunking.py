from langchain_text_splitters import RecursiveCharacterTextSplitter


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150,
)


def chunk_text(text: str) -> list[str]:
    """Split webpage content into overlapping chunks"""
    
    return text_splitter.split_text(text)


