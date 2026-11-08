import numpy as np

def extract_epochs(filtered_signal, events, fs, t_min, t_max):
    """
    חותך מקטעי זמן (Epochs) מתוך האות המסונן סביב כל נקודת גירוי (Event).
    """
    # חישוב כמות הדגימות לפני ואחרי הגירוי לפי זמן (בשניות) ותדר הדגימה (fs)
    pre_samples = int(abs(t_min) * fs)
    post_samples = int(t_max * fs)
    
    epochs = []
    # חיתוך האות עבור כל אחד מהאירועים
    for event in events:
        start_idx = event - pre_samples
        end_idx = event + post_samples
        
        # נוודא שהמקטע שאנחנו מנסים לחתוך לא חורג מגבולות האות
        if start_idx >= 0 and end_idx < len(filtered_signal):
            epochs.append(filtered_signal[start_idx:end_idx])
            
    # החזרת המקטעים כמערך של NumPy
    return np.array(epochs)

def calculate_psd(epochs, fs):
    """
    מחשב את צפיפות ספקטרום העוצמה (PSD) באמצעות התמרת פורייה (FFT).
    """
    # ממוצע של כל המקטעים (חישוב ERP)
    mean_epoch = np.mean(epochs, axis=0)
    
    n_samples = len(mean_epoch)
    
    # הפעלת התמרת פורייה מהירה (FFT) על הממוצע
    fft_result = np.fft.fft(mean_epoch)
    
    # יצירת ציר התדרים
    frequencies = np.fft.fftfreq(n_samples, 1/fs)
    
    # חישוב PSD (צפיפות ספקטרום העוצמה - הערך המוחלט בריבוע)
    psd = np.abs(fft_result) ** 2
    
    # לקיחת רק התדרים החיוביים (כי תדר שלילי לא רלוונטי בגרף)
    pos_idx = frequencies >= 0
    
    return frequencies[pos_idx], psd[pos_idx], mean_epoch