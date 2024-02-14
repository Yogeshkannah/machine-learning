import streamlit as st
from googleapiclient.discovery import build
import re
from langdetect import detect
import demoji
import matplotlib.pyplot as plt
# from googletrans import Translator
import nltk
nltk.download ('averaged_perceptron_tagger')
nltk.download('brown')
from textblob import TextBlob
import googleapiclient.discovery
import requests
from bs4 import BeautifulSoup

st.set_page_config(layout="wide")
st.write(
    """
    <style>
    .title {
        text-align: center;
        color:#FF5733;
    }
    .link{
        color:#0000ff;
    }
    .info{
        color:#ffbf00;
    }
    .title2{
        color:#ff8000;
    }
    .author{
        color:#bf00ff;
    }
    .title5{
        color:#006600;
    }
    .ans{
        color:#006600;
    }
    .red{
        color:#990000;
    }
    .grey{
        color:#e6e6e6;
    }
    out{
        color:#4dff4d;
        text-align:center;
    }
    
    </style>
    
       """,
    unsafe_allow_html=True,
)

# Create a centered heading in the wider Streamlit window
st.markdown('<h1 class="title">MULTILINGUAL SENTIMENT ANALYSIS FOR YOUTUBE EDUCATIONAL VIDEOS USING NLP AND MACHINE LEARNING APPROACH</h1>', unsafe_allow_html=True)
st.write("")
st.write("")
st.markdown('<h4 class="info">This machine learning model can prove highly valuable in assessing user sentiment and video \
    quality by considering various factors, including comments, views, likes, subscriber counts, \
        and the video\'s publication date.</h4>', unsafe_allow_html=True)
st.markdown('<h2 class="link">Enter Youtube Video Link:</h2>', unsafe_allow_html=True)
link=st.text_input("")
API_KEY = 'AIzaSyA95t-mAtHEdIVEzg0EUkA1PxUWP5v5168'

def extract_video_id(link):
        
    # Regular expression pattern to match YouTube video IDs
    pattern = r'watch\?v=([A-Za-z0-9_-]+)'

    # Search for the pattern in the YouTube link
    try:
        match = re.findall(pattern, link)
    except HttpError:
        st.write("Link is not a valid youtube video link..")
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
    
    

    # st.write(comments)
    # print(len(comments))
    # print(comments)
    return comments

def remove_emojis(lst):
    # Initialize the demoji library
    demoji.download_codes()
    cleaned_sentence=[]
    # Remove emojis from the text
    for text in lst:
        cleaned_text = demoji.replace(text, '')
        if len(cleaned_text)>1:
            cleaned_sentence.append(cleaned_text)
    # print(cleaned_sentence)
    return cleaned_sentence

def detect_languages(lst):
    
    ta=0
    en=0
    other=0
    dict1={}
    tamil_lst=[]
    english_lst=[]
    other_languages=[]
    for i in lst:
        text=i
        language=""
        if len(i)>=15:
            try:
                language=detect(text)
                # print(language)
            except Exception as e:
                # st.write(i)
                pass
        if language == 'ta':
            ta+=1
            tamil_lst.append(i)
        elif language == 'en':
            en+=1
            english_lst.append(i)
        else:
            other+=1
            other_languages.append(i)
        if language in dict1:
            dict1[language]+=1
        else:
            dict1[language]=1
        if len(language)==0:
            english_lst.append(i)
            
    print(en)
    # st.write("The tamil comments are: ")
    st.markdown('<h4 class="title2">The Tamil comments are:</h4>',unsafe_allow_html=True)
    st.write(tamil_lst)
    # st.write("The english comments are: ")
    st.markdown('<h4 class="title2">The English comments are: </h4>',unsafe_allow_html=True)
    st.write(english_lst)
    # st.write("The other language comments are: ")
    # st.write(other_languages)
    # print(dict1)
    return en,ta,other,english_lst,tamil_lst

def chart(lst):
   
    st.write(
    """
    <style>
    .title3{
        color:#00ff00;
    }
    </style>
    
       """,
    unsafe_allow_html=True,
    )
    st.markdown('<h4 class="title3">This Chart represents the visual representation of comments in the video: </h4>',unsafe_allow_html=True)
    # Data to be displayed in the pie chart
    labels = ['english', 'tamil', 'other']
      # Sizes or proportions of each slice

    # Create a pie chart
    plt.figure(figsize=(8,4))
    plt.pie(lst, labels=labels, autopct='%1.1f%%', startangle=140)

    # Add a title
    plt.title('Sample Pie Chart')

    # Display the chart
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('pie_chart.png')
    st.image('pie_chart.png', caption='Pie Chart')


def sentimental(lst):
    positive=0
    negative=0
    neutral=0
    pos_=[]
    neg_=[]
    for i in lst:
        blob=TextBlob(i)
        # blob.sentiment
        if blob.sentiment.polarity >0:
            pos_.append(blob.sentiment.polarity)
            print()
            positive+=1
            # st.write(i)
        elif blob.sentiment.polarity==0:
            neutral+=1
        elif blob.sentiment.polarity<0:
            neg_.append(blob.sentiment.polarity)
            # print(i)
            negative+=1
    print(pos_)
    print(neg_)
    st.markdown('<h1 class="ans">Positive comments:</h1>',unsafe_allow_html=True)
    # st.write("positive"+str(positive))
    st.markdown(f'<h2 class="grey";">{positive}</h2>', unsafe_allow_html=True)
    # st.write("negative"+str(negative))
    st.markdown('<h1 class="red">Negative comments:</h1>',unsafe_allow_html=True)
    st.markdown(f'<h2 class="grey";">{negative}</h2>', unsafe_allow_html=True)
    # st.write("neutral"+str(neutral))
    st.markdown('<h1 class="link">Neutral comments:</h1>',unsafe_allow_html=True)
    st.markdown(f'<h2 class="grey";">{neutral}</h2>', unsafe_allow_html=True)
    return positive,negative,neutral,pos_,neg_

