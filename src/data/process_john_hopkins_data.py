# %load ../src/data/process_john_hopkins_data.py
import pandas as pd
import numpy as np

from datetime import datetime


def process_JH_data():
    data_path_git = '../data/raw/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    pd_raw = pd.read_csv(data_path_git)
    pd_data_base = pd_raw.rename(columns = {'Country/Region': 'country', 'Province/State' : 'state'})

    pd_data_base['state']=pd_data_base['state'].fillna('no')

    pd_data_base=pd_data_base.drop(['Lat','Long'],axis=1)
    test_pd = pd_data_base.set_index(['state','country']).T.stack(level=[0,1]).reset_index().rename(columns={'level_0':'date', 0:'confirmed'},)

    test_pd['date']=test_pd.date.astype('datetime64[ns]')

    test_pd.to_csv('../data/processed/COVID_relational_confirmed.csv',sep=';',index=False)
    print(' Number of rows stored: '+str(test_pd.shape[0]))

if __name__ == '__main__':

    process_JH_data()
