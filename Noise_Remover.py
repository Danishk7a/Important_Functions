import os
import librosa
import noisereduce as nr
import soundfile as sf

# Use an absolute path to ensure the file can be found
file_path = './audio.wav'

# Check if the file exists
if not os.path.isfile(file_path):
    raise FileNotFoundError(f"Audio file not found: {file_path}")

try:
    # Load the audio file using librosa
    y, sr = librosa.load(file_path, sr=None)
except Exception as e:
    print(f"Error loading audio with librosa: {e}")
    # Fall back to pydub if librosa fails
    from pydub import AudioSegment
    audio = AudioSegment.from_file(file_path)
    y = np.array(audio.get_array_of_samples())
    sr = audio.frame_rate

# Perform noise reduction
reduced_noise = nr.reduce_noise(y=y, sr=sr)

# Save the reduced noise audio to a new file
output_path = './reduced_noise_audio.wav'
sf.write(output_path, reduced_noise, sr)

print(f"Noise reduced audio saved at: {output_path}")
