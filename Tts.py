import pyttsx4
import pyaudio

def voice_selection(voice):
  global engine
  custom = True
  if voice == 1:
    selection = 'sound_files/Why_cobble_here.wav'
  elif voice == 2:
    selection = 'sound_files/Dad.wav'
  else:
    engine = pyttsx4.init()
    custom = False
  if custom:
    engine = pyttsx4.init('coqui_ai_tts')
    engine.setProperty('speaker_wav', selection)


def say_hi():
  engine = pyttsx4.init()
  engine.say("Hi")
  engine.runAndWait()

def tts(message):
  engine.say(message)
  engine.runAndWait()

def tts_mumbo(message):
  engine = pyttsx4.init('coqui_ai_tts')
  engine.setProperty('speaker_wav', 'sound_files/Why_cobble_here.wav')
  engine.say(message)
  engine.runAndWait()