def tam_to_eng(lst):
    translator = Translator()
    eng_lst=list()
    for tamil_comment in lst:
        # Translate Tamil to English
        translated_comment = translator.translate(tamil_comment, src='ta', dest='en')

        # Get the translated text
        english_comment = translated_comment.text
        eng_lst.append(english_comment)
        
        print("Tamil Comment:", tamil_comment)
        print("English Translation:", english_comment)
    return eng_lst

def bar_chart(pos,neg,neut):
    st.markdown('<h4 class="title3">This Bar represents the visual representation of sentiment in comments in the video: </h4>',unsafe_allow_html=True)
    lst=[pos,neg,neut]

    # Corresponding labels for the values
    categories = ['Positive', 'Negative', 'Neutral']
    plt.figure(figsize=(8,4))
    # Create a bar chart
    plt.bar(categories, lst)

    # Add labels and a title
    plt.xlabel('Sentiments')
    plt.ylabel('Count')
    plt.title('Sentiment analysis')
    plt.savefig('pie_chart2.png')
    st.image('pie_chart2.png', caption='Pie Chart')
    # Show the bar chart
    # plt.show()


# Initialize the YouTube Data API
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

def get_video_info(video_id):
    # Call the YouTube API to get video details
    try:

        video_response = youtube.videos().list(
            part='snippet,statistics',
            id=video_id
        ).execute()
    except Exception:
        st.warning("Invalid link")

    # Extract the relevant information
    video = video_response['items'][0]
    snippet = video['snippet']
    statistics = video['statistics']

    # Get the data you want
    video_title = snippet['title']
    content_creator_name = snippet['channelTitle']
    published_date = snippet['publishedAt']
    views = statistics['viewCount']
    likes = statistics.get('likeCount', 0)
    # subscribers = statistics.get('subscriberCount', 0)
    
    result={
        'Video Title': video_title,
        'Content Creator Name': content_creator_name,
        'Published Date': published_date,
        'Views': views,
        'Likes': likes,
        # 'Subscribers': subscribers
    }

    return result

def get_subs_count(channel_url):
    response = requests.get(channel_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    soup=str(soup)
    print(type(soup))
    pattern = r"subscribers\"}},\"simpleText\":\"(\d.+) subscribers\"},\"trackingParams\""

    # Search for the pattern in the YouTube link
    match = re.findall(pattern, soup)
    # print(match)
    # st.write(match)
    return match
    
def calci(pos,neut,total_comments):
    sum=pos+neut
    x=(sum*100)/total_comments
    return x


if link:
    video_id=extract_video_id(link)
    video_info=get_video_info(video_id)
    st.markdown('<h3 class="author">Video Title:</h4>',unsafe_allow_html=True)
    st.write(video_info["Video Title"])
    st.markdown('<h3 class="author">Content Creator Name:</h4>',unsafe_allow_html=True)
    st.write(video_info["Content Creator Name"])
    st.markdown('<h3 class="author">Published Date:</h4>',unsafe_allow_html=True)
    st.write(video_info["Published Date"])
    st.markdown('<h3 class="author">Views:</h4>',unsafe_allow_html=True)
    st.write(video_info["Views"])
    st.markdown('<h3 class="author">Likes:</h4>',unsafe_allow_html=True)
    st.write(video_info["Likes"])
    st.markdown('<h3 class="author">Subscriber count:</h4>',unsafe_allow_html=True)
    subscriber_Count=get_subs_count(link)
    st.write(subscriber_Count[0])
    comments=get_coments(video_id[0])
    # st.write(video_id)



    st.markdown('<h4 class="title2">The Total Number Of Comments Extracted From This Video IS:</h4>',unsafe_allow_html=True)
    st.write(len(comments))
    cleaned_comments=remove_emojis(comments)
    english,tamil,other,english_lst,tamil_lst=detect_languages(cleaned_comments)
    
    # st.write("The total number of tamil comments are --> ",tamil)
    # st.write("The total number of english comments are --> ",english)
    # st.write("The total number of other language comments are --> ",other)
    chart([english,tamil,other])
    # if(tamil>0):
    #     tam_to_english=tam_to_eng(tamil_lst)
    #     print(tam_to_english)
    #     english_lst+=tam_to_english
    
    st.markdown('<h2 class="link">After performing the Sentimental analysis:</h2>',unsafe_allow_html=True)
    pos,neg,neut,positive_curve,negative_curve=sentimental(english_lst)
    bar_chart(pos,neg,neut)
   
    result = calci(pos,neut,len(comments))

    st.markdown('<h1 class="out">OUTPUT</h1>',unsafe_allow_html=True)
    if result>50:
        st.markdown('<h2 class="title2">This video has the positive comments of </h2>',unsafe_allow_html=True)
        st.markdown(f'<h3 class="out">{result}%</h3>',unsafe_allow_html=True)
    else:
        st.markdown('<h2 class="title2">This video has the negative comments of </h2>',unsafe_allow_html=True)
        st.markdown(f'<h3 class="out">{result}%</h3>',unsafe_allow_html=True)
    # print(x)
    # st.write(x)
    
