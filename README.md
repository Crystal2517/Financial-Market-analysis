# Financial Market Analysis

I used Python to look at 30 years of financial data from 1995 to 2025. I wanted to practise working with a real dataset and see how different assets changed over time. I looked at the data, checked for missing values, calculated percentage changes and created a chart to compare the results.

## What I Analysed

I looked at:

* Apple
* Microsoft
* Amazon
* Tesla
* S&P 500
* Bitcoin
* Gold
* US Dollar

## Dataset

The dataset contains daily data from 1995 to 2025.

**Source:** Kaggle — Stock Market 30-yr Dataset (1995-2025) by Asim Islam. I used the `30_yr_market_data.csv` file from the dataset.

## What I Did

### 1. Explored the data

I used Pandas to look at the dataset and understand:

* How many rows and columns it had
* The types of data in each column
* The date range
* How much data was missing

The dataset contains **9,229 rows** and covers **January 1995 to December 2025**.

### 2. Looked at missing data

I checked how many values were missing for each asset.

I also checked when each asset first appeared in the dataset. This helped me understand that some missing values were there because certain assets didn't have data for the whole period.

For example, Tesla and Bitcoin have less data because they were added to the dataset later.

### 3. Calculated percentage changes

I used Pandas to calculate the percentage change between one value and the previous value. I did this for all eight assets so I could see how the values changed over time.

### 4. Compared the assets

I first compared each asset using its first and last available value. I then noticed that the assets didn't all have data for the same amount of time, so I created another comparison using **September 2014 to December 2025**.

This gave me:

| Asset     | Percentage change |
| --------- | ----------------: |
| Bitcoin   |        19,236.18% |
| Tesla     |         2,507.17% |
| Amazon    |         1,335.37% |
| Microsoft |         1,136.94% |
| Apple     |         1,118.02% |
| Gold      |           254.03% |
| S&P 500   |           244.54% |
| US Dollar |            15.99% |

These numbers are the change between the first and last available values during this period.

## Chart

I used **Matplotlib** to create a bar chart comparing the assets. Bitcoin's percentage change is much larger than the others, so it makes the difference between the assets very noticeable on the chart.

![Asset comparison chart](<img width="2906" height="1668" alt="image" src="https://github.com/user-attachments/assets/012097c5-7ae4-423a-99af-c72fc4f1d209" />)

## What I Learned

This project helped me practise:

* Python
* Pandas
* Matplotlib
* CSV files
* Looking through real datasets
* Finding and understanding missing data
* Working with dates
* Using loops
* Creating new columns
* Calculating percentage changes
* Creating DataFrames
* Sorting data
* Creating charts
* Understanding and explaining results

## Limitations

Things to keep in mind when looking at the results:

* The assets don't all have data going back to 1995.
* Different assets don't have data for every date e.g weekends and holidays
* The comparison only looks at the first and last available values.
* The assets are different types, so the results aren't a perfect comparison.

