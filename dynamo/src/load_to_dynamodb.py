from decimal import Decimal

# we have to convert the types as the boto3 takes decimals not float values
def convert_types(docs):
    if isinstance(docs,dict):
        return {k:convert_types(v) for k,v in docs.items()}
    elif isinstance(docs,list):
        return [convert_types(i) for i in docs]
    elif isinstance(docs, float):
        return Decimal(str(docs))
    return docs

def load_data(documents,table):
    for doc in documents:
        item = convert_types(doc)
        table.put_item(Item=item)



