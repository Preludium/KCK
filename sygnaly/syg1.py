import numpy as np
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt

# from frequency_estimator import freq_from_hps 
# downloaded from https://github.com/endolith/waveform-analyzer/

def freq_from_hps(signal, fs):
    """Estimate frequency using harmonic product spectrum
    Low frequency noise piles up and overwhelms the desired peaks
    """
    N = len(signal)
    signal -= np.mean(signal)  # Remove DC offset

    # Compute Fourier transform of windowed signal
    windowed = signal * kaiser(N, 100)

    # Get spectrum
    X = log(abs(rfft(windowed)))

    # Downsample sum logs of spectra instead of multiplying
    hps = copy(X)
    for h in arange(2, 9): # TODO: choose a smarter upper limit
        dec = decimate(X, h)
        hps[:len(dec)] += dec

    # Find the peak and interpolate to get a more accurate peak
    i_peak = argmax(hps[:len(dec)])
    i_interp = parabolic(hps, i_peak)[0]

    # Convert to equivalent frequency
    return fs * i_interp / N  # Hz

filename = 'Vocaroo_s1KZzNZLtg3c.wav'
# downloaded from http://vocaroo.com/i/s1KZzNZLtg3c

# Parameters
time_start = 0  # seconds
time_end = 1  # seconds
filter_stop_freq = 70  # Hz
filter_pass_freq = 100  # Hz
filter_order = 1001

# Load data
fs, audio = wavfile.read(filename)
audio = audio.astype(float)

# High-pass filter
nyquist_rate = fs / 2.
desired = (0, 0, 1, 1)
bands = (0, filter_stop_freq, filter_pass_freq, nyquist_rate)
filter_coefs = signal.firls(filter_order, bands, desired, nyq=nyquist_rate)

# Examine our high pass filter
w, h = signal.freqz(filter_coefs)
f = w / 2 / np.pi * fs  # convert radians/sample to cycles/second
plt.plot(f, 20 * np.log10(abs(h)), 'b')
plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Frequency [Hz]')
plt.xlim((0, 300))

# Apply high-pass filter
filtered_audio = signal.filtfilt(filter_coefs, [1], audio)

# Only analyze the audio between time_start and time_end
time_seconds = np.arange(filtered_audio.size, dtype=float) / fs
audio_to_analyze = filtered_audio[(time_seconds >= time_start) &
                                  (time_seconds <= time_end)]

fundamental_frequency = freq_from_hps(audio_to_analyze, fs)
print 'Fundamental frequency is {} Hz'.format(fundamental_frequency)