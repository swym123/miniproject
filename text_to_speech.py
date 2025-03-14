import torch
import soundfile as sf
import uuid
from transformers import pipeline
from datasets import load_dataset

# Load TTS model
synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

# Load speaker embeddings dataset
dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
default_speaker_embedding = torch.tensor(dataset[7306]["xvector"]).unsqueeze(0)

def generate_audio(text, speaker_embedding=default_speaker_embedding):
    """Generates AI-based speech for the given text."""
    speech = synthesiser(text, forward_params={"speaker_embeddings": speaker_embedding})

    # Generate a unique filename to prevent overwriting
    audio_path = "output.wav"
    sf.write(audio_path, speech["audio"], samplerate=speech["sampling_rate"])

    return audio_path
