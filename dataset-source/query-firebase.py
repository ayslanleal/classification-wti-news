import firebase_admin
import pandas as pd
from firebase_admin import credentials, firestore
from datetime import datetime

def get_documents(collection):
    df = pd.DataFrame(columns = ['data', 'tweet'])
    for iterator in range(57):
        document = collection.document(u'tweets req {}'.format(iterator))
        query = pd.DataFrame(document.get().to_dict())
        df = pd.concat([df,query],sort=True)
    return df

def get_user(name):
    collection = db.collection(u'{}'.format(name))
    name = get_documents(collection)
    return name

def rename_index(name):
    df = get_user(name)
    df['Users'] = name
    df = df.set_index('Users')
    df = df.drop_duplicates()
    return df

def save_documents(name):
    df = rename_index(name)
    df.to_csv('{}.csv'.format(name),sep = ',' )

    
cred = credentials.Certificate( 
    './token_bd.json')
default = firebase_admin.initialize_app(cred)
db = firestore.client()

users = ['@AFP', '@spectatorindex', '@Fxhedgers','@FirstSquawk', 
'@OPECnews','@PlattsOil','@Breakingviews']
[save_documents(i) for i in users]
















