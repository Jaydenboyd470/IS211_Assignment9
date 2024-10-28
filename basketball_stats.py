#URL: https://www.cbssports.com/nba/stats/player/scoring/nba/regular/all-pos/qualifiers/?sortdir=descending&sortcol=ppg 

import requests
from bs4 import BeautifulSoup

def fetch_nba_stats():
    url = "https://www.cbssports.com/nba/stats/player/scoring/nba/regular/all-pos/qualifiers/?sortdir=descending&sortcol=ppg"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve data")
        return

    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the player stats
    table = soup.find('table')
    if not table:
        print("No stats table found on the page")
        return

    # Extract the table rows
    rows = table.find_all('tr')[1:11]  # Skip the header row, get top 10 rows

    # Print the headers
    print(f"{'Rank':<5} {'Player':<25} {'Position':<10} {'Team':<5} {'PPG':<5}")

    # Process each row to extract player details
    for idx, row in enumerate(rows, start=1):
        columns = row.find_all('td')
        if len(columns) >= 5:
            player_name = columns[0].text.strip()
            position = columns[1].text.strip()
            team = columns[2].text.strip()
            points_per_game = columns[3].text.strip()
            print(f"{idx:<5} {player_name:<25} {position:<10} {team:<5} {points_per_game:<5}")

if __name__ == "__main__":
    fetch_nba_stats()
