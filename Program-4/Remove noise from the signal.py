
#################### Remove noise from the signal ####################

import numpy as np
import matplotlib.pyplot as plt
import wave
import struct

freq          = 1000
num_samples   = 48000
sampling_rate = 48000.0

noise_freq = int(input("Enter the noise frequency: "))

sine_wave   = [np.sin(2*np.pi*freq*x/sampling_rate) for x in range(num_samples)]
sine_noise  = [np.sin(2*np.pi*noise_freq*x/sampling_rate) for x in range(num_samples)]

sine_wave   = np.array(sine_wave)
sine_noise  = np.array(sine_noise) 

combined = sine_wave + sine_noise
datafft =  np.fft.fft(combined)
freq2   =  np.abs(datafft[:len(datafft)])

filtered_freq = []
index = 0 
for f in freq2:
    if index > 950 and index < 1050:
        if f >1:
            filtered_freq.append(f)
        else:
            filtered_freq.append(0)
    else:
        filtered_freq.append(0)
    index += 1

recovered = np.fft.ifft(filtered_freq)

plt.subplot(4,1,1)
plt.title("Asli")
plt.subplots_adjust(hspace=1)
plt.plot(sine_wave[:500])

plt.subplot(4,1,2)
plt.title("noise")
plt.plot(sine_noise[:5000])

plt.subplot(4,1,3)
plt.title("combined")
plt.plot(combined[:5000])

plt.subplot(4,1,4)
plt.title("recovered")
plt.plot(recovered[:500])

plt.show()

