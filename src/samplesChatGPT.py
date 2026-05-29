"""
====================
SAMPLING - GME & FTX
====================



"""
#%%
# Import Libraries
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%%
# Load FTX Comments and Identify Emotions
comments = []
for i in [x for x in os.listdir('data/comments/processed') if x[:3]=='ftx']:
    f = open ('data/comments/processed/'+i, "r")
    comments += json.loads(f.read())
keys = list(comments[0].keys())
df_ftx_comments = pd.DataFrame.from_dict({k:[x[k] for x in comments] for k in keys})
del comments
del keys

df_ftx_comments['emotionraw'] = df_ftx_comments['emotion']
df_ftx_comments['emotion'] = df_ftx_comments['emotionraw'].apply(lambda x: emotionGroup(x))
df_ftx_comments['valence'] = df_ftx_comments['emotionraw'].apply(lambda x: emotionGroup(x, valence=True))

#%%
# Load GME Comments and Identify Emotions
comments = []
for i in [x for x in os.listdir('data/comments/processed') if x[:8]=='gamestop']:
    f = open ('data/comments/processed/'+i, "r")
    comments += json.loads(f.read())
keys = list(comments[0].keys())
df_gme_comments = pd.DataFrame.from_dict({k:[x[k] for x in comments] for k in keys})
del comments
del keys

df_gme_comments['emotionraw'] = df_gme_comments['emotion']
df_gme_comments['emotion'] = df_gme_comments['emotionraw'].apply(lambda x: emotionGroup(x))
df_gme_comments['valence'] = df_gme_comments['emotionraw'].apply(lambda x: emotionGroup(x, valence=True))

#%%
# Create samples
ftx = df_ftx_comments.groupby('emotion', group_keys=False).apply(lambda x: x.sample(20))[df_ftx_comments['emotion'] != 'error'][['textDisplay', 'emotion']]
gme = df_gme_comments.groupby('emotion', group_keys=False).apply(lambda x: x.sample(20))[df_ftx_comments['emotion'] != 'error'][['textDisplay', 'emotion']]

ftx['idx'] = ftx.groupby('emotion').cumcount()+1
ftx['pasteText'] = ftx['idx'].astype(str) + '. ' + ftx['textDisplay']
gme['idx'] = gme.groupby('emotion').cumcount()+1
gme['pasteText'] = gme['idx'].astype(str) + '. ' + gme['textDisplay']

ftx.to_csv("data/ftx_samples.csv", index=False, encoding='utf-8-sig')  
gme.to_csv("data/gme_samples1.csv", index=False, encoding='utf-8-sig')  

# %%
# Grouping
def emotionGroup(
    emotion: str,
    valence: bool = False
) -> str:

    data = {
        'admiration': ['Affection', 'Positive'],
        'amusement': ['Happiness', 'Positive'],
        'anger': ['Anger', 'Negative'],
        'annoyance': ['Anger', 'Negative'],
        'approval': ['Satisfaction', 'Positive'],
        'caring': ['Affection', 'Positive'],
        'confusion': ['Fear', 'Negative'],
        'curiosity': ['Fear', 'Negative'],
        'desire': ['Fear', 'Negative'],
        'disappointment': ['Depression', 'Negative'],
        'disapproval': ['Anger', 'Negative'],
        'disgust': ['Contempt', 'Negative'],
        'embarrassment': ['Depression', 'Negative'],
        'excitement': ['Happiness', 'Positive'],
        'fear': ['Fear', 'Negative'],
        'gratitude': ['Satisfaction', 'Positive'],
        'grief': ['Depression', 'Negative'],
        'joy': ['Happiness', 'Positive'],
        'love': ['Affection', 'Positive'],
        'nervousness': ['Fear', 'Negative'],
        'optimism': ['Happiness', 'Positive'],
        'pride': ['Affection', 'Positive'],
        'realization': ['Satisfaction', 'Positive'],
        'relief': ['Happiness', 'Positive'],
        'remorse': ['Contempt', 'Negative'],
        'sadness': ['Depression', 'Negative'],
        'surprise': ['Happiness', 'Positive'],
        'neutral': ['Neutral', 'Neutral'],
        'error': ['Neutral', 'Neutral']
    }

    if valence:
        try: 
            x = data[emotion.lower()][1]
        except:
            x = 'error'

    else:
        try: 
            x = data[emotion.lower()][0]
        except:
            x = 'error'
    
    return x

# %%
# FTX - Load Chat GPT results and process
chatgpt_ftx = pd.read_csv("data/ftx_samples.csv")

chatgpt_ftx['emotionraw'] = chatgpt_ftx['cleanedChatGPT']
chatgpt_ftx['emotionGPT'] = chatgpt_ftx['emotionraw'].apply(lambda x: emotionGroup(x))
chatgpt_ftx['valenceGPT'] = chatgpt_ftx['emotionraw'].apply(lambda x: emotionGroup(x, valence=True))

#chatgpt_ftx[chatgpt_ftx['emotion'] != chatgpt_ftx['emotionGPT']]
#chatgpt_ftx[chatgpt_ftx['valence'] != chatgpt_ftx['valenceGPT']]

chatgpt_ftx.to_csv("data/ftx_samples_emotions.csv", index=False, encoding='utf-8-sig')  

# %%
# GME - Load Chat GPT results and process
chatgpt_gme = pd.read_csv("data/gme_samples.csv")

chatgpt_gme['emotionraw'] = chatgpt_gme['cleanedChatGPT']
chatgpt_gme['emotionGPT'] = chatgpt_gme['emotionraw'].apply(lambda x: emotionGroup(x))
chatgpt_gme['valenceGPT'] = chatgpt_gme['emotionraw'].apply(lambda x: emotionGroup(x, valence=True))

#chatgpt_gme[chatgpt_gme['emotion'] != chatgpt_gme['emotionGPT']]
#chatgpt_gme[chatgpt_gme['valence'] != chatgpt_gme['valenceGPT']]

chatgpt_gme.to_csv("data/gme_samples_emotions.csv", index=False, encoding='utf-8-sig')  

# %%
