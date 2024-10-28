#URL: https://finance.yahoo.com/quote/AAPL/history/?p=AAPL
import requests
from bs4 import BeautifulSoup

def fetch_apple_stock_data():
    url = "https://finance.yahoo.com/quote/AAPL/history/?p=AAPL"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    response = requests.get(url, headers=headers) 
    #Note:A header must be used here to act as a human retrieving data rather than a robot, which Yahoo blocks from pulling data
    if response.status_code != 200:
        print("Failed to retrieve data. Status code:", response.status_code)
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    
    if not table:
        print("No historical data table found on the page")
        return

    print(f"{'Date':<15} {'Close Price':<10}")
    rows = table.find_all('tr')[1:]

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 6:
            date = columns[0].text.strip()
            close_price = columns[4].text.strip()
            print(f"{date:<15} {close_price:<10}")

if __name__ == "__main__":
    fetch_apple_stock_data()
