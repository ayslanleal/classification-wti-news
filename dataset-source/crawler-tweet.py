import tweepy as tw
import re
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(
    './archives/token_bd.json')
default = firebase_admin.initialize_app(cred)

consumer_key = 'auth_tt.json'
consumer_secret = 'auth_tt.json'
acess_token = 'auth_tt.json'
acess_token_secret = 'auth_tt.json'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, acess_token_secret)
api = tw.API(auth)
db = firestore.client()

def obter_tweets(usuario, limite, pag):
    resultados = api.user_timeline(
        screen_name=usuario, count=limite, tweet_mode='extended', page=pag)
    tweets = []
    for r in resultados:
        tweet = re.sub(r'http\S+', '', r.full_text)
        tweets.append(tweet.replace('\n', ' '))
    return tweets

def obter_data(usuario, limite, pag):
    resultados = api.user_timeline(
        screen_name=usuario, count=limite, tweet_mode='extended', page=pag)
    datas = []
    for r in resultados:
        data = r.created_at
        datas.append(data)
    return datas

users = ['@Fxhedgers','@Breakingviews','@FirstSquawk.csv','@OPECnews.csv','@PlattsOil.csv','@spectatorindex.csv']

for i in range(20):
    tweets = obter_tweets(usuario=users[i], limite=300, pag = 0)
    datas = obter_data(usuario=users[i], limite = 300, pag = 0)
    collection = db.collection(u'{}'.format(users[i])).document(u'tweets req {}'.format(0))
    collection.set({
        u'tweet' : tweets,
        u'data' : datas
    })
    print(f'Requisição do usuario {i} concluida')

