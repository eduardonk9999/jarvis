import speech_recognition as sr
import subprocess

# Função para capturar a fala do usuário
def capturar_voz():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Diga algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {texto}")
        return texto.lower()  # Converte tudo para minúsculas para comparação
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return None
    except sr.RequestError as e:
        print(f"Erro ao acessar o serviço de reconhecimento de voz: {e}")
        return None

# Função para executar um comando no terminal Linux
def executar_comando_no_terminal(comando):
    try:
        # Usa o gnome-terminal para executar o comando
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', comando + '; exec bash'])
    except Exception as e:
        print(f"Erro ao executar o comando no terminal: {e}")

# Função principal para capturar voz e executar comandos
def conversa():
    while True:
        pergunta = capturar_voz()
        
        if pergunta is None:
            continue
        
        # Verifica se o comando é para executar o hack
        if "jarvis" in pergunta and "execute hack" in pergunta:
            comando = "whoami"  # Comando para mostrar o nome do usuário
            executar_comando_no_terminal(comando)
        else:
            print("Comando não reconhecido.")

# Iniciar a conversa
if __name__ == "__main__":
    conversa()
