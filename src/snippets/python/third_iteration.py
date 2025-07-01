import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging
import logging.config
import json
from typing import Tuple


LOGGING_CONFIG_FILE = "logging-config.json"

logger = logging.getLogger("")


def main():
    logger.info("--- Cuisine Analysis Script Started ---")

    try:
        cuisines_df: pd.DataFrame = pd.read_csv("./cuisines.csv", index_col=0)
        logger.info("Cuisines dataset loaded successfully.")
    except Exception as e:
        logger.critical(
            f"An unexpected error occurred while loading 'cuisines.csv': {e}",
            exc_info=True,
        )
        return

    target_cuisines: Tuple[str, ...] = tuple(cuisines_df["cuisine"].unique()) + (
        "nonexistent_cuisine ;)",
    )

    logger.info(f"Identified target cuisines: {', '.join(target_cuisines)}")

    for cuisine in target_cuisines:
        logger.info(f"Initiating analysis for cuisine: '{cuisine}'.")
        sorted_cuisine_ingredients: pd.DataFrame = get_sorted_cuisine_ingredients(
            cuisines_df, cuisine
        )

        plot_cuisine_ingredients(sorted_cuisine_ingredients, cuisine)

    logger.info("--- Cuisine Analysis Script Finished ---")


def get_sorted_cuisine_ingredients(
    df: pd.DataFrame,
    cuisine_name: str,
) -> pd.DataFrame:
    """
    Filters a DataFrame by cuisine and returns a sorted DataFrame of ingredient counts.
    """
    logger.info(f"Processing ingredients for cuisine: '{cuisine_name}'.")

    filtered_by_cuisine = df[df["cuisine"].str.lower() == cuisine_name.lower()]

    if filtered_by_cuisine.empty:
        logger.warning(
            f"No data found for cuisine: '{cuisine_name}'. Returning empty DataFrame."
        )
        return pd.DataFrame()

    logger.debug(f"Found {len(filtered_by_cuisine)} rows for '{cuisine_name}'.")

    ingredient_counts_series: pd.Series = filtered_by_cuisine.T.drop(
        ["cuisine"], errors="ignore"
    ).sum(axis=1)
    cuisine_counts: pd.DataFrame = ingredient_counts_series.to_frame("value")

    present_ingredients: pd.DataFrame = cuisine_counts[cuisine_counts["value"] != 0]
    logger.debug(
        f"Identified {len(present_ingredients)} present ingredients for '{cuisine_name}'."
    )

    sorted_ingredients: pd.DataFrame = present_ingredients.sort_values(
        by="value", ascending=False
    )

    logger.info(f"Successfully sorted ingredients for '{cuisine_name}'.")

    return sorted_ingredients


def plot_cuisine_ingredients(
    df_to_plot: pd.DataFrame, cuisine_name: str, top_n: int = 10
) -> None:
    """
    Plots the top N most common ingredients for a given cuisine.
    """
    logger.info(f"Attempting to plot top {top_n} ingredients for '{cuisine_name}'.")

    if df_to_plot.empty:
        logger.warning(
            f"Skipping plot for '{cuisine_name}': DataFrame to plot is empty."
        )
        return

    title: str = f"Top {top_n} Most Common {cuisine_name.capitalize()} Ingredients"

    try:
        df_to_plot.head(top_n).plot.barh(title=title)
        plt.xlabel("Count")
        plt.ylabel("Ingredient")
        plt.gca().invert_yaxis()
        plt.show()
        logger.info(f"Plot displayed successfully for '{cuisine_name}'.")
    except Exception as e:
        logger.error(
            f"Failed to plot ingredients for '{cuisine_name}': {e}", exc_info=True
        )


if __name__ == "__main__":

    try:
        with open(LOGGING_CONFIG_FILE, "r") as f:
            config_dict = json.load(f)
        logging.config.dictConfig(config_dict)
        logger.info(f"Logging configured successfully from {LOGGING_CONFIG_FILE}.")
    except Exception as e:
        print(f"An unexpected error occurred during logging setup: {e}")
        exit(1)

    main()
