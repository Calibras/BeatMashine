import array
import numpy as np
from pydub import AudioSegment
import pygame
import sounddevice as sd
import numpy as np
import keyboard
from scipy.io.wavfile import write
import wave
import time
import timeit

def aufnahme():
    duration = 5  # seconds
    fs = 44100  # Sample rate

    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    print("AUFNAHME!")
    sd.wait()  # Wait until recording is finished
    print("ENDE AUFNAHME")

    write("output.wav", fs, myrecording)


"""
sound1 = AudioSegment.from_wav("sounds/clap.wav")
speedsound1 = sound1.speedup(1.5)
sound2 = AudioSegment.from_wav("sounds/crash.wav")
sound3 = AudioSegment.silent(duration=500)  # 0,5 Sekunden Stille

combined = sound1 + speedsound1 + sound1 + sound2

combined.export("output.wav", format="wav")

"""

soundA = AudioSegment.from_wav("sounds/clap.wav")
soundB = AudioSegment.from_wav("sounds/crash.wav")
result =  AudioSegment.silent(duration=1)

running = True
print("aufnahme gestartet")
lastPress = timeit.default_timer()
while running:
    eingabe = input()
    if eingabe == "a":
        now = timeit.default_timer()
        pauseLength = now - lastPress
        lastPress = now
        pauseSegment = AudioSegment.silent(duration=int(pauseLength * 1000))
        result = result + pauseSegment
        result = result + soundA
    elif eingabe == "s":
        result += soundB
    elif eingabe == "1":
        running = False

result.export("output.wav", format="wav")

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("output.wav")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.wait(100)

pygame.quit()


