#stephen fitzsimon 27 July 2022
#prepare module for the Magic The Gathering Card prediction project
import pandas as pd # to handle the dataframe
import numpy as np
from sklearn.model_selection import train_test_split

RAND_SEED = 1729

def prepare_dataframe(df):
    df = drop_columns(df)
    df = extract_price_data(df)
    df = make_foil_boolean_columns(df)
    df = fill_nulls(df)
    return df.dropna()

def split_data(df):
    '''Splits the possum dataframe into train, test and validate subsets
    Args:
        df (DataFrame) : dataframe to split
    Return:
        train, test, validate (DataFrame) :  dataframes split from the original dataframe
    '''
    #make train and test
    train, validate = train_test_split(df, train_size = 0.75, random_state=RAND_SEED)
    #make validate
    validate, test = train_test_split(validate, train_size = 0.5, random_state=RAND_SEED)
    return train, validate, test
    

def fill_nulls(df):
    df['flavor_name'] = df['flavor_name'].fillna('no_flavor')
    df['content_warning'] = df['content_warning'].map({1.0:True, np.NaN:False})
    #ask about the following two, it only applies to vanguards.  keep it?
    df['hand_modifier'] = df['hand_modifier'].fillna(0)
    df['life_modifier'] = df['life_modifier'].fillna(0)
    df['color_indicator'] = df['color_indicator'].fillna('no_color_indicator')
    #maybe make a boolean
    df['printed_name'] = df['printed_name'].fillna('no_printed_name')
    #only applies to planeswalkers, maybe drop
    df['loyalty'] = df['loyalty'].fillna(0)
    df['frame_effects'] = df['frame_effects'].fillna('no_frame_effects')
    df['watermark'] = df['watermark'].fillna('no_waterwark')
    #might pass to make_list_column or make a boolean
    df['produced_mana'] = df['produced_mana'].fillna('no_produced_mana')
    df['security_stamp'] = df['security_stamp'].fillna('no_security_stamp')
    #make into boolean columns?
    df['promo_types'] = df['promo_types'].fillna('no_promo')
    #presuming these are unranked so zero
    df['penny_rank'] = df['penny_rank'].fillna(0)
    #same as penny_rank comment
    df['edhrec_rank'] = df['edhrec_rank'].fillna(0)
    df['flavor_text'] = df['flavor_text'].fillna('no_flavor_text')
    #empty list means none? some of these are split cards?
    df['colors'] = df['colors'].fillna('no_colors')
    #is there a better value to fill in for no toughness or no power?
    df['toughness'] = df['toughness'].fillna(0)
    df['power'] = df['power'].fillna(0)
    df['oracle_text'] = df['oracle_text'].fillna('no_oracle_text')
    #is there a better value for no mana cost?
    df['mana_cost'] = df['mana_cost'].fillna('no_mana_cost')
    return df

def drop_columns(df):
    """
    Drops the columns that will not be used in the analysis
    Args:
        df (DataFrame) : a dataframe containing the scryfall data
    Returns:
        df (DataFrame) :  a dataframe without the columns in columns_to_drop
    """
    #columns that will drop
    columns_to_drop = [
        'object',
        'oracle_id',
        'multiverse_ids',
        'mtgo_id',
        'mtgo_foil_id',
        'tcgplayer_id',
        'cardmarket_id',
        'uri',
        'scryfall_uri',
        'image_uris',
        'set_uri',
        'set_search_uri',
        'scryfall_set_uri',
        'rulings_uri',
        'prints_search_uri',
        'card_back_id',
        'artist_ids',
        'illustration_id',
        'related_uris',
        'all_parts',
        'arena_id',
        'preview',
        'card_faces',
        'tcgplayer_etched_id',
        'printed_type_line',
        'printed_text',
        'variation_of'
    ]
    #drop columns and return the dataframe
    return df.drop(columns = columns_to_drop)

def extract_price_data(df):
    """
    Extracts the price data from the price column
    Args:
        df (DataFrame) : a dataframe containing the scryfall data
    """
    # make columns for the data
    # each row contains a dictionary of data, use a lambda function 
    # applied to each item to extact the value
    df['usd'] = df.prices.apply(lambda r : r['usd'])
    # df['usd'] = df['usd'].fillna(0)
    # df['usd_foil'] = df.prices.apply(lambda r : r['usd_foil'])
    # df['usd_foil'] = df['usd_foil'].fillna(0)
    # df['eur'] = df.prices.apply(lambda r : r['eur'])
    # df['eur'] = df['eur'].fillna(0)
    # df['eur_foil'] = df.prices.apply(lambda r : r['eur_foil'])
    # df['eur_foil'] = df['eur_foil'].fillna(0)
    #cast to a float value
    df['usd'] = df.usd.astype(float)
    # df['usd_foil'] = df.usd_foil.astype(float)
    # df['eur'] = df.usd.astype(float)
    # df['eur_foil'] = df.usd_foil.astype(float)
    #return the dataframe
    return df

def make_foil_boolean_columns(df):
    df['is_foil'] = df.finishes.apply(lambda r : 'foil' in r)
    df['is_etched'] = df.finishes.apply(lambda r : 'etched' in r)
    df['is_glossy'] = df.finishes.apply(lambda r : 'glossy' in r)
    return df