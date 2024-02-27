from flask import Flask, request, render_template
import requests

app = Flask(__name__)

GOOGLE_PLACES_API_KEY = 'AIzaSyAj0VJtl8C6oDTyJnIOqGjppUfTg0VeAO8'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        address = request.form['address']
        query = request.form['query']
        location = get_location_from_address(address)
        if location:
            results = search_places(query, location)
            return render_template('results.html', results=results)
        else:
            error = "No se pudo encontrar la ubicación. Intenta con otra dirección."
            return render_template('home.html', error=error)
    return render_template('home.html')

def get_location_from_address(address):
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_PLACES_API_KEY}"
    response = requests.get(geocode_url)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return f"{location['lat']},{location['lng']}"
    else:
        return None

def search_places(query, location, radius=500):
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&location={location}&radius={radius}&key={GOOGLE_PLACES_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data['results']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

