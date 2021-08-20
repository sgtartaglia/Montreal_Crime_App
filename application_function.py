import pandas as pd
import requests
import streamlit as st
## import and clean crime data
df_crime = pd.read_csv('interventionscitoyendo.csv',encoding = "ISO-8859-1")
df_crime.head()
df_crime_modified = df_crime.copy()
df_crime_modified.columns = df_crime_modified.columns.str.lower()
df_crime_modified.head()
df_crime_modified.describe()
df_crime_modified.longitude = df_crime_modified.longitude.astype(str)
df_crime_modified.latitude = df_crime_modified.latitude.astype(str)
df_crime_modified.longitude
df_crime_modified.longitude = df_crime_modified.longitude.str.slice(0,7)
df_crime_modified.latitude = df_crime_modified.latitude.str.slice(0,6)
df_crime_modified['long lat'] = df_crime_modified.longitude.astype(str) + ', '+ df_crime_modified.latitude.astype(str)
df_crime_modified.head()
df_crime_modified.loc[df_crime_modified['latitude'] == '1.0']

## import coordinadte data 
df_corr = pd.read_csv('CanadianPostalCodes202108.csv')
df_corr.head()
df_corr.LONGITUDE = df_corr.LONGITUDE.astype(str)
df_corr.LATITUDE = df_corr.LATITUDE.astype(str)
df_corr.LONGITUDE = df_corr.LONGITUDE.str.slice(0,7)
df_corr.LATITUDE = df_corr.LATITUDE.str.slice(0,6)
df_corr['long lat'] = df_corr.LONGITUDE + ', ' + df_corr.LATITUDE
df_corr_dropped = df_corr.drop_duplicates(subset='long lat')

df_corr_dropped
## Merge Data from crime data and postal code data
df_merged = pd.merge(left = df_crime_modified, right=df_corr_dropped, how='left', left_on=['long lat'], right_on=['long lat'])
df_merged

df_merged
df_merged.describe()
df_merged
df_merged.drop(columns=['PROVINCE_ABBR','TIME_ZONE','LATITUDE','LONGITUDE','x','y','longitude','latitude','pdq'], inplace = True)
df_merged.head()
df_merged.describe()
df_merged['postal'] = df_merged.POSTAL_CODE.str.slice(0,3)
df_merged
## Import borough postal code data
df_postal = pd.read_csv('Montreal Postal Codes.csv')
df_postal.head()
df_final = pd.merge(left=df_merged, right= df_postal, left_on='postal', right_on='postal codes')

df_final.head()
df_final['borough'].value_counts().reset_index().to_csv('incidents per b.csv')
df_final.columns = df_final.columns.str.lower()
df_final.drop(columns=['postal'], inplace=True)
df_final.head()
df_final['borough1']= [i for i in df_final['borough'].str.split(r'(?<=[a-z])(?=[A-Z])')]
df_final
df_final['neighbourhood'] = df_final['borough1'].map(lambda x: x[0])
df_final
df_final.replace({'La':'Lasalle','Downtown Montreal North(Mc':'Downtown Montreal','Place Desjardins':'Downtown Montreal','Tour de la Bourse':'Downtown Montreal'}, inplace=True)
df_final.neighbourhood.unique()
df_final
df_eng = df_final.copy()
df_eng.head()
df_eng.drop(columns=['borough','borough1'], inplace=True)
df_eng['categorie'].replace({'Vol de véhicule à moteur':'Motor vehicle theft',
                                                    'Introduction':'Home Invasion',
                                                    'Méfait':'Mischief',
                                                    'Vol dans / sur véhicule à moteur':'Theft in / from a motor vehicle',
                                                    'Vols qualifiés':'Confirmed Theft',
                                                    'Infractions entrainant la mort':'Offenses resulting in death'}, inplace=True)
df_eng.categorie.unique()

def post_look_up(postal):
    postal = postal.upper()
    postal_df = df_eng.loc[df_eng['postal codes'] == postal]
    df_groupby = postal_df.groupby('categorie')['neighbourhood'].count().reset_index()
    df_groupby.rename(columns={'neighbourhood':'# of crimes','categorie':'category'}, inplace=True,)
    return df_groupby


df_eng.loc[df_eng['postal codes'] == 'H4B']
df_eng['year'] = df_eng['date'].str.slice(0,4)
df_eng.head()

def YoY(postal):
    postal = postal.upper()
    df_year = df_eng.loc[df_eng['postal codes'] == postal]
    return df_year.groupby('year')['neighbourhood'].count()


def crime_by_year(postal_code,year):
    df_new = df_eng.loc[(df_eng['postal codes'] == postal_code) & (df_eng['year'] == year)]
    return df_new.groupby('categorie')['neighbourhood'].count()
    

def get_neighbourhood(postal):
    hood = df_eng.loc[df_eng['postal codes'] == postal, 'neighbourhood']
    return ''.join(hood.unique())