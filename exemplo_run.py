import subprocess

def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, 
                                 shell=True, 
                                 capture_output=True, 
                                 text=True)
        
        print(f"Comando executado: {comando}")
        print(f"Saída: {resultado.stdout}")
        
        if resultado.returncode != 0:
            print(f"Erro: {resultado.stderr}")
            
    except Exception as e:
        print(f"Erro ao executar o comando: {str(e)}")

# Exemplo de usoif __name__ == "__main__":
    executar_comando("dir")  # No Windows
    executar_comando("echo Olá Mundo!")
