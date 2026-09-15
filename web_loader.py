import trafilatura


def fetch_page_content(url: str) -> str | None:
    """Download and extract the main text from a webpage"""
    
    downloaded = trafilatura.fetch_url(url)
    
    if downloaded is None:
        return None 
    
    content = trafilatura.extract(
        downloaded,
        include_comments=False,
        include_tables=False,
    )
    
    return content