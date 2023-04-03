import speech_recognition as sr
import Levenshtein


# define the file paths
text_file_path = "9780153506277.txt"
audio_file_path = "myvoice.wav"

# read the text from the file
with open(text_file_path, "r", encoding="utf-8") as f:
    text = f.read()

# split the text into smaller chunks
chunk_size = 500  # number of characters per chunk
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# create a recognizer object
r = sr.Recognizer()

# use the audio file as the audio source
with sr.AudioFile(audio_file_path) as source:
    audio = r.record(source)

# transcribe the audio using Google Speech Recognition API
try:
    transcribed_text = r.recognize_google(audio)
    print(f"Transcribed text: {transcribed_text}")
except sr.UnknownValueError:
    pass

# compare the transcribed text to the target text using SequenceMatcher
from difflib import SequenceMatcher
similarity_ratio = SequenceMatcher(None, text, transcribed_text).ratio()

print(f"Similarity ratio: {similarity_ratio}")
