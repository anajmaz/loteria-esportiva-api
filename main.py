from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def scrape_vlr_rankings():
    url = "https://www.vlr.gg/rankings"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    teams = []
    
    for td in soup.find_all('td', class_='rank-item-team'):
        team_info = td.find('a')
        team_name = team_info.find('div').text.strip()
        team_image = team_info.find('img')['src']
        teams.append({'name': team_name, 'image': team_image})
    
    return teams

@app.route('/api/vlr-rankings', methods=['GET'])
def get_vlr_rankings():
    data = scrape_vlr_rankings()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
