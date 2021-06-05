import record as rec
import os
#import keyboard
import time

path = input("Digite o identificador da amostra: ")
i = int(input("Digite o numero inicial da amostra: ") or 0)
number = int(input("Digite o numero de amostras: ") or 0)

for z in range(number):
    print("Gravando...")
    rec.recordToFile("sounds/{}/output_{}.wav".format(path, i))
    print("Amostra {} gravada".format(i))
    i = i + 1
