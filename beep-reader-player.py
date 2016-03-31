import pygame
import numpy as np

sampling_rate = 44100
bits = 16
channels = 1
volume = 4096
freq = 440
duration = 1000

pygame.mixer.pre_init(sampling_rate, -bits, channels) 
pygame.init()

snd_list = []
for x in range(0,sampling_rate):
    value = volume * np.sin(2 * np.pi * freq * x / sampling_rate)
    snd_list.append(value)
snd_array = np.array(snd_list).astype(np.int16)

sound = pygame.sndarray.make_sound(snd_array)
sound.play(-1)
pygame.time.delay(duration)
sound.stop()
