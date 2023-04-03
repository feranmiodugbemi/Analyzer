import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from difflib import SequenceMatcher
import gradio as gr
import Levenshtein

#This app.py 

def transcribe():
    # Load the audio file
    audio_file = AudioSegment.from_wav("shindara.wav")

    # Split the audio file on silence
    chunks = split_on_silence(audio_file, min_silence_len=500, silence_thresh=-50)

    # Create a recognizer object
    r = sr.Recognizer()

    try:# Transcribe each chunk
        transcribed_text = ""
        for chunk in chunks:
            # Export the chunk to a WAV file
            chunk.export("temp.wav", format="wav")
    
            # Recognize the text from the chunk
            with sr.AudioFile("temp.wav") as source:
                audio = r.record(source)
            text = r.recognize_google(audio)
    
            # Add the recognized text to the full transcribed text
            transcribed_text += text
    except sr.UnknownValueError:
        pass
        # Calculate the similarity score
    target_text = """
   The Mystery of the Missing Cat

“Ginger!” called Greg. 
“Ginger!” he called again. 
“Dad, I can’t find my cat!” 
“She’s just busy playing. She will be back to eat,” said Dad. 
Ginger didn’t come home. Greg started to become upset. 

Greg and Dad went to see Mr. Scott. 
“Mr. Scott, have you seen Ginger?” Greg asked. “She’s missing!” 
“No,” said Mr. Scott. “You should talk to Mrs. Norris.” 

“Hello, Mrs. Norris,” said Greg, “have you seen Ginger?”  
Mrs. Norris said she hadn’t.
“Say, are you looking for Ginger?” called Mr. Sanchez.  
“She’s a visitor here sometimes.”  
Ginger was not there. 

When Greg went to bed, Ginger was still missing. He had been busy looking high and low. 
In the night, Greg woke up. He could hear something scratching. 
“Dad, I hear something in my room!” he called. 

Dad and Greg waited by the door. Greg nudged Dad. 
“Listen,” said Greg. “It’s coming from under my bed!” 

Then Greg remembered Ginger! He looked under the bed and saw a face and two yellow eyes. 
“Look, Dad!” he called. “Ginger has kittens!” 
“Now we know where she’s been,” smiled Dad. 

The next day, Greg gathered the people from the street. 
“Come look!” Greg said. “We have found Ginger!” 


    """
    
    similarity_score = SequenceMatcher(None, target_text.lower(), transcribed_text.lower()).ratio()
    
        # Print the similarity score
    
    print("Similarity Score:", similarity_score)
    print(Levenshtein.ratio(target_text.lower(), transcribed_text.lower()))
    return "Your confidence level is {similarity_score}".format(similarity_score=similarity_score)


transcribe()

