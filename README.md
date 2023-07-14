# Snake-Recognizer
Can classify 18 different types of venomous snakes <br/>
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
**Data Augmentation:** fastai provides default data augmentation which operates in GPU. <br/>
Details can be found in `notebooks/data_prep.ipynb`

# Training and Data Cleaning
**Training:** Fine-tuned a resnet34 model for 5 epochs (3 times) and got upto ~92% accuracy. <br/>
**Data Cleaning:** The longest portion of the time spend on was this one. There were numerous noises as I collected the data from the browser. Additionally, some of the photographs contained different shapes and objecst. Using fastai ImageClassifierCleaner, I updated and cleaned the data. Except for the last occasion, which was the last iteration of the model, I purged the data after every training or fine-tuning session. <br/>

# Model Deployment
I deployed to model to HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [here](https://huggingface.co/spaces/msideadman/cap-recognizer). <br/>
<img src = "deployment/gradio_app.png" width="700" height="350">

# API integration with GitHub Pages
The deployed model API is integrated [here](msi1427.github.io/Cap-Recognizer/) in GitHub Pages Website. Implementation and other details can be found in `docs` folder.