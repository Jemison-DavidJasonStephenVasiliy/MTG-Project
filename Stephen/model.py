from math import sqrt

import pandas as pd
from scipy import stats
import sklearn.metrics as metrics
from sklearn.neighbors import RadiusNeighborsRegressor, KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression, LassoLars
from sklearn.svm import LinearSVR

import model_constants

### GLOBAL CONSTANTS

# ensures that the models are always the same as in the notebook
RAND_SEED = 1729 

#sets up the model strategies
MODEL_STRATEGY_DICTIONARY = {
}

#holds the model strategy types
MODEL_STRATEGIES = []

### MODEL MAKER

def model_maker(train, validate, return_predictions = False):
    outputs = []
    train_predictions = train[['id', 'usd']].copy()
    validate_predictions = validate[['id', 'usd']].copy()
    #make baseline model
    output_mean, output_median = make_baseline_model(train, validate)
    outputs.append(output_mean)
    outputs.append(output_median)
    X_train, y_train, X_val, y_val = scale_and_make_X_and_y(train, validate)
    # make a simple linear svr
    output_lsvr = make_linearsvr_model(X_train, y_train, X_val, y_val, return_predictions = return_predictions)
    outputs.append(output_lsvr)
    return outputs

def test_model_function(train, validate):
    outputs = [] 
    train_predictions = train[['id', 'usd']].copy()
    validate_predictions = validate[['id', 'usd']].copy()
    #make baseline model
    output_mean, output_median = make_baseline_model(train, validate)
    outputs.append(output_mean)
    outputs.append(output_median)
    #add model
    X_train, y_train, X_val, y_val = scale_and_make_X_and_y(train, validate)
    output = make_decisiontree_model_weighted(X_train, y_train, X_val, y_val, return_predictions = False)
    outputs.append(output)
    return outputs

### MODEL FUNCTIONS

def model_loop(train, validate, return_predictions = True):
    outputs = []
    train_predictions = train[['id', 'name', 'usd']].copy()
    validate_predictions = validate[['id', 'name', 'usd']].copy()
    #make baseline model
    output_mean, output_median = make_baseline_model(train, validate)
    outputs.append(output_mean)
    outputs.append(output_median)
    X_train, y_train, X_val, y_val = scale_and_make_X_and_y(train, validate)
    for model_item in model_constants.MODELS:
        output, train_predict, val_predict = make_model(X_train, y_train, X_val, y_val, model_item['model'], model_item['name'], return_predictions = return_predictions)
        train_predictions[f"{model_item['name']}_predictions"] = train_predict['predicted']
        validate_predictions[f"{model_item['name']}_predictions"] = val_predict['predicted']
        outputs.append(output)
    if return_predictions:
        return outputs, train_predictions, validate_predictions
    else:
        return outputs

def make_model(X_train, y_train, X_val, y_val, model, model_name, return_predictions = True):
    model = model.fit(X_train, y_train['usd'])
    y_train['predicted'] = model.predict(X_train)
    y_val['predicted'] = model.predict(X_val)
    output = evaluate_train_validate_model(y_train, y_val, model_name)
    if return_predictions:
        return output, y_train, y_val
    else:
        return output 

### BASELINE MODEL

def make_baseline_model(train, validate, return_df = False):
    """
    Creates two baseline model, one based on mean and one based on median.  Returns a dataframe
    Containing their evaluation metrics.
    """
    outputs = []
    baseline_model_mean = train.loc[:, ['id', 'usd']]
    baseline_model_median = train.loc[:, ['id', 'usd']]
    baseline_model_val_mean = validate.loc[:, ['id', 'usd']]
    baseline_model_val_median = validate.loc[:, ['id', 'usd']]
    baseline_model_mean['predicted'] = train.usd.mean()
    baseline_model_median['predicted'] = train.usd.median()
    baseline_model_val_mean['predicted'] = train.usd.mean()
    baseline_model_val_median['predicted'] = train.usd.median()
    output_mean = evaluate_train_validate_model(baseline_model_mean, baseline_model_val_mean, 'baseline_mean')
    output_median = evaluate_train_validate_model(baseline_model_median, baseline_model_val_median, 'baseline_median')
    if return_df:
        return pd.DataFrame([output_mean, output_median])
    else:
        return output_mean, output_median

### MODEL EVALUATION FUNCTION

def evaluate_train_validate_model(model_train, model_validate, model_name):
    #calculate the metrics to evaluate
    mse2_train = metrics.mean_squared_error(model_train['usd'], model_train['predicted'])
    mse2_validate = metrics.mean_squared_error(model_validate['usd'], model_validate['predicted'])
    r2_train = metrics.r2_score(model_train['usd'], model_train['predicted'])
    r2_validate = metrics.r2_score(model_validate['usd'], model_validate['predicted'])
    evs_train = metrics.explained_variance_score(model_train['usd'], model_train['predicted'])
    evs_validate = metrics.explained_variance_score(model_validate['usd'], model_validate['predicted'])
    #store in a dictionary and return to call
    model_metrics = {
        'model':model_name,
        'train_RMSE':sqrt(mse2_train),
        'train_r2':r2_train,
        'train_explained_variance':evs_train,
        'validate_RMSE':sqrt(mse2_validate),
        'validate_r2':r2_validate,
        'validate_explained_variance':evs_validate
    }
    return model_metrics

### FUNCTIONS TO MAKE COLUMNS FOR MODEL

def scale_and_make_X_and_y(train, validate):
    """
    Scales the columns for modeling based off of the list in model_constants,
    then make the X and y sets for train and validate
    """
    #drop the target variable, usd
    X_train = train.drop(columns=['id', 'name', 'usd'])
    X_val = validate.drop(columns=['id', 'name', 'usd'])
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
    Flow control function to prepare the dataframe for modeling
    Note that the entire dataframe needs to be passed and then 
    split via the prepare file
    """
    # make/drop columns for the model
    df = make_legality_columns(df)
    df = make_card_type_column(df)
    df = make_list_to_str_columns(df)
    df = drop_non_modeling_columns(df)
    # transform by encoding and scaling
    df = encode_columns(df)
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

# # TREE MODELS

# def make_decisiontree_model_weighted(X_train, y_train, X_val, y_val, return_predictions = True):
#     dt = DecisionTreeRegressor()
#     dt = dt.fit(X_train, y_train['usd'])
#     y_train['predicted'] = dt.predict(X_train)
#     y_val['predicted'] = dt.predict(X_val)
#     output = evaluate_train_validate_model(y_train, y_val, 'DecisionTreeRegressor')
#     if return_predictions:
#         return output, y_train, y_val
#     else:
#         return output  

# # NEIGHBORS MODELS

# def make_kneighbors_model_weighted(X_train, y_train, X_val, y_val, return_predictions = True):
#     nn = KNeighborsRegressor(weights = 'distance')
#     nn = nn.fit(X_train, y_train['usd'])
#     y_train['predicted'] = nn.predict(X_train)
#     y_val['predicted'] = nn.predict(X_val)
#     output = evaluate_train_validate_model(y_train, y_val, 'KNeighborsRegressor_weighted')
#     if return_predictions:
#         return output, y_train, y_val
#     else:
#         return output  

# def make_kneighbors_model(X_train, y_train, X_val, y_val, return_predictions = True):
#     nn = KNeighborsRegressor()
#     nn = nn.fit(X_train, y_train['usd'])
#     y_train['predicted'] = nn.predict(X_train)
#     y_val['predicted'] = nn.predict(X_val)
#     output = evaluate_train_validate_model(y_train, y_val, 'KNeighborsRegressor')
#     if return_predictions:
#         return output, y_train, y_val
#     else:
#         return output    

# def make_radiusneighbors_model_weighted(X_train, y_train, X_val, y_val, return_predictions = True):
#     rn = RadiusNeighborsRegressor(radius = 5, weights = 'distance')
#     rn = rn.fit(X_train, y_train['usd'])
#     y_train['predicted'] = rn.predict(X_train)
#     y_val['predicted'] = rn.predict(X_val)
#     output = evaluate_train_validate_model(y_train, y_val, 'RadiusNeighborsRegressor_weighted')
#     if return_predictions:
#         return output, y_train, y_val
#     else:
#         return output

# def make_radiusneighbors_model(X_train, y_train, X_val, y_val, return_predictions = True):
#     rn = RadiusNeighborsRegressor(radius = 5)
#     rn = rn.fit(X_train, y_train['usd'])
#     y_train['predicted'] = rn.predict(X_train)
#     y_val['predicted'] = rn.predict(X_val)
#     output = evaluate_train_validate_model(y_train, y_val, 'RadiusNeighborsRegressor')
#     if return_predictions:
#         return output, y_train, y_val
#     else:
#         return output

# #LINEAR MODELS

# def make_linearsvr_model(X_train, y_train, X_val, y_val, return_predictions = True):
#     lsvr = LinearSVR()
#     lsvr = lsvr.fit(X_train, y_train['usd'])
#     y_train['predicted'] = lsvr.predict(X_train)
#     y_val['predicted'] = lsvr.predict(X_val)
#     output = evaluate_train_validate_model(y_train, y_val, 'LinearSVR')
#     if return_predictions:
#         return output, y_train, y_val
#     else:
#         return output
    
# def make_linear_regression_model(X_train, y_train, X_val, y_val, return_predictions = True):
#     lr = LinearRegression()
#     lr = lr.fit(X_train, y_train['usd'])
#     y_train['predicted'] = lr.predict(X_train)
#     y_val['predicted'] = lr.predict(X_val)
#     output = evaluate_train_validate_model(y_train, y_val, 'LinearRegression')
#     if return_predictions:
#         return output, y_train, y_val
#     else:
#         return output
    
# def make_lassor_lars(X_train, y_train, X_val, y_val, return_predictions = True):
#     llars = LassoLars()
#     llars = llars.fit(X_train, y_train['usd'])
#     y_train['predicted'] = llars.predict(X_train)
#     y_val['predicted'] = llars.predict(X_val)
#     output = evaluate_train_validate_model(y_train, y_val, 'LassoLars')
#     if return_predictions:
#         return output, y_train, y_val
#     else:
#         return output
