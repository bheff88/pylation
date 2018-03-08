# PyLation - Relational Network (RN) for Keras
Note: I will probably not have time to maintain this package, so anyone who can take over should feel free...I wouldn't mind a small amount of credit if you find this repository helpful. 

'pip install pylation'

## This Project
This code was initially written for [Dr. Brian Jackel](http://contacts.ucalgary.ca/info/phas/profiles/486-146343) at the University of Calgary [Department of Physics and Astronomy](https://phas.ucalgary.ca/) (with funding provided by the Canadian Space Agency). Brian had me spend most of 2017 working on Neural Network (NN) based forecasting methods with the purpose of applying them towards forecasting space weather - which is known (in extreme cases) to cause severe damage to Earth-based technology, especially at higher latitudes. We used data from ~100 magnetometers stationed throughout northern Canada as well as the OMNI solar wind data from NASA. Several pages are needed for full specs on the management and filtering of the years of (sometimes painfully) inconsistent data, but I won't get into specifics here - instead, I'll be posting a script that should do everything from pull the data to filter all the NaNs and properly shape the arrays for use with Relational Networks (RN's)...but it might take a few more weeks to polish up. (click [here](https://arxiv.org/pdf/1706.01427.pdf) for the original paper on RN's from DeepMind). 

In a nutshell, the final script (not yet posted here, and the training set is pretty big) has the ability to forcast the approximate distribution of magnetic field flux between t0+1hr and t0+2hr based off data between t0-1hr and t0. Most importantly, it is trained in such a way to forecast at arbitrary lat/long coordinates (within a range of course - i.e, you can't predict the flux in China based off data from Canada but you can predict the flux in British Columbia based off data from Alberta). The model is far from perfect and I'm positive that it could be quite easily improved by someone who actually knows what they're doing.


### Some potential applications for Relational Networks
PyLation is easily linked with other Keras layers (LSTM, Dense, CNN etc.), which makes life pretty easy for those in predictive analytics! To attract your attention, below are a few things this package (or likely a better version of it) **might** be applicable to. Fyi: these are just from brainstorming as I type, so please feel free to attempt and keep me posted...if it works we'll try and get it into production for you (for a small % of your profit of course).

1. Weather forecasting (pretty well known field, but industry standard is pretty spotty, especially close to mountain ranges or large bodies of water).
2. Habitable planet detection (would be pretty cool to work on, if not overly profitable).
3. Forest fire prediction (British Columbia & California ---> desperate need in the coming decades).
4. Realestate prices (pretty easy, but new data is hard to find).
5. Ocean currents & jetstream behaviour (should be able to find some data for this) - it would be interesting to see if an RN is able to extrapolate the effects of climate change based on a huge amount of historical data, I'll bet $100.00 on it beating current models.
6. Resturaunt industry (predicting the busy nights...we're pretty bad at it currently, and minimum wage is about to go up again in Alberta).
7. Traffic patterns (link with CNN's and traffic camera data maybe).
8. Algorithmic trading stuff (not tellin!!).


#### Introduction to Relational Networks 

RNs are structured to learn or infer relationships between unique objects in a system - i.e. they learn the rules governing interactions between objects in a system. Basically, RNs are a system of stacked, inter-connected multilayered perceptrons that are much less sensitive to hyperparameter selection. Results indicate they are more robust and broadly generalizable to a variety of applications. Furthermore, they can easily be used in unison with any type of previously developed Neural Network model. While LSTM's are known for natural language processing and CNN's for image classification, RN's should be known for their ability to learn the physics governing the behaviour of a system.

Over the past year I was able to hack PyLation together (hack is an understatement), and it actually turned out fairly well. For those of you familiar with Keras, using this package will come quite naturally. Instead of having to define the hyperparameters for every single layer, I've modified things slightly to generalize all the hyperparameters to a set of easily modifiable python dictionaries (see examples or the in-code documentation). Also, there's a brief animation on how Relational Networks operate on input data in general [here](https://www.youtube.com/edit?o=U&video_id=ZlUcn1TAMlA). It isn't a very descriptive animation if you're hoping to learn the math, but not bad for visualizing how the data flows through the network.

On a related note: If you really want to get your head wrapped around how Relational Networks function, you absolutely need to be familiar with the more fundamental neural networks. You should be able to use LSTM's for LSTM problems, CNN's for CNN problems, MLP's for MLP problems etc. Don't just familiarize yourself with the theory; spend time on hyperparameter optimization, GPU-based computations - rent a cheap AWS server and pay by the hour then terminate it when you are done for the day (I worked full time for months doing this and spent less than $200.00 total), try and familiarize yourself with server computations, then use keras-gpu from anaconda. There are GREAT examples available on the keras git repository, refer to them but don't just copy and paste them...you'll never learn that way. 

Oh, and like any efficient data scientist, expect to spend about 90% of your time on Google, about 9.9999% of your time debugging your scripts and the remaining 0.0001% of your time zoned out as your network fails to train properly. Just be patient. Very patient. Basically, if you are able to wrap your head around RN's in less then a month or two you should fly out to Calgary and come work for me (cough...algorithmic trading...cough cough...for now...cough cough) or fly out to Calgary and we'll show you how to get set up on your own - in the data science industry there's more profit to be made **honestly** if you know what you're doing. One request: spend some time in Calgary, the oil and gas industry gave us a bad reputation in some of the more progressive locales from what I understand. But it's a great city with great people...and some conveniently cheap (and recently vacated) office space - as well as equally convenient and cheap apartment rentals. Furthermore, the University of Calgary is quickly becoming a world class institution...you might as well join the party.

## Getting Started

#### Deep Learning

Deep learning is an intimidating subject to invest time in - everyone learns at a different pace and there is no guarantee how long before you start seeing positive returns on your time. My best advice is to be very patient with yourself, if this were an easy subject everyone would already know it. Fortunately, the complexity of this field - coupled with fairly recent advancements in GPU computation technology - has made deep learning ripe with opportunity.


#### GPU Computations/Amazon Web Services

If you are unfamiliar with Amazon Web Services (AWS), please spend some time on google. AWS offers some very helpful tutorials, so I will not go into too much depth here, but the prices are modest and the security is very trustworthy.








