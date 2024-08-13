import pandas as pd
data={"days":[1,2,3,4,5],"steps":[1234,2345,3456,4567,5678]}
df=pd.DataFrame(data)
df["+1000 steps"]=df["steps"]+1000
fi=df(df["+1000 steps"]>7000)("days")
print("\n Dataframe \n:",df)
print("\n days on which steps were >7000",fi)
