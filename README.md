# Leveraging Twitter to Map Natural Disasters **In Progress**
Project by: Garrett Bradley, Ishan Deulkar, and Cory Rutkowski

## Problem Statement

During a Natural Disaster how can we utilize Social Media to help locate specific areas that require immediate assistance?
During any natural disaster one of the first areas of focus should be on rescuing people in need of immediate assistance. However, due to the nature of these events this isn't always easily possible. This can be due to downed power and phone lines which make communicationn near impossible at times. We set out to try to utilize social media, specifically Twitter, to see if its user's tweets can better help inform emergency responders of where to focus their rescue efforts.

## Executive Summary


### Goals:

The goals of our project were to be able to collect a large amount of tweets relating to a certain natural disaster (in our specific case, Hurricane Harvey in 2017) and see if user's tweets could help inform emergency responders of specific areas to focus on during a true emergency situation. Using these tweets we wanted to map rescue requests in order to allow rescue coordinators to use our map to strategize and implement their best tactics on where to focus their search and rescue efforts.


### Methodology:

In order to complete our goal we followed several steps. 
First, we compiled tweets related to Hurricane Harvey during the time period of August 17, 2017 - September 9, 2017 into a pandas DataFrame. These tweets were to be analyzed for emergency requests and then mapped.
We needed to create a model in order to be able to categorize our tweets as either 'Emergency' or 'Non-Emergency' related. We used a pre-made dataset from figure-eight.com that already classified tweets into various emergency related categories to train our model.
Once our model was successfully trained, we ran it on our Hurricane Harvey tweets dataset to pull out all of the 'Emergency' tweets.
Next we used an a function to analyze our 'Emergency' related tweets, looking for those related to requests for aid/assistance, to focus on those tweets containing a physical address in the body of the text. Using these addresses, we converted them in to Latitude and Longitude coordinates and then visualized each tweet onto a Houston based map. Our goal was for rescue coordiators to be able to use this map to strategize and implement their best tactics on where to focus their rescue efforts.


### Data:

