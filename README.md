# PyLation - Relational Network (RN) for Keras

'pip install pylation'

## This Project
This code was initially written for [Dr. Brian Jackel](http://contacts.ucalgary.ca/info/phas/profiles/486-146343) at the University of Calgary [Department of Physics and Astronomy](https://phas.ucalgary.ca/) (with funding provided by the [Canadian Space Agency](http://www.asc-csa.gc.ca/eng/Default.asp)). Brian had me spend most of 2017 working on Neural Network (NN) based forecasting methods with the purpose of applying them towards forecasting space weather - which is known (in extreme cases) to cause severe damage to Earth-based technology, especially at higher latitudes. We used data from ~100 magnetometers stationed throughout Northern Canada as well as the OMNI solar wind data from NASA. Several pages are needed for full specs on the management and filtering of the years of (sometimes painfully) inconsistent data, but I won't get into that here - instead, I'll be posting a script that should do everything from pull the data to filter all the NaNs and properly shape the arrays for use with Relational Networks (RN's)...but it might take a few more weeks to polish up. (click [here](https://arxiv.org/pdf/1706.01427.pdf) for the original paper on RN's from DeepMind). 

In a nutshell, the final script (not yet posted here) has the ability to forcast the approximate distribution of magnetic field flux between t<sub>0</sub>+1hr and t<sub>0</sub>+2hr based off data between t<sub>0</sub>-1hr and t<sub>0</sub>. Most importantly, it is trained in such a way to forecast at arbitrary lat/long coordinates (within a range of course - i.e, you can't predict the flux in China based off data from Canada but you can predict the flux in British Columbia based off data from Alberta). The model is far from perfect and I'm positive that it could be quite easily improved by someone with some more expertise. Click [here](https://youtu.be/_Vd5kf4zBtg) for a hacky animation on some of the results (I made it for my own research purposes and wasn't really planning on showing it off, but I lost the script that made it, so this is as good as it'll get for the time being).


### Some potential applications for Relational Networks
PyLation is easily linked with other Keras layers (LSTM, Dense, CNN etc.), which makes life pretty easy for those in predictive analytics! To attract your attention, below are a few things this package (or likely a better version of it) **might** be applicable to. Fyi: please feel free to attempt any of these and keep me posted...if it works we'll try and get it into production for you (it can be a lonely difficult time trying to get something into production, especially when seeking trustworthy business partners).

1. Weather forecasting: Pretty well known field, but industry standard is spotty, especially close to mountain ranges. For example, in Calgary, Alberta we are basically told it will most likely be pretty cold, but there is also a chance of it being pretty warm, as well as a chance that it might be quite windy. Essentially, forecasting methods in highly variable climates have large margins of error - something not always appreciated by those in more temperate regions.
2. Habitable planet detection: Already being attempted with NN's I'm sure, but it would be very cool to spend time on, if not overly profitable - likely need high precision machines and all the data that is available.
3. Wildfire prediction: British Columbia & California ---> there will be a desperate need in the coming decades. Likely will need autonomous weather surveillance stations, terabytes of overhead imagery, thousands of cheap but well placed moisture monitors, and historical wildfire data, all of this is inexpensive relative to the damages caused by fires. Unfortunately, due to the differences in geography, the regional systems will require customization, meaning it should be collaberative between locations in the world that are experiencing these very costly wildfires -> This might already be in the works, it's hard to know, but Relational Networks will help out.
4. Realestate prices: Pretty easy, but new data is hard (and probably $$$$) to find.
5. Ocean currents & jetstream behaviour (should be able to find some data for this) - it would be interesting to see if an RN is able to extrapolate the effects of climate change based on a huge amount of historical data from various sources, I'll wager on it outperforming current models.
6. Service Industry: You could monitor in-house customer service standards based off a number of easily collected variables -> for example, in a resturaunt, each table would need a small camera directed at it (not the customer, but the food) to collect live data on everything from rate of consumption, remaining quantities, as well as customer preferences (sign in via app upon arrival??). A Relational Network should be able to tie it all together and simply notify the staff. Example:

 "TABLE-88;   SEAT-03;   DETECTED-Credit Card on table + food half finished;       SOLUTION-Payment machine + take-out box"
 "TABLE-05;   SEAT-02;   DETECTED-Water empty + food delivered + cutlery on floor; SOLUTION-Water jug + new cutlery"
 "TABLE-12;   SEAT-03;   DETECTED-Beer full + food complete;                       SOLUTION-Desert Menu + clearing tray"

This could all be done with open source software, and it could be done much easier than training a car to drive itself. Service standards could be nearly flawless and the continuous anxiety for those working within the service industry would be much more manageable...trust me, when you have to serve 10 tables at once your "to-do list" is a complete nightmare, and one mistake can lead to a customer deciding to write an email to your boss about the "idiotic server who forgot the beer for 4 minutes"....

Just hire more staff you say? Minimum wage increase doesn't allow for that. Grinds my gears.

7. Traffic patterns: Link with CNN's and traffic camera data maybe...my guess is this is well researched and optimized already, but you never know.

8. Financial fraud detection: Pretty basic math really. Will be especially relevant (and applicable) to the blockchain and much easier to implement than in banks or large coorporations who use the now very dated "wire transfer system". Unless they adopt blockchain...which they will - but from what I hear even just adopting a new insurance provider in a large corporation is a mess. Imagine saying; "we no longer accept wire transfers...", there would be one or two complaints. 

8. Algorithmic trading stuff: Not tellin!!


#### Introduction to Relational Networks 

RNs are structured to learn or infer relationships between unique objects in a system - i.e. they learn the rules governing interactions between objects in a system. Basically, RNs are a system of stacked, inter-connected multilayered perceptrons that are much less sensitive to hyperparameter selection. Results indicate they are more robust and broadly generalizable to a variety of applications. Furthermore, they can easily be used in unison with any type of previously developed Neural Network model. While LSTM's are known for natural language processing and CNN's for image classification, RN's should be known for their ability to learn the physics governing the behaviour of a system.

Over the past year I was able to hack PyLation together (hack is an understatement), and it actually turned out fairly well. For those of you familiar with Keras, using this package will come quite naturally. Instead of having to define the hyperparameters for every single layer, I've modified things slightly to generalize all the hyperparameters to a set of easily modifiable python dictionaries (see examples or the in-code documentation). Also, there's a brief animation on how Relational Networks operate on input data in general [here](https://youtu.be/ZlUcn1TAMlA). It isn't a very descriptive animation if you're hoping to learn the math, but not bad for visualizing how the data flows through the network.

On a related note: If you really want to get your head wrapped around how Relational Networks function, you absolutely need to be familiar with the more fundamental neural networks. You should be able to use LSTM's for LSTM problems, CNN's for CNN problems, MLP's for MLP problems etc. Don't just familiarize yourself with the theory; spend time on hyperparameter optimization, GPU-based computations - rent a cheap AWS server and pay by the hour then terminate it when you are done for the day (I worked full time for months doing this and spent less than $200.00 total), try and familiarize yourself with server computations, then use keras-gpu from anaconda. There are GREAT examples available on the keras git repository, refer to them but don't just copy and paste them...you'll never learn that way. 

Oh, and like any efficient data scientist, expect to spend about 90% of your time on Google, about 9.9999% of your time debugging your scripts and the remaining 0.0001% of your time zoned out as your network fails to train properly. Just be patient. Very patient. Basically, if you are able to wrap your head around RN's in less then a month or two you should fly out to Calgary and come work for me (cough...algorithmic trading...cough cough...for now...cough cough) or fly out to Calgary and we'll show you how to get set up on your own - in the data science industry there's more profit to be made by all working **honestly** together, but only if you know what you're doing. One request: spend some time in Calgary, the oil and gas industry gave us a bad reputation in some of the more progressive locales from what I understand. But it's a great city with great people...with some conveniently cheap (and recently vacated) office space - as well as equally convenient and cheap apartment rentals. Furthermore, the University of Calgary is quickly becoming a world class institution...you might as well join the party.

## Getting Started

#### Deep Learning

Deep learning is an intimidating subject to invest time in - everyone learns at a different pace and there is no guarantee how long before you start seeing positive returns on your time. My best advice is to be very patient with yourself, if this were an easy subject everyone would already know it. Fortunately, the complexity of this field - coupled with fairly recent advancements in GPU computation technology - has made deep learning ripe with opportunity.

#### GPU Computations/Amazon Web Services

If you are unfamiliar with Amazon Web Services (AWS), please spend some time on google. AWS offers some very helpful tutorials, so I will not go into too much depth here, but the prices are modest and the security is very trustworthy.

#### Installing PyLation

Pretty simple installation. I recommend setting up an anaconda virtual environment on an AWS server Ubuntu image that has GPU compute capabilities already installed. Once that is all set up, PyLation can be found on PyPi: **"pip install pylation"**. You might also need to install keras-gpu. **"conda install keras-gpu"** should do the trick. I don't think I'm missing any other dependancies, but if I am it will be obvious. 

Alternatively, just pull this directory onto your machine and keep all your scripts in it. Should work, let me know if it doesn't. 


## About the Author
Braden Heffernan:

Physicist/Bartender born and raised in Calgary, Alberta. Graduated in 2016 then worked for Brian Jackel at the University of Calgary for most of 2017. Recently founded Vulpine Intelligence Inc - we are a small team of 3 physicists (1 space, 1 nuclear, 1 astro), an electrical engineer, and a mathmetician. For the past few months (w.r.t March 2018) we have been developing some pretty neat algorithmic trading software...I'm actually writing this as we're doing some beta tests (results look good, so that's exciting). We're always looking for new talent and we're not too fussy about your educational background (some math and computer science is pretty necessary though). Drop me a message on Facebook and I'll try to respond as quickly as possible. Happy to answer any questions or comments. 

If you feel like donating to help keep this maintained....

BTC: 32F641D45BU5yycpGdzTzwe27hDenVt1DC

ETH: 0x159F4489cb36b76f4CA2ed78C9439A60F5a1193c


## Thanks









