import speech_recognition as sr
import wave
import pyaudio
def now():
	r = sr.Recognizer()
	with sr.Microphone() as source:
	  r.adjust_for_ambient_noise(source)  # here
	  print("say-->")
	  audio = r.listen(source)
          x=r.recognize_google(audio)
          print('user->'+ x)
	  return x
	  
