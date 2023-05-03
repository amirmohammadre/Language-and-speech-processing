
#################### Calculate the frequency of a Wave file ####################

import numpy as np
import matplotlib.pyplot as plt
import wave
import struct

num_samples = 48000
    
file2   ="firstwav.wav"
wavfile = wave.open(file2,'rb')

data = wavfile.readframes(num_samples)
wavfile.close()

data    = struct.unpack('{n}h'.format(n = num_samples), data)
data    = np.array(data)
datafft = np.fft.fft(data)

freq    = np.abs(datafft)

plt.subplot(2,1,1)
plt.title("Hoze Zaman")
plt.subplots_adjust(hspace=1)
plt.plot(data[0:400])

plt.subplot(2,1,2)
plt.plot(freq)
plt.title("Ferekans")
plt.xlim(0,1200)

plt.show()

print("The Frequency is {} Hz".format(np.argmax(freq)))

