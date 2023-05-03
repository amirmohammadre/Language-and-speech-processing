
#################### Add noise to the signal ####################

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

plt.subplot(3,1,1)
plt.title("Asli")
plt.subplots_adjust(hspace=1)
plt.plot(sine_wave[:1000])

plt.subplot(3,1,2)
plt.title("noise")
plt.plot(sine_noise[:5000])

plt.subplot(3,1,3)
plt.title("combined")
plt.plot(combined[:5000])

plt.show()

