import pyttsx4
import pyaudio

engine = pyttsx4.init('coqui_ai_tts')
engine.setProperty('speaker_wav', 'sound_files/Why_cobble_here.wav')

engine.say('this is an english text to voice test.')
engine.runAndWait()
