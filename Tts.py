import pyttsx4
import pyaudio

def voiceSelection(voice):
  global engine
  Custom = True
  if voice == 1:
    selection = 'sound_files/Why_cobble_here.wav'
  elif voice == 2:
    selection = 'sound_files/Dad.wav'
  else:
    engine = pyttsx4.init()
    Custom = False
  if Custom:
    engine = pyttsx4.init('coqui_ai_tts')
    engine.setProperty('speaker_wav', selection)


def sayHi():
  engine = pyttsx4.init()
  engine.say("Hi")
  engine.runAndWait()

def tts(message):
  engine.say(message)
  engine.runAndWait()

def ttsMumbo(message):
  engine = pyttsx4.init('coqui_ai_tts')
  engine.setProperty('speaker_wav', 'sound_files/Why_cobble_here.wav')
  engine.say(message)
  engine.runAndWait()
