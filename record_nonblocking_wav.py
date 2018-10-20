"""
Record sound from built-in microphone (non-blocking way for real-time processing) and write it to wave file
https://gist.github.com/sloria/5693955
http://people.csail.mit.edu/hubert/pyaudio/docs/
https://docs.python.org/2/library/wave.html
"""

import pyaudio
import wave
import time
#import numpy as np

#in_data (recorded data), frame_count (number of frames), time_info['current_time'], status (PaCallbackFlags)
#callback function called in separate thread when new audio data is available
def callback(in_data, frame_count, time_info, status):
    wavfile.writeframes(in_data) #write recorded data to wavfile
    #np.fromstring(in_data, np.int16) #string to int
    #paContinue - more audio data to come | paComplete - this was the last block of data
    return (in_data, pyaudio.paContinue)

#instantiate recorder
recorder = pyaudio.PyAudio()
#create .wav file for writing
wavfile = wave.open('temp.wav', 'wb') #open file temp.wav for writing
wavfile.setnchannels(2) #set number of channels
wavfile.setsampwidth(recorder.get_sample_size(pyaudio.paInt16)) #set sample width to the size for the paInt16 format
wavfile.setframerate(44100) #set frame rate
#create stream
stream = recorder.open(format = pyaudio.paInt16, #sampling size and format
                       channels = 2, #num of channels
                       rate = 44100, #sampling rate
                       input = True, #input (record) stream
                       frames_per_buffer = 1024, #number of frames per buffer
                       stream_callback = callback #callback function for non-blocking operation
                       )
#recording
stream.start_stream() #start recording (non-blocking)
time.sleep(5) #record for 5 seconds (or you can do operations here)
stream.stop_stream() #stop recording
#close errthing
stream.close()
wavfile.close()
recorder.terminate()
