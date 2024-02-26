import pandas as pd
import seaborn as sns
import spacy
import matplotlib.pyplot as plt
from transformers import pipeline
import sys
from unicodedata import normalize
import re

class DataProcessor:
    def __init__(self, csv_path: str):
        '''
        Initialize the DataProcessor object by loading data from a CSV file into a DataFrame.

        ### Args:
        * `csv_path` (str): The file path of the CSV file to be processed.

        ### Attributes:
        * `csv_path` (str): Stores the file path of the CSV file.
        * `data` (DataFrame): Stores the data loaded from the CSV file.

        ### Available Methods:
        * `preprocess_data`: Preprocesses the loaded data by performing cleaning and normalization operations.
        '''
        self.csv_path = csv_path
        self.data = pd.read_csv(self.csv_path)


    def preprocess_data(self):
        '''
         Preprocesses the data by performing several cleaning steps.

        ### Steps:
        1. Eliminates duplicate entries.
        2. Converts text to lowercase.
        3. Removes leading and trailing spaces.
        4. Normalizes the text to remove non-ASCII characters.
        5. Applies a regular expression to keep only alphabetic characters and spaces.
        6. Drops rows where 'Comentarios' is NaN or 'nan'.

        ### Returns:
        * `DataFrame`: The first few rows of the preprocessed data for preview.
        '''
        # Eliminate duplicates
        self.data.drop_duplicates(inplace=True)

        # Convert to lowercase
        self.data['Comentarios'] = self.data['Comentarios'].astype(str).str.lower()

        # Eliminate spaces and normalize
        self.data['Comentarios'] = self.data['Comentarios'].astype(str).str.strip()
        self.data['Comentarios'] = self.data['Comentarios'].apply(lambda x: normalize('NFKD', x).encode('ascii', 'ignore').decode('ascii'))

        # Apply regular expression
        self.data['Comentarios'] = self.data['Comentarios'].apply(lambda x: re.sub(r'[^a-zA-Z\\s]', '', x))

        # Drop NaN values
        self.data = self.data.dropna(subset=['Comentarios'])
        self.data = self.data[self.data['Comentarios'].str.lower() != 'nan']

        return self.data.head()

# =============== DEBUGGING ===============
if __name__ == '__main__':

    test = DataProcessor(
        csv_path = "D:/school/Iot/Iot git/comments1.csv"
    )
    
    test.preprocess_data()
