# https://stackoverflow.com/questions/53691128/how-to-start-recording-when-something-is-said-python
import speech_recognition as sr
import time
import ur_socket_connection
import chess_board
from recognize_speech_from_mic import recognize_speech_from_mic
from time import sleep


# Words that sphinx should listen closely for. 0-1 is the sensitivity
# of the wake word.
keywords = [("robot", 1), ("hey robot", 1), ]

source = sr.Microphone()
cb = chess_board.chess_board(x0 = 0.24014, y0 = -0.46005, x7 = -.02449, y7 = -0.72676)
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def split(word): 
    return [char for char in word]

def callback(recognizer, audio):  # this is called from the background thread

    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
        print(speech_as_text)

        # Look for your "Ok Google" keyword in speech_as_text
        if "robot" in speech_as_text or "hey robot":
            recognize_main()

    except sr.UnknownValueError:
        print("Oops! Didn't catch that")


def recognize_main():
    while(1):
        while(1):
            print('State your move')
            voice_move = recognize_speech_from_mic(recognizer, microphone)
            if voice_move["transcription"]:
                break
            if not voice_move["success"]:
                break
            print("Try again...\n")

        if voice_move["error"]:
            print("ERROR: {}".format(voice_move["error"]))
            break

        print("You said: {}".format(voice_move["transcription"]))
        
        if len(voice_move["transcription"]) == 4:
            str_list = split(voice_move["transcription"])
            try:
                int_list = [int(i) for i in str_list]
                print(int_list)
                if all(i < 8 for i in int_list):
                    x=cb.move(int_list[0],int_list[1],int_list[2],int_list[3])
                    print(x)
                    # s.pass_msg(x)
                    sleep(10)
            except:
                print("Try again...\n")

def start_recognizer():
    recognizer.listen_in_background(source, callback)
    time.sleep(1000000)

start_recognizer()