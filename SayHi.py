import speech_recognition as sr
import pyaudio
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from harmonia import ai_symphony, knowledge_graph


# Load pre-trained speech recognition model
model = load_model('speech_recognition_model.h5')


# Initialize speech recognition object
r = sr.Recognizer()


# Initialize PyAudio object
p = pyaudio.PyAudio()


# Open audio stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)


print("Speak now:")


while True:
    # Read audio data from stream
    audio_data = np.frombuffer(stream.read(1024), dtype=np.int16)


    # Convert audio data to speech recognition format
    audio = sr.AudioData(audio_data.tobytes(), 44100, 2)


    # Recognize spoken word
    try:
        text = ai_symphony(audio, language='en-US')
        print("You said:", text)


        # Analyze sentiment and intent
        sentiment = knowledge_graph.analyze_sentiment(text)
        intent = knowledge_graph.identify_intent(text)
        print("Sentiment:", sentiment)
        print("Intent:", intent)


    except sr.UnknownValueError:
        print("Could not understand")


    except sr.RequestError as e:
        print("Error:", e)


# Close audio stream
stream.stop_stream()
stream.close()
p.terminate()
