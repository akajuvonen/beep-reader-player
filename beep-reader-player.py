import pygame
import numpy as np

# Add the data points to an array (create the wave)
def create_wave(bits,sampling_rate,volume,freq,duration):
    volume = pow(2,bits-1)-1
    snd_list = []
    for x in range(0,int(sampling_rate*duration)):
        value = volume * np.sin(2 * np.pi * freq * x / sampling_rate)
        snd_list.append(value)
    snd_array = np.array(snd_list).astype(np.int16)
    return snd_array

def main():
    # Set some variables
    sampling_rate = 44100
    bits = 16
    channels = 1
    volume = 0.5
    freq = 440
    duration = 2.0
    wait_duration = duration

    # Initialize pygame mixer
    pygame.mixer.pre_init(sampling_rate, -bits, channels) 
    pygame.init()

    wave = create_wave(bits,sampling_rate,volume,freq,duration)
    # Get the sound based on the array
    sound = pygame.sndarray.make_sound(wave)
    # Play and loop
    sound.play()
    # Stop after <duration>
    pygame.time.delay(int(wait_duration*1000))
    # Stop playing
    sound.stop()

if __name__=="__main__":
    main()
