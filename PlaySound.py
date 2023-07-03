# import pygame
# from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play


# pygame.init()

# def winningSoundPygame():
#     winSound = pygame.mixer.Sound('sound_files/Win.wav')
#     winSound.play()

# def winningSoundPlaysound():
#     playsound('sound_files/Win.wav')

def winningSound():
    Sound = AudioSegment.from_file('sound_files/Win.wav', format="wav")
    Sound -= 10
    play(Sound)
    exit()
    

if __name__ == "__main__":
    winningSound()