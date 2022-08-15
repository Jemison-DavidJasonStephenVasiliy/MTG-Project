# Import dataframe module
import pandas as pd

# Import visualization modules
import matplotlib.pyplot as plt
import seaborn as sns

# Import statistical module
from scipy import stats

# Import Regex
import re

#=============================================================================#

### Vasiliy's explore and hypothesis functions
def get_legalites_chart(df):
    '''
    To hammer out the visuals here I will have to go over the code that has gotten me the results: To do so would require starting with identifying where they meet I started from the top and got all of the peices assembled.
    '''
    df['standard'] = df.legalities.apply(lambda r : r['standard'])
    df['future'] = df.legalities.apply(lambda r : r['future'])
    df['historic'] = df.legalities.apply(lambda r : r['historic'])
    df['gladiator'] = df.legalities.apply(lambda r : r['gladiator'])
    df['pioneer'] = df.legalities.apply(lambda r : r['pioneer'])
    df['explorer'] = df.legalities.apply(lambda r : r['explorer'])
    df['modern'] = df.legalities.apply(lambda r : r['modern'])
    df['legacy'] = df.legalities.apply(lambda r : r['legacy'])
    df['pauper'] = df.legalities.apply(lambda r : r['pauper'])
    df['vintage'] = df.legalities.apply(lambda r : r['vintage'])
    df['penny'] = df.legalities.apply(lambda r : r['penny'])
    df['commander'] = df.legalities.apply(lambda r : r['commander'])
    df['brawl'] = df.legalities.apply(lambda r : r['brawl'])
    df['historicbrawl'] = df.legalities.apply(lambda r : r['historicbrawl'])
    df['alchemy'] = df.legalities.apply(lambda r : r['alchemy'])
    df['paupercommander'] = df.legalities.apply(lambda r : r['paupercommander'])
    df['duel'] = df.legalities.apply(lambda r : r['duel'])
    df['oldschool'] = df.legalities.apply(lambda r : r['oldschool'])
    df['premodern'] = df.legalities.apply(lambda r : r['premodern'])

    smu = df[df.standard == 'legal'].usd.mean()
    fmu = df[df.future == 'legal'].usd.mean()
    hmu = df[df.historic == 'legal'].usd.mean()
    gmu = df[df.gladiator == 'legal'].usd.mean()
    pmu = df[df.pioneer == 'legal'].usd.mean()
    emu = df[df.explorer == 'legal'].usd.mean()
    mmu = df[df.modern == 'legal'].usd.mean()
    lmu = df[df.legacy == 'legal'].usd.mean()
    pamu = df[df.pauper == 'legal'].usd.mean()
    vmu = df[df.vintage == 'legal'].usd.mean()
    pemu = df[df.penny == 'legal'].usd.mean()
    cmu = df[df.commander == 'legal'].usd.mean()
    bmu = df[df.brawl == 'legal'].usd.mean()
    hmu = df[df.historicbrawl == 'legal'].usd.mean()
    amu = df[df.alchemy == 'legal'].usd.mean()
    pcmu = df[df.paupercommander == 'legal'].usd.mean()
    dmu = df[df.duel == 'legal'].usd.mean()
    omu = df[df.oldschool == 'legal'].usd.mean()
    premu = df[df.premodern == 'legal'].usd.mean()

    unrounded_answers = {"Standard": [smu],
            "Future": [fmu],
            "Historic": [hmu],
            "Gladiator": [gmu],
            "Pioneer": [pmu],
            "Explorer": [emu],
            "Modern": [mmu],
            "Legacy": [lmu],
            "Pauper": [pamu],
            "Vintage": [vmu],
            "Penny": [pemu],
            "Commander": [cmu],
            "Brawl": [bmu],
            "Historice Brawl": [hmu],
            "Alchemy": [amu],
            "Pauper Commander": [pcmu],
            "Duel": [dmu],
            "Oldschool": [omu],
            "Premodern": [premu]}

    answers = pd.DataFrame.from_dict(unrounded_answers)

    sns.barplot(data = answers, orient = "h")

