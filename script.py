import requests
import bs4

res = requests.get("https://www.scoresandodds.com/mlb")
soup = bs4.BeautifulSoup(res.text, 'lxml')

for row in soup.select('.event-card-row'):
    if row.select('.tbd .data-moneyline'):
        print(row.select('.team-name a')[0].text + " opened/closed at:")
        print(row.select('.data-moneyline')[0].text + "/" + row.select('.data-moneyline')[4].text)
    elif row.select('.win .data-moneyline'):
        print(row.select('.team-name a')[0].text + " opened/closed at:")
        print(row.select('.data-moneyline')[0].text + "/" + row.select('.data-moneyline')[4].text)
    elif row.select('.loss .data-moneyline'):
        print(row.select('.team-name a')[0].text + " opened/closed at:")
        print(row.select('.data-moneyline')[0].text + "/" + row.select('.data-moneyline')[4].text)