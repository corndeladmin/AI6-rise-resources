import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cuisines: pd.DataFrame = pd.read_csv("./cuisines.csv", index_col=0)

indian_cuisines: pd.DataFrame = cuisines[cuisines["cuisine"] == "indian"]

ingredient_counts_series: pd.Series = indian_cuisines.T.drop(["cuisine"]).sum(axis=1)

indian_cuisine_counts: pd.DataFrame = ingredient_counts_series.to_frame("value")

indian_cuisine_present_ingredients: pd.DataFrame = indian_cuisine_counts[
    indian_cuisine_counts["value"] != 0
]

sorted_indian_cuisine_ingredients: pd.DataFrame = indian_cuisine_present_ingredients.sort_values(
    by="value", ascending=False
)

sorted_indian_cuisine_ingredients.head(10).plot.barh(
    title="Top 10 Most Common Indian Ingredients"
)
plt.xlabel("Count")
plt.ylabel("Ingredient")
plt.show()