import speech_recognition as sr

recognizer = sr.Recognizer()


try:
    with sr.Microphone() as source:
        print("Ajustando o ruído ambiente... Aguarde.")
        recognizer.adjust_for_ambient_noise(source)
        print("Pode falar agora...")



        # capturando o áudiiio
        audio = recognizer.listen(source)
        print("Audio capturado com sucesso!")

        # convertendo pra texto
        texto = recognizer.recognize_google(audio, language='pt-BR')
        print("Você disse: " + texto)
except sr.UnknownValueError:
    print("Não consegui entender o que você disse.")
except sr.RequestError as e:
    print(f"Erro ao acessar o serviço de reconhecimento: {e}")