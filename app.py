from flask import Flask, request, render_template
import requests

app = Flask(__name__)

GOOGLE_PLACES_API_KEY = 'AIzaSyAj0VJtl8C6oDTyJnIOqGjppUfTg0VeAO8'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        results = search_places(query)
        return render_template('results.html', results=results)
    return render_template('home.html')

def search_places(query):
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={GOOGLE_PLACES_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data['results']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

