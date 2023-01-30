from bs4 import BeautifulSoup
import requests

URL = "https://en.wikipedia.org/wiki/List_of_roller_coaster_rankings"

def main():
  resp = requests.get(URL)
  soup = BeautifulSoup(resp.text, "html.parser")
  
  best = []
  types = soup.select(".wikitable.sortable")
  for statType in types:
    entries = statType.select("tbody tr")
    for entry in entries:
      if len(entry.select("td")) < 1:
        continue
      pos = entry.select_one("th").getText().strip() # python version trim()
      name = entry.select("td")[0].getText().strip()
      park = entry.select("td")[1].getText().strip()
      country = entry.select("td")[2].getText().strip()
      val = entry.select("td")[3].getText().strip()
      if pos == "1":
        best.append({
          "type": statType.select_one("caption").contents[0],
          "name": name,
          "park": park,
          "country": country,
          "val": val,
        })
        break

  for record in best:
    print(f"{record['type']}: {record['val']} held by {record['name']} in {record['park']} of {record['country']}")


if __name__ == "__main__":
  main()