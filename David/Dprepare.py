#stephen fitzsimon 27 July 2022
#prepare module for the Magic The Gathering Card prediction project
import pandas as pd # to handle the dataframe
import acquire as a
import numpy as np
import prepare as p
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split


# Acquire and Prepare functions with train, validate and test
df = a.get_data(query_url = False)
print(df.shape)
df = p.prepare_dataframe(df)
train, validate, test = p.split_data(df)
train.shape, validate.shape, test.shape

# Hypothesis 1
# H0:The amount of cards created is not = to the artist value.
# HA:The amount of cards created is not = to the artist value.

# Bar plor to show Artist and USD price, for top artist
def vis_artist_by_usd(train):
    train2 = train.sort_values(by=['usd'], ascending=False,)[:100]
    plt.figure(figsize=(10,10))
    sns.barplot(data=train2, x='usd', y='artist')
    plt.title('Rarity vs Artist/USD price')
    plt.xlabel('USD price')
    plt.ylabel('Artist name')
    plt.show()

vis_artist_by_usd(train)

# Median price for all cards based on Rarity and USD price
def vis_rarity_by_usd(train):
    plt.figure(figsize=(10,10))
    sns.barplot(data=train, x='usd', y='rarity')
    plt.title('Median price: Rarity vs USD price')
    plt.xlabel('USD price')
    plt.ylabel('Artist name')
    plt.show()

vis_rarity_by_usd(train)

#--------------------------------------------------------------------------------#


# Hypothesis 2
# H0: artist and rarity of cards is = to price
# HA: artist and rarity of cards is not = to price 

# Bar plot to show Artist, USD price and top 60 cards in the rarity category
def vis_artist_rarity_usd(train):
    train2 = train.sort_values(by=['usd'], ascending=False,)[:60]
    plt.figure(figsize=(10,10))
    sns.barplot(data=train2, x='usd', y='artist', hue='rarity')
    plt.title('Rarity vs Artist/USD price')
    plt.xlabel('USD price')
    plt.ylabel('Artist name')
    plt.show()

vis_artist_rarity_usd(train)
#=================================================================================#

# Hypothesis 3
# H0: set_type and rarity of cards is = to price 
# HA: set_type and rarity of cards is not = to price

# Most expensive cards by set_type
sns.countplot(data= df, y='set_type')


# top 100 cards: Set_type and Rarity 
def usd_rarity_set_type_total(train):
    train2 = train.sort_values(by=['usd'], ascending=False,)[:100]
    plt.figure(figsize=(10,10))
    sns.barplot(data=train2, x='usd', y='set_type', hue='rarity', estimator=sum)
    plt.title('Price vs Set_type/Rarity')
    plt.xlabel('USD price')
    plt.ylabel('Set_type')
    plt.show()

usd_rarity_set_type_total(train)

# Key takeaway
# Rare cards are the most expensive regardless of set_type
# In the charts there are only a few none rare cards in the top 100 high value price range.

#=====================================================================================# 

# Hypothesis 4
# Is there a relationship between collector number and usd?

# Median price for all cards based Collector, Set Type and USD price
def vis_collector_set_by_usd(train):
    train2 = train.sort_values(by=['usd'], ascending=False,)[:20]
    plt.figure(figsize=(10,10))
    sns.barplot(data=train2, x='usd', y='collector_number', hue='set_type')
    plt.title('Median price: collector_number vs USD price')
    plt.xlabel('USD price')
    plt.ylabel('collector_number')
    plt.show()
 
vis_collector_set_by_usd(train)

