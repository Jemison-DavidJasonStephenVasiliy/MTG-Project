![Header](https://media.magic.wizards.com/images/wallpaper/Wallpaper_PristineAngel_1280x960.jpg)
## Table of Contents
1. About the Project  
[Goals](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#goals) | [Background](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#background) | [The Data](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#the-data) | [Deliverables](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#deliverables) | [Outline](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#project-outline)  

2. Data Dictionary  
[Original Features](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#original-features) | [Engineered Features](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#engineered-features)  

3. Initial Thoughts & Hypotheses  
[Thoughts](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#thoughts) | [Hypotheses](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#hypotheses)  

4. Project Steps  
[Acquire](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#acquire) | [Prepare](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#prepare) | [Explore](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#explore) | [Model](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#model) | [Conclusions](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#conclusions)  

5. How to Reproduce & More  
[Steps](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#steps) | [Tools & Requirements](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#tools--requirements) | [License](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#License) | [Creators](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#Creators)

## About the Project
What makes a magic card valuable?. You can check out our presentation [here](https://www.canva.com/design/DAFHo-H72x8/kxxQCPwFWXkUekQowv5xvg/view?utm_content=DAFHo-H72x8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink).

### Goals
- Build a dataset of cards using Scryfall's API
- Identify the drivers of card prices
- Create a regression model to predict the price of a card that has an RMSE lower than the baseline

### Background
What makes a card valuable? According to MTGGoldfish News [here](https://www.mtggoldfish.com/articles),
>    "Determining a collectible cards value is not necessarily a straight forward affair.  Often a cards popularity is affected by 
> the design of the card or the desirability of the art itself from esteemed artists."  

By analyzing Scryfall's API data, we will determine what influences a card's value.

### The Data 
Our dataset came from a Scryfall.com and TCGPlayer.com. It includes over 20,000 cards in the collectible card game from the 90s to today. 


### Deliverables
- Video presentation
- Presentation slides via Canva [here](https://www.canva.com/design/DAFHo-H72x8/kxxQCPwFWXkUekQowv5xvg/view?utm_content=DAFHo-H72x8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)  
- Tableau Storybook [here]()
- GitHub repository with analysis

### Project Outline
The files within the repository are organized as follows. The /images and /sandbox contents are not necessary for reproduction.  
![Outline](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/blob/main/images/Outline.png?raw=true)

### Timeline
- [X] Project Planning: July 27th
- [X] Aquisition and Prep: July 28th
- [X] Exploration: December 14th
- [X] Modeling: December 15th
- [X] Finalize Minimum Viable Product (MVP): EOD December 15th
- [X] Improve/Iterate MVP: December 17th
- [X] Finalize Presentation: December 31st

### Acknowledgments


<kbd>[Back to Table of Contents](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#table-of-contents)</kbd>

## Data Dictionary
### Original Features
Below are the features included in the orginal data acquired from the Scryfall API.  


PROPERTY	TYPE	ATN	DETAILS
id	UUID		A unique ID for this bulk item.
uri	URI		The Scryfall API URI for this file.
type	String		A computer-readable string for the kind of bulk item.
name	String		A human-readable name for this file.
description	String		A human-readable description for this file.
download_uri	URI		The URI that hosts this bulk file for fetching.
updated_at	Timestamp		The time when this file was last updated.
compressed_size	Integer		The size of this file in integer bytes.
content_type	MIME Type		The MIME type of this file.
content_encoding	Encoding		The Content-Encoding encoding that will be used to transmit this file when you download it.
| Feature         | Data Type | Description                                                                                 |
|-----------------|-----------|---------------------------------------------------------------------------------------------|
| id              | UUID      | A unique ID for this bulk item.                                                             |
| uri             | URI       | The Scryfall API URI for this file.                                                         |
| type            | String    | A computer-readable string for the kind of bulk item.                                       |
| name            | String    | A human-readable name for this file.                                                        |
| description     | String    | A human-readable description for this file.                                                 |
| download_uri    | URI       | The URI that hosts this bulk file for fetching.                                             |
| updated_at      | Timestamp | The time when this file was last updated.                                                   |
| compressed_size | Integer   | The size of this file in integer bytes.                                                     |
| content_type    | MIME Type | The MIME type of this file.                                                                 |
| content_encoding| Encoding  | The Content-Encoding encoding that will be used to transmit this file when you download it. |
|                 |           |
|                 |           |
|                 |           |
|                 |           |
|                 |           |
|                 |           |
|                 |           |
|                 |           |
|                 |           |

### Engineered Features
Using domain knowledge and exploration insights, we also engineered features using the original data. These created features are below.  
| Feature Name             | Description                                                                                                |
|--------------------------|------------------------------------------------------------------------------------------------------------|
|                          |                                                                                                            |
|                          |                                                                                                            |
|                          |                                                                                                            |
|                          |                                                                                                            |
|                          |                                                                                                            |
|                          |                                                                                                            |

<kbd>[Back to Table of Contents](https://github.com/SpotiScryers/SpotiScry#table-of-contents)</kbd>
## Initial Thoughts & Hypotheses
### Thoughts
* What are the drivers of popularity on Spotify?
* Is there a seasonality to the popularity of tracks?
* Are originals or remixes more popular?
* Since 2020 has been the year of the pandemic, are more people listening to sad songs right now?
* Are people's musical tastes expanding or experimenting due to the "new normal" of stay-at-home culture?
* Does loudness have a relationship with popularity?
* Does the instrumental-to-lyrical ratio of a track have an effect on its popularity?

### Hypotheses

𝐻0: Mean of song popularity of explicit tracks = Mean of song popularity of non-explicit tracks<br>
𝐻𝑎: Mean of song popularity of explicit tracks > Mean of song popularity of non-explicit tracks

𝐻0: Mean of popularity of major key songs =< Mean of popularity of minor key songs<br>
𝐻𝑎: Mean of popularity of major key songs > Mean of popularity of minor key songs

𝐻0: Mean of popularity of time signature 4 =< Mean of popularity of all songs<br>
𝐻𝑎: Mean of popularity of time signature 4 > Mean of popularity of all songs

𝐻0: There is no linear relationship between song length and popularity.<br>
𝐻𝑎: There is a linear relationship between song length and popularity.

𝐻0: There is no linear relationship between liveness and popularity.<br>
𝐻𝑎: There is a linear relationship between liveness and popularity.

𝐻0: There is no difference in popularity between tracks released by the top 10 labels or not.<br>
𝐻𝑎: Tracks released by the top 10 labels are more likely to be popular.

𝐻0: There is no difference in popularity between tracks released by the worst 5 labels or not.<br>
𝐻𝑎: Tracks released by the worst 5 labels are more likely to be unpopular.

𝐻0: there is no difference between songs released in 2020 popularity and the overall average.<br>
𝐻𝑎: there is a difference between songs released in 2020 popularity and the overall average.

<kbd>[Back to Table of Contents](https://github.com/SpotiScryers/SpotiScry#table-of-contents)</kbd>
## Project Steps
### Acquire
Data was acquired from Spotify API using the spotipy library. Going to this website https://developer.spotify.com/dashboard/login let us create a spotify web app that gave us a client id and client secret. This allowed us to use the create_spotipy_client function to create our own spotipy client that could access the API.  
![Acquire-Visual](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/blob/main/images/aquisition.png?raw=true)

The dataframe is saved as a csv file and has around 5900 observations, otherwise in the acquire.py file there is function for grabbing the entire capstone playlist as well as a function for acquiring any additional playlists should you choose. There are 24 columns in the original data frame, this ranges from track and album metadata to audio features for that track. There are very few nulls which have been marked as null in the data acquisition function for ease of removal later in prepare.
### Prepare
Functions to prepare the dataframe are stored in two seperate files depending on their purpose, prepare.py and preprocessing.py:  

**prepare.py:** Functions for cleaning and ordering data
* release dates that only specify the year are set to '01-01' for month and day
* nulls are dropped
* set track id to index
* change dtypes to correct type
* fix tempos
    * From Kwame: "As a hip-hop artist and producer, I know firsthand how BPM (beats per minute, aka the tempo of a song) can often be miscalculated as twice their actual value. This is because most song tempos fall in-between 90 and 160 BPM, and a computer can wrongly detect tempo as double-time in slower tempos below 90. There are some genres that have faster BPM, such as 170 to 190 for Drum ’n’ Bass, however, in Hip-Hop I’ve found that the BPM is wrongly miscalculated in this way when it’s shown as 170 and above. Therefore, in our data, I chose to halve the tempos of all tracks with 170 BPM or greater for a more accurate look at tempo."

**preprocessing.py:** Functions for adding features we found interesting / modyifying data for ease of use in exploration
* convert track length from ms to seconds & minutes
* lowercase artist, album, and track name
* create column for year, month, and day for release date
* bin release year by decade

### Explore
During exploration we looked at these features:
* if a track is explicit
* liveness
* song length
* time signature
* key
* loudness
* original vs remix
* instrumentalness
* danceability

![Subgenre Popularity](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/blob/main/images/Genre_with_Title.png?raw=true)

![Popular Tempos](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/blob/main/images/Tempo_with_Title.png?raw=true)

![Popular Key Signatures](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/blob/main/images/Key_with_Title.png?raw=true)

### Model
First we made a baseline model to compare our model performances. The baseline was based on the average popularity for a track in our train split, which means our baseline prediction came out to a popularity of 38. The baseline model had an RMSE of 22.8 on the train split. We created various regression models and fit to the train data.  

**Feature Groups**
We used three sets of feauture groups. 
- Select K best: selects features according to the k highest scores (top 5)
- Recursive Feature Elimination: features that perform best on a simple linear regression model (top 5)
- Combination (unique features from both groups, 7 features)

**Models Evaluated**
* OLS Linear Regression
* LASSO + LARS
* Polynomial Squared + Linear Regression
* Support Vector Regression using RBF Kernel
* General Linear Model with Normal Distribution

**Evaluation Metric**  
Models are evaluated by calculating the root mean squared error (RMSE) or residual of the predicted value to the actual observation. The smaller the RMSE, the better the model performed. A visual of this error is below.  
![Model-Error](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/blob/main/images/model_error.png?raw=true)

**Final Model:**  
Polynomial Squared + Linear Regression was our final model we performed on test, predicting 6% better than the baseline.  

| Model                         | Train RMSE | Validate RMSE | Test RMSE |
|-------------------------------|------------|---------------|-----------|
| Polynomial 2nd Degree         | 21.599581  | 21.5257       | 21.5236   |
| OLS Linear Regression         | 21.796331  | 21.7566       |           |
| Support Vector Regression     | 21.812662  | 21.6988       |           |
| General Linear Model - Normal | 21.821093  |               |           |
| Baseline - Average            | 22.897138  |               |           |
| LASSO + LARS                  | 22.897138  |               |           |  

**How It Works:**  
Polynomial Regression: a combination of the Polynomial features algorithm and simple linear regression. Polynomial features creates new variables from the existing input variables. Using a degree of 2, the algorithm will square each feature, take the combinations of them, and use the results as new features. The degree is a parameter that is a polynomial used to create a new feature. For example, if a degree of 3 is used, each feature would be cubed, squared, and combined with each other feature. Finally, a regression model is fit to the curved line of best fit depending on the degree. An example of determining best fit is below.  

![Model_Evaluation](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/blob/main/images/Model_Evaluation.png?raw=true)

### Conclusions  
Key drivers for popularity include **danceability with speechiness**, whether a track is **explicit**, **energy**, **track number**, and whether a track has **featured artists** or not. The best performing model was our **2nd Degree Polynomial Regression** model with an RMSE of **21.5236** on the testing dataset. The most popular songs were about ~2 minutes long.

<kbd>[Back to Table of Contents](https://github.com/SpotiScryers/SpotiScry#table-of-contents)</kbd>
## How to Reproduce  
### Steps  
1. ~Read through the README.md file~ :white_check_mark:  
2. Download acquire.py, prepare.py, preprocessing.py, and data folder.
3. If you don't have spotipy installed run this in your terminal: ~~~pip install spotipy~~~  
4. Login/Sign up at https://developer.spotify.com/dashboard/login to create a Spotify webapp that'll give you your client id and client secret.
5. Create an env.py file in your working directory and save this code after swaping out your individual client id and secret: 
~~~
cid = YOURCLIENTID
c_secret = YOURCLIENTSECRET
~~~
6. Using the functions in acquire create a spotipy client.
7. Use the functions in prepare.py and preprocessing.py to clean and set up your data.
8. Enjoy exploring the data!  

### Tools & Requirements
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
## License
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
## Creators
[David Mitchell](https://github.com/dlmitc3), [Jason Turner](https://github.com/Jason-R-Turner), [Stephen FitzSimon](https://github.com/stephenfitzsimon), [Vasiliy Melkozerov](https://github.com/VasiliyAMelkozerov)  
<kbd>[Back to Table of Contents](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#table-of-contents)</kbd>