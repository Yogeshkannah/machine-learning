import streamlit as st
import spacy
import pandas as pd
import matplotlib.pyplot as plt
nlp=spacy.load("en_core_web_lg")
from spacy.lang.en.stop_words import STOP_WORDS
from itertools import islice
from youtube_comment_downloader import *
import re




def commentDownlod(link):
    downloader = YoutubeCommentDownloader()
    comments = downloader.get_comments_from_url(link,sort_by=SORT_BY_POPULAR)
    lst=[]
    pattern="'text': '([a-zA-Z\s\D]+)', 'time'"
    ctr=0
    # try:
    #     while True:
    #         value = next(comments)
    #         st.write(value)
    #         st.write(value["text"])
    #         # st.write(type(value))
    #         # result=re.findall(pattern,value.strip())
    #         # lst.append(result)
    #         # st.write(result)
    #         ctr+=1
    # except StopIteration:
    #     pass
    for comment in islice(comments, 1000):
        result=re.findall(pattern,str(list(comments)).strip())
    for i in result:
        lst.append([i])
    # for i in lst:
    #     st.write(i)
    st.header("total number of highlighted comments: ")
    st.write(len(lst))
    return lst
    # st.write("the total comments are: ",ctr)


    # for comment in islice(comments, 100):
    #     result=re.findall(pattern,str(list(comments)).strip())
    # for i in result:
    #     lst.append([i])
    # for i in lst:
    #     st.write(i)
    # st.header("total number of highlighted comments: ")
    # st.write(len(lst))
    # return lst


def linkchecker(link):
    
    pattern="(https:\/\/www.youtube.com\/)"
    found=re.findall(pattern,link)
    print(found)
    if(len(found)==1):
        commentDownlod(link)
    else:
        st.write("this is no a valid link")

link = st.text_input('copy the link')
st.write('The current video link is', link)
if len(link)>=1:
    linkchecker(link)



            




