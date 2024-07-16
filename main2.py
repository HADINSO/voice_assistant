import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_microphone_index():
    audio = sr.Microphone.list_microphone_names()
    for i, name in enumerate(audio):
        print(f"Micrófono con nombre \"{name}\" encontrado para `Microphone(device_index={i})`")
    index = int(input("Seleccione el índice del micrófono: "))
    return index

def listen(device_index=None):
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=device_index) as source:
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
    mic_index = get_microphone_index()
    while True:
        command = listen(device_index=mic_index)
        if command:
            if "salir" in command:
                speak("Adiós")
                break
            elif "hola" in command:
                speak("Hola, ¿cómo puedo ayudarte?")
            elif "hora" in command:
                now = datetime.datetime.now().strftime("%H:%M")
                speak(f"Son las {now}")
            elif "fecha" in command:
                today = datetime.datetime.now().strftime("%d/%m/%Y")
                speak(f"Hoy es {today}")
            elif "buscar" in command:
                speak("¿Qué quieres buscar?")
                query = listen(device_index=mic_index)
                if query:
                    webbrowser.open(f"https://www.google.com/search?q={query}")
                    speak(f"Buscando {query} en Google")
            elif "abrir" in command:
                speak("¿Qué aplicación quieres abrir?")
                app = listen(device_index=mic_index)
                if app:
                    try:
                        os.system(f"start {app}")
                        speak(f"Abriendo {app}")
                    except Exception as e:
                        speak(f"No puedo abrir {app}")
            else:
                speak("No tengo una respuesta para ese comando.")

if __name__ == "__main__":
    main()
