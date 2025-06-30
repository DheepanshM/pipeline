import pandas as pd

def normalize_technologies(df):
    return df.explode("technologies") #if the cloumn has multiple values ,it divides using explode