import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyse}}

    res = requests.post(url, headers=headers, json=data)

    if res.status_code == 400:
        emotions = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
    else:
        emotions = res.json()["emotionPredictions"][0]["emotion"]
        emotions["dominant_emotion"] = max(emotions, key=emotions.get)

    return emotions
