# COMP 370 Homework 5 - 311 Question Formulation

This a project looking at a [311 complaint dataset](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9) gathered by the city of New York.

This repo contains

-   Tools to:

    -   Filter and trim down the dataset
    -   Analyze the dataset

-   A report answering the 2 refined questions within

# Setup / Installation

## Trim dataset and add headers

### With a script

run `create_trimmed.sh <path/to/untarred/data>`

### Manually

To only get data from 2020

```shell
grep -P "^\d{8,10},\d{2}/\d{2}/2020" <data> > output.csv
```

Add headers to csv file (one file already exists in /data)

```shell
cat headers.csv > <newfile> && cat output.csv >> <newfile>
```
