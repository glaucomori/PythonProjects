# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquiveSize = float(input('Qual é o tamanho do arquivo para download (em MB)? '))
internetSpeed = float(input('Qual é a velocidade de um link de Internet (em Mbps)? '))
arquiveSizeInBits = arquiveSize * 8
downloadTimeInSeconds = arquiveSizeInBits / internetSpeed
time = round(downloadTimeInSeconds)
print(f'O tempo aproximado de download é de {time} segundos')