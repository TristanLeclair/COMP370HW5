from pandas import DataFrame


def shrink_df(df: DataFrame) -> DataFrame:
    # Select only Complaint Type and Borough from dataframe
    df_shrink = df[["Complaint Type", "Borough"]].copy()
    return df_shrink
