import speech_recognition as s_r

def record_audio():
    my_mic = s_r.Microphone()
    r = s_r.Recognizer()

    with my_mic as source:
        #reduce noise
        r.adjust_for_ambient_noise(source)
        #take voice input from the microphone 
        audio = r.listen(source) 
        return r,audio

def print_audio(r,audio):
    return(r.recognize_google(audio))   
