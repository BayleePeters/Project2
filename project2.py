#import required modules
import pandas as pd
import numpy as np

#create new data frame from CSV for sales
salesDF = pd.read_csv("D:\ACC470\salesFINAL.csv")

#display transaction count for sales
print("The total sales transactions are " + str(salesDF.shape[0]))

#displays sum of sales transactions
total = salesDF["SalesDollars"].sum()
total = round(total)
print ("The total sales dollars is " + str(total))

#create new data frame from CSV for purchases
purchasesDF = pd.read_csv("D:\ACC470\purchasesFINAL.csv")

#display transaction count for purchases
print("The total purchases transactions are " + str(purchasesDF.shape[0]))

#displays sum of purchase transactions
total = purchasesDF["Dollars"].sum()
total = round(total)
print ("The total purchase dollars is " + str(total))

#create new data frame from CSV for beginning inventory
beginventoryDF = pd.read_csv("D:\ACC470\BegInvFINAL.csv")

#display transaction count for sales
print("The total beginning inventory transactions are " + str(beginventoryDF.shape[0]))

#create new data frame from CSV for 2016 purchase price with only brand and purchase price data
purpriceDF = pd.read_csv("2016PurchasePrices.csv")
purpriceDF = purpriceDF[["Brand", "PurchasePrice"]]

#merge purchase price data frame and beginning inventory data frame on brand
begpurbrandDF = pd.merge(purpriceDF, beginventoryDF, on = "Brand")

#Add calculated field Ext Cost
begpurbrandDF["ExtCost"] = begpurbrandDF["PurchasePrice"] * begpurbrandDF["onHand"]

#displays sum of Ext Cost
total = begpurbrandDF["ExtCost"].sum()
total = round(total)
print ("The total Ext Cost for beginning inventory is " + str(total))

#create new data frame from CSV for ending inventory
endinventoryDF = pd.read_csv("D:\ACC470\EndInvFINAL.csv")

#display transaction count for ending inventory
print("The total ending inventory transactions are " + str(endinventoryDF.shape[0]))

#merge purchase price data frame and ending inventory data frame on brand
endpurbrandDF = pd.merge(purpriceDF, endinventoryDF, on = "Brand")

#Add calculated field Ext Cost
endpurbrandDF["ExtCost"] = endpurbrandDF["PurchasePrice"] * endpurbrandDF["onHand"]

#displays sum of Ext Cost
total = endpurbrandDF["ExtCost"].sum()
total = round(total)
print ("The total Ext Cost for ending inventory is " + str(total))








