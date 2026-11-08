import matplotlib.pyplot as plt
import numpy as np
from utils.preprocessing import generate_synthetic_eeg, bandpass_filter
from utils.analysis import extract_epochs, compute_psd

def main():
    print("Starting EEG Processing Pipeline...")
    
    # 1. יצירת אות EEG סינתטי
    print("1. Generating synthetic raw EEG data...")
    raw_signal, fs, triggers = generate_synthetic_eeg(duration_sec=10.0, fs=250.0)
    
    # 2. סינון האות (באחריות סטודנט א')
    print("2. Applying bandpass filter (1.0 - 40.0 Hz)...")
    try:
        filtered_signal = bandpass_filter(raw_signal, lowcut=1.0, highcut=40.0, fs=fs, order=4)
    except NotImplementedError as e:
        print(f"Error in preprocessing: {e}")
        return

    # 3. חילוץ מקטעים סביב טריגרים (באחריות סטודנט ב')
    print(f"3. Extracting epochs around {len(triggers)} triggers...")
    try:
        epochs = extract_epochs(filtered_signal, triggers, pre_samples=50, post_samples=150)
        print(f"   Shape of extracted epochs: {epochs.shape}")
    except NotImplementedError as e:
        print(f"Error in epoching: {e}")
        return

    # 4. חישוב PSD (באחריות סטודנט ב')
    print("4. Computing Power Spectral Density (PSD) on mean epoch...")
    try:
        mean_epoch = np.mean(epochs, axis=0)
        frequencies, psd = compute_psd(mean_epoch, fs=fs)
    except NotImplementedError as e:
        print(f"Error in spectral analysis: {e}")
        return

    fig, axes = plt.subplots(3, 1, figsize=(10, 8))
    
    time_axis = np.arange(len(raw_signal)) / fs
    axes[0].plot(time_axis[:1000], raw_signal[:1000], label="Raw Signal (Noisy)", color='gray', alpha=0.7)
    axes[0].plot(time_axis[:1000], filtered_signal[:1000], label="Filtered Signal (1-40 Hz)", color='blue')
    axes[0].set_title("Time Domain: Raw vs. Filtered Signal")
    axes[0].set_xlabel("Time (seconds)")
    axes[0].set_ylabel("Amplitude")
    axes[0].legend()
    
    epoch_time = np.linspace(-0.2, 0.6, epochs.shape[1])
    axes[1].plot(epoch_time, mean_epoch, color='teal', linewidth=2)
    axes[1].axvline(0, color='red', linestyle='--', label='Trigger (t=0)')
    axes[1].set_title("Averaged ERP / Epoch Response")
    axes[1].set_xlabel("Time (seconds)")
    axes[1].set_ylabel("Amplitude")
    axes[1].legend()
    
    valid_freq_idx = frequencies <= 45
    axes[2].plot(frequencies[valid_freq_idx], psd[valid_freq_idx], color='purple')
    axes[2].set_title("Frequency Domain: Power Spectrum (PSD)")
    axes[2].set_xlabel("Frequency (Hz)")
    axes[2].set_ylabel("Power")
    
    plt.tight_layout()
    print("Pipeline finished successfully! Displaying plots...")
    plt.show()

if __name__ == "__main__":
    main()
