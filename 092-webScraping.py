from bs4 import BeautifulSoup
import requests

def main():
  # Most Popular (100)
  #URL = "https://www.imdb.com/chart/moviemeter/"
  # TOP 250
  URL = "https://www.imdb.com/chart/top/"

  resp = requests.get(URL)
  soup = BeautifulSoup(resp.text, "html.parser")

  movies = soup.select(".lister-list tr")
  for movie in movies:
    img = movie.select_one(".posterColumn img").get("src")
    title = movie.select_one(".titleColumn a").getText()
    rating = movie.select_one(".imdbRating").getText()
    print(f"{title.strip()}: {rating.strip()} / 10")
  

if __name__ == "__main__":
  main()