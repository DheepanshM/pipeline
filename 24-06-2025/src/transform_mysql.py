import pandas as pd

def transform_data(data):

    
    #removing duplicates
    data=data.drop_duplicates()
    #check if any null values
    print(data.isnull().sum())
    #sort the values by order amount
    data=data.sort_values(by='order_amount',ascending=False)
    return data