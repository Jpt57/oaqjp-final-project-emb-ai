import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonFile = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = jsonFile, headers = header)

    mydict = json.loads(response.text)

    emotions = mydict['emotionPredictions'][0]['emotion']

    # Find the emotion with the highest score and label it the 
    # dominant_emotion
    highest_score = 0
    output_string = ''

    
    for i, j in emotions.items():

        if j > highest_score:
            highest_score = j
            dominant_emotion = i

    emotions['dominant_emotion'] = dominant_emotion       

    return emotions
