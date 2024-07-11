# this is to analyze the Google Activity Log

import pandas as pd

df = pd.read_csv('./activities.csv')
df.drop('Is Non-routable IP Address', axis=1, inplace=True)
df.drop('Activity Country', axis=1, inplace=True)
df.drop('Activity Region', axis=1, inplace=True)
df.drop('Activity City', axis=1, inplace=True)
cols = df.columns
interesting_data = []
user_agents = df['User Agent String']
unique_user_agent_strings = user_agents.unique()
products = df['Product Name']
subproducts = df['Sub-Product Name']
interesting_data.append(user_agents)
interesting_data.append(products)
interesting_data.append(subproducts)
youtube_activity = df[df['Product Name'] == 'YouTube']
other_activity = df[df['Product Name'] == 'Other']
def print_unique_values(df, cols):
    for col in cols:
        print(col)
        input()
        print(df[col].unique())
        input()
