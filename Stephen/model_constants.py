# model_constants.py This file holds some of the 
# constants that will be used in model.py; 
# note: this is mainly to clean up the top of the 
# model.py file

from sklearn.neighbors import RadiusNeighborsRegressor, KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression, LassoLars
from sklearn.svm import LinearSVR
from sklearn.ensemble import RandomForestRegressor
# ensures that the models are always the same as in the notebook
RAND_SEED = 1729 

### MODEL CONSTANTS

# holds all the models that are made by the model maker
MODELS = [
    {
        'name':'DecisionTreeRegressor',
        'model':DecisionTreeRegressor(random_state = RAND_SEED)
    },
    {
        'name':'LinearSVR',
        'model':LinearSVR()
    },
    {
        'name':'LinearRegression',
        'model':LinearRegression()
    },
    {
        'name':'LassoLars',
        'model':LassoLars()
    },
    {
        'name':'RadiusNeighborsRegressor',
        'model':RadiusNeighborsRegressor(radius = 5)
    },
    {
        'name':'RadiusNeighborsRegressor_weighted',
        'model':RadiusNeighborsRegressor(radius = 5, weights='distance')
    },
    {
        'name':'KNeighborsRegressor',
        'model':KNeighborsRegressor()
    },
    {
        'name':'KNeighborsRegressor_weighted',
        'model':KNeighborsRegressor(weights = 'distance')
    },
    {
        'name':'RandomForestRegressor',
        'model':RandomForestRegressor(random_state = RAND_SEED)
    }
]

### GROUPS OF COLUMNS TO PREPARE DATAFRAME FOR MODELING

#columns that will not be used in models
DROP_COLUMNS = [
    'mana_cost',
    'oracle_text',
    'type_line',
    'keywords',
    'set_id',
    'set',
    'flavor_text',
    'prices',
    'released_at',
    'legalities',
    'artist',
    'power',
    'toughness',
    'collector_number'
]

# columns that will be encoded
ENCODED_COLUMNS = [
    'lang',
    # 'layout',
    # 'image_status',
    'colors',
    # 'color_identity',
    'games',
    'finishes',
    # 'set_name',
    'set_type',
    'rarity',
    'border_color',
    'frame',
    'promo_types',
    'security_stamp',
    'produced_mana',
    'watermark',
    'frame_effects',
    'loyalty',
    # 'printed_name',
    'color_indicator',
    # 'flavor_name',
    'standard_legality',
    'future_legality',
    'historic_legality',
    'gladiator_legality',
    'pioneer_legality',
    'explorer_legality',
    'modern_legality',
    'legacy_legality',
    'pauper_legality',
    'vintage_legality',
    'penny_legality',
    'commander_legality',
    'brawl_legality',
    'historicbrawl_legality',
    'alchemy_legality',
    'paupercommander_legality',
    'duel_legality',
    'oldschool_legality',
    'premodern_legality',
    'card_type'
]

# contains the columns that will be scaled
SCALED_COLUMNS = [
    'cmc', 
    'life_modifier', 
    'hand_modifier',
    'edhrec_rank', 
    'penny_rank'
]
#for now, drop them
DROP_COLUMNS += SCALED_COLUMNS

#testing to drop more columns:
DROP_COLUMNS += [   
    'layout',
    'image_status',
    'flavor_name',
    'printed_name',
    'set_name',
    'color_identity'
]