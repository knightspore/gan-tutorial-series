import pandas as pd
# ZA Twitter LSTM

df = pd.read_csv("./../_datasets/twitter_za/data.csv")
df = df[["tweet_text"]]
df.head()
