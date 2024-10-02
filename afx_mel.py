import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import soundfile as sf
from tqdm import tqdm

df = pd.read_csv("mushra_final.csv")


def load_audio(file_path):
    try:
        data, samplerate = sf.read(file_path)
        return data, samplerate
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None, None


def plot_mel_spectrograms(indices, titles, columns, name="temp.png"):
    num_rows = len(indices)
    num_cols = len(columns)

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, num_rows * 3))

    for i, idx in enumerate(indices):
        row = df.iloc[idx]
        subtype = row["subtype"]
        for j, col in enumerate(columns):
            ax = axes[i, j] if num_rows > 1 else axes[j]
            audio_data, sr = load_audio(row[col])
            if audio_data is not None and sr is not None:
                mel_spectrogram = librosa.feature.melspectrogram(
                    y=audio_data, sr=sr, n_mels=128, fmax=8000
                )
                mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)
                img = librosa.display.specshow(
                    mel_spectrogram_db,
                    cmap="jet",
                    sr=sr,
                    fmax=8000,
                    ax=ax,
                )
            else:
                ax.text(0.5, 0.5, "File not found", ha="center", va="center")
                img = None  # No image to colorbar

            # Set column titles only on the first row
            if i == 0:
                ax.set_title(titles[j])

            # Set row labels on the first column
            if j == 0:
                ax.set_ylabel(
                    subtype,
                    rotation="vertical",
                    va="center",
                    ha="right",
                    labelpad=20,
                    fontsize=12,
                    color="black",
                )

    plt.tight_layout(rect=[0.1, 0, 1, 1])  # Adjust layout to fit the row labels
    plt.savefig(name, bbox_inches="tight")


if __name__ == "__main__":
    complex_columns = [
        "ref_dry",
        "ref_wet",
        "tar_dry",
        "tar_wet",
        "pred1",
        "pred2",
    ]
    single_columns = [
        "ref_dry",
        "ref_wet",
        "tar_dry",
        "tar_wet",
        "pred1",
        "pred2",
        # "random_param",
    ]

    plot_mel_spectrograms(
        indices=[1, 2, 3, 4, 5],
        titles=[
            "ref_dry",
            "ref_wet",
            "tar_dry",
            "tar_wet",
            "single_effect",
            "multi_effect",
        ],
        columns=complex_columns,
        name="mel_single.png",
    )

    plot_mel_spectrograms(
        indices=[23, 24, 25, 26, 27],
        titles=[
            "ref_dry",
            "ref_wet",
            "tar_dry",
            "tar_wet",
            "single_effect",
            "multi_effect",
        ],
        columns=complex_columns,
        name="mel_monolithic.png",
    )

    plot_mel_spectrograms(
        indices=[18, 19, 20, 21, 22],
        titles=[
            "ref_dry",
            "ref_wet",
            "tar_dry",
            "tar_wet",
            "single_effect",
            "multi_effect",
        ],
        columns=complex_columns,
        name="mel_complex.png",
    )
