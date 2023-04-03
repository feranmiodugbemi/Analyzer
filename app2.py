import torch
import librosa
import numpy as np
import soundfile as sf
import speech_recognition as sr
from sklearn import svm
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
from nltk import edit_distance

# Define the path to the pre-trained ASR model and tokenizer
model_path = "facebook/wav2vec2-large-960h-lv60-self"
tokenizer_path = "facebook/wav2vec2-large-960h-lv60-self"

# Load the ASR model and tokenizer
model = Wav2Vec2ForCTC.from_pretrained(model_path)
tokenizer = Wav2Vec2Tokenizer.from_pretrained(tokenizer_path)

# Define the path to the audio file and target text file
audio_path = "myvoice.wav"
target_text_path = "9780153506277.txt"

# Load the audio file and target text
audio, sr = librosa.load(audio_path, sr=None, mono=True, res_type='kaiser_fast')
target_text = open(target_text_path, encoding='utf-8').read().strip()


# Convert audio to PyTorch tensor
input_values = tokenizer(audio, return_tensors="pt").input_values

# Perform ASR
with torch.no_grad():
    logits = model(input_values).logits
predicted_transcription = tokenizer.decode(torch.argmax(logits, dim=-1)[0])

# Define the feature extraction function
def extract_features(audio_file):
    # Load audio file and extract features
    audio, sr = librosa.load(audio_file, sr=None, mono=True, res_type='kaiser_fast')
    # Extract MFCC features
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    # Extract spectral contrast features
    contrast = librosa.feature.spectral_contrast(y=audio, sr=sr)
    # Combine features
    features = np.vstack((mfcc, contrast))
    return features.T

# Extract audio features
audio_features = extract_features(audio_path)

# Train the SVM model
X = audio_features
Y = np.zeros(X.shape[0])  # Set target labels to 0 for now
model = svm.SVC(kernel='linear', C=1.0)
model.fit(X, Y)

# Classify the audio using SVM model
predicted_label = model.predict(audio_features)

# Calculate the edit distance between the predicted transcription and the target text
ed = edit_distance(predicted_transcription, target_text)

# Evaluate the speech quality based on the edit distance
if ed <= 5:
    predicted_score = 4
elif ed <= 10:
    predicted_score = 3
elif ed <= 20:
    predicted_score = 2
else:
    predicted_score = 1

print("Predicted speech quality score:", predicted_score)
