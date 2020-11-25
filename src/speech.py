import speech_recognition as sr
from time import sleep
import chess_board
import ur_socket_connection

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def split(word): 
    return [char for char in word]  

if __name__ == "__main__":

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    cb = chess_board.chess_board(x0 = 0.24014, y0 = -0.46005, x7 = -.02449, y7 = -0.72676)
    HOST = "192.168.0.12"
    PORT = 8000
    s = ur_socket_connection.ur_socket_connection(HOST,PORT)

    # show instructions and wait 3 seconds before starting the game
    print("Welcome to robot chess\n")
    sleep(3)

    while(1):
        while(1):
            input("Press Enter to continue...")
            print('State your move')
            move = recognize_speech_from_mic(recognizer, microphone)
            if move["transcription"]:
                break
            if not move["success"]:
                break
            print("Try again...\n")

        if move["error"]:
            print("ERROR: {}".format(move["error"]))
            break

        print("You said: {}".format(move["transcription"]))
        
        if len(move["transcription"]) == 4:
            print("You said: {}".format(move["transcription"]))
            str_list = move["transcription"]
            try:
                int_list = [int(i) for i in str_list]
                print(int_list)
                if all(i < 8 for i in int_list):
                    x=cb.generate_movestring(int_list[0],int_list[1],int_list[2],int_list[3])
                    print(x)
                    s.pass_msg(x)
                    sleep(10)
            except:
                print("Try again...\n")
