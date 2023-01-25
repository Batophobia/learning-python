import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import matplotlib.pyplot as plt

def cleanData(data):
  #print(data.isna().values.any())
  #print(data.duplicated().values.any())
  SCRAPE_DATE = pd.Timestamp('2018-05-01')
  data.Release_Date = pd.to_datetime(data.Release_Date)
  data = data[data.Release_Date < SCRAPE_DATE].copy()
  columns = ['USD_Production_Budget', 
             'USD_Worldwide_Gross',
             'USD_Domestic_Gross']
  for c in columns:
    data[c] = data[c].astype("string").str.replace(r'[,$]', '', regex=True)
    data[c] = pd.to_numeric(data[c])
  return data

def removeGrossless(data):
  return data.query('USD_Worldwide_Gross != 0')

def addDecade(data):
  data["Decade"] = data.Release_Date.dt.year // 10 * 10
  return data

def getHighsLows(data):
  #data.info()
  dataLimits = data.describe()
  # HIGHS
  print(data[data.USD_Production_Budget == dataLimits.USD_Production_Budget["max"]])
  print(data[data.USD_Worldwide_Gross == dataLimits.USD_Worldwide_Gross["max"]])
  print(data[data.USD_Domestic_Gross == dataLimits.USD_Domestic_Gross["max"]])
  # LOWS
  print(data[data.USD_Production_Budget == dataLimits.USD_Production_Budget["min"]])
  #print(data[data.USD_Worldwide_Gross == dataLimits.USD_Worldwide_Gross["min"]])
  #print(data[data.USD_Domestic_Gross == dataLimits.USD_Domestic_Gross["min"]])

def getForeign(data):
  international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
  print(f'Number of international releases: {len(international_releases)}')
  return international_releases

def getFlops(data):
  flops = data.query('USD_Worldwide_Gross < USD_Production_Budget')
  print(f'Number of movies that lost money: {len(flops)}')
  return flops

def main():
  FILENAME = "./day77/cost_revenue_dirty.csv"
  data = pd.read_csv(FILENAME)
  data = cleanData(data)
  data = removeGrossless(data)
  data = addDecade(data)
  
  #getHighsLows(data)
  #print(getForeign(data).tail())
  #print(getFlops(data))

  plt.figure(figsize=(8,4), dpi=200)
  #sb.scatterplot(data=data, x="USD_Worldwide_Gross", y="USD_Production_Budget")
  with sb.axes_style("darkgrid"):
    ax = sb.regplot(
      data=data,
      x="USD_Worldwide_Gross",
      y="USD_Production_Budget",
      color="#2f4b7c",
      scatter_kws={'alpha': 0.4},
      line_kws={'color': '#ff7c43'}
    )
    ax.set(ylim=(0, 350000000),
           xlim=(0, 2500000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions') 
  plt.show()
  
if __name__ == "__main__":
  main()