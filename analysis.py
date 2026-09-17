# Financial market analysis 
# taking financial data, cleaning and analysisng financial data to identify patterns and trends
# visualising the results
import pandas as pd
import matplotlib.pyplot as plt # to create charts
data = pd.read_csv("data/30_yr_market_data.csv") # loads the data from the csv file
print(data.head()) # loads the first 5 rows og the csv file
data.info() # show information about the dataset

data["Date"] = pd.to_datetime(data["Date"]) # turns the date coloumn into real dates instead of a string
print(data["Date"].dtype) # double checks the date coloumn is now a date

print("Start date:", data["Date"].min()) # finds the earliest date in the dataset
print("End date:", data["Date"].max()) # finds the latest date in the dataset 

# investigate missing values
missing_values = data.isnull().sum() # counts the missing values in each coloumn
print(missing_values)
missing_percentage = (missing_values/len(data)) * 100 # finds the percentage of missing values for each column
missing_percentage = missing_percentage.sort_values(ascending = False) # sorts the missing percentages from highest to lowest 
print(missing_percentage)

first_tesla = data["Tesla"].first_valid_index() # finds the first row where tesla has a value
print("First tesla data:", data.loc[first_tesla, "Date"]) # locates the row and prints the value from the date column

first_apple = data["Apple"].first_valid_index() # comparing with apple to investigate the meaning of the missing data
print("First apple data:", data.loc[first_apple, "Date"])

first_missing_apple = data["Apple"].isnull().idxmax() # find the first row where apple is missing. isnull creates a list of missing values true means is missing idxmax finds the index of the first true value
print("First apple missing date:", data.loc[first_missing_apple, "Date"])

last_missing_apple = data.loc[data["Apple"].isnull(), "Date"].max() # finds the last date where apple is missing to see if the missing data from early on in the dataset or if there are missing values
print ("Last missing apple date:", last_missing_apple) 

apple_missing_dates =data.loc[data["Apple"].isnull(), "Date"] # shows all the dates where apple is missing 
print(apple_missing_dates.head(10)) # prints first and last 10 dates with missing values, to investigate why it was missing to help clean up data 
print(apple_missing_dates.tail(10))

# selecting assets for my analysis
assets = [
    "Apple",
    "Microsoft",
    "Amazon",
    "Tesla",
    "S&P500",
    "Bitcoin",
    "Gold",
    "US Dollar"
] 

analysis_data = data[["Date"] + assets] # creates a new dataset with the assests i want to analyse

print(analysis_data.head()) # printing first 5 rows to test it worked

for asset in assets: # loops through the assets to find the first date for each asset
    first_date = data[asset].first_valid_index()
    print("First", asset ,"date:", data.loc[first_date, "Date"])

for asset in assets: # calculates percentage change for each asset and returns it
    analysis_data[f"{asset} Return"] = analysis_data[asset].pct_change() # creates a new column each loop and calculates the percentage return for each asset
    print(analysis_data[["Date", asset, f"{asset} Return"]].head(10))

apple_return_comparison = analysis_data["Apple"].dropna()
first_apple_price = apple_return_comparison.iloc[0] # gives the first value 
last_apple_price = apple_return_comparison.iloc[-1] # gives the last value 
print("First apple value:" , first_apple_price)
print("last apple value:", last_apple_price)

# comparison over 30 year period
return_results = []
for asset in assets: # return comparison with all the assets from 1995
    available_values = analysis_data[asset].dropna()
    first_price = available_values.iloc[0]
    last_price = available_values.iloc[-1]

    price_change = last_price - first_price
    overall = price_change / first_price 
    overall_comparison = overall * 100
    return_results.append ({
        "Asset": asset,
        "Overall return" : overall_comparison
    })
    print (f"{asset} overall return:{overall_comparison}")

results = pd.DataFrame(return_results) # turned calculations into a dataframe 
results["Overall return"] = results["Overall return"].round(2) # makes data clearer by rounding to 2dp
results = results.sort_values("Overall return", ascending = False) # sorts the results from highest to lowest 
print(results)

# comparison from 2017-2025

comparison_start = pd.Timestamp("2014-09-17") # start date for fair comparison as bitcoins first available data was in 2014
comparison_data = analysis_data[
    analysis_data["Date"] >= comparison_start # checks if date is on or after september 2014, keeps only true
].copy() # creates dataframe called comparison_data 
print(comparison_data.head())

comparison_results=[]

for asset in assets:
    available_values = comparison_data[asset].dropna() # using comparison_data insead of analysis_data because we are calculating from a certain period
    first_price = available_values.iloc[0]
    last_price = available_values.iloc[-1]
    price_change = last_price - first_price
    overall = price_change /first_price 
    overall_comparison = overall * 100
    comparison_results.append({
        "Asset": asset,
        "Common period return": overall_comparison
    })
comparison_results =pd.DataFrame(comparison_results)
comparison_results["Common period return"] = comparison_results["Common period return"].round(2)
comparison_results = comparison_results.sort_values("Common period return", ascending=False)
print(comparison_results)



plt.bar(
    comparison_results["Asset"],
    comparison_results["Common period return"] 
) # this creates a chart of common period returns 

plt.title ("Asset returns from September 2014 to December 2025")
plt.xlabel("Asset")
plt.ylabel("Return (%) ")
plt.xticks(rotation=45) # makes asset names more readable 
plt.tight_layout() # makes the chart fit neatly 
plt.show() # shows chart 






