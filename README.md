# PyLation - Relational Network for Keras

* Please note that this package and all its contents are still under development but will be useable by the end of January  

#### Introduction to Relational Networks 

Relational Networks (RNs) are a gaining recognition within field of Deep Learning, introduced by DeepMind in 2017 (click [here](https://arxiv.org/pdf/1706.01427.pdf) for the original paper). RNs are fundamentally structured to learn or infer relationships between unique objects in a system - i.e. they learn the rules governing interactions between objects in a system. Basically, RNs are a system of stacked, inter-connected multilayered perceptrons that are much less sensitive to hyperparameter selection. Results indicate they are more robust and broadly generalizable to a variety of applications such as image classification and weather forecasting. Furthermore, they can easily be used in unison with any type of previously developed Neural Network model (as shown in [examples](examples)).


#### Introduction to PyLation

PyLation is a fairly straight forward Relational Network package. Within the code I have attempted to provide documentation on the fundamentals of Relational Networks and have included several examples, mostly taken from [keras](https://keras.io/) and adapted to this package. Please contact me with any questions or comments, I'm new to the open source community and am unfamiliar with how things work so am definitely appreciative of any assitance out there. 

For those interested, this initially began as a research project for [Dr. Brian Jackel](http://contacts.ucalgary.ca/info/phas/profiles/486-146343) at the University of Calgary [Department of Physics and Astronomy](https://phas.ucalgary.ca/). Dr. Jackel hired me to experiment with Neural Networks for forecasting space weather (or Geomgnetic Storms) using a combination of solar wind satellite data and Earth-based magnetometer data. Forecasting solar storms is an inherently difficult problem (which I will not delve into here, but a paper is forthcoming) and I quickly found that simple Multi-Layered Perceptrons (MLPs) were unable to provide reliable forecasts. Upon gaining this knowledge I began experimenting and familiarizing myself with other Deep Learning algorithms (LSTM, CNN, etc.) but they were still unable to adequately satisfy our forecasting parameters. Eventually we found the afformentioned [paper](https://arxiv.org/pdf/1706.01427.pdf) and I began applying their ideas to the geomagnetic storm project. The results were great and the code eventually morphed into this usable (hopefully) package.

## Getting Started

#### Deep Learning

Deep learning is an intimidating subject to invest time in - everyone learns at a different pace and there is no guarantee how long before you start seeing positive returns on your time. My best advice is to be very patient with yourself, if this were an easy subject everyone would already know it. Fortunately, the complexity of this field - coupled with fairly recent advancements in GPU computation technology - has made deep learning ripe with opportunity to apply these algorithms in new and exciting ways.

If you are unfamiliar with Deep Learning I would suggest 'at least' spending time going through the Keras [tutorials/examples](https://github.com/keras-team/keras/tree/master/examples), although spending a few weeks building a neural network solely in python would be very advantageous. It will likely be difficult to grasp Relational Networks without first spending some time on more fundamental Deep Learning concepts. 

#### Relational Networks

If you have prior experience with Deep Learning but are unfamiliar with Relational Networks, please see the original [paper](https://arxiv.org/pdf/1706.01427.pdf). I have also created a brief animation of how Relational Networks operate on input data in general [here](https://www.youtube.com/edit?o=U&video_id=ZlUcn1TAMlA). 

#### GPU Computations/Amazon Web Services

If you are unfamiliar with Amazon Web Services (AWS), please spend some time learning how to set up a virtual machine. AWS offers some very helpful tutorials on doing this, so I will not go into too much depth here. Additionally, due to the complexity of the opperations performed, it is highly recommended that you utilize a GPU during training. 

For those who prefer skipping the (sometimes painstaking) process of setting up a machine from scratch for GPU computations, you can find a custom Ubuntu 16.04 image [here](https://aws.amazon.com/). I will do my best to maintain this distribution as long as people are using it. Below are the instructions necessary to set up this virtual machine - please see amazon web services [documentation](https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/) for instructions on signing up for an AWS account etc. 

#### Using the AWS pre-built image

This pre-built image has everything necessary to begin working with RNs immediately. 

1. 

### Installing PyLation

* I will be setting up an anaconda repository then its just 'conda install pylation'
### Using PyLation

Please see the Examples section of this repository for descriptions and tutorials on a variety of different applications for Relational Networks. Each example is fairly well documented but please let me know if there is anything unclear or confusing within the code.








