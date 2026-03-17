import os
import shutil

print("=== Organizador de Arquivos ===")

# CAMINHO (troque se quiser)
caminho = r"C:\Users\geova\Downloads"

pastas = {
    "Imagens": [".png", ".jpg", ".jpeg"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Outros": []
}

def organizar_arquivos():
    for pasta in pastas:
        caminho_pasta = os.path.join(caminho, pasta)
        os.makedirs(caminho_pasta, exist_ok=True)

    for arquivo in os.listdir(caminho):
        caminho_arquivo = os.path.join(caminho, arquivo)

        if os.path.isfile(caminho_arquivo):
            movido = False

            for pasta, extensoes in pastas.items():
                if any(arquivo.lower().endswith(ext) for ext in extensoes):
                    destino = os.path.join(caminho, pasta, arquivo)
                    shutil.move(caminho_arquivo, destino)
                    print(f"Movido: {arquivo} → {pasta}")
                    movido = True
                    break

            if not movido:
                destino = os.path.join(caminho, "Outros", arquivo)
                shutil.move(caminho_arquivo, destino)
                print(f"Movido: {arquivo} → Outros")

organizar_arquivos()

print("Organização concluída!")