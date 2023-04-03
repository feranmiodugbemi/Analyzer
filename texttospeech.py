import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the voice properties (optional)
voices = engine.getProperty('voices')  # Get available voices
engine.setProperty('voice', voices[1].id)  # Set the voice (you can change the index to choose a different voice)
engine.setProperty('rate', 150)  # Set the speaking rate (words per minute)

# Convert text to speech
text = """
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
engine.say(text)
engine.save_to_file(text, 'voice2.wav')
engine.runAndWait()
