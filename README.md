# PyLation - Relational Network (RN) for Keras

## This Project
This code was initially written for Brian Jackel at the University of Calgary Department of Space Physics (with funding provided by the Canadian Space Agency). Brian had me spend most of 2017 working on Neural Network (NN) based forecasting methods with the purpose of applying them towards forecasting space weather - which is known (in extreme cases) to cause severe damage to Earth-based technology, especially at higher latitudes. We used data from ~100 magnetometers stationed throughout northern Canada as well as the OMNI solar wind data from NASA. Several pages are needed for full specs on the management and filtering of the years of (sometimes painfully) inconsistent data, but I won't get into specifics here - instead, I'll be posting a script that should do everything from pull the data to filter all the NaNs and properly shape the arrays for use with Relational Networks (RN's)...but it might take a few more weeks to polish up. 

After months of trying all kinds of different NN's, I was kindly passed a new paper introduced by DeepMind in 2017 (click [here](https://arxiv.org/pdf/1706.01427.pdf) on what they named "Relational Networks". While fairly difficult to fully understand (I've spent 8 months working on them and am still figuring out new ideas from the paper), they seemed like a very powerful tool for forecasting. While LSTM's are known for natural language processing and CNN's for image classification, RN's should be known for their ability to learn physics - I was able to (somewhat) successfully predict the motion of a 4 pendulum system (with random weights and velocities) and create an animation that looked ALMOST realistic based only off initial conditions - I was just trying to learn RN's so didn't spend much time on it, but the results were pretty amazing. 

When confortable with RN's, under the guidance of Brian Jackel, I began applying them to the field of geomagnetic storm prediction. In a nutshell, the final program has the ability to forcast the approximate distribution of magnetic field flux between t0+1hr and t0+2hr based off data between t0-1hr and t0. Most importantly, it is trained in such a way to forecast at arbitrary lat/long coordinates (within a range of course - i.e, you can't predict the flux in China based off data from Canada but you can predict the flux in British Columbia based off data from Alberta). The model is far from perfect and I'm positive that it could be quite easily improved by someone who knows what they're doing (**Please help :p**) but I've reached my temporary limit for a single data set.

### The PyLation Package

I was able to hack this Relational Network package together (hack is an understatement), and it actually turned out fairly well. For those of you familiar with Keras, using this package will come quite naturally. However, instead of having to define the hyperparameters for every single layer, I've modified things slightly to generalize all the hyperparameters to a set of easily modifiably python dictionaries (see examples or the in-code documentation). 

On a related note: If you really want to get your head wrapped around how a Relational Networks function, you absolutely need to be familiar with the more fundamental neural networks. You should be able to use LSTM's for LSTM problems, CNN's for CNN problems, MLP's for MLP problems etc. Don't just familiarize yourself with the theory; spend time on hyperparameter optimization, GPU-based computations - rent a cheap AWS server and pay by the hour then terminate it when you are done for the day (I worked full time for months doing this and spent less than $200.00 total), try and familiarize yourself with server computations, then use keras-gpu from anaconda. There are GREAT examples available on the keras git repository, refer to them but don't just copy and paste them...you'll never learn that way. 

Oh, and like any efficient data scientist, expect to spend about 90% of your time on Google, about 9.9999% of your time debugging your scripts and the remaining 0.0001% of your time zoned out as your network fails to train properly. Just be patient. Very patient. Basically, if you are able to wrap your head around RN's in less then a month or two you should fly out to Calgary and come work for me (cough...algorithmic trading...cough cough...for now...cough cough) or fly out to Calgary and we'll show you how to get set up on your own - in the data science industry there's more profit to be made **honestly** if you're properly educated. Only requirement: spend some free time in Calgary, the oil and gas industry gave us a bad reputation in some of the more progressive locales from what I understand. But it's a great city with great people...and some conveniently cheap (and recently vacated) office space - as well as equally convenient and cheap apartment rentals. 


#### Some potential applications for Relational Networks
This package is easily linked with other Keras layers (LSTM, Dense, CNN etc.), which opens even more doors. Below are a few things that this package (or likely a better version of it) **might** be applicable to. Fyi: these are just from brainstorming as I write this, feel free to attempt any of the below...but maybe keep me posted!

1. Weather forecasting (easier on Earth than in outer space...trust me).
2. Habitable planet detection (public data I think).
3. Forest fire prediction (will need better data that is free).
4. Realestate prices (data is private I beleive).
5. Ocean currents & jetstream behaviour (should be able to find some data for this) - it would be interesting to see if an RN is able to extrapolate the effects of global warming based on a huge amount of historical data, I'll put $10.00 on it being close.
6. Resturaunt industry (predicting the busy nights...we're pretty bad at it currently).
7. Traffic patterns (link with CNN's and traffic camera data maybe).
8. Algorithmic trading stuff (not tellin!!).



#### Introduction to Relational Networks 

RNs are structured to learn or infer relationships between unique objects in a system - i.e. they learn the rules governing interactions between objects in a system. Basically, RNs are a system of stacked, inter-connected multilayered perceptrons that are much less sensitive to hyperparameter selection. Results indicate they are more robust and broadly generalizable to a variety of applications such as weather forecasting. Furthermore, they can easily be used in unison with any type of previously developed Neural Network model (as shown in [examples](examples)).


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








