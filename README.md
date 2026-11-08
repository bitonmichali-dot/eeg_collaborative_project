# EEG Collaborative Processing Lab

פרויקט תרגול מעשי בעיבוד נתונים בפייתון למדעי המוח, בדגש על עבודה צוותית מודולרית וניהול גרסאות ב-GitHub.

---

##  מבנה הפרויקט

```text
eeg_collaborative_lab/
├── utils/
│   ├── __init__.py
│   ├── preprocessing.py   # מודול עיבוד מקדים (סטודנט א')
│   └── analysis.py        # מודול ניתוח ספקטרלי ומקטעים (סטודנט ב')
├── main.py                # סקריפט הריצה הראשי שמחבר את הפייפליין
├── requirements.txt       # ספריות נדרשות
├── .gitignore
└── README.md
```

---

## 👥 חלוקת תפקידים

### סטודנט א' — עיבוד מקדים (`utils/preprocessing.py`)
- פונקציית `bandpass_filter(data, lowcut, highcut, fs, order=4)`:
  - חישוב תדר נייקוויסט ונרמול תדרי החיתוך.
  - יצירת מסנן Butterworth בעזרת `scipy.signal.butter`.
  - סינון האות הדו-כיווני (Zero-phase) בעזרת `scipy.signal.filtfilt`.

### סטודנט ב' — ניתוח ספקטרלי ומקטעים (`utils/analysis.py`)
- פונקציית `extract_epochs(data, trigger_indices, pre_samples, post_samples)`:
  - חיתוך חלונות זמן סביב אירועים/טריגרים.
  - החזרת מערך דו-ממדי של `numpy`.
- פונקציית `compute_psd(epoch_signal, fs)`:
  - חישוב התמרת פורייה ממשית (`np.fft.rfft`).
  - חישוב ציר התדרים (`np.fft.rfftfreq`).
  - הפקת צפיפות ספקטרום העוצמה (PSD).

---

## 🚀 זרימת עבודה ב-Git & GitHub (שלב אחר שלב)

1. **Fork & Clone**:
   - סטודנט א' מבצע Fork לריפו המקורי.
   - סטודנט א' מוסיף את סטודנט ב' כ-Collaborator ב-GitHub (`Settings` -> `Collaborators`).
   - שני הסטודנטים מבצעים Clone למחשב המקומי:
     ```bash
     git clone <REPO_URL>
     cd eeg_collaborative_lab
     ```

2. **Branching**:
   - סטודנט א': `git checkout -b feature/preprocessing`
   - סטודנט ב': `git checkout -b feature/analysis`

3. **מימוש ובדיקה מקומית**:
   - השלמת קטעי ה-`TODO` בקבצים הייעודיים.
   - התקנת תלויות:
     ```bash
     pip install -r requirements.txt
     ```

4. **Commit & Push**:
   ```bash
   git add .
   git commit -m "Implement missing functions"
   git push origin <feature-branch-name>
   ```

5. **Pull Request & Code Review**:
   - פתיחת PR ל-`main`.
   - ביצוע Code Review ואישור (Approve + Merge) הדדי.

6. **סנכרון והרצה**:
   ```bash
   git checkout main
   git pull origin main
   python main.py
   ```
