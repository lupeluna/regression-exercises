import pandas as pd
import numpy as np
import os

# acquire
from env import host, user, password
from pydataset import data

# turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split


# Create helper function to get the necessary connection url.
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
    
    
    
    # Use the above helper function and a sql query in a single function.
def new_telco_data():
    '''
    This function reads data from the Codeup db into a df.
    '''
    telco_query = '''SELECT customer_id, monthly_charges, tenure, total_charges
                FROM customers
                WHERE contract_type_id = 3'''
    
    
    # reads SQL query into a DataFrame
    df = pd.read_sql(telco_query, get_connection('telco_churn'))
    return df
    
    
def wrangle_telco():
    '''
    checks for existing telco_churn csv file and loads if present, otherwise runs 
    new_telco_data function to acquire data
    '''
    if os.path.isfile('telco_churn.csv'):
        df = pd.read_csv('telco_churn.csv', index_col=0)
    else:
        # pull in data and creates csv file if not already present
        df = new_telco_data()
        df.to_csv('telco_churn.csv')
        
    # replace symbols, etc with Nans
    df = df.replace(r'^\s*$', np.nan, regex=True)
    
    # replace Nans in total_charges with value from monthly_charges
    df.total_charges = df.total_charges.fillna(df.monthly_charges)
    
    # change total_charges data type with value from monthly_charges
    df['total_charges'] = df['total_charges'].astype('float')    
    return df

