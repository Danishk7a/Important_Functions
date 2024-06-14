from scipy.io import wavfile
import noisereduce as nr
from pydub import AudioSegment
from pydub.effects import normalize

# Load audio file
sampling_rate, audio_data = wavfile.read('audio.wav')

# Assuming you have a noise clip or can estimate noise profile
# For example, get noise profile from a portion of audio
noise_clip = audio_data[0:10000]

# Reduce noise using noisereduce library
reduced_noise = nr.reduce_noise(audio_clip=audio_data, noise_clip=noise_clip)

# Convert numpy array to AudioSegment for processing
audio_segment = AudioSegment(
    reduced_noise.tobytes(), 
    frame_rate=sampling_rate, 
    sample_width=reduced_noise.dtype.itemsize, 
    channels=1  # Assuming mono audio
)

# Apply equalization or other effects as needed
# Example: Boosting high frequencies
eq_audio = audio_segment.high_pass_filter(100)  # Example high-pass filter to boost high frequencies

# Normalize to target loudness
normalized_audio = normalize(eq_audio)

# Export the processed audio
normalized_audio.export("processed_audio.wav", format="wav")
