import requests

def main():
  # https://dashboard.sheety.co/
  SHEET_URL = ""

  def postRow(json):
    return requests.post(SHEET_URL, json=json)
  
  def getSheet():
    return requests.get(SHEET_URL)
  
  test = {
    "sheet1": {
      "pie": "Pecan",
      "chairLegs": 6,
      "dollars": 22
    }
  }
  resp = postRow(test)
  print(resp)
  print(resp.status_code)
  print(resp.text)

  resp = getSheet()
  print(resp)
  print(resp.status_code)
  print(resp.text)
  

if __name__ == "__main__":
  main()