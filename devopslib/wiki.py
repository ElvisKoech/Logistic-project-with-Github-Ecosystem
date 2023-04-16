import wikipedia
from yake import KeywordExtractor

# build a function to return a summary of a wikipedia page
def get_summary(page_name):
    """Returns a summary of a wikipedia page."""
    summary = wikipedia.summary(page_name)
    return summary


# build a function search for a wikipedia page for match
def search_for_match(page_name):
    """Returns a summary of a wikipedia page."""
    summary = wikipedia.search(page_name)
    return summary


# build a function to return  wikipedia pages
def get_wiki_pages(page):
    """Returns a list of all wikipedia pages."""
    pages = wikipedia.page(page)
    return pages


# build a function to return keywords from wikipedia page
def get_wiki_keywords(page):
    """Returns a list of all wikipedia keywords."""
    content = get_wiki_pages(page).content
    extractor = KeywordExtractor()
    keywords = extractor.extract_keywords(content)
    return {keyword: score for keyword, score in keywords.items[:10]}
