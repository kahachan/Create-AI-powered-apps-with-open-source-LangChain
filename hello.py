import gradio as gr

def greet(nama):
    return "Halo " + nama + ", Selamat bergabung di IBM Academy!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch(share=True)