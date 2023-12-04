"""
Module that sets up an endpoint for sentiment analysis.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_handler():
    """
    Function that handles the /emotionDetection endpoint.
    """

    text_to_analyze = request.args.get("textToAnalyze")

    if text_to_analyze is not None:
        result = emotion_detector(text_to_analyze)

        if result["dominant_emotion"] is None:
            return "Invalid text! Please try again!"

        output = f"For the given statement, the system response is 'anger': {result['anger']},"
        output += f" 'disgust': {result['disgust']}, 'fear': {result['fear']},"
        output += f" 'joy': {result['joy']} and 'sadness': {result['sadness']}."
        output += f" The dominant emotion is {result['dominant_emotion']}."
        return output

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
