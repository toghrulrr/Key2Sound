"""
Onset detection of wav file
https://librosa.github.io/librosa/_modules/librosa/onset.html
"""

import matplotlib.pyplot as plt
import numpy as np
import librosa

#read file
signal, rate = librosa.load("recording.wav") #read wav file (signal = data) (rate = sample rate)
#find offsets
onset_frames = librosa.onset.onset_detect(y = signal, sr = rate) #estimated positions of detected onsets (frame indices)
#do conversions
onset_seconds = librosa.frames_to_time(onset_frames, sr = rate) #convert frames to seconds
signalTime = np.linspace(0, len(signal)/rate, num=len(signal)) #time interval for wav file signal
#plot
plt.plot(signalTime, signal, color='b') #plot signal (wav file)
plt.plot(onset_seconds, [0.2]*len(onset_seconds), 'ro', markersize = 3) #plot onset seconds as dots
plt.show()
