import pandas as p
"""
#series created from list
data=[100,12,34]
series=p.Series(data,index=["Jeeshma","sahithi","sagar"])
print(series.loc["Jeeshma"])
print(series[series>=100])
#series craeted from dic
screen={
    "day1" : 7,
    "day2" : 3,
    "day3" : 4,
    "day4" : 5
}
series=p.Series(screen)
print(series.loc["day1"])
print(series.iloc[1])
series.loc["day3"]=2
print(series)
#creating dataframe using dic
data={
    "Name" : ["Jeeshma","Sahithi","Hemanth"],
    "Age" : [12,23,34]
    }
df=p.DataFrame(data,index=[1,2,3])
print(df.loc[1])
# add a new column
df["class"]=[10,3,7]
print(df)
#add a new rows
#values not given are set to Nan
new=p.DataFrame([{"Name":"sasidhar","Age":21},
                 {"Name":"Sagar","Age":19}
                 ],index=[4,5])
df=p.concat([df,new])
print(df)
#reading csv and json files
df=p.read_csv("test.csv")
#j=p.read_json("file") used to read json file
#df.to_string() used to print everything in terminal instead of...
#print(df.to_string())
#selection:
#selection by column
#print(df["Name"].to_string())
#selecting mutli colums
#print(df[["Name","Height"]])
#selection by row:
#print(df.loc[0])
#to change the a column in dataframe into labels
#df=p.read_csv("test.py",index_col="Name")
#to get only desired columns of a row
#print(df.loc[0,["Height","Name"]])
#to select multi consecutive rows
#print(df.loc[0:3])
#df=p.read_csv("test.csv")
print(df[df["Height"]>=2])
legendary_pokemon=df[(df["Legendary"]==1) &
                     (df["Height"]>=2)]
print(legendary_pokemon)
#df=p.read_csv("test.csv")
#for entire dataframe
print(df.mean(numeric_only=1))
#for single column
print(df["Height"].mean())
#using groupby()
gp=df.groupby("Height")
print(gp["Weight"].mean())"""
df=p.read_csv("test.csv")
#dropping columns
#df=df.drop(columns=["No"])
#print(df)
#droppping row when data of a particular column is not available
#df=df.dropna(subset=["Type1"])
#print(df)
#filling not available data of a particular column with a partcular value
#df=df.fillna({"Type1":"None"})
#print(df.to_string())
#update a particular vale with another particular value
df["Type1"]=df["Type1"].replace({"Grass":"GRASS",
                                 "Fire":"FIRE",})
print(df)