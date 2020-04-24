

import requests
import bs4

game_id = 5
url = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + str(game_id)
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text, features='lxml')
print(soup.find('name').text)


game_id1 = 40
url1 = 'https://www.boardgamegeek.com/xmlapi/boardgame/' + str(game_id1)
result1 = requests.get(url1)
soup1 = bs4.BeautifulSoup(result1.text, features='lxml')
print("Name:", soup1.find('name').text)
print("Max players:",soup1.find('maxplayers').text)
print("Min players:", soup1.find('minplayers').text)
print("Description:", soup1.find('description'[0]).text)

