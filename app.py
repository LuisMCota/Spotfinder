from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GOOGLE_PLACES_API_KEY = 'AIzaSyAj0VJtl8C6oDTyJnIOqGjppUfTg0VeAO8'

@app.route('/search')
def search_places():
    query = request.args.get('query')
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={GOOGLE_PLACES_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