#-----------------------------------------------------------------------------#

def hypothesis_test_legalities(df, alpha = 0.05):
    '''
    One sample T-Test.
    '''
    t, p = stats.ttest_1samp(df.usd, df[df.standard == "legal"].usd.mean())
    print(t, p/2, alpha)

    if p/2 > alpha:
        print("We fail to reject the null hypothesis")
    elif t < 0:
        print("We fail to reject the null hypothesis")
    else:
        print("We reject the null hypothesis")
    
#-----------------------------------------------------------------------------#

def top_7_sets(df):
    '''
    NEEDS DOC STRING!
    '''
    top7 = df[(df['set_name'] == 'Mirrodin') | (df['set_name'] == "Throne of Eldraine") | (df['set_name'] == "Worldwake") | (df['set_name'] == "Exodus") | (df['set_name'] == "Urza\'s Saga") | (df['set_name'] == "Arabian Nights") | (df['set_name'] == "Limited Edition Alpha")]
    plt.figure(figsize=(10,5))
    sns.barplot(data = top7, x=top7.usd, y=top7.set_name)
    plt.title('USD price by top 7 most popular sets')
    plt.xlabel('USD Price')
    plt.ylabel('Set Name')
    plt.show()

#-----------------------------------------------------------------------------#

def hypothesis_test_set_name(df, alpha = 0.05):
    '''
    One sample T-Test.
    '''
    t, p = stats.ttest_1samp(df.usd, df[df.set_name == "Mirrodin"].usd.mean())
    print(t, p/2, alpha)

    if p/2 > alpha:
        print("We fail to reject the null hypothesis")
    elif t < 0:
        print("We fail to reject the null hypothesis")
    else:
        print("We reject the null hypothesis")

#-----------------------------------------------------------------------------#

def cmc_by_price(df):
    '''
    NEEDS DOC STRING!
    '''
    plt.figure(figsize=(15,10))
    sns.barplot(data = df, x = df.cmc, y = df.usd)
    plt.title('Converted Mana Cost by Price in USD')
    plt.xlabel('CMC')
    plt.ylabel('USD Price')
    plt.show()

#-----------------------------------------------------------------------------#

def hypothesis_test_cmc(df, alpha = 0.05):
    '''
    One sample t-test.
    '''
    cost_to_test = df['cmc'].unique().tolist()
    outputs = []
    for cost in cost_to_test:
        in_year_sample = df[(df['cmc'] == cost) & (df['usd'] > 0)]['usd']
        overall_mean = df['usd'].mean()
        t, p = stats.ttest_1samp(in_year_sample, overall_mean)
        output = {
            'mana_cost':cost,
            'cost_mean':in_year_sample.mean(),
            't_stat':t,
            'p_value':p,
            'reject_null': t > 0 and p/2 < alpha
        }
        outputs.append(output)
    return pd.DataFrame(outputs).sort_values('reject_null', ascending = False).head(5)

#=============================================================================#

### Stephen's explore data functions
def vis_usd_by_released_at(df):
    '''
    NEEDS DOC STRING!
    '''
    plt.figure(figsize=(10,10))
    sns.lineplot(data=df[df['usd'] > 0], x='released_at', y='usd')
    plt.title('USD price and Released Date')
    plt.xlabel('Release Date')
    plt.ylabel('USD price')
    plt.show()
    
#-----------------------------------------------------------------------------#

def make_year_released_column(df):
    '''
    NEEDS DOC STRING!
    '''
    df['year_released'] = df['released_at'].dt.year
    return df

#-----------------------------------------------------------------------------#

def vis_usd_by_year(df):
    '''
    NEEDS DOC STRING!
    '''
    df = make_year_released_column(df)
    plt.figure(figsize=(10,10))
    sns.barplot(data=df[df['usd'] > 0], x='year_released', y='usd')
    plt.title('USD price by year released')
    plt.xlabel('Year released')
    plt.ylabel('USD Price')
    plt.show()
    
#-----------------------------------------------------------------------------#

def hypothesis_test_years(df, alpha = 0.05):
    '''
    NEEDS DOC STRING!
    '''
    years_to_test = df['year_released'].unique().tolist()
    outputs = []
    for year in years_to_test:
        in_year_sample = df[(df['year_released'] == year) & (df['usd'] > 0)]['usd']
        overall_mean = df['usd'].mean()
        t, p = stats.ttest_1samp(in_year_sample, overall_mean)
        output = {
            'year':year,
            'year_mean':in_year_sample.mean(),
            't_stat':t,
            'p_value':p,
            'reject_null': t > 0 and p/2 < alpha
        }
        outputs.append(output)
    return pd.DataFrame(outputs).sort_values('reject_null', ascending = False).head(5)

#-----------------------------------------------------------------------------#

def make_card_type_column(df):
    '''
    NEEDS DOC STRING!
    '''
    card_cats = ['Card', 'Vanguard', 'Plane', 'Creature', 'Land', 'Enchantment', 'Artifact', 'Sorcery', 'Instant', 'Legendary', 'Token']
    df['card_type'] = 'other_type'
    for card_cat in card_cats:
        df.loc[df['type_line'].str.contains(card_cat).fillna(False), 'card_type'] = card_cat.lower()
    df.loc[df['type_line'].str.contains('Card // Card').fillna(False), 'card_type'] = 'split_card'
    return df

def vis_by_card_type(df):
    '''
    NEEDS DOC STRING!
    '''
    df = make_card_type_column(df)
    plt.figure(figsize=(10,10))
    sns.barplot(data=df[df['usd'] > 0], y='card_type', x='usd')
    plt.title('USD price by basic card type')
    plt.xlabel('USD Price')
    plt.ylabel('Basic Card Type')
    plt.show()
    
#-----------------------------------------------------------------------------#

def hypothesis_test_card_type(df, alpha = 0.05):
    '''
    NEEDS DOC STRING!
    '''
    card_types_to_test = df['card_type'].unique().tolist()
    outputs = []
    for card_type in card_types_to_test:
        in_card_sample = df[(df['card_type'] == card_type) & (df.usd > 0.01)]['usd']
        overall_mean = df['usd'].mean()
        t, p = stats.ttest_1samp(in_card_sample, overall_mean)
        output = {
            'card_type':card_type,
            'overall_mean':overall_mean,
            'card_type_mean':in_card_sample.mean(),
            't_stat':t,
            'p_value':p,
            'reject_null': t > 0 and p/2 < alpha
        }
        outputs.append(output)
    return pd.DataFrame(outputs).sort_values('reject_null', ascending = False)

#-----------------------------------------------------------------------------#

def make_games_boolean_columns(df):
    '''
    NEEDS DOC STRING!
    '''
    df_new = df[['id', 'usd', 'name', 'games']].copy()
    games_values = []
    for r in df.games:
        games_values += r
    game_values = list(set(games_values))
    df_new['games_str'] = df_new['games'].apply(lambda r : ' '.join(r))
    for game_type in game_values:
        df_new[f'is_{game_type.lower()}'] = df_new.games_str.str.contains(game_type)
    return df_new

def vis_game_type(df):
    '''
    NEEDS DOC STRING!
    '''
    games_df = make_games_boolean_columns(df)
    bool_columns = games_df.select_dtypes(include=bool).columns
    fig, axes = plt.subplots(3, 1, figsize = (10, 25), constrained_layout=True)
    for i, bool_col in enumerate(bool_columns):
        sns.barplot(data = games_df, x=bool_col, y='usd', ax = axes[i])
    fig.suptitle('Card USD Price by Game type')
    plt.show()

#-----------------------------------------------------------------------------#

def vis_game_type_by_combo(df):
    '''
    NEEDS DOC STRING!
    '''
    df_new = df[['id', 'usd', 'name', 'games']].copy()
    df_new['games_str'] = df_new['games'].apply(lambda r : ' '.join(r))
    plt.figure(figsize=(10,10))
    sns.barplot(data = df_new, y='games_str', x='usd')
    plt.title('USD Price by Games Combination')
    plt.show()

#-----------------------------------------------------------------------------#

def hypothesis_test_game_type(df, alpha = 0.05):
    '''
    NEEDS DOC STRING!
    '''
    games_df = make_games_boolean_columns(df)
    bool_columns = games_df.select_dtypes(include=bool).columns
    outputs = []
    for bool_col in bool_columns:
        is_true_sample = games_df[(games_df[bool_col])]['usd']
        overall_mean = games_df['usd'].mean()
        t, p = stats.ttest_1samp(is_true_sample, overall_mean)
        output = {
            'game_type':bool_col,
            'card_count': games_df[(games_df[bool_col]) & (games_df.usd > 0.01)]['usd'].count(),
            'game_type_mean':is_true_sample.mean(),
            't_stat':t,
            'p_value':p,
            'reject_null': t > 0 and p/2 < alpha
        }
        outputs.append(output)
    return pd.DataFrame(outputs).sort_values('reject_null', ascending=False)

#-----------------------------------------------------------------------------#

def hypothesis_test_game_type_combinations(df, alpha = 0.05):
    '''
    NEEDS DOC STRING!
    '''
    games_df = df[['id', 'usd', 'name', 'games']].copy()
    games_df['games_str'] = games_df['games'].apply(lambda r : ' '.join(r))
    test_values = games_df['games_str'].value_counts().index.tolist()
    outputs = []
    for test_val in test_values:
        in_sample = games_df[(games_df['games_str'] == test_val)]['usd']
        overall_mean = games_df['usd'].mean()
        t, p = stats.ttest_1samp(in_sample, overall_mean)
        output = {
            'games_combination':test_val,
            'card_count':games_df[(games_df['games_str'] == test_val) & (games_df.usd > 0.01)]['usd'].count(),
            'in_sample_mean':in_sample.mean(),
            't_stat':t,
            'p_value':p,
            'reject_null': t > 0 and p/2 < alpha
        }
        outputs.append(output)
    return pd.DataFrame(outputs).sort_values('reject_null', ascending=False)
    
#-----------------------------------------------------------------------------#

def viz_rarity_price(df):
    '''
    NEEDS DOC STRING!
    '''
    plt.figure(figsize=(10,10))
    sns.barplot(data = df, x = 'rarity', y = 'usd', palette = sns.color_palette())
    plt.title('Card Rarity and USD Price')
    plt.xlabel('Rarity Type')
    plt.ylabel('USD Price')
    plt.show()
    
#-----------------------------------------------------------------------------#

def viz_card_type_rarity(df):
    '''
    NEEDS DOC STRING!
    '''
    plt.figure(figsize=(10,10))
    sns.countplot(data = df, x = 'rarity', hue = 'card_type', palette = sns.color_palette())
    plt.title('Card Rarity and Basic Card Types')
    plt.xlabel('Rarity Type')
    plt.show()

#-----------------------------------------------------------------------------#

def viz_rare_uncommon_card_type_prices(df):
    '''
    NEEDS DOC STRING!
    '''
    plt.figure(figsize=(10,10))
    sns.barplot(data = df[df['rarity'].isin(['rare', 'uncommon', 'mythic'])], x = 'rarity', y= 'usd', hue = 'card_type', palette = sns.color_palette())
    plt.title('Card Rarity and Basic Card Types by USD Price')
    plt.xlabel('Rarity Type')
    plt.ylabel('USD Price')
    plt.show()
    
