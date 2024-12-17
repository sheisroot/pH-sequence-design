import tkinter as tk
from tkinter import filedialog
import pandas as pd

def load_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Excel", "*.xlsx"), ("All Files", "*.*")])

    return file_path

    

def convert(excel_file):
    df = pd.read_excel(excel_file)
    csv_file = "output_file.csv"
    df.to_csv(csv_file, index=False)
    return csv_file

def preview_csv(csv_file):
    df = pd.read_csv(csv_file)
    print(df.head())

if __name__ == "__main__":
    print("HELLO_______________THERE")
    csv_file = convert(load_file())
    if input("Preview the file? Y/N: ").upper() == 'Y':
        preview_csv(csv_file)