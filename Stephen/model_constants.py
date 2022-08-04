# model_constants.py This file holds some of the 
# constants that will be used in model.py; 
# note: this is mainly to clean up the top of the 
# model.py file


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
    'legalities'
]

# columns that will be encoded
ENCODED_COLUMNS = [
    'lang',
    'layout',
    'image_status',
    'power',
    'toughness',
    'colors',
    'color_identity',
    'games',
    'finishes',
    'set_name',
    'set_type',
    'collector_number',
    'rarity',
    'artist',
    'border_color',
    'frame',
    'promo_types',
    'security_stamp',
    'produced_mana',
    'watermark',
    'frame_effects',
    'loyalty',
    'printed_name',
    'color_indicator',
    'flavor_name',
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