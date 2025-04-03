import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def fetch_google_doc_table(doc_url):
    """
    Fetches the table data from a Google Doc given its URL and returns the parsed data as a list of tuples.
    Each tuple contains (x-coordinate, character, y-coordinate).
    """
    # Extract the document ID from the URL
    doc_id = doc_url.split("/d/")[1].split("/")[0]
    export_url = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
    
    response = requests.get(export_url)
    if response.status_code != 200:
        raise Exception("Failed to retrieve the document.")
    
    text = response.text.splitlines()
    data = []
    found_table = False
    
    for line in text:
        columns = line.split('\t')  # Assuming tab-separated values
        if found_table and len(columns) == 3:
            try:
                x = int(columns[0].strip())
                char = columns[1].strip()
                y = int(columns[2].strip())
                data.append((x, char, y))
            except ValueError:
                continue  # Skip invalid lines
        elif 'x-coordinate' in line and 'y-coordinate' in line:
            found_table = True  # Found the table header
    
    return data

def print_unicode_grid(doc_url):
    """
    Fetches table data from a Google Doc and prints the corresponding Unicode character grid.
    """
    data = fetch_google_doc_table(doc_url)
    
    if not data:
        print("No table data found.")
        return
    
    # Determine grid size
    max_x = max(x for x, _, _ in data)
    max_y = max(y for _, _, y in data)
    
    # Initialize grid with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Populate the grid with characters
    for x, char, y in data:
        grid[y][x] = char
    
    # Print the grid
    for row in grid:
        print(''.join(row))

# Example usage:
# print_unicode_grid("https://docs.google.com/document/d/your_document_id_here/edit")