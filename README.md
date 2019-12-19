# reciclAPI

## Introduction:
In this project I have depeloped an API with a Convolutional Neural Network that receives waste images, process them, and responds with the kind of material it thinks is made: 

* Battery
* Cardboard
* Glass
* Metal
* Paper
* Plastic
* Tetrapak
* Trash

## Technologies: 
You can find an API and a simple web page running on Flask that call the Fastai model trained over Pytorch.
* https://www.palletsprojects.com/p/flask/
* https://www.fast.ai/
* https://pytorch.org/ 

If your PC has nVIDIA GPU, I recommend you to install CUDA drivers for your GPU model:
* https://developer.nvidia.com/cuda-downloads


## How to use it:
### Web
Just clone this repo and run `api.py` in your computer. Then open the browser and go to `localhost:8080`. Finally, upload a waste image and receive an answer telling you the kind of material it is made.

### API
Clone the repo and run run `api.py` in your computer. Open Postman, click in `body` and then in `form-data`. The `Key` field must be "file" type and must contain "post" word. `Value` field should contain the image you want to upload.
After uploading the waste image you will receive a JSON with the kind of material it is made.