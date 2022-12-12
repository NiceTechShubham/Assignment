
# Importing Pandas library to read the data

import pandas as pd



# Importing both csv files and storing it on "amazon" and "flipkart" variable

amazon=pd.read_csv("C:/Users/Shubham/Desktop/DS-assignment/DS - Assignment Part 2 data set/amz_com-ecommerce_sample.csv",encoding='unicode_escape')
flipkart=pd.read_csv(r"C:\Users\Shubham\Desktop\DS-assignment\DS - Assignment Part 2 data set\flipkart_com-ecommerce_sample.csv",encoding='unicode_escape')



# Renaming some column names of both dataframes

amazon.rename(columns={"product_name":"Product name in Amazon","retail_price":"Retail Price in Amazon","discounted_price":"Discounted Price in Amazon"},inplace=True)
flipkart.rename(columns={"product_name":"Product name in Flipkart","retail_price":"Retail Price in Flipkart","discounted_price":"Discounted Price in Flipkart"},inplace=True)




# Creating two new tables from old tables with few required columns only

a=flipkart[["uniq_id","Product name in Flipkart","Retail Price in Flipkart","Discounted Price in Flipkart"]]
b=amazon[["uniq_id","Product name in Amazon","Retail Price in Amazon","Discounted Price in Amazon"]]





# Joining both tables on the similar column of both tables and storing it on a new variable

c=pd.merge(a,b,on="uniq_id")




# Removing "uniq_id" column

c=c.drop(['uniq_id'],axis=1)




# Showing the first five row of the table

c.head()



# Exporting csv file into excel format.

c.to_excel(r"C:\Users\Shubham\Desktop\DS-assignment\DS - Assignment Part 2 data set\Data2.xlsx",index=False)

