# Import visualization modules
import matplotlib.pyplot as plt
import seaborn as sns

# Import statistical module
from scipy import stats

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


def avg_nonfoil_only_and_both_foil_and_nonfoil_and_diff(df):
    '''
    Returns the average price of cards in USD for non-foil only and card with both foin and non-foil versions and the difference from non-foil only.
    '''
    avg_nonfoil_only = df.nonfoil_only_usd.mean()
    avg_foil_and_nonfoil = df.foil_and_nonfoil_usd.mean()
    return f'The average USD price of non-foil only cards is ${round(avg_nonfoil_only, 2)},  and for cards with both foil and non-foil is ${round(avg_foil_and_nonfoil, 2)}. The difference in average price is ${round((avg_nonfoil_only - avg_foil_and_nonfoil),2)}.'


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


def nonfoil_only_or_not_viz(df):
    '''
    Combines explore functions for question one visualization
    '''
    df = add_nonfoil_only_and_both_foil_and_nonfoil_columns(df)
    df = add_columns_with_usd_prices_for_nonfoil_cards(df)
    diff = avg_nonfoil_only_and_both_foil_and_nonfoil_and_diff(df)
    viz = only_foil_vs_both_versions_viz(df)
    return viz, diff


def q1_hypothesis_test(df):
    '''
    Hypothesis testing for question 1 using Two-sample T-Test with a 95% confidence interval.
    '''
    # Sets alpha to 0.05 for 95% Confidence Interval
    α = 0.05
    
    print(f'Variance for non-foil only cards is {round(df.nonfoil_only_usd.var(), 3)}.')
    print(f'Variance for cards with both foil and non-foil cards is {round(df.foil_and_nonfoil_usd.var(), 3)}.')

    # T-Test returning t and p values ignoring nan values
    t, p = stats.ttest_ind(df.foil_and_nonfoil_usd, df.nonfoil_only_usd, equal_var = False, nan_policy = 'omit')
    
    # Prints statement for t-statistic and p-value
    if (t < 0) & (p/2 < α):
        print(f'The t-statistic is {round(t,3)} less than 0, and the p-value of {(p/2):.3e} is statistically significant.')
    elif (t < 0) & (p/2 > α):
        print(f'The t-statistic is {round(t,3)} less than 0, but the p-value of {(p/2):.3e} is not statistically significant.')
    elif (t > 0) & (p/2 < α):
        print(f'The t-statistic is {round(t,3)} more than 0, but the p-value of {(p/2):.3e} is statistically significant.')
    else:
        print(f'The t-statistic is {round(t,3)} more than 0, and the p-value of {(p/2):.3e} is not statistically significant.')
     
    # Prints statement for either accepting or rejecting the Null Hypothesis
    if p/2 < α:
        print("We reject the Null Hypothesis")
    else:
        print("We fail to reject the Null Hypothesis")
    return
          
    
def add_columns_with_usd_prices_for_reprints_and_first_printings(df):
    '''
    Adds two columns to the dataframe with the usd prices of all first printings and reprints of cards.
    '''
    # Creates a column with USD prices for reprint cards
    df.loc[df['reprint'] == True, 'reprints_usd'] = df['usd']
    
    # Creates a column with USD prices for first card printings
    df.loc[df['reprint'] == False, 'first_prints_usd'] = df['usd']
    return df


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


def avg_reprints_and_first_printings_and_diff(df):
    '''
    Returns the average price of cards in USD for reprints and first printings and the difference from reprints.
    '''
    avg_reprints = df.reprints_usd.mean()
    avg_first_prints = df.first_prints_usd.mean()
    return f'The average USD price of reprinted cards is ${round(avg_reprints, 2)},  and first print cards is ${round(avg_first_prints, 2)}. The difference in average price is ${round((avg_reprints - avg_first_prints),2)}.'


def reprint_or_not_viz(df):
    '''
    Combines explore functions for question one visualization
    '''
    df = add_columns_with_usd_prices_for_reprints_and_first_printings(df)
    diff = avg_reprints_and_first_printings_and_diff(df)
    viz = reprints_vs_first_prints_viz(df)
    return viz, diff


def q2_hypothesis_test(df):
    '''
    Hypothesis testing for question two using Two-sample T-Test with a 95% confidence interval.
    '''
    # Sets alpha to 0.05 for 95% Confidence Interval
    α = 0.05
    
    print(f'Variance for non-foil only cards is {round(df.reprints_usd.var(), 3)}.')
    print(f'Variance for cards with both foil and non-foil cards is {round(df.first_prints_usd.var(), 3)}.')

    # T-Test returning t and p values ignoring nan values
    t, p = stats.ttest_ind(df.first_prints_usd, df.reprints_usd, equal_var = False, nan_policy = 'omit')
    
    # Prints statement for t-statistic and p-value
    if (t < 0) & (p/2 < α):
        print(f'The t-statistic is {round(t,3)} less than 0, and the p-value of {(p/2):.3e} is statistically significant.')
    elif (t < 0) & (p/2 > α):
        print(f'The t-statistic is {round(t,3)} less than 0, but the p-value of {(p/2):.3e} is not statistically significant.')
    elif (t > 0) & (p/2 < α):
        print(f'The t-statistic is {round(t,3)} more than 0, but the p-value of {(p/2):.3e} is statistically significant.')
    else:
        print(f'The t-statistic is {round(t,3)} more than 0, and the p-value of {(p/2):.3e} is not statistically significant.')
     
    # Prints statement for either accepting or rejecting the Null Hypothesis
    if p/2 < α:
        print("We reject the Null Hypothesis")
    else:
        print("We fail to reject the Null Hypothesis")
    return


