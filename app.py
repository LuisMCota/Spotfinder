import tkinter as tk
from tkinter import messagebox
import requests

GOOGLE_PLACES_API_KEY = 'AIzaSyAj0VJtl8C6oDTyJnIOqGjppUfTg0VeAO8'


def search():
    query = entry.get()
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={GOOGLE_PLACES_API_KEY}"
    response = requests.get(url)
    data = response.json()
    display_results(data['results'])

def display_results(results):
    results_text.delete('1.0', tk.END)
    for result in results:
        name = result['name']
        address = result['formatted_address']
        rating = result.get('rating', 'N/A')
        results_text.insert(tk.END, f"{name}\n{address}\nRating: {rating}\n\n")

app = tk.Tk()
app.title("Buscador de Lugares")

label = tk.Label(app, text="Ingrese su búsqueda:")
label.pack()

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Buscar", command=search)
button.pack()

results_text = tk.Text(app, height=15, width=50)
results_text.pack()

app.mainloop()
