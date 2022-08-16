![Header](https://media.magic.wizards.com/images/wallpaper/WP_Johnny_2560x1600.jpg)
## Table of Contents
1. About the Project  
[Goals](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#goals) | [Background](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#background) | [The Data](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#the-data) | [Deliverables](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#deliverables) | [Outline](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#project-outline)  

2. Data Dictionary  
[Original Features](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#original-features) | [Engineered Features](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#engineered-features)  

3. Initial Thoughts & Hypotheses  
[Thoughts](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#thoughts) | [Hypotheses](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#hypotheses)  

4. Project Steps  
[Acquire](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#acquire) | [Prepare](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#prepare) | [Explore](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#explore) | [Model](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#model) | [Conclusions](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#conclusions)  

5. How to Reproduce & More  
[Steps](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#steps) | [Tools & Requirements](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#tools--requirements) | [License](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#License) | [Creators](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#Creators)

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
![Outline](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick/(tbd)

### Timeline
- [X] Project Planning: July 28th
- [X] Aquisition and Prep: July 29th
- [X] Exploration: Aug 3rd
- [X] Modeling: Aug 4th
- [X] Finalize Minimum Viable Product (MVP): EOD Aug 5th
- [X] Improve/Iterate MVP: Aug 11th
- [X] Finalize Presentation: Aug 19th

### Acknowledgments


<kbd>[Back to Table of Contents](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#table-of-contents)</kbd>

## Data Dictionary
Below are the features that we used after preparing our dataset acquired from the Scryfall API which are defined on their [Card Objects](https://scryfall.com/docs/api/cards) site.  

| Column          | Data type | Description                                                                                 |
|-----------------|-----------|---------------------------------------------------------------------------------------------|
| artist          | String    | The name of the illustrator of this card. Newly spoiled cards may not have this field yet.  |
| cmc             | Decimal   | The card’s converted mana cost. Note that some funny cards have fractional mana costs.      |
| games           | Array     | A list of games that this card print is available in, paper, arena, and/or mtgo.            |
| id              | UUID      | An unique ID for this card in Scryfall’s database.                                          |
| lang            | String    | A language code for this printing.                                                          |
| legalities      | Object    | An object describing the legality of this card across play formats. Possible legalities are legal, not_legal, restricted, and banned.                                                                                          |
| name            | String    | The name of this card. If this card has multiple faces, this field will contain both names separated by ␣//␣.|
| rarity          | String    | This card’s rarity. One of common, uncommon, rare, special, mythic, or bonus.               |
| released_at     | Date      | The date this card was first released.                                                      |
| reprint         | Boolean   | True if this card is a reprint.                                                             |
| set_name        | String    | This card’s full set name.                                                                  |
| type_line       | String    | The type line of this particular face, if the card is reversible.                           |



### Engineered Features
We engineered the features seen below from the original data using domain expertise and insights gleaned from our dataset.  
| Feature Name             | Description                                                                                    |
|--------------------------|------------------------------------------------------------------------------------------------|
| card_type                | Categories for the different card type lines.                                                  |
| first_prints_usd         | Price in USD for the original printings of cards.                                              |
| foil                     | Boolean that is True for foil cards.                                                           |
| foil_and_nonfoil         | Boolean that is True for cards that have both foil & non-foil versions.                        |
| foil_and_nonfoil_usd     | Card prices in USD for which 'foil_and_nonfoil' is True.                                       |
| nonfoil                  | Boolean that is True for non-foil cards.                                                       | 
| nonfoil_only             | Boolean that is True for cards with only non-foil versions.                                    |
| nonfoil_only_usd         | Card prices in USD for which 'nonfoil_only' is True.                                           |
| reprints_usd             | Card prices in USD for which 'reprint' is True.                                                |      
| usd                      | Prices in USD for which 'price' is has a 'usd' value.                                          |
| year_released            | Year value derived from 'released_at' Date.                                                    |

<kbd>[Back to Table of Contents](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#table-of-contents)</kbd>
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


<kbd>[Back to Table of Contents](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick#table-of-contents)</kbd>
## Project Steps
### Acquire
We acquired our data from the Scryfall API using their "Default Card" json file at this site: https://scryfall.com/docs/api/bulk-data.
![Acquire-Visual](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick/(tbd)

The dataframe is saved as a json file and has around 71,000 observations.  The acquire.py file has a function for grabbing the latest dataset. There are 56 columns in the original data frame. There are many NaNs which have been left until the later sections to be dealt with.

### Prepare
Functions to prepare the dataframe are stored in two seperate files depending on their purpose, prepare.py and model.py:  

**prepare.py:** Functions for cleaning and ordering data
* nulls are dropped
* change dtypes to correct type
* extracted USD from 'prices' column into its own column
* split dataframe into test, validate, and train



### Explore
During exploration we looked at these features:
* Set Type
* Card Types
* Rarity
* Foil/Non-Foil
* Language and Locality

![Card Popularity](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick(tdb)

![Popular Formats](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick(tbd)

![Card Frame Styles](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick/(tbd)

### Model
- The final model is a RandomForestRegressor with 200 features and predictions are made on unseen test data.
- The model metrics improve with the test data in both MAE and within-a-dime.
- From plotting the residuals, it is clear that more expensive cards are likely to be underestimated; sometimes by a significant amount.

**Feature Groups**
We used these sets of feauture groups. 
- Price point clusters

**Models Evaluated**
* RandomForestRegressor
* KNeighborsRegressor
* DecisionTreeRegressor
* LinearSVR


**Evaluation Metric**  
- Mean Absolute Error (MAE).  This is chosen because models tended to poorly predict expensive cards, leading to the RMSE being a poor metric since it over emphasizes large errors
- Card predictions within a dime of the actual value.  The models tended to be better at predicting lower priced cards.  Since the use case is to determine if new cards hit many price points in the market, if a larger percentage of cards are accurately predicted, more price points can be easily marketed to with the model.

![Model-Error](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick/(tbd)

**Final Model:**  
RandomForestRegressor was our final model we performed on test, predicting ##% better than the baseline.  

| Model                               | Train      | Validate      | Test      |
|-------------------------------------|------------|---------------|-----------|
| Baseline Mean	                      | 5.827456   | 5.724399e+00  |           |
| Baseline Median                     | 3.721033   | 3.632730e+00  |           |
| Random Forest Regressor             | 1.442782   | 2.765467e+00  | 2.532968  |
| K-Neighbors Regressor-weighted      | 0.926974   | 2.927149e+00  |           |
| K-Neighbors Regressor               | 2.482755   | 2.994726e+00  |           |
| Decision Tree Regressor             | 0.913396   | 3.065815e+00  |           |
| Linear SVR                          | 3.379344   | 3.292252e+00  |           |
| XG Boost Regressor                  | 3.407522   | 3.599480e+00  |           |
| Radius Neighbors Regressor-weighted | 0.913396   | 3.639562e+00  |           |
| Radius Neighbors Regressor          | 5.428092   | 5.330757e+00  |           |
| Linear Regression                   | 5.509399   | 1.057490e+07  |           |



![Model_Evaluation](https://github.com/Jemison-DavidJasonStephenVasiliy/Magic-Trick(tbd)

### Conclusions  
Using Scryfall data we are predicting the USD price of Magic The Gathering cards. This allows the publisher to determine the price of newly published cards by their similarity to other cards to make sure that they are hitting all the likely price points within the current market. It will also allow buyers and sellers to determine the price of cards with no or little current price data.

<kbd>[Back to Table of Contents](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project/#table-of-contents)</kbd>
## How to Reproduce  
### Steps  
1. ~Read through the README.md file~ :white_check_mark:  
2. Download the acquire.py, prepare.py, explore.py, and modeling.py modules.
3. Visit https://scryfall.com/docs/api/bulk-data for the most up-to-date dataset.
4. Use the acquire function to import your dataset.
5. Pip install XGboost.
6. Use the prepare function to clean up your dataframe.
7. Explore the data as you like.

### Tools & Requirements
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/works-on-my-machine.svg)](https://forthebadge.com)
## License
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
## Creators
[David Mitchell](https://github.com/dlmitc3), [Jason Turner](https://github.com/Jason-R-Turner), [Stephen FitzSimon](https://github.com/stephenfitzsimon), [Vasiliy Melkozerov](https://github.com/VasiliyAMelkozerov)  
<kbd>[Back to Table of Contents](https://github.com/Jemison-DavidJasonStephenVasiliy/MTG-Project#table-of-contents)</kbd>