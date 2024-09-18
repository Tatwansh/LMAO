import arxiv
import pandas as pd
import re

def retr(q):
    search = arxiv.Search(query=q, max_results=100, sort_by=arxiv.SortCriterion.SubmittedDate)
    papers = list(search.results())
    data = []

    for result in papers:
        result.pdf_url = re.sub(r'v\d+$', '', result.pdf_url)

        data.append({"authors": result.authors,
                     "Categories": result.categories,
                     "commentss": result.comment,
                     "doi": result.doi,
                     "entry_id": result.entry_id,
                     "journal_ref": result.journal_ref,
                     "pdf_url": "https://export." + result.pdf_url.split("://")[-1],
                     "primary_category": result.primary_category,
                     "summary": result.summary,
                     "title": result.title,
                     "updated": result.updated
                     })
    df = pd.DataFrame(data)
    print(df.head())
