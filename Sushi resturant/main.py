import pandas

data = pandas.read_csv("Sales.csv")

#Canada
data_Canada = data[data.location == "Canada"]
sales_Canada = data_Canada.sales.sum()
data_Canada.to_csv("reports/Data_Canada.csv")

#United States
data_United_States = data[data.location == "United States"]
sales_United_States = data_United_States.sales.sum()
data_United_States.to_csv("reports/Data_United_States.csv")

#United Kingdom
data_United_Kingdom = data[data.location == "United Kingdom"]
sales_United_kingdom = data_United_Kingdom.sales.sum()
data_United_Kingdom.to_csv("reports/Data_United_Kingdom.csv")

#Germany
data_Germany = data[data.location == "Germany"]
sales_Germany = data_Germany.sales.sum()
data_Germany.to_csv("reports/Data.Germany.csv")

# Groupby metrics
grouped = data.groupby("location")["sales"].sum()
grouped.to_csv("reports/Cities_Sales.csv")

median = data.groupby("location")["sales"].median()
median.to_csv("reports/Median_sales.csv")

mean = data.groupby("location")["sales"].mean()
mean.to_csv("reports/Mean_sales.csv")
