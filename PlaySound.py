from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

# import pygame

# pygame.init()

# def winning_sound_pygame():
#     win_sound = pygame.mixer.Sound('sound_files/Win.wav')
#     win_sound.play()

# def winning_sound_playsound():
#     playsound('sound_files/Win.wav')

def winning_sound():
    sound = AudioSegment.from_file('sound_files/Win.wav', format="wav")
    sound -= 10
    play(sound)
    exit()
    

if __name__ == "__main__":
    # winning_sound_pygame()
    winning_sound()