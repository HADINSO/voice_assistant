import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio, language='es-ES')
        print(f"Has dicho: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("No he entendido lo que has dicho.")
        return ""
    except sr.RequestError:
        print("No se puede acceder al servicio de reconocimiento de voz.")
        return ""

def main():
    while True:
        command = listen()
        if command:
            if "salir" in command:
                speak("Adiós")
                break
            elif "hola" in command:
                speak("Hola, ¿cómo puedo ayudarte?")
            elif "hora" in command:
                from datetime import datetime
                now = datetime.now().strftime("%H:%M")
                speak(f"Son las {now}")
            else:
                speak("No tengo una respuesta para ese comando.")

if __name__ == "__main__":
    main()
