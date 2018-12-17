# PyLation - Relational Network (RN) for Keras

'pip install pylation'

## This Project
This code was initially written for [Dr. Brian Jackel](http://contacts.ucalgary.ca/info/phas/profiles/486-146343) at the University of Calgary [Department of Physics and Astronomy](https://phas.ucalgary.ca/) (with funding provided by the [Canadian Space Agency](http://www.asc-csa.gc.ca/eng/Default.asp)). Brian had me spend most of 2017 working on Neural Network (NN) based forecasting methods with the purpose of applying them towards forecasting space weather - which is known (in extreme cases) to cause severe damage to Earth-based technology, especially at higher latitudes. We used data from ~100 magnetometers stationed throughout Northern Canada as well as the OMNI solar wind data from NASA. Several pages are needed for full specs on the management and filtering of the years of (sometimes painfully) inconsistent data, but I won't get into that here. Click [here](https://arxiv.org/pdf/1706.01427.pdf) for the original paper on RN's from DeepMind. 

In a nutshell, the final script (not yet posted here) has the ability to forcast the approximate distribution of magnetic field flux between t<sub>0</sub>+1hr and t<sub>0</sub>+2hr based off data between t<sub>0</sub>-1hr and t<sub>0</sub>. Most importantly, it is trained in such a way to forecast at arbitrary lat/long coordinates (within a range of course - i.e, you can't predict the flux in China based off data from Canada but you can predict the flux in British Columbia based off data from Alberta). The model is far from perfect and I'm positive that it could be quite easily improved by someone with some more expertise. Click [here](https://youtu.be/_Vd5kf4zBtg) for a hacky animation on some of the results (I made it for my own research purposes and wasn't really planning on showing it off, but I lost the script that made it, so this is as good as it'll get for the time being).


### Some potential applications for Relational Networks
PyLation is easily linked with other Keras layers (LSTM, Dense, CNN etc.), which makes life pretty easy for those in predictive analytics.

1. Weather forecasting: Pretty well known field, but industry standard is spotty, especially close to mountain ranges.
2. Wildfire prediction: British Columbia & California
3. Realestate prices: Pretty easy, but new data is hard (and probably $$$$) to find.
4. Traffic patterns: Link with CNN's and traffic camera data maybe...my guess is this is well researched and optimized already, but you never know.
5. Financial fraud detection
6. Trading & Stock Forecasting

#### Introduction to Relational Networks 

RNs are structured to learn or infer relationships between unique objects in a system - i.e. they learn the rules governing interactions between objects in a system. Basically, RNs are a system of stacked, inter-connected multilayered perceptrons that are much less sensitive to hyperparameter selection. Results indicate they are more robust and broadly generalizable to a variety of applications. Furthermore, they can easily be used in unison with any type of previously developed Neural Network model. While LSTM's are known for natural language processing and CNN's for image classification, RN's should be known for their ability to learn the physics governing the behaviour of a system.

On a related note: If you really want to get your head wrapped around how Relational Networks function, you absolutely need to be familiar with the more fundamental neural networks. You should be able to use LSTM's for LSTM problems, CNN's for CNN problems, MLP's for MLP problems etc. Don't just familiarize yourself with the theory; spend time on hyperparameter optimization, GPU-based computations - rent a cheap AWS server and pay by the hour then terminate it when you are done for the day (I worked full time for months doing this and spent less than $200.00 total), try and familiarize yourself with server computations, then use keras-gpu from anaconda. There are GREAT examples available on the keras git repository, refer to them but don't just copy and paste them...you'll never learn that way. 


## Getting Started

#### Deep Learning

Deep learning is an intimidating subject to invest time in - everyone learns at a different pace and there is no guarantee how long before you start seeing positive returns on your time. My best advice is to be very patient with yourself, if this were an easy subject everyone would already know it. Fortunately, the complexity of this field - coupled with fairly recent advancements in GPU computation technology - has made deep learning ripe with opportunity.

#### GPU Computations/Amazon Web Services

If you are unfamiliar with Amazon Web Services (AWS), please spend some time on google. AWS offers some very helpful tutorials, so I will not go into too much depth here, but the prices are modest and the security is very trustworthy.

#### Installing PyLation

Pretty simple installation. I recommend setting up an anaconda virtual environment on an AWS server Ubuntu image that has GPU compute capabilities already installed. Once that is all set up, PyLation can be found on PyPi: **"pip install pylation"**. You might also need to install keras-gpu. **"conda install keras-gpu"** should do the trick. I don't think I'm missing any other dependancies, but if I am it will be obvious. 

Alternatively, just pull this directory onto your machine and keep all your scripts in it. Should work, let me know if it doesn't. 









