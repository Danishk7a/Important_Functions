import torch
from TTS.api import TTS

# Ensure the correct device is set (e.g., "cpu" or "cuda")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize the multilingual TTS model for voice cloning
model_name = "tts_models/multilingual/multi-dataset/your_tts"
tts = TTS(model_name=model_name, progress_bar=False).to(device)

# Define the text and the reference audio file path
text = "Hello, this is a cloned voice message generated by the TTS model."
speaker_wav_path = "audio.ogg"
output_path = "cloned_output.wav"

# Generate and save the cloned speech file
tts.tts_to_file(text=text, speaker_wav=speaker_wav_path, language="en", file_path=output_path)

print(f"Cloned speech generated and saved to {output_path}")
