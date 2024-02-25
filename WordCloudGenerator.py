import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from stop_words import get_stop_words

class WordCloudGenerator:
    def __init__(self, csv_path, language='spanish'):
        self.csv_path = csv_path
        self.language = language
        self.stopwords = get_stop_words(self.language)
        self.data = None
        self.texto_limpiado = ""

# Loads data from the CSV file and extracts the 'Comentarios' column
    def load_data(self):
        self.data = pd.read_csv(self.csv_path)
        comentarios = self.data['Comentarios'].dropna()
        return comentarios

# Cleans the data by extracting only alphanumeric words and converting them to lowercase
    def clean_data(self, comentarios):
        words_alnum = [word for comment in comentarios for word in comment.split() if word.isalnum()]
        words_cleaned = [word.lower() for word in words_alnum if word.lower() not in self.stopwords]
        self.texto_limpiado = ' '.join(words_cleaned)

# Generates the wordcloud using the cleaned function
    def generate_wordcloud(self, width=1200, height=600, max_words=500):
        wordcloud = WordCloud(width=width, height=height, background_color='white', max_words=max_words).generate(self.texto_limpiado)
        return wordcloud

# Shows generated wordcloud
    def display_wordcloud(self, wordcloud):
        plt.figure(figsize=(15, 7.5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

# Usage of class
csv_file_path = (r"C:\Users\cesco\Desktop\Personal\UPY\7\IoT\datos_y_comentarios_merida_norte.xlsx - Places.csv")
wc_generator = WordCloudGenerator(csv_file_path)
comentarios = wc_generator.load_data()
wc_generator.clean_data(comentarios)
wordcloud = wc_generator.generate_wordcloud()
wc_generator.display_wordcloud(wordcloud)
