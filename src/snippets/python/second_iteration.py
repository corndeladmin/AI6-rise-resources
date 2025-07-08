import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    # Load the dataset
    cuisines_df: pd.DataFrame = pd.read_csv("./cuisines.csv", index_col=0)

    # Get the list of unique cuisines
    target_cuisines: np.ndarray[str] = cuisines_df["cuisine"].unique()

    # For each cuisine, process and plot ingredient data
    for cuisine in target_cuisines:
        sorted_ingredients: pd.DataFrame = get_sorted_cuisine_ingredients(
            cuisines_df, cuisine
        )
        plot_cuisine_ingredients(sorted_ingredients, cuisine)


def get_sorted_cuisine_ingredients(
    df: pd.DataFrame,
    cuisine_name: str,
) -> pd.DataFrame:
    """
    Filters a DataFrame by cuisine and returns a sorted DataFrame of ingredient counts.
    """
    # Filter rows matching the given cuisine (case-insensitive)
    filtered = df[df["cuisine"].str.lower() == cuisine_name.lower()]

    # Sum the ingredient counts, dropping the 'cuisine' column
    ingredient_totals: pd.Series = (
        filtered
        .T
        .drop(["cuisine"])
        .sum(axis=1)
    )

    # Convert to DataFrame for plotting
    counts_df: pd.DataFrame = ingredient_totals.to_frame(name="value")

    # Keep only ingredients that are actually used
    present_ingredients: pd.DataFrame = counts_df[counts_df["value"] != 0]

    # Sort by frequency
    sorted_ingredients = present_ingredients.sort_values(by="value", ascending=False)

    return sorted_ingredients


def plot_cuisine_ingredients(
    df_to_plot: pd.DataFrame, cuisine_name: str, top_n: int = 10
) -> None:
    """
    Plots the top N most common ingredients for a given cuisine.
    """
    # Get plot title
    title: str = f"Top {top_n} Most Common {cuisine_name.capitalize()} Ingredients"

    # Plot horizontal bar chart
    df_to_plot.head(top_n).plot.barh(title=title)
    plt.xlabel("Count")
    plt.ylabel("Ingredient")
    plt.gca().invert_yaxis()
    plt.show()


if __name__ == "__main__":
    main()
