


import os
import PyPDF2
from PyPDF2 import PdfReader

# define a palavra que queremos procurar
palavra = "palavra-chave"

# define o caminho da pasta onde os arquivos estão localizados
pasta = "C:/Users/LUIS\Desktop/Projetos/PDF_Search/Diario"

# Lista para armazenar os arquivos que contêm a palavra
arquivos_com_palavra = []

# Loop pelos arquivos da pasta
for arquivo in os.listdir(pasta):
    # Verifica se o arquivo é PDF
    if arquivo.lower().endswith('.pdf'):
        print(f"Lendo '{arquivo}'...")
        # Abre o arquivo em modo leitura binária
        with open(os.path.join(pasta, arquivo), 'rb') as pdf_file:
            # Cria o objeto leitor de PDF
            leitor = PyPDF2.PdfReader(pdf_file)
            # Loop pelas páginas do arquivo
            for pagina in range(len(leitor.pages)):
                # Extrai o texto da página e converte para minúsculo
                texto = leitor.pages[pagina].extract_text().lower()
                # Verifica se a palavra está presente no texto
                if palavra.lower() in texto:
                    # Adiciona o nome do arquivo à lista de arquivos com a palavra
                    arquivos_com_palavra.append(arquivo)
                    break  # interrompe o loop pelas páginas
        print(f"Concluído a leitura de '{arquivo}'.")

# Verifica se foram encontrados arquivos com a palavra
if len(arquivos_com_palavra) > 0:
    # Imprime a lista de arquivos com a palavra
    print(f"Foram encontrados {len(arquivos_com_palavra)} arquivos com a palavra '{palavra}':")
    for arquivo in arquivos_com_palavra:
        print(arquivo)
else:
    # Imprime uma mensagem de aviso
    print(f"A palavra '{palavra}' não foi encontrada em nenhum arquivo PDF da pasta.")
