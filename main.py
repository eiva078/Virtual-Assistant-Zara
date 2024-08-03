import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()

def aiprocess(command):

  client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
  )

  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": "You are a virtual assistant named zara, skilled in general task like alexa and google cloud"},
      {"role": "user", "content": command}
    ]
  )
  return completion.choices[0].message.content

def processcommand(c):
  if("open google" in c.lower()):
    webbrowser.open("https://www.google.com/")
  elif("open linkedln" in c.lower()):
    webbrowser.open("https://www.linkedin.com/")
  elif("open youtube" in c.lower()):
    webbrowser.open("https://www.youtube.com/")
  elif("open facebook" in c.lower()):
    webbrowser.open("https://www.facebook.com/")
  elif("play" in c.lower()):
    music = c.lower().split(" ")[1]
    link = musicLibrary.songs[music]
    webbrowser.open(link)
  else:
    # Let OpenAI handel this request
    output = aiprocess(c)
    speak(output)

if __name__=="__main__":
  speak("Initializing zara...")

  while True:
    recognizer = sr.Recognizer()                              # Create a Recognizer instance

    try:                                                      # Perform speech recognition using Google Web Speech API
      with sr.Microphone() as source:                         # Capture audio input from the microphone
        print("Speak something...")
        audio_data = recognizer.listen(source, timeout=2, phrase_time_limit=1)

      text = recognizer.recognize_google(audio_data)
      if(text.lower()=="hello"):
        speak("Yeah")
        
        with sr.Microphone() as source:                       # Listen for command
          print("Zara activated...")
          audio_data = recognizer.listen(source)
          command = recognizer.recognize_google(audio_data)
          processcommand(command)

    except Exception as e:
      print("Error", e)