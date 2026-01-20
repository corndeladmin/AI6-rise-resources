import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    # Load the dataset
    cuisines_df: pd.DataFrame = pd.read_csv("./cuisines.csv")

    # Get the list of unique cuisines
    target_cuisines: np.ndarray[str] = cuisines_df["cuisine"].unique()

    # For each cuisine, process and plot ingredient data
    for cuisine in target_cuisines:
        sorted_ingredients: pd.Series = get_sorted_cuisine_ingredients(
            cuisines_df, cuisine
        )
        plot_cuisine_ingredients(sorted_ingredients, cuisine)


def get_sorted_cuisine_ingredients(
    df: pd.DataFrame,
    cuisine_name: str,
) -> pd.Series:
    """
    Filters a DataFrame by cuisine and returns a sorted Series of ingredient counts.
    """
    # Filter rows matching the given cuisine (case-insensitive)
    filtered: pd.DataFrame = df[df["cuisine"].str.lower() == cuisine_name.lower()]

    # Count how many recipes use each ingredient
    ingredient_counts: pd.Series = filtered.groupby("ingredient").size()

    # Sort by frequency
    sorted_ingredients: pd.Series = ingredient_counts.sort_values(ascending=False)

    return sorted_ingredients


def plot_cuisine_ingredients(
    ingredients: pd.Series, cuisine_name: str, top_n: int = 10
) -> None:
    """
    Plots the top N most common ingredients for a given cuisine.
    """
    # Get plot title
    title: str = f"Top {top_n} Most Common {cuisine_name.capitalize()} Ingredients"

    # Plot horizontal bar chart
    ingredients.head(top_n).plot.barh(title=title)
    plt.xlabel("Count")
    plt.ylabel("Ingredient")
    plt.gca().invert_yaxis()
    plt.show()


if __name__ == "__main__":
    main()
