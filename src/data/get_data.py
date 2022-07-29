import subprocess
import os

import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup

import json

def get_data_john_hopkins():
    #Data retrieval by a git pull request
    git_pull = subprocess.Popen( "/usr/bin/git pull" ,
                         cwd = os.path.dirname( 'data/raw/COVID-19/' ),
                         shell = True,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE )
    (out, error) = git_pull.communicate()

    print("Error : " + str(error))
    print("out : " + str(out))


def get_current_data_germany():
    #Get current data from germany
    #data=requests.get('https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/Coronaf%C3%A4lle_in_den_Bundesl%C3%A4ndern/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')

    data=requests.get('https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')

    json_obj = json.loads(data.content)
    final_list=[]
    for k,v in enumerate (json_obj['features'][:]):
        final_list.append(v['attributes'])

    pd_full_list=pd.DataFrame(final_list)
    pd_full_list.to_csv('data/raw/NPGEO/germany_state_data.csv',sep=';')
    print(' Number of regions rows: '+str(pd_full_list.shape[0]))

if __name__ == '__main__':
    get_data_john_hopkins()
    get_current_data_germany()