#-----------------------------------------------------------------------------#

def rarity_card_type_hypothesis_tests(df, alpha = 0.05):
    '''
    NEEDS DOC STRING!
    '''
    outputs = []
    rarities_to_test = ['rare', 'uncommon', 'mythic']
    overall_mean = df['usd'].mean()
    for rarity_type in rarities_to_test:
        rarity_df = df[df.rarity == rarity_type]
        card_types_list = rarity_df['card_type'].unique().tolist()
        for card_type in card_types_list:
            subgroup = rarity_df[rarity_df['card_type'] == card_type]['usd']
            t, p = stats.ttest_1samp(subgroup, overall_mean)
            output = {
                'rarity_type':rarity_type,
                'card_type':card_type,
                'overall_mean':overall_mean,
                'subgroup_mean':subgroup.mean(),
                't_stat': t,
                'p_value': p,
                'reject_null': t > 0 and p/2 < alpha
            }
            outputs.append(output)
    return pd.DataFrame(outputs).sort_values('reject_null', ascending=False).head(15)

#=============================================================================#

### Jason's final notebook explore functions
def add_nonfoil_only_and_both_foil_and_nonfoil_columns(df):
    '''
    Adds columns to dataframe for cards with only non-foil versions
    and those with both foil and non-foil versions.
    '''
    # Creates column for cards that have only non-foil versions
    df['nonfoil_only'] = (df.loc[:, 'nonfoil'] == True) & (df.loc[:, 'foil'] == False)
    
    # Creates column for cards that have both foil & non-foil versions
    df['foil_and_nonfoil'] = df.loc[:, 'nonfoil'] == df.loc[:, 'foil']
    return df

#-----------------------------------------------------------------------------#

def add_columns_with_usd_prices_for_nonfoil_cards(df):
    '''
    Adds columns to dataframe with the usd prices of all non-foil cards with 
    separate columns for non-foil only and both foil & non-foil cards.
    '''
    # Creates a column with USD prices for non-foil only cards
    df.loc[df['nonfoil_only'] == True, 'nonfoil_only_usd'] = df['usd']
    
    # Creates a column with USD prices for cards with both foil and non-foil versions
    df.loc[df['foil_and_nonfoil'] == True, 'foil_and_nonfoil_usd'] = df['usd']
    return df

#-----------------------------------------------------------------------------#

def avg_nonfoil_only_and_both_foil_and_nonfoil_and_diff(df):
    '''
    Returns the average price of cards in USD for non-foil only and card with both foin and non-foil versions and the difference from non-foil only.
    '''
    avg_nonfoil_only = df.nonfoil_only_usd.mean()
    avg_foil_and_nonfoil = df.foil_and_nonfoil_usd.mean()
    return f'The average USD price of non-foil only cards is ${round(avg_nonfoil_only, 2)},  and for cards with both foil and non-foil is ${round(avg_foil_and_nonfoil, 2)}. The difference in average price is ${round((avg_nonfoil_only - avg_foil_and_nonfoil),2)}.'

#-----------------------------------------------------------------------------#

def only_foil_vs_both_versions_viz(df):
    '''
    Creates a bar plot for columns in the dataframe for if it's non-foil only or not.
    '''
    plt.figure(figsize = (30,15))
    sns.barplot(x = 'nonfoil_only', y = 'usd', data = df)
    plt.title('Difference in Average Price of Only Foils and Both Foils & Non-Foils')
    plt.xlabel('Only Non-Foils or Cards with Both Foil & Non-Foil')
    plt.ylabel('Price in USD')
    plt.xticks([0, 1],['Both Foils and Non-Foils', 'Only Non-Foils'])
    return plt.show()

#-----------------------------------------------------------------------------#

