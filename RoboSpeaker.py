import win32com.client as wincom

if __name__ == '__main__':
    speak= wincom.Dispatch("SAPI.Spvoice")
    print("Welcome to SpeakAI 1.1. Created by Rajeshwar ")
    while True:
        x=input("Enter what you want me to speak : ")
        if x=="q":
            speak.Speak("Bye Bye , See you soon")
            break
        
        speak.Speak(x)