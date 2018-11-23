#!/usr/bin/env python3

import speech_recognition as sr

# load audio file from same directory
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")

# use audio file as input
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Google Speech Recognition
try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

