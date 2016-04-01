import pygame
import numpy as np

# Add the data points to an array (create the wave)
def create_wave(bits,sampling_rate,volume,freq,duration):
    """Creates an array of sine wave values based on certain parameters.
    Arguments:
    bits -- How many bits are used in the values, e.g., 16
    sampling_rate -- How many samples per second, e.g., 44100
    volume -- Volume, from 0 to 1 (max)
    freq -- The frequency of the note
    duration -- Duration of the note in seconds
    Returns:
    snd_array -- Array of the notes sine wave values, as 16-bit numpy integers
    """
    # Calculate the volume based on the used bit value (signed int)
    if volume<0: volume = 0
    if volume>1: volume = 1
    volume = pow(2,bits-1)-1
    # An empty list
    snd_list = []
    # Fill the list with sine wave values
    for x in range(0,int(sampling_rate*duration)):
        value = volume * np.sin(2 * np.pi * freq * x / sampling_rate)
        snd_list.append(value)
    # Create a numpy array of the list, needed later.
    # Note: We don't create a numpy array earlier, because when
    # appending values to it, a new array is always created.
    # That is not efficient.
    snd_array = np.array(snd_list).astype(np.int16)
    return snd_array

def main():
    # Set some variables
    sampling_rate = 44100
    bits = 16
    # In this case: mono
    channels = 1
    # Volume from 0 to 1
    volume = 0.5
    # Note frequency
    freq = 440
    # Note duration in seconds
    duration = 2.0
    # The duration this program is alive, right now the same as note duration
    wait_duration = duration

    # Initialize pygame mixer
    pygame.mixer.pre_init(sampling_rate, -bits, channels) 
    pygame.init()

    # Create the wave
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
