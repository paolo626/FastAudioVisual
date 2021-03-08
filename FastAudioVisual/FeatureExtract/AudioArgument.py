import librosa
import numpy as np
from specAugment import spec_augment_tensorflow
from matplotlib import pyplot as plt
import random
import math
from scipy.fftpack import fft

## ok 
def ArgumentAudio(y, sr,n_steps=3,rate=1.2):
    """Agument Audio feature
    :param y: np.ndarray [shape=(n,)], real-valued the input signal (audio time series)
    :param sr: sample rate of 'y'
    :param size: the length (seconds) of random crop from original audio, default as 3 seconds
    :return: MFCC feature
    """

    y_ps = librosa.effects.pitch_shift(y, sr, n_steps=3)  # frequency change audio high or low
    y_ts = librosa.effects.time_stretch(y, rate=1.2)

    return  y_ps


def ArgumentMel(mel_spectrogram):
    """
     Agument Mel feature 
    param y: np.ndarray [shape=(n,)], real-valued the input signal (audio time series)
    param sr: sample rate of 'y'
    param size: the length (seconds) of random crop from original audio, default as 3 seconds
    return: MFCC feature
    """

    warped_masked_spectrogram = spec_augment_tensorflow.spec_augment(mel_spectrogram=mel_spectrogram)
    #warped_masked_spectrogram = spec_augment_pytorch.spec_augment(mel_spectrogram=mel_spectrogram)



    #plt.figure(figsize=(10, 4))
    #librosa.display.specshow(librosa.power_to_db(warped_masked_spectrogram, ref=np.max), y_axis='mel', fmax=8000, x_axis='time')
    #plt.title("Augmented Spectrogram")
    #plt.tight_layout()
    #plt.show()
    #plt.savefig('bbb')}
    return  warped_masked_spectrogram


def ArgumentNoise(signal, snr_low=15, snr_high=30, nb_augmented=2):
    '''
    Function to add noise to a signals with a desired Signal Noise ratio (SNR)
    '''
    
    # Signal length
    signal_len = len(signal)

    # Generate White noise
    noise = np.random.normal(size=(nb_augmented, signal_len))
    
    # Compute signal and noise power
    s_power = np.sum((signal / (2.0 ** 15)) ** 2) / signal_len
    n_power = np.sum((noise / (2.0 ** 15)) ** 2, axis=1) / signal_len
    
    # Random SNR: Uniform [15, 30]
    snr = np.random.randint(snr_low, snr_high)
    
    # Compute K coeff for each noise
    K = np.sqrt((s_power / n_power) * 10 ** (- snr / 10))
    K = np.ones((signal_len, nb_augmented)) * K
    
    # Generate noisy signal
    return signal + K.T * noise








        