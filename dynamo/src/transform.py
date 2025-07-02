import pandas as pd

def transform_data(documents):
    seen = set()
    unique_docs = []

    for doc in documents:
        doc.pop("_id", None)  # Remove _id
        doc_key = str(sorted(doc.items()))  # Convert to a hashable string
        if doc_key not in seen:
            seen.add(doc_key)
            unique_docs.append(doc)

    return unique_docs
