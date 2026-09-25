from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detection_app():
    text_to_analyze = request.args.get("textToAnalyze")

    # Obtain the result from the emotion_detector function
    result = emotion_detector(text_to_analyze)

    for i in result:
       if result[i] == None:
        return "Invalid text! Please try again!"

    anger_score = result["anger"]
    disgust_score = result["disgust"]
    fear_score = result["fear"]
    joy_score = result["joy"]
    sadness_score = result["sadness"]
    dominant_emotion = result['dominant_emotion']

    # Return the following string
    response = f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, and 'sadness': {sadness_score}. The dominant emotion is <b> {dominant_emotion}. </b>"

    return response

@app.route("/")
def render_index_page():

    return render_template('index.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

