from transformers import pipeline

# Load text summarization model
text_pipe = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    """Summarizes the input text."""
    if not text.strip():
        return "Error: No text provided!"
    
    summary = text_pipe(text, max_length=60, min_length=10, do_sample=False)[0]['summary_text']
    return summary
