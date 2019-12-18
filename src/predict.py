#!/usr/bin/env python3 

from fastai.vision import *
from fastai.metrics import error_rate
from pathlib import Path
import os

def predict(image):
    # Get the path of our dataset
    path = Path(os.getcwd())/"data"

    # Let's make that all images are in the same position
    tfms = get_transforms(do_flip=True,flip_vert=True)

    # Load test data
    data = ImageDataBunch.from_folder(path,test="test",ds_tfms=tfms,bs=16)

    # Now I define the kind of learner in order to be able to load my trained model:
    learn = cnn_learner(data,models.resnet34,metrics=error_rate, callback_fns=ShowGraph)

    # Load the trained model:
    learn = learn.load("best_model")

    # Load the image we want to predict:
    img = open_image('new_test/{}'.format(image))

    # Resize the image:
    new_height = 512 * img.data.shape[1] / img.data.shape[2]
    img.resize(torch.Size([img.shape[0],int(new_height),512]))

    # Return the prediction made by the model:
    pred_class,pred_idx,outputthirds = learn.predict(img)
    return pred_class