def nonfoil_only_or_not_viz(df):
    '''
    Combines explore functions for question one visualization
    '''
    df = add_nonfoil_only_and_both_foil_and_nonfoil_columns(df)
    df = add_columns_with_usd_prices_for_nonfoil_cards(df)
    diff = avg_nonfoil_only_and_both_foil_and_nonfoil_and_diff(df)
    viz = only_foil_vs_both_versions_viz(df)
    return viz, diff

#-----------------------------------------------------------------------------#

def hypothesis_test_foil_vs_nonfoil(df):
    '''
    Hypothesis testing for using Two-sample T-Test with a 95% confidence interval.
    '''
    # Sets alpha to 0.05 for 95% Confidence Interval
    α = 0.05
    
    print(f'Variance for non-foil only cards is {round(df.nonfoil_only_usd.var(), 3)}.')
    print(f'Variance for cards with both foil and non-foil cards is {round(df.foil_and_nonfoil_usd.var(), 3)}.')

    # T-Test returning t and p values ignoring nan values
    t, p = stats.ttest_ind(df.foil_and_nonfoil_usd, df.nonfoil_only_usd, equal_var = False, nan_policy = 'omit')
    
    # Prints statement for t-statistic and p-value
    if (t < 0) & (p/2 < α):
        print(f'The t-statistic of {round(t,3)} is less than 0, and the p-value of {(p/2):.3e} is statistically significant.')
    elif (t < 0) & (p/2 > α):
        print(f'The t-statistic of {round(t,3)} is less than 0, but the p-value of {(p/2):.3e} is not statistically significant.')
    elif (t > 0) & (p/2 < α):
        print(f'The t-statistic of {round(t,3)} is more than 0, but the p-value of {(p/2):.3e} is statistically significant.')
    else:
        print(f'The t-statistic of {round(t,3)} is more than 0, and the p-value of {(p/2):.3e} is not statistically significant.')
     
    # Prints statement for either accepting or rejecting the Null Hypothesis
    if p/2 < α:
        print("We reject the Null Hypothesis")
    else:
        print("We fail to reject the Null Hypothesis")
    return
          
#-----------------------------------------------------------------------------#

def add_columns_with_usd_prices_for_reprints_and_first_printings(df):
    '''
    Adds two columns to the dataframe with the usd prices of all first printings and reprints of cards.
    '''
    # Creates a column with USD prices for reprint cards
    df.loc[df['reprint'] == True, 'reprints_usd'] = df['usd']
    
    # Creates a column with USD prices for first card printings
    df.loc[df['reprint'] == False, 'first_prints_usd'] = df['usd']
    return df

#-----------------------------------------------------------------------------#

def reprints_vs_first_prints_viz(df):
    '''
    Creates a bar plot for columns in the dataframe for reprints or first printings.
    '''
    plt.figure(figsize = (30,15))
    sns.barplot(x = 'reprint', y = 'usd', data = df)
    plt.title('Difference in Average Price of Reprints and First Printings')
    plt.xlabel('Reprints or First Printings')
    plt.ylabel('Price in $USD')
    plt.xticks([0, 1],['First Printings', 'Reprints'])
    return plt.show()

#-----------------------------------------------------------------------------#

def avg_reprints_and_first_printings_and_diff(df):
    '''
    Returns the average price of cards in USD for reprints and first printings and the difference from reprints.
    '''
    avg_reprints = df.reprints_usd.mean()
    avg_first_prints = df.first_prints_usd.mean()
    return f'The average USD price of reprinted cards is ${round(avg_reprints, 2)},  and first print cards is ${round(avg_first_prints, 2)}. The difference in average price is ${round((avg_reprints - avg_first_prints),2)}.'

#-----------------------------------------------------------------------------#

def reprint_or_not_viz(df):
    '''
    Combines explore functions for reprint visualization
    '''
    df = add_columns_with_usd_prices_for_reprints_and_first_printings(df)
    diff = avg_reprints_and_first_printings_and_diff(df)
    viz = reprints_vs_first_prints_viz(df)
    return viz, diff

