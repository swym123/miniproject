import gradio as gr
from summarizer import summarize_text
from text_to_speech import generate_audio

def process_summarization(text):
    """Summarizes text and generates speech."""
    summary = summarize_text(text)
    if "Error" in summary:
        return summary, None
    
    audio_path = generate_audio(summary)
    return summary, audio_path

# def process_text_generation(prompt, max_length):
#     """Generates text using GPT-2."""
#     return generate_text(prompt, max_length)

# Create Gradio Tabs
with gr.Blocks() as app:
    gr.Markdown("# AI Text Processing Tool")

    with gr.Tabs():
        # Tab 1: Summarization + TTS
        with gr.Tab("Text Summarization & Speech"):
            gr.Markdown("### Enter text to summarize and generate speech")
            text_input = gr.Textbox(lines=5, placeholder="Enter text to summarize...")
            summary_output = gr.Textbox(label="Summary")
            audio_output = gr.Audio(label="Generated Audio")
            summarize_btn = gr.Button("Summarize & Generate Audio")
            summarize_btn.click(process_summarization, inputs=text_input, outputs=[summary_output, audio_output])

        # Tab 2: Text Generation
        # with gr.Tab("Text Generation (GPT-2)"):
        #     gr.Markdown("### Enter a prompt to generate text")
        #     prompt_input = gr.Textbox(lines=2, placeholder="Enter prompt for text generation...")
        #     max_length_input = gr.Slider(50, 500, step=10, value=100, label="Max Length")
        #     generated_text_output = gr.Textbox(label="Generated Text")
        #     generate_btn = gr.Button("Generate Text")
        #     generate_btn.click(process_text_generation, inputs=[prompt_input, max_length_input], outputs=generated_text_output)

# Run the app
if __name__ == "__main__":
    app.launch()
