import pandas as pd 
from langchain_core.documents import Document

def dataconverter():

    product_data = pd.read_csv(r'E:\pandas\flipkart_project\data\flipkart_project_data.csv')

    data = product_data[["Product Name", "Price", "Description", "Ratings"]]

    product_list= []

    for index, row in data.iterrows():
        object = {
            "product_name": row["Product Name"],
            "description" : row['Description']

        }
    product_list.append(object)

    docs = []

    for object in product_list:
        metadata = {"product_name": object["product_name"]}
        page_content = object["description"]

        doc = Document(page_content=page_content, metadata=metadata)
        docs.append(doc)

    return docs
