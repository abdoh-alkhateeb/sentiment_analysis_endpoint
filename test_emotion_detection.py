import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(result, "joy")

    def test_joy(self):
        result = emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(result, "anger")

    def test_joy(self):
        result = emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        self.assertEqual(result, "disgust")

    def test_joy(self):
        result = emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(result, "sadness")

    def test_joy(self):
        result = emotion_detector("I am really afraid that this will happen")["dominant_emotion"]
        self.assertEqual(result, "fear")

if __name__ == '__main__':
    unittest.main()
