from setuptools import setup, find_packages
import codecs
import argparse
import sys
import pandas as pd
from pathlib import Path

package_path = Path(__file__).parent.parent.parent
sys.path.append(str(package_path))

from src.util import printboo

def main():
    (df) = parseArgs()
    # print(df.info())
    pass


def parseArgs() -> pd.DataFrame:
    parser = argparse.ArgumentParser(description="WIP")
    parser.add_argument(
        "-i",
        help="the input csv file",
        required=True,
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
    )
    args = parser.parse_args()
    file = args.i
    df = pd.read_csv(file, encoding="utf-8")
    return df


if __name__ == "__main__":
    main()
