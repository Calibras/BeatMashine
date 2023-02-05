import array
import numpy as np
from pydub import AudioSegment
import pygame
import sounddevice as sd
import numpy as np
import keyboard
from scipy.io.wavfile import write
import timeit

def aufnahme():
    duration = 5  # seconds
    fs = 44100  # Sample rate

    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    print("AUFNAHME!")
    sd.wait()  # Wait until recording is finished
    print("ENDE AUFNAHME")

    write("output.wav", fs, myrecording)

def pausenKiller():
    # Lade die Audiodatei
    sound = AudioSegment.from_file("input.mp3", format="mp3")

    # Bestimme die Stillebereiche in der Audiodatei
    silent_ranges = sound.silent_ranges(min_silence_len=100, silence_thresh=-16)

    # Entferne die Stillebereiche aus der Audiodatei
    for start, end in silent_ranges:
        sound = sound[:start] + sound[end:]

    # Speichere die bearbeitete Audiodatei
    sound.export("output.mp3", format="mp3")

def ueberlappen():
    # Lade die Audiodateien
    sound_a = AudioSegment.from_file("sound_a.mp3", format="mp3")
    sound_b = AudioSegment.from_file("sound_b.mp3", format="mp3")

    # Kürze Sound A auf die ersten 10 Sekunden
    sound_a = sound_a[:10 * 1000]

    # Fange mit Sound B erst nach 5 Sekunden an
    sound_b = sound_b[5 * 1000:]

    # Überlagere Sound A und Sound B
    result = sound_a.overlay(sound_b)

    # Speichere das Ergebnis

"""
sound1 = AudioSegment.from_wav("sounds/clap.wav")
speedsound1 = sound1.speedup(1.5)
sound2 = AudioSegment.from_wav("sounds/crash.wav")
sound3 = AudioSegment.silent(duration=500)  # 0,5 Sekunden Stille

combined = sound1 + speedsound1 + sound1 + sound2

combined.export("output.wav", format="wav")

"""

soundA = AudioSegment.from_wav("sounds/clap.wav")
soundS = AudioSegment.from_wav("sounds/crash.wav")
result =  AudioSegment.silent(duration=1)

running = True
print("aufnahme gestartet")
lastPress = timeit.default_timer()


def on_press_k(e):
    print("K wurde gedrückt")

def on_press_a(e):
    print("A wurde gedrückt")
    addSound(soundA)
def on_press_s(e):
    print("S wurde gedrückt")
    addSound(soundS)
def addSound(sound):
    global result
    global lastPress

    now = timeit.default_timer()
    pauseLength = now - lastPress
    pauseSegment = AudioSegment.silent(duration=int(pauseLength * 250))
    lastPress = timeit.default_timer()

    result = result + pauseSegment
    result = result + sound
def main():
    keyboard.on_press_key("a", on_press_a)
    keyboard.on_press_key("k", on_press_k)
    keyboard.on_press_key("s", on_press_s)
    keyboard.wait("esc")
    export(result)

def export(exportFile):
    exportFile.export("output.wav", format="wav")
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("output.wav")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

    pygame.quit()
def spielerei():
    result = soundA
    length = length_in_ms = len(soundA)
    foo = AudioSegment.silent(duration=int(length / 2))
    foo += soundA
    result.overlay(foo)
    export(soundA + soundA + soundS + soundA + soundA)
