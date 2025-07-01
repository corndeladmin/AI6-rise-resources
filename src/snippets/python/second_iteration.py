import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    cuisines_df: pd.DataFrame = pd.read_csv("./cuisines.csv", index_col=0)
    target_cuisines: np.ndarray[str] = cuisines_df["cuisine"].unique()

    for cuisine in target_cuisines:
        sorted_cuisine_ingredients: pd.DataFrame = get_sorted_cuisine_ingredients(
            cuisines_df, cuisine
        )
        plot_cuisine_ingredients(sorted_cuisine_ingredients, cuisine)


def get_sorted_cuisine_ingredients(
    df: pd.DataFrame,
    cuisine_name: str,
) -> pd.DataFrame:
    """
    Filters a DataFrame by cuisine and returns a sorted DataFrame of ingredient counts.
    """
    filtered_by_cuisine = df[df["cuisine"].str.lower() == cuisine_name.lower()]

    ingredient_counts_series: pd.Series = filtered_by_cuisine.T.drop(["cuisine"]).sum(
        axis=1
    )
    cuisine_counts: pd.DataFrame = ingredient_counts_series.to_frame("value")

    present_ingredients: pd.DataFrame = cuisine_counts[cuisine_counts["value"] != 0]

    sorted_ingredients: pd.DataFrame = present_ingredients.sort_values(
        by="value", ascending=False
    )

    return sorted_ingredients


def plot_cuisine_ingredients(
    df_to_plot: pd.DataFrame, cuisine_name: str, top_n: int = 10
) -> None:
    """
    Plots the top N most common ingredients for a given cuisine.
    """
    title: str = f"Top {top_n} Most Common {cuisine_name.capitalize()} Ingredients"
    df_to_plot.head(top_n).plot.barh(title=title)
    plt.xlabel("Count")
    plt.ylabel("Ingredient")
    plt.gca().invert_yaxis()
    plt.show()


if __name__ == "__main__":
    main()