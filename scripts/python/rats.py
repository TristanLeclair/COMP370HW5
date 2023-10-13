import sys
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt
import datetime as datetime
from pathlib import Path

package_path = Path(__file__).parent.parent.parent
sys.path.insert(0, str(package_path))

from src.utils.utils import parseArgs


def main():
    (df, output) = parseArgs(
        description="Generate a graph depicting the most common locations for rodent complaints"
    )
    df_grouped = group_by_location_type(df)

    df_trimmed = trim(df_grouped)

    plot(df_trimmed, output)

    pass


def trim(df: pd.DataFrame) -> pd.DataFrame:
    df_trimmed = df.copy()
    # trim the data only incidents that have at least 10% as many as the most common
    df_trimmed = df_trimmed[df_trimmed["count"] >= (df_trimmed["count"].max() * 0.05)]
    return df_trimmed


def group_by_location_type(df: pd.DataFrame) -> pd.DataFrame:
    df_grouped = df.copy().groupby(["Location Type"]).size().reset_index(name="count")
    # rank by count
    df_grouped = df_grouped.sort_values(by=["count"], ascending=False)
    print(df_grouped.head(10))
    return df_grouped


def plot(df: pd.DataFrame, output: str):
    # plt.rcParams["figure.figsize"] = (20, 15)
    # plt.tight_layout()
    plt.figure(constrained_layout=True)

    plt.title("Most common locations for rodent complaints")
    # label axes
    plt.xlabel("Location Type")
    plt.ylabel("Count")
    plt.bar(df["Location Type"], df["count"])
    # show the count on top of the bar
    for p in plt.gca().patches:
        plt.gca().annotate(
            str(p.get_height()),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, 10),
            textcoords="offset points",
        )
    # angle the x-axis labels
    plt.xticks(rotation=45)
    plt.savefig(output)


if __name__ == "__main__":
    main()
