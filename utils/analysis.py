import numpy as np

def extract_epochs(data, trigger_indices, pre_samples=50, post_samples=150):
    """
    חיתוך חלונות זמן (Epochs) סביב אירועים/טריגרים.
    מחזיר מערך דו-ממדי: (מספר חלונות, אורך חלון בדגימות).
    """
    # ==========================================
    # TODO (סטודנט ב' - חלק 1):
    # 1. צור רשימה ריקה לאיסוף החלונות.
    # 2. רוץ בלולאה על כל אינדקס ב-trigger_indices.
    # 3. בדוק שחלון הזמן (start: idx - pre_samples, end: idx + post_samples) לא חורג מגבולות המערך data.
    # 4. חתוך את המקטע מתוך data, הוסף לרשימה והחזר כמערך דו-ממדי של numpy (np.array).
    # ==========================================
    raise NotImplementedError("Student B: Please implement extract_epochs()")

def compute_psd(epoch_signal, fs):
    """
    חישוב צפיפות הספקטרום בעזרת FFT (Real FFT).
    מחזיר ציר תדרים ועוצמת הספק (Power Spectral Density).
    """
    # ==========================================
    # TODO (סטודנט ב' - חלק 2):
    # 1. מצא את אורך האות n.
    # 2. חשב את רכיבי התדרים הממשיים בעזרת np.fft.rfft(epoch_signal).
    # 3. חשב את ציר התדרים בעזרת np.fft.rfftfreq(n, d=1.0/fs).
    # 4. חשב את צפיפות ספקטרום העוצמה (PSD): (np.abs(fft_vals) ** 2) / (n * fs).
    # 5. החזר: frequencies, power_spectrum.
    # ==========================================
    raise NotImplementedError("Student B: Please implement compute_psd()")
