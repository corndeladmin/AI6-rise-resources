import pandas as pd
import numpy as np

# Our Pokemon team data, where types are currently just codes
pokemon_team = pd.DataFrame(
    {
        "Pokedex_Number": [1, 4, 7, 25, 6],
        "Type_Code": ["GRS01", "FIR02", "WTR03", "ELE04", "FIR02"],
    }
)

# Pokemon Type Decoder Dictionary, translating codes to full names
pokemon_type_decoder = {
    "GRS01": "Grass",
    "FIR02": "Fire",
    "WTR03": "Water",
    "ELE04": "Electric",
}

# Series.map(): Used for substituting each value in a Series with another value, that may be derived from a function, a dict or a Series.
pokemon_team["Type_Name"] = pokemon_team["Type_Code"].map(pokemon_type_decoder)

print(pokemon_team)

#    Pokedex_Number Type_Code Type_Name
# 0               1     GRS01     Grass
# 1               4     FIR02      Fire
# 2               7     WTR03     Water
# 3              25     ELE04  Electric
# 4               6     FIR02      Fire
