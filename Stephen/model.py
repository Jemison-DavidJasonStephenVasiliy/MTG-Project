#for RMSE metric
from math import sqrt
from itertools import product

#handle dataframes
import pandas as pd

#for plotting
import seaborn as sns
import matplotlib.pyplot as plt

#for calulating metrics
from scipy import stats
import sklearn.metrics as metrics

# for feature selection over models
from sklearn.feature_selection import SelectKBest, f_regression

# models used
from sklearn.neighbors import RadiusNeighborsRegressor, KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import LinearSVR
import xgboost as xgb

# for clustering
from sklearn.cluster import Birch

#constants used from the file
import model_constants

### GLOBAL CONSTANTS

# ensures that the models are always the same as in the notebook
RAND_SEED = 1729

### FINAL MODEL

def final_model(train, validate, test):
    """
    Takes in all three data subsets and returns the metrics for the final model along with predictions of test
    """
    outputs = list()
    #split the data into X an y
    X_train, y_train, X_val, y_val = make_X_and_y(train, validate)
    _, _, X_test, y_test = make_X_and_y(train, test)
    # get columns to model on
    cols_model = select_k_best(X_train, y_train, 250)
    # get predictions from the model
    train_predict, validate_predict, test_predict = make_final_model(
                                                                    X_train[cols_model], 
                                                                    y_train, 
                                                                    X_val[cols_model], 
                                                                    y_val, 
                                                                    X_test[cols_model], 
                                                                    y_test
                                                                    )
    #calculate the residual
    test_predict['residual'] = test_predict['predicted'] - test_predict['usd']
    #get evaluations
    output = evaluate_final_model(train_predict, validate_predict, test_predict)
    outputs.append(output)
    return outputs, test_predict
    
def make_final_model(X_train, y_train, X_val, y_val, X_test, y_test):
    """
    Creates the final RadomForestRegressor and predicts on all three data sets
    """
    #make and fit model
    model = RandomForestRegressor(random_state = RAND_SEED)
    model = model.fit(X_train, y_train['usd'])
    #get predictions
    y_train['predicted'] = model.predict(X_train)
    y_val['predicted'] = model.predict(X_val)
    y_test['predicted'] = model.predict(X_test)
    return y_train, y_val, y_test

def evaluate_final_model(train_pred, val_pred, test_pred):
    """
    Calculates the final model's metrics for evaluation
    """
    #calculate the metrics to evaluate
    mae_train = metrics.mean_absolute_error(train_pred['usd'], train_pred['predicted'])
    mae_validate = metrics.mean_absolute_error(val_pred['usd'], val_pred['predicted'])
    mae_test = metrics.mean_absolute_error(test_pred['usd'], test_pred['predicted'])
    #store in a dictionary and return to call
    model_metrics = {
        'model':'RandomForestRegressor',
        'train_MAE':mae_train,
        'train_within_a_dime': (abs(train_pred['predicted'] - train_pred['usd']) < 0.11).mean(),
        'validate_MAE':mae_validate,
        'validate_within_a_dime': (abs(val_pred['predicted'] - val_pred['usd']) < 0.11).mean(),
        'test_MAE':mae_test,
        'test_within_a_dime':(abs(test_pred['predicted'] - test_pred['usd']) < 0.11).mean()
    }
    return model_metrics

def residual_plot(df):
    """
    Plot the residuals of the final model
    """
    plt.figure(figsize = (10,10))
    sns.scatterplot(data=df, x = 'usd', y = 'residual')
    plt.title('Plot of final model residuals')
    plt.xlabel('USD Price')
    plt.ylabel('Residual')
    plt.show()
    
### MODEL TIER TWO

def make_models_features(train, validate, return_predictions=False):
    """
    Make the models and test out the best features and their effect
    """
    outputs = list()
    train_predictions = train[['id', 'name', 'usd']].copy()
    validate_predictions = validate[['id', 'name', 'usd']].copy()
    #make baseline to compare
    output_mean, output_median = make_baseline_model(train, validate)
    outputs.append(output_mean)
    outputs.append(output_median)
    #split into X and y
    X_train, y_train, X_val, y_val = make_X_and_y(train, validate)
    #get the columns to model on 
    cols_to_model = get_k_best_columns(X_train, y_train)
    #loop through the sets of columns
    for col_subset in cols_to_model:
        #get column subsets
        X_train_subset = X_train[col_subset]
        X_val_subset = X_val[col_subset]
        #make the models and save the output
        output = make_linearSVR(X_train_subset, y_train, X_val_subset, y_val, return_predictions = False)
        outputs.append(output)
        output = make_kneighbors_model_weighted(X_train_subset, y_train, X_val_subset, y_val, return_predictions = False)
        outputs.append(output)
        output = make_decisiontree_regressor(X_train_subset, y_train, X_val_subset, y_val, return_predictions = False)
        outputs.append(output)
        output = make_randomforest_regressor(X_train_subset, y_train, X_val_subset, y_val, return_predictions = False)
        outputs.append(output)
    if return_predictions:
        return outputs, train_predictions, validate_predictions
    else:
        return outputs
    
def make_kneighbors_model_weighted(X_train, y_train, X_val, y_val, return_predictions = True):
    """
    Fit and predict on the kneighbors model
    """
    #make the model and fit it
    nn = KNeighborsRegressor(weights = 'distance')
    nn = nn.fit(X_train, y_train['usd'])
    #get predictions
    y_train['predicted'] = nn.predict(X_train)
    y_val['predicted'] = nn.predict(X_val)
    #evaluate
    output = evaluate_train_validate_model(y_train, y_val, 'KNeighborsRegressor_weighted')
    output['kbest_features'] = X_train.shape[1]
    if return_predictions:
        return output, y_train, y_val
    else:
        return output
    
def make_linearSVR(X_train, y_train, X_val, y_val, return_predictions = True):
    """
    Fit and predict on the linear svr model
    """
    #make and fit the model
    model = LinearSVR()
    model = model.fit(X_train, y_train['usd'])
    #get predicitons
    y_train['predicted'] = model.predict(X_train)
    y_val['predicted'] = model.predict(X_val)
    #evaluate
    output = evaluate_train_validate_model(y_train, y_val, f'LinearSVR')
    output['kbest_features'] = X_train.shape[1]
    if return_predictions:
        return output, y_train, y_val
    else:
        return output
    
def make_decisiontree_regressor(X_train, y_train, X_val, y_val, return_predictions = True):
    """
    fit and predict on the decision tree model
    """
    #make the model and fit it
    dt = DecisionTreeRegressor(random_state = RAND_SEED)
    dt = dt.fit(X_train, y_train['usd'])
    #predict
    y_train['predicted'] = dt.predict(X_train)
    y_val['predicted'] = dt.predict(X_val)
    #evaluate
    output = evaluate_train_validate_model(y_train, y_val, 'DecisionTreeRegresson')
    output['kbest_features'] = X_train.shape[1]
    if return_predictions:
        return output, y_train, y_val
    else:
        return output

def make_randomforest_regressor(X_train, y_train, X_val, y_val, return_predictions = True):
    """
    Fit and predict on a random forest model
    """
    #make the model and fit it
    rf = RandomForestRegressor(random_state = RAND_SEED)
    rf = rf.fit(X_train, y_train['usd'])
    #predict the model
    y_train['predicted'] = rf.predict(X_train)
    y_val['predicted'] = rf.predict(X_val)
    # evaluate the model
    output = evaluate_train_validate_model(y_train, y_val, 'RandomForestRegression')
    output['kbest_features'] = X_train.shape[1]
    if return_predictions:
        return output, y_train, y_val
    else:
        return output

### SELECT KBEST COLUMNS

def select_k_best(X_train, y_train, k_select):
    """
    get the select the k best features
    """
    #make the selector
    f_selector = SelectKBest(f_regression, k=k_select)
    #fit the selector
    f_selector = f_selector.fit(X_train, y_train['usd'])
    #get the columns
    f_support = f_selector.get_support()
    return X_train.loc[:,f_support].columns.to_list()

def get_k_best_columns(X_train, y_train, k_select_min = 100, k_select_max = 300):
    """
    Get sets of the k best columns
    """
    column_sets_for_modeling = []
    for i in range(k_select_min, k_select_max+50, 50):
        column_sets_for_modeling.append(select_k_best(X_train, y_train, i))
    return column_sets_for_modeling
    
### MODEL TIER ONE
### The models used and in model_constants.MODELS as a list of dictionaries
    
def model_loop(train, validate):
    """
    Testsa a series of algorithms and evaluates them
    """
    outputs = []
    #make baseline model
    output_mean, output_median = make_baseline_model(train, validate)
    outputs.append(output_mean)
    outputs.append(output_median)
    #split the data into X and y
    X_train, y_train, X_val, y_val = make_X_and_y(train, validate)
    for model_item in model_constants.MODELS:
        #get model and its evaluation
        output = make_model(X_train, y_train, X_val, y_val, model_item['model'], model_item['name'])
        outputs.append(output)
    return outputs

def make_model(X_train, y_train, X_val, y_val, model, model_name):
    """
    Makes a model and predicts on it
    """
    #fit model
    model = model.fit(X_train, y_train['usd'])
    #predict
    y_train['predicted'] = model.predict(X_train)
    y_val['predicted'] = model.predict(X_val)
    #evaluate
    output = evaluate_train_validate_model(y_train, y_val, model_name)
    return output 

### FUNCTIONS TO MAKE COLUMNS FOR MODEL

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
    df = cap_high_usd(df)
    # transform by encoding 
    df = encode_columns(df)
    # make cluster features
    df = make_multi_clusters(df, Birch, 'birch')
    return df

def cap_high_usd(df):
    #cap the highest usd price to 200
    df.loc[df.usd > 200, 'usd'] = 200
    return df

def add_cluster_column(df, cluster_algo, algo_name):
    """
    adds a feature column using clusters
    """
    #make clusters
    algo = cluster_algo
    algo = algo.fit(df.loc[:, ~df.columns.isin(['id', 'name', 'usd'])])
    preds = algo.predict(df.loc[:, ~df.columns.isin(['id', 'name', 'usd'])])
    score = metrics.silhouette_score(df.loc[:, ~df.columns.isin(['id', 'name', 'usd'])], preds)
    output = {
        'model_name': algo_name,
        'score': score
    }
    return output, preds

def make_multi_clusters(df, model, model_name):
    """
    makes a series of clusters to model on using all features except the target and id columns
    """
    outputs = list()
    df_preds = df[['id', 'name', 'usd']]
    for num_clusters in range(5, 7):
        output, preds = add_cluster_column(df, model(n_clusters = num_clusters), f"{model_name}_{num_clusters}")
        outputs.append(output)
        df[f"{model_name}_{num_clusters}"] = preds
    return df

def make_X_and_y(train, validate):
    """
    Scales the columns for modeling based off of the list in model_constants,
    then make the X and y sets for train and validate
    """
    #drop the target variable, usd
    X_train = train.drop(columns=['id', 'name', 'usd'])
    X_val = validate.drop(columns=['id', 'name', 'usd'])
    y_train = train[['id', 'name', 'usd']]
    y_val = validate[['id', 'name', 'usd']]
    return X_train, y_train, X_val, y_val

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
    """
    Evaluates train and validate models and produces a dictionary of metrics
    """
    #calculate the metrics to evaluate
    mae_train = metrics.mean_absolute_error(model_train['usd'], model_train['predicted'])
    mae_validate = metrics.mean_absolute_error(model_validate['usd'], model_validate['predicted'])
    #store in a dictionary and return to call
    model_metrics = {
        'model':model_name,
        'train_MAE':mae_train,
        'train_within_a_dime': (abs(model_train['predicted'] - model_train['usd']) < 0.11).mean(),
        'validate_MAE':mae_validate,
        'validate_within_a_dime': (abs(model_validate['predicted'] - model_validate['usd']) < 0.11).mean()
    }
    return model_metrics
