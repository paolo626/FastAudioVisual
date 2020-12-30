


import numpy as np
import librosa
import random
 
def extract_logmel(y, sr, size=3):
    """
    extract log mel spectrogram feature
    :param y: the input signal (audio time series)
    :param sr: sample rate of 'y'
    :param size: the length (seconds) of random crop from original audio, default as 3 seconds
    :return: log-mel spectrogram feature
    """
    # normalization
    y = y.astype(np.float32)
    normalization_factor = 1 / np.max(np.abs(y))
    y = y * normalization_factor
 
    # random crop
    start = random.randint(0, len(y) - size * sr)
    y = y[start: start + size * sr]
 
    # extract log mel spectrogram #####
    melspectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=1024, n_mels=60)
    logmelspec = librosa.power_to_db(melspectrogram)
 
    return logmelspec


 
def extract_mfcc(y, sr, size=3):
    """
    extract MFCC feature
    :param y: np.ndarray [shape=(n,)], real-valued the input signal (audio time series)
    :param sr: sample rate of 'y'
    :param size: the length (seconds) of random crop from original audio, default as 3 seconds
    :return: MFCC feature
    """
    # normalization
    y = y.astype(np.float32)
    normalization_factor = 1 / np.max(np.abs(y))
    y = y * normalization_factor
 
    # random crop
    start = random.randint(0, len(y) - size * sr)
    y = y[start: start + size * sr]
 
    # extract log mel spectrogram #####
    melspectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=1024)
    mfcc = librosa.feature.mfcc(S=librosa.power_to_db(melspectrogram), n_mfcc=20)
    mfcc_delta = librosa.feature.delta(mfcc)
    mfcc_delta_delta = librosa.feature.delta(mfcc_delta)
    mfcc_comb = np.concatenate([mfcc, mfcc_delta, mfcc_delta_delta], axis=0)
 
    return mfcc_comb




def noisy_signal(signal, snr_low=15, snr_high=30, nb_augmented=2):
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