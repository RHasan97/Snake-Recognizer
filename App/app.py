from fastai.vision.all import load_learner
import gradio as gr

snake_labels = (
    "Monocled cobra",
    "Egyptian cobra",
    "Black-necked spitting cobra",
    "Samar cobra",
    "Red spitting cobra",
    "Javan spitting cobra",
    "Spectacled cobra",
    "Russell's viper",
    "Horned vipers",
    "Bush vipers",
    "Eyelash viper",
    "Saw-scaled vipers",
    "Banded krait",
    "Black mamba",
    "Inland taipan",
    "Eastern brown snake",
    "Rattle snake",
    "King cobra"
)

model = load_learner('snake-recognizer-v0.pkl')

def recognize_snake(photo):
    pred,idx, probs = model.predict(photo)
    return pred


image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()
examples = [
    'viper-2.jpg',
    'shutterstock_2062214282-edited-1-scaled.jpg',
    'download (3).jpg',
    'download (4).jpg',
    'Naja_sputatrix.jpg',
    'download (6).jpg',
    'download.jpg'
    ]

iface = gr.Interface(fn=recognize_snake, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)