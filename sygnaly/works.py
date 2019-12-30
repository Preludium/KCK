from pylab import *
import numpy as np
from scipy import *
import scipy.io.wavfile
from scipy import signal
import matplotlib.pyplot as plt
import glob
import matplotlib.colors

# w - czestotliwosc probkowania
def sprawdzacz(signalData, w):
    low = 120
    high = 6000
    signalData = np.array(signalData) # to numpy array
    if (len(signalData.shape) > 1): # if array 2D then make it 1D
        signalData = [s[0] for s in signalData]

    signal = []
    if w*3 < len(signalData):
        for i in range(w, w*3):
            signal.append(signalData[i])
    else:
        signal = signalData

    signalfft = fft(signal)
    signalfft = abs(signalfft)

    signal = []
    freqs = range(int(len(signalfft) / 2))
    for i in freqs:
        signal.append(signalfft[i])

        if i < low or i > high:
            signal[i] = 0

    output = []
    result = signal.copy()
    output.append(signal)
    for i in range(1, 8):
        output.append(scipy.signal.decimate(signal, i)) # downsampling the signal by applying filter
        for j in range(len(output[i])):
            result[j] = result[j] * output[i][j] # apply filtered signal to destination array

    for i in range(len(result)):
        if result[i] < 1:
            result[i] = 0

    # plt.subplot(211)
    # p1 = plt.plot(freqs, signal, '-')
    # plt.yscale('log')

    # plt.subplot(212)
    # p2 = plt.plot(freqs, result, '-')
    # plt.yscale('log')
    # plt.show()

    print(freqs[argmax(result, 0)])
    if freqs[argmax(result, 0)] > 350:
        return("K")
    else:
        return("M")

def checkall():
    files = glob.glob("./audio/*.wav")
    wins = []
    for i in range(len(files)):
        files[i] = files[i][2:]
        files[i] = files[i].replace('\\', '/')
        wins.append(files[i][-5])

    wins_num = 0
    loss_num = 0
    for i in range(0, len(files)):
        try:
            w, signalData = scipy.io.wavfile.read(files[i])
            result = sprawdzacz(signalData, w)
        except:
            result = 'K'
        
        if result == wins[i]:
            wins_num = wins_num + 1
        else:
            loss_num = loss_num + 1 

        print(files[i], result)

        print("win ",wins_num, ", loss ", loss_num)

# w, signalData = scipy.io.wavfile.read("audio/047_K.wav")
# sprawdzacz(signalData, w)
checkall()