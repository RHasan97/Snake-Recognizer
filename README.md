# Snake-Recognizer
This is an image classification model. It can classify 18 different types of venomous snakes <br/>
The types the model is able to identify:<br/>
1. Monocled cobra
2. Egyptian cobra
3. Black-necked spitting cobra
4. Samar cobra
5. Red spitting cobra
6. Javan spitting cobra
7. Spectacled cobra
8. Russell's viper
9. Horned vipers
10. Bush vipers
11. Eyelash viper
12. Saw-scaled vipers
13. Banded krait
14. Black mamba
15. Inland taipan
16. Eastern brown snake
17. Rattle snake
18. King cobra



# Dataset Preparation
**Data Collection:** Downloaded from DuckDuckGo using term name <br/>
**DataLoader:** Used fastai DataBlock API to set up the DataLoader. <br/>
**Data Augmentation:** Fastai provides default data augmentation which operates in GPU. <br/>
Details can be found in `Notebooks/snake_data_prep.ipynb`

# Training and Data Cleaning
**Training:** Fine-tuned a resnet34 model for 5 epochs (4 times) and got up to ~92% accuracy. <br/>
**Data Cleaning:** The longest portion of the time spent was this one. There were numerous noises as I collected the data from the browser. Additionally, some of the photographs contained different shapes and objects. Using Fastai ImageClassifierCleaner, I updated and cleaned the data. Except for the last occasion, which was the last iteration of the model, I purged the data after every training or fine-tuning session. <br/>

# Model Deployment
I deployed to model to HuggingFace Spaces Gradio App. The implementation can be found in the `App` folder [here](https://huggingface.co/spaces/Rhasan97/snake-recognizer). <br/>
<img src = "App/deployment/gradio_app.png" width="700" height="350">

# API integration with GitHub Pages
The deployed model API is integrated [here](https://rhasan97.github.io/Snake-Recognizer/) in GitHub Pages Website. Implementation and other details can be found in the `docs` folder.
