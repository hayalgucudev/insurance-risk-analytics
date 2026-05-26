"""
EDA utility functions.
"""

import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram(df, column):
    """
    Plot histogram for a column.
    """
    df[column].hist(bins=30)
    plt.title(f"{column} Distribution")
    plt.show()


def plot_boxplot(df, column):
    """
    Plot boxplot for outlier detection.
    """
    sns.boxplot(x=df[column])
    plt.title(f"{column} Boxplot")
    plt.show()
