import streamlit as st
from googleapiclient.discovery import build
import re
from langdetect import detect
import demoji
import matplotlib.pyplot as plt
from googletrans import Translator
import nltk
nltk.download ('averaged_perceptron_tagger')
nltk.download('brown')
from textblob import TextBlob
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

link=st.text_input("enter the link")

def extract_video_id(link):
        
    # Regular expression pattern to match YouTube video IDs
    pattern = r'watch\?v=([A-Za-z0-9_-]+)'

    # Search for the pattern in the YouTube link
    match = re.findall(pattern, link)
    # print(match)
    # st.write(match)
    return match




def get_coments(video_id):
        
    # Set up the YouTube Data API
    youtube = build('youtube', 'v3', developerKey='AIzaSyA95t-mAtHEdIVEzg0EUkA1PxUWP5v5168')

    # Specify the video ID of the video you want to retrieve comments for
    

    # Retrieve comments for the video
    comments = []
    nextPageToken = None
    while True:
        comment_response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            pageToken=nextPageToken,
            maxResults=100
        ).execute()
        
        for comment in comment_response['items']:
            text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(text)
        
        nextPageToken = comment_response.get('nextPageToken')
        if not nextPageToken:
            break

    st.write(comments)
    # print(len(comments))
    print(type(comments))
    return comments

def detect_language(lst):
    with open('model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    v=CountVectorizer()
    transformed_data = v.fit_transform(lst)
    # lst_count=v.transform(transformed_data)
    pred=loaded_model.predict(transformed_data)
    print(pred)

if link:
    video_id=extract_video_id(link)
    comments=get_coments(video_id[0])
    detect_language(comments)