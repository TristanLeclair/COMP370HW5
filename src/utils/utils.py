from typing import Tuple
import sys
import argparse
import pandas as pd

def parseArgs(description = "Python script", output_default = "test.png") -> Tuple[pd.DataFrame, str]: 
    """Parse the input data and the output filename passed to the script"""
    parser = argparse.ArgumentParser(
        description=description
    )
    parser.add_argument(
        "-i",
        help="the input csv file",
        required=True,
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
    )
    parser.add_argument(
        "-o", help="the output png file", required=False, default=output_default
    )
    args = parser.parse_args()
    file = args.i
    output = args.o
    df = pd.read_csv(file, encoding="utf-8")
    return (df, output)
