from transformers import pipeline

# Load text generation model
text_gen_pipe = pipeline("text-generation", model="google/gemma-3-1b-it")

def generate_text(prompt, max_length=100):
    """Generates text based on the given prompt."""
    if not prompt.strip():
        return "Error: No input provided!"
    
    output = text_gen_pipe(prompt, max_length=max_length, num_return_sequences=1)
    return output[0]["generated_text"]
