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
    (df, output) = parseArgs()
    df_grouped = group_by_month(df)

    df_noise = filter_noise(df_grouped)
    # order by month
    df_noise = df_noise.sort_values(by=["month", "count"], ascending=[True, False])

    plot(df_noise, output)

    pass


def plot(df_noise: pd.DataFrame, filename: str = "noise.png") -> None:
    """Plot the data and save as png"""
    # plot the data with matplotlib and output as png, create a subplot per month
    # make the plot bigger
    plt.rcParams["figure.figsize"] = (20, 15)
    fig = plt.figure()
    for i in df_noise["month"].unique():
        df_monthly = df_noise[df_noise["month"] == i]
        # aggregate the count per descriptor
        df_monthly = (
            df_monthly.groupby(["Descriptor"]).agg({"count": "sum"}).reset_index()
        )
        # sort by count
        df_monthly = df_monthly.sort_values(by=["count"], ascending=False)

        ax = fig.add_subplot(3, 4, int(i))

        ax.bar(x=df_monthly["Descriptor"], height=df_monthly["count"])
        ax.title.set_text(datetime.datetime.strptime(i, "%m").strftime("%B"))

        ax.set_xticks(df_monthly["Descriptor"])
        # spread out the x-axis labels
        ax.set_xticklabels(df_monthly["Descriptor"], rotation=45)
        # show the count on top of the bar
        for p in ax.patches:
            ax.annotate(
                str(p.get_height()),
                (p.get_x() + p.get_width() / 2.0, p.get_height()),
                ha="center",
                va="center",
                xytext=(0, 10),
                textcoords="offset points",
            )

    # more space between subplots
    plt.subplots_adjust(wspace=0.25, hspace=1.5)
    plt.savefig(filename)


def group_by_month(df: pd.DataFrame) -> pd.DataFrame:
    df["date"] = pd.to_datetime(df["Created Date"])
    df["month"] = df["date"].dt.strftime("%m")
    # count Complayint Type per month
    df_grouped = (
        df.copy()
        .groupby(["Complaint Type", "Descriptor", "month"])
        .size()
        .reset_index(name="count")
    )
    # rank by count
    df_grouped = df_grouped.sort_values(by=["month"], ascending=True)
    # then rank by count
    df_grouped = df_grouped.sort_values(by=["count"], ascending=False)
    return df_grouped


def filter_noise(df: pd.DataFrame) -> pd.DataFrame:
    df_noise = df[df["Complaint Type"].str.contains("Noise")]
    # only select top 5 Complaint Types per month
    df_noise = df_noise.groupby(["month"]).head(5)
    return df_noise


if __name__ == "__main__":
    main()
