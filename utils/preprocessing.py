import numpy as np
from scipy import signal

def generate_synthetic_eeg(duration_sec=10.0, fs=250.0):
    """
    מייצר אות דמוי-EEG סינתטי:
    גל אלפא (10Hz) + גל בטא (20Hz) + סחיפת תדר נמוך (<1Hz) ורעש רשת (50Hz).
    מחזיר: raw_signal, fs, trigger_indices
    """
    n_samples = int(duration_sec * fs)
    t = np.linspace(0, duration_sec, n_samples, endpoint=False)
    
    slow_drift = 1.5 * np.sin(2 * np.pi * 0.3 * t)   # Drift תדר נמוך
    alpha_wave = 1.2 * np.sin(2 * np.pi * 10 * t)   # גל אלפא
    beta_wave  = 0.6 * np.sin(2 * np.pi * 20 * t)   # גל בטא
    line_noise = 0.8 * np.sin(2 * np.pi * 50 * t)   # רעש רשת 50Hz
    gaussian_noise = np.random.normal(0, 0.4, n_samples)
    
    raw_signal = slow_drift + alpha_wave + beta_wave + line_noise + gaussian_noise
    
    # טריגרים כל 2 שניות
    trigger_times = np.arange(1.0, duration_sec - 1.0, 2.0)
    trigger_indices = (trigger_times * fs).astype(int)
    
    return raw_signal, fs, trigger_indices

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    """
    סינון תדרים מסוג Butterworth Bandpass דו-כיווני (Zero-phase filtering).
    """
    # ==========================================
    # TODO (סטודנט א'):
    # 1. חשב את תדר נייקוויסט (0.5 * fs) ונרמל את lowcut ו-highcut לפיו.
    # 2. צור את מקדמי המסנן (b, a) באמצעות signal.butter עם מסנן מסוג 'bandpass'.
    # 3. סנן את האות data בעזרת signal.filtfilt והחזר את האות המסונן.
    # ==========================================
    raise NotImplementedError("Student A: Please implement bandpass_filter()")
