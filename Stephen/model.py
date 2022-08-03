import pandas as pd
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
import model_constants

### GLOBAL CONSTANTS

# ensures that the models are always the same as in the notebook
RAND_SEED = 1729 

#sets up the model strategies
MODEL_STRATEGY_DICTIONARY = {
}

#holds the model strategy types
MODEL_STRATEGIES = []

### FUNCTIONS TO MAKE COLUMNS FOR MODEL

def scale_and_make_X_and_y(train, validate):
    """
    Scales the columns for modeling based off of the list in model_constants,
    then make the X and y sets for train and validate
    """
    #drop the target variable, usd
    X_train = train.drop(columns=['id', 'name', 'usd'])
    X_val = train.drop(columns=['id', 'name', 'usd'])
    #make the scaler and fit it
    # scaler = StandardScaler()
    # scaler = scaler.fit(train[model_constants.SCALED_COLUMNS])
    #transform the columns for X_train
    # X_train[model_constants.SCALED_COLUMNS] = pd.DataFrame(scaler.transform(train[model_constants.SCALED_COLUMNS]), columns = model_constants.SCALED_COLUMNS)
    #X_train = X_train.merge(X_scaled_train, on='id')
    #transform the columns for X_validate
    #X_scaled_val = scaler.transform(validate[model_constants.SCALED_COLUMNS])
    #X_val = pd.concat([X_val, pd.DataFrame(X_scaled_train)]).drop(columns=model_constants.SCALED_COLUMNS)
    #make y dataframes with relevant columns to use
    y_train = train[['id', 'name', 'usd']]
    y_val = validate[['id', 'name', 'usd']]
    return X_train, y_train, X_val, y_val

def prepare_model_df(df):
    """
    Flow control function to prepare a dataframe
    """
    # make/drop columns for the model
    df = make_legality_columns(df)
    df = make_card_type_column(df)
    df = make_list_to_str_columns(df)
    df = drop_non_modeling_columns(df)
    # transform by encoding and scaling
    df = encode_columns(df)
    return df

def scale_columns(df):
    """
    Scales the numeric columns from the SCALED_COLUMNS
    constant from the model_constants module
    """
    return df

def encode_columns(df):
    """
    Encodes all the categorical columns in the ENCODED_COLUMNS
    constant from the model_constants module
    """
    #make dummies and return the dataframe
    dummy_df = pd.get_dummies(df, columns = model_constants.ENCODED_COLUMNS, drop_first = True)
    return dummy_df

def drop_non_modeling_columns(df):
    """
    Drops columns not used in modeling
    """
    return df.drop(columns = model_constants.DROP_COLUMNS)

def make_year_released_column(df):
    """
    Extracts the year released from the released_at column
    """
    df['year_released'] = df['released_at'].dt.year
    return df

def extract_legality_string(df, legality_to_abstract):
    """
    Extract categorial data from the legalities column and creates a new 
    column for the card's legality
    """
    df[f"{legality_to_abstract}_legality"] = df['legalities'].apply(lambda r : r[legality_to_abstract])
    return df

def make_legality_columns(df):
    """
    Gets all the game rules and makes a legalities column
    """
    game_legalities = df.legalities.iloc[0].keys()
    for game_legality in game_legalities:
        df = extract_legality_string(df, game_legality)
    return df

def make_card_type_column(df):
    """
    Make a card types column that holds the basic card type value
    """
    card_cats = [
        'Card', 
        'Vanguard', 
        'Plane', 
        'Creature', 
        'Land', 
        'Enchantment', 
        'Artifact', 
        'Sorcery', 
        'Instant', 
        'Legendary', 
        'Token'
    ]
    df['card_type'] = 'other_type'
    for card_cat in card_cats:
        df.loc[df['type_line'].str.contains(card_cat).fillna(False), 'card_type'] = card_cat.lower()
    df.loc[df['type_line'].str.contains('Card // Card').fillna(False), 'card_type'] = 'split_card'
    return df

def make_list_to_str_columns(df):
    #relevant columns
    columns_to_make_strings = [
        'games', 
        'colors', 
        'color_identity', 
        'finishes', 
        'color_indicator', 
        'produced_mana', 
        'frame_effects',
        'promo_types'
    ]
    for col_name in columns_to_make_strings:
        #not all of the values are lists, so only join the list values 
        df[col_name] = df[col_name].apply(lambda r : '_'.join(r) if isinstance(r, list) else r)
        df[col_name] = df[col_name].apply(lambda r : 'none' if r == '' else r)
    return df