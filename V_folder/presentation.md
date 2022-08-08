# Initial paper for reading 

## Stephen exploration
Rather what it is saying is: that the majority of Magic: the Gathering cards are rather affordable. With most of them being around 10 cents. This would make sense to explain why magic the gathering is popular in the first place, its accessibility and price. Most of the market is incredibly affordable with 75% of the cards being less the 50 cents. This may explain how this game and company have been existing for almost 30 years. That takeaway was before recognizing that there is a large chunk with no values because it is an online card. On the re-read half of the cards are worth around a quarter.
Only 25% of the market is worth more than 5 dollars and 76 cents. Promos are a small. Subset of the cards but are generally worth more then an average basic card.
Odd, there are. More valuable non-foil cards
Penny_rank and edhrec_rank are weak indicators of price
Reserved cards are significantly more. Expensive then the. Rest oft he cards
Card types are not a good. Indicator of price, neither are keywords
The “price by release date” doesn’t quite illustrate price but it does illustrate that more card production has ramped up after 2012 (this may signal how the prices stay so affordable) and also why a lot of the new cards are so affordable. The very expensive ones were the first couple of years printing and a hug spike in (what looks like)1997.

## David’s takeaways:
The amount of cards an artist has made is not a good predictor of card price. Generally some artists make more than others in what appears to be a normal distribution. If you turn your head it is a normal distribution skewed to the right. What has also been discovered is that rarity is not a good indicator of price. The baseline assumption that how “rare” a card is would determine its price. Oddly enough on average commons cost more than mythic and rare. The total amount of cards an artist is featured in does not have an effect on price.

## Jason's takeaways:
How much difference between foil vs non-foil card versions from the same set?
There is a price difference between foil and non-foil of $10.91. 
Reprinted cards are more expensive then the original.
It was surprising that foils cost less then the non-foils.
That can be attributed to the fact that older MTG cards existed and were printed before the foil technique was introduced. The majority of the cards have the base black border and normal frames. We would like to test features in what combinations are effective in predicting price. This can include what production years or set types. 

## Formalize and summarize
Find 5 central connecting features to expand on.

## Model interpretation:
We have a working model! Its so cool!!!!! We made a computer predict a price based off of what the card looks like. Conceptually it sounds like magic but that's neither here nor there. 
The first card I found was "Pyrmaids" it caught my eye because of the huge disperity between the prediction and actual price. In the dataset Pyramids is valued at $175.77 usd. The predicted value from our model says it is worth 12.08! How funny! On one market there are 130 of these cards <a href="https://www.cardmarket.com/en/Magic/Products/Singles/Arabian-Nights/Pyramids">here</a>. So what the model is telling us is that while it may be a solid card that is worth getting, it shouldn't be this high. Now that I think about it I am not even sure what metrics are being measured here. Because pyramid seems like a solid card in any control deck.  But I do not know if the model can compute game value worth. Like maybe that is a metric that exists somewhere. Say for example a 3 mana land corrupt. It can also be coincidently expensive because it is a collectors item. So the model takes in all of the features. It focuses on if it ion the paper game, legalities. Select K-best features rarity if in just paper and legalities, there is a security standpoint. The model's strengths are  in (48%  of the predictions are within  a dime of the price)(when it crosser the upper quartile threshold the accuracy decreases dramatically(really past the median price))

### editor's translation
We made a computer predict a price based on what the card looks like. Conceptually it sounds like magic but that's neither here nor there. 

The first card I found was called Pyramids. It caught my eye because of the huge disparity between the prediction and actual price. In the dataset, Pyramids is valued at $175.77. Meanwhile, the predicted value from our model says it is worth $12.08! How funny! 

In one market, there are 130 of these cards (a link). So, the model is telling us that, while it may be a solid card worth getting, its price shouldn't be this high. Now that I think about it though, I am not even sure what metrics are being measured here. Pyramids cards seem like a solid addition to any control deck, but I do not know if the model can compute game value. But maybe that is a metric that exists somewhere. For example, a 3 mana land corrupt can also be expensive because it is a collectors item. 

The model takes in all of the features. It focuses on if it is on the paper game, legalities. Select K-best features rarity if in just paper and legalities, there is a security standpoint. The model's strengths are in (48% of the predictions are within  a dime of the price)(when it crosses the upper quartile threshold the accuracy decreases dramatically(really past the median price)

## Revisit the elavator





## an experpt on legalities
What do the legalitites mean. What are they, when have they statred? What are the rules to them. Have they changed an evloved as time has gone on?


---------

(Anecdotes: there are no exclusively foiled cards....interesting). 
In the games column there are many of the same entries with the words mixed

We made a computer predict a price based on what the card looks like. Conceptually it sounds like magic but that's neither here nor there. 

The first card I found was called Pyramids. It caught my eye because of the huge disparity between the prediction and actual price. In the dataset, Pyramids is valued at $175.77. Meanwhile, the predicted value from our model says it is worth $12.08! How funny! 

In one market, there are 130 of these cards (a link). So, the model is telling us that, while it may be a solid card worth getting, its price shouldn't be this high. Now that I think about it though, I am not even sure what metrics are being measured here. Pyramids cards seem like a solid addition to any control deck, but I do not know if the model can compute game value. But maybe that is a metric that exists somewhere. For example, a 3 mana land corrupt can also be expensive because it is a collectors item. 

The model takes in all of the features. It focuses on if it is on the paper game, legalities. Select K-best features rarity if in just paper and legalities, there is a security standpoint. The model's strengths are in (48% of the predictions are within  a dime of the price)(when it crosses the upper quartile threshold the accuracy decreases dramatically(really past the median price)