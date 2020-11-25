import ur_socket_connection
import chess_board
import speech_recognition as sr
from recognize_speech_from_mic import recognize_speech_from_mic
from time import sleep

# Initialize the socket object for communication with the teach pendant
HOST = "192.168.0.12" # The remote host
PORT = 8000 # The same port as used by the server
# s = ur_socket_connection.ur_socket_connection(HOST,PORT)

# A8=(7,0)         ...  ... H8=(7,7)=(y7,x7)
#    .                          .
#    .                          .
# A1=(0,0)=(y0,x0) ...  ... H1=(0,7)

cb = chess_board.chess_board(x0 = 0.24014, y0 = -0.46005, x7 = -.02449, y7 = -0.72676)
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Function for splitting string into individual list elements (ie: 0153 -> ['0','1','5','3'])
def split(word): 
    return [char for char in word]


# Main loop for chess program
while(1):
    while(1):
        input("Press Enter to continue...")
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
        except:
            print("Try again...\n")