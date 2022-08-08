![Header](https://media.magic.wizards.com/images/wallpaper/WP_Johnny_2560x1600.jpg)
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

[Here's](https://www.notion.so/jason-r-turner/Magic-FAQs-5315dcd4ad564d6ea92f6e9f10d99b6a) a link to some Magic FAQs that helped us understand the fundamentals involved to make informed decisions in our project 


By analyzing Scryfall's API data, we will determine what influences a card's value.

### The Data 
Our dataset came from [https://scryfall.com/docs/api/bulk-data](https://scryfall.com/docs/api/bulk-data). It includes over 20,000 functionally unique cards from a collectible card game starting from the 90s till present day. 


### Deliverables
- 7-10 minute live presentation
- Presentation slides via Canva [here](https://www.canva.com/design/DAFHo-H72x8/kxxQCPwFWXkUekQowv5xvg/view?utm_content=DAFHo-H72x8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)  
- GitHub repository with analysis

### Project Outline
The files within the repository are organized as follows. The /images and /sandbox contents are not necessary for reproduction.  
![Outline](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/(tbd)

### Timeline
- [X] Project Planning: July 28th
- [X] Aquisition and Prep: July 29th
- [X] Exploration: Aug 3rd
- [X] Modeling: Aug 4th
- [X] Finalize Minimum Viable Product (MVP): EOD Aug 5th
- [X] Improve/Iterate MVP: Aug 11th
- [X] Finalize Presentation: Aug 19th

### Acknowledgments


<kbd>[Back to Table of Contents](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#table-of-contents)</kbd>

## Data Dictionary
Below are the features that we used after preparing our dataset acquired from the Scryfall API which are defined on their [Card Objects](https://scryfall.com/docs/api/cards) site.  

| Column          | Data type | Description                                                                                 |
|-----------------|-----------|---------------------------------------------------------------------------------------------|
| object          | String    | A content type for this object, always card.                                                |
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
We engineered the features seen below from the original data using domain expertise and insights gleaned from our dataset.  
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
* What affect does game style have on price?
* Does the artist affect the price?
* Is there a difference in price between sets?
* What affect does reprint have on the price?
* How have card prices been affected by lockdowns due to the Covid-19 pandemic?
* Does legality affect the price?
* Does rarity affect the price?
* What affect does release date have on the price?
* What affect does foil have on the price?
* Does the set type and rarity of the cards affect the price in USD?
* What is the overlap between card types and rarity?
* What effect does basic card type have on price?


### Hypotheses

$H_0$: There is not a signficant difference between foil & non-foil cards.<br>
$H_a$: There is a significant difference between foil & non-foil cards.

$H_0$ = There is not a signficant difference in USD prices between reprints & first printings.<br>
$H_a$ = There is a significant difference in USD prices between reprints & first printings.

$H_0$ Year $x$ has a average price per card equal to or less than the general average price.<br>
$H_a$ Year $x$ has a average price per card greater than the general average price.

$H_0$ : Mean price for card type $x$ is less than or equal to the overall mean price.<br>
$H_a$ : Mean price for card type $x$ is greater than the overall mean price.

$H_0$ : The mean usd price for cards which are available in game type $x$ is less than or equal to the mean usd price of those not available in game type $x$.<br>
$H_a$ : The mean usd price for cards which are available in game type $x$ is greater than the mean usd price of those not available in game type $x$.

$H_0$ : Cards of $raritytype$ and $cardtype$ have a mean value less than or equal to the overall card mean value.<br>
$H_a$ : Cards of $raritytype$ and $cardtype$ have a mean value greater than the overall card mean value.

$H_0$: The total amount of cards created by artist x is = to the value of cards there cards.<br>
$H_a$: The total amount of cards created by artist x is not = to the value of cards there cards.

$H_0$: <br>
$H_a$: 

<kbd>[Back to Table of Contents](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Projecty#table-of-contents)</kbd>
## Project Steps
### Acquire
We acquired our data from the Scryfall API using their "Default Card" json file at this site: https://scryfall.com/docs/api/bulk-data. It  This allowed us to use the create_spotipy_client function to create our own spotipy client that could access the API.  
![Acquire-Visual](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/(tbd)

The dataframe is saved as a json file and has around 71,000 observations.  The acquire.py file has a function for grabbing the latest dataset. There are 56 columns in the original data frame. There are many NaNs which have been left until the later sections to be dealt with.

### Prepare
Functions to prepare the dataframe are stored in two seperate files depending on their purpose, prepare.py and modeling.py:  

**prepare.py:** Functions for cleaning and ordering data
* nulls are dropped
* change dtypes to correct type
* 

**preprocessing.py:** Functions for adding features we found interesting / modyifying data for ease of use in exploration
* 
* 
* 


### Explore
During exploration we looked at these features:
* 
* 
* 

![Card Popularity](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/(tdb)

![Popular Formats](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/(tbd)

![Card Frame Styles](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/(tbd)

### Model
(text)  

**Feature Groups**
We used these sets of feauture groups. 
- 
- 
- 

**Models Evaluated**
* OLS Linear Regression
* 
* 


**Evaluation Metric**  
(text)

![Model-Error](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/(tbd)

**Final Model:**  
(Model types) was our final model we performed on test, predicting ##% better than the baseline.  

| Model                         | Train  | Validate  | Test  |
|-------------------------------|------------|---------------|-----------|
| OLS Linear Regression         |  |       |    |
|          |   |        |           |
|      |   |        |           |
|  |   |               |           |
|             |   |               |           |
|                   |  |               |           |  

**How It Works:**  
(text)  

![Model_Evaluation](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/(tbd)

### Conclusions  
(text)

<kbd>[Back to Table of Contents](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/#table-of-contents)</kbd>
## How to Reproduce  
### Steps  
1. ~Read through the README.md file~ :white_check_mark:  
2. Download the acquire.py, prepare.py, explore.py, and modeling.py modules.
3. Visit https://scryfall.com/docs/api/bulk-data for the most up-to-date dataset  
4. Use the acquire function to import your dataset
5. Use the prepare function to clean up your dataframe.
6. Explore the data for as you like.

### Tools & Requirements
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/works-on-my-machine.svg)](https://forthebadge.com)
## License
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
## Creators
[David Mitchell](https://github.com/dlmitc3), [Jason Turner](https://github.com/Jason-R-Turner), [Stephen FitzSimon](https://github.com/stephenfitzsimon), [Vasiliy Melkozerov](https://github.com/VasiliyAMelkozerov)  
<kbd>[Back to Table of Contents](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#table-of-contents)</kbd>