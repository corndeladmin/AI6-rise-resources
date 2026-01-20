import pandas as pd
import matplotlib.pyplot as plt

cuisines: pd.DataFrame = pd.read_csv("./cuisines.csv")

indian_cuisines: pd.DataFrame = cuisines[cuisines["cuisine"] == "indian"]

indian_cuisine_ingredient_counts: pd.Series = indian_cuisines.groupby("ingredient").size()

sorted_ingredients: pd.Series = indian_cuisine_ingredient_counts.sort_values(ascending=False)

sorted_ingredients.head(10).plot.barh(title="Top 10 Most Common Indian Ingredients")
plt.xlabel("Count")
plt.ylabel("Ingredient")
plt.gca().invert_yaxis()
plt.show()
