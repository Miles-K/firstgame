import Difficulty
import UserInput
import Tts
import GameHandler

if __name__ == "__main__":
    Tts.voice_selection(1)
    Difficulty.difficulty_selector()
    GameHandler.game_question_start()
    GameHandler.game_question()