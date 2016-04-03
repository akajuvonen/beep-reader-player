import pygame
import numpy as np

# Add the data points to an array (create the wave)
def create_note(bits,sampling_rate,volume,freq,duration):
    """Creates a single note as a sine wave.
    Arguments:
    bits -- How many bits are used in the values, e.g., 16
    sampling_rate -- How many samples per second, e.g., 44100
    volume -- Volume, from 0 to 1 (max)
    freq -- The frequency of the note
    duration -- Duration of the note in seconds
    Returns:
    snd_array -- A list of sine wave values based on the current note
    """
    # Calculate the volume based on the used bit value (signed int)
    if volume<0: volume = 0
    if volume>1: volume = 1
    volume = pow(2,bits-1)-1
    # An empty list
    note = []
    # Fill the list with sine wave values
    for x in range(0,int(sampling_rate*duration)):
        value = volume * np.sin(2 * np.pi * freq * x / sampling_rate)
        note.append(value)
    return note

def create_melody(bits,sampling_rate,volumes,freqs,durations):
    """Creates and returns a melody consisting of one or more notes.
    Arguments:
    bits -- How many bits are used in the values, e.g., 16
    sampling_rate -- How many samples per second, e.g., 44100
    volumes -- A list of volumes for individual notes
    freqs -- A list of frequencies for individual notes
    durations -- Note durations in a list
    Returns:
    melody -- A list of wave values based on the current melody
    """
    melody = []
    # Go through the list
    for volume,freq,duration in zip(volumes,freqs,durations):
        # Create an individual note
        note = create_note(bits,sampling_rate,volume,freq,duration)
        # Add a note to the melody list
        melody.extend(note)
    return melody

def calculate_freq(note):
    """Calculates the frequency of a give note based on it's name and frequency of A4=440Hz.
    """
    notes = ['C4','C#4','D4','D#4','E4','F4','F#4','G4','G#4','A4','A#4','B4']
    baseind = notes.index('A4')
    noteind = notes.index('note')
    n = baseind - noteind
    a = 1.059463094359
    f0 = 440
    freq = f0 * pow(a,n)
    return freq

def main():
    # Set some variables
    sampling_rate = 8000
    bits = 16
    # In this case: mono
    channels = 1
    # Volumes from 0 to 1
    volumes = [0.5,0.5]
    # Note frequencies
    freqs = [440,880]
    # Note durations in seconds
    durations = [1.0,2.0]
    # The duration this program is alive, right now the same as note duration
    wait_duration = sum(durations)

    # Initialize pygame mixer
    pygame.mixer.pre_init(sampling_rate, -bits, channels) 
    pygame.init()

    # Create the wave
    melody = create_melody(bits,sampling_rate,volumes,freqs,durations)
    # Create a numpy array of the list, needed later.
    # Note: We don't create a numpy array earlier, because when
    # appending values to it, a new array is always created.
    # That is not efficient.
    melody = np.array(melody).astype(np.int16)
    # Get the sound based on the array
    sound = pygame.sndarray.make_sound(melody)
    # Play and loop
    sound.play()
    # Stop after <duration>
    pygame.time.delay(int(wait_duration*1000))
    # Stop playing
    sound.stop()

if __name__=="__main__":
    main()
