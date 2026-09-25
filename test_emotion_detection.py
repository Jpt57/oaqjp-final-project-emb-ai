import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test the emotion detector for the emotion joy
        result_joy = emotion_detector("I am glad this happened") # This will return a dictionary of the result
        dominant_emotion_joy = result_joy["dominant_emotion"] # Obtain the dominate emotion from the returned dictionary
        self.assertEqual(dominant_emotion_joy, "joy")

        # Test the emotion detector for the emotion anger
        result_anger = emotion_detector("I am really mad about this") # This will return a dictionary of the result
        dominant_emotion_anger = result_anger["dominant_emotion"] # Obtain the dominate emotion from the returned dictionary
        self.assertEqual(dominant_emotion_anger, "anger")

        # Test the emotion detector for the the emotion disgust
        result_disgust = emotion_detector("I feel disgusted just hearing about this") # This will return a dictionary of the result
        dominant_emotion_disgust = result_disgust["dominant_emotion"] # Obtain the dominate emotion from the returned dictionary
        self.assertEqual(dominant_emotion_disgust, "disgust")

        # Test the emotion detector for the emotion sadness
        result_sadness = emotion_detector("I am so sad about this") # This will return a dictionary of the result
        dominant_emotion_sadness = result_sadness["dominant_emotion"] # Obtain the dominate emotion from the returned dictionary
        self.assertEqual(dominant_emotion_sadness, "sadness")

        # Test the emotion detector for the emotion fear
        result_fear = emotion_detector("I am really afraid that this will happen") # This will return a dictionary of the result
        dominant_emotion_fear = result_fear["dominant_emotion"] # Obtain the dominate emotion from the returned dictionary
        self.assertEqual(dominant_emotion_fear, "fear")

unittest.main()