#stephen fitzsimon 27 July 2022
#Acquire module for the Magic The Gathering Card prediction project
import os #to check for filenames
import json #to handle json files
import requests
import pandas as pd #to handle dataframes


#holds the filename of the json
FILENAME = 'default-cards-20220727090443.json'

### FUNCTIONS TO GET DATA FROM URL OR FILE

def get_data(query_url=False):
    """
    Retrieves the data from the saved file or from the url if 
    no file is present.
    Args:
        query_url (bool) : forces a url query (default=False)
    Returns:
        data (DataFrame) : a dataframe constaining scryfall data
    """
    #check if file exists or query_url is true
    if query_url or not os.path.exists(FILENAME):
        #get data from url
        print('Getting file from URL...')
        read_from_url()
        df = read_from_file()
    else:
        #file found, read data from file
        print('Found file in working directory!')
        df = read_from_file()
    #return the data
    return df

def read_from_file():
    """
    Reads the json as a dataframe
    Returns:
        DataFrame : DataFrame from saved file
    """
    return pd.read_json(FILENAME)

def read_from_url():
    """
    Gets the json file from the Scryfall website and writes it 
    to a json file
    """
    #holds the url for the scryfall data
    url = 'https://c2.scryfall.com/file/scryfall-bulk/default-cards/default-cards-20220727210548.json'
    response = requests.get(url)
    data = response.json()
    print('Retrieved data from url!')
    #write data to the file
    with open(FILENAME, 'w') as f:
        json.dump(data, f)
        print('Saved data to file!')\
    