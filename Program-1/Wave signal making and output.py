
#################### Wave signal making and output ####################

#import modules
import numpy as np
import matplotlib.pyplot as plt
import wave
import struct

freq          = 1000     #frequency
sampling_rate = 48000.0  #sampling_rate
num_samples   = 48000    #number samples
amp           = 16000    #amplitude

file = "firstwav.wav"    #output_file

#define function y(t)=Asin(2pift)
sine_wave = [np.sin(2*np.pi*freq*x/sampling_rate) for x in range(num_samples)]

nframes   = num_samples         #count frames
comptype  = "NONE"              #compress type
compname  = "not compressed"    #compress name
nchannels = 1                   #number channels
sampwidth = 2                   #Wave file width based on byte

#open the wave file and write the above parameters
wav_file = wave.open(file,'wb')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

for s in sine_wave:
    wav_file.writeframes(struct.pack('h',int(s*amp)))

