import pandas
data=pandas.read_csv("Sales.csv")
grouped=data.groupby("location")["sales"].sum()
grouped.to_csv("reports/Cities_Sales.csv")
median=data.groupby("location")["sales"].median()
median.to_csv("reports/Median_sales.csv")
mean=data.groupby("location")["sales"].mean()
mean.to_csv("reports/Mean_sales.csv")