#-----------------------------------------------------------------------------#

def hypothesis_test_reprint_or_not(df):
    '''
    Hypothesis testing using Two-sample T-Test with a 95% confidence interval.
    '''
    # Sets alpha to 0.05 for 95% Confidence Interval
    α = 0.05
    
    print(f'Variance for non-foil only cards is {round(df.reprints_usd.var(), 3)}.')
    print(f'Variance for cards with both foil and non-foil cards is {round(df.first_prints_usd.var(), 3)}.')

    # T-Test returning t and p values ignoring nan values
    t, p = stats.ttest_ind(df.first_prints_usd, df.reprints_usd, equal_var = False, nan_policy = 'omit')
    
    # Prints statement for t-statistic and p-value
    if (t < 0) & (p/2 < α):
        print(f'The t-statistic of {round(t,3)} is less than 0, and the p-value of {(p/2):.3e} is statistically significant.')
    elif (t < 0) & (p/2 > α):
        print(f'The t-statistic of {round(t,3)} is less than 0, but the p-value of {(p/2):.3e} is not statistically significant.')
    elif (t > 0) & (p/2 < α):
        print(f'The t-statistic of {round(t,3)} is more than 0, but the p-value of {(p/2):.3e} is statistically significant.')
    else:
        print(f'The t-statistic of {round(t,3)} is more than 0, and the p-value of {(p/2):.3e} is not statistically significant.')
     
    # Prints statement for either accepting or rejecting the Null Hypothesis
    if p/2 < α:
        print("We reject the Null Hypothesis")
    else:
        print("We fail to reject the Null Hypothesis")
    return

#=============================================================================#

### David's final notebook explore data functions
def vis_artist_by_usd(train):
    '''
    Bar plot to show Artist and USD price, for top artist.
    '''
    train2 = train.sort_values(by=['usd'], ascending=False,)[:100]
    plt.figure(figsize=(10,10))
    sns.barplot(data=train2, x='usd', y='artist')
    plt.title('Rarity vs Artist/USD price')
    plt.xlabel('USD price')
    plt.ylabel('Artist name')
    plt.show()

#-----------------------------------------------------------------------------#
    
def vis_rarity_by_usd(train):
    '''
    Median price for all cards based on Rarity and USD price.
    '''
    plt.figure(figsize=(10,10))
    sns.barplot(data=train, x='usd', y='rarity')
    plt.title('Median price: Rarity vs USD price')
    plt.xlabel('USD price')
    plt.ylabel('Artist name')
    plt.show()

#-----------------------------------------------------------------------------#

def vis_artist_rarity_usd(df):
    '''
    Bar plot to show Artist, USD price and top 60 cards in the rarity category.
    '''
    train2 = df.sort_values(by=['usd'], ascending=False,)[:60]
    plt.figure(figsize=(10,10))
    sns.barplot(data=train2, x='usd', y='artist', hue='rarity')
    plt.title('Rarity vs Artist/USD price')
    plt.xlabel('USD price')
    plt.ylabel('Artist name')
    plt.show()

#-----------------------------------------------------------------------------#

def viz_expensive_cards_by_set_type(df):
    '''
    Most expensive cards by set type.
    '''
    plt.figure(figsize=(10,10))
    sns.countplot(data= df, y='set_type')
    plt.title('Set Types')
    plt.xlabel('Count')
    plt.show()

#-----------------------------------------------------------------------------#

def usd_rarity_set_type_total(train):
    '''
    The top 100 cards by set type and Rarity.
    '''
    train2 = train.sort_values(by=['usd'], ascending=False,)[:100]
    plt.figure(figsize=(10,10))
    sns.barplot(data=train2, x='usd', y='set_type', hue='rarity', estimator=sum)
    plt.title('Price vs Set_type/Rarity')
    plt.xlabel('USD price')
    plt.ylabel('Set_type')
    plt.show()

#=============================================================================#