Data for our project was collected from several different sources. 
Our data for training our Emergency Classification model was taken from a dataset from the Multilingual Disaster Response Messages page on the figure-eight.com website.
Our actual testing data used for tweet mapping was collected from two sources:
- Kaggle: This dataset of tweets collected during the time of Hurricane Harvey and arranged into a Kaggle dataset by Kaggle user: Dan (https://www.kaggle.com/dan195)
- NTU: Our other dataset of tweets came from Mark Edward Phillips at the University of North Texas. He collected Hurricane Harvey tweets as well and was kind enough to allow us access to them for the purposes of this project. (https://digital.library.unt.edu/ark:/67531/metadc993940/: accessed January 29, 2018, University of North Texas Libraries, Digital Library,digital.library.unt.edu)

Once all of the data was collected and imported into pandas it was cleaned. There were only ~1% of null values in the dataset, so those were dropped. In checking for duplicate tweets, it was discovered that there were nearly 200,000 duplicate tweets so those were removed as well.
After all of the pre-processing was complete we had a dataset containing 267,682 Tweets.


#### Data Dictionary

|Feature|Type|Description|
|---|---|---|
|date|datetime|The date the tweet was created.| 
|id|object|The unique id of the tweet| 
|tweet|object|The body text of the tweet|  


### Model: 
Our modeling process was broken into two main steps. First we had to create a classification model that would classify tweets as either 'Emergency' related or'Non-Emergency' related. Once this was accomplished, we then fed the 'Emergency' related tweets into another function to pull out any specific addresses mentioned within the tweet body. These addresses are what we used to be able to map all of the rescue request tweets.

#### Emergency Classification Model
3 different models were created for this project:
1. CountVectorizer and Random Forests
2. CountVectorizer and Naive Bayes
3. CountVectorizer and Support Vector Machines

We utilized a GridSearchCV to generate optimal parameters for our models. The min_df was set at 2 so that rare words that occured in only one tweet would be excluded. We excluded stop-words from our models to decrease noise. We used a ______ function to pass through the CountVectorizer to focus just on the roots of the words.

Best model features:

1. CountVectorizer and Random Forests
- max_features = 
- ngram_range = ()
- stop_words = stop_words
- max_depth = 
- min_samples_leaf = 
- min_samples_split = 
- n_estimators =   

2. CountVectorizer and Naive Bayes
- max_features = 
- ngram_range = ()
- stop_words = stop_words
    

3. CountVectorizer and Support Vector Machines
- max_features = 
- ngram_range = ()
- stop_words = stop_words
                  

#### Model Scores

Baseline accuracy for the dataset was ______%

1. CountVectorizer and Random Forests - accuracy score of  
2. CountVectorizer and Support Vector Machines - accuracy score of 
3. CountVectorizer and Naive Bayes - accuracy score of 

Our best classification model is CountVectorizer and . 

#### Address Model

Once we sorted our tweets into 'Emergency' related, we then needed to collect of the physical addresses contained within the tweets. Using Google Maps API we created a database of all street names within the Houston area. Using a combination of methods, we were able to pull out the physical street and street number address from specific tweets. We did this via:
- Pre-built Address parsing tools 
- Manual regexp & string manipulation 
- Cross referencing addresses against known street names
- Passing partial addresses into multiple geocoders for validation
This allowed us to then translate these addresses into Latitude and Longitude coordinates for mapping.


### Mapping:

Using all of the Lat. and Long. coordinates we marked them all on a map using Google Maps and the Folium visualization library in python to help notify rescue teams which areas required assistance. 

#### Example 1:
![Screenshot](https://github.com/)

#### Example 2:
![Screenshot](https://github.com/)


### Constraints/Limitations

Twitter’s free API will only allow you to scrape the past 7 days worth of tweets. Location data for  tweets is very hard to find due to the majority of users not turning the feature on as well as Twitter removing this feature recently. This causes a major challenge when trying to come up with user's locations if they don't specify the address directly in the tweet.

For the address verification, address street name length presents a challenge. It is easy to match up single word street names (ie Oak St or Jade Blvd) but names with more than two words or a cardinal direction tended to cause additional problems for our functions (ie Palm Harbor Drive or E Oak Street).


### Conclusions and Recommendations:

Based on our results this project is something that could be implemented into future rescue operations with some additional added features/changes. For different locations affected by a natural disaster, we would need to either have beforehand, or soon after the disaster occurs, create a database of city street names for our function to reference.


### Next Steps

There were several areas that we wanted to improve on:

__Model Date and Time:__ Incorporating time into our model would allow for even more up to date information for the disaster relief teams to be able to utilize to a more effective degree.
__Map Interactions:__ Adding additional interactive features to our maps, such as being able to see the specific tweet for each coordinate.
__Additional Applications:__ Expand this into a functioning mobile/web application would allow for more features and resources to be available to the rescue organizations.
__Specialized Hashtag:__ For every natural disaster, having FEMA/other disaster relief organizations work with Twitter directly to create a specific hashtag related to emergency related tweets. This way anyone who needs immediate assistance can include this hashtag in their tweets and it would make it much easier for the model to be able to sort tweets looking for this specific hashtag.
__Other Social Media:__ Expanding this model to look at information coming from different forms of social media (Snapchat, Instagram) would allow additional resources for people in need to reach out for help.
__Database Creation:__ Having pre-made street/address databases for as many cities as possible before the disaster occurs would greatly decrease the amount of time required to process all of the necessary information in order to generate our disaster map.


### Slides

You can view the [presentation slides](https://docs.google.com/presentation/d/10ZApvLVwmNZgL5VeSmSjSGsa6tB28ApVWLPaOXeqW7s/edit?usp=sharing)

### References

- [Geolocational Tweet Information](https://codete.com/blog/observing-world-tweeting-tendencies-in-real-time-part-2/)
- [Twitter Removing Geolocational Information as a Feature](https://www.niemanlab.org/2019/06/twitter-is-turning-off-location-data-on-tweets-a-small-win-for-privacy-but-a-small-loss-for-journalists-and-researchers/)
- [Kaggle Hurricane Harvey Tweets Dataset](https://www.kaggle.com/dan195/hurricaneharvey)
- [NTU Hurricane Harvey Tweets Dataset](Phillips, Mark Edward. Hurricane Harvey Twitter Dataset, dataset, 2017-08-18/2017-09-22; https://digital.library.unt.edu/ark:/67531/metadc993940/: accessed January 29, 2018, University of North Texas Libraries, Digital Library,digital.library.unt.edu)
- [Model Training Dataset](https://www.figure-eight.com/dataset/combined-disaster-response-data/)

