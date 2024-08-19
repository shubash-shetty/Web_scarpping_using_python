import pandas as pd

scrapper = pd.read_html("https://en.wikipedia.org/wiki/Premier_League_records_and_statistics")

df = scrapper[0]

df.to_csv('premier_league.csv', index=False)

df_scrapped_file = pd.read_csv('premier_league.csv')
print("\n")
print(df_scrapped_file)

##for i, table in enumerate(scrapper):
##    print("-------------")
##    print(i)
##   print(table)