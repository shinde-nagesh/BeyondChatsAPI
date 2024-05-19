
import requests
import json
import tkinter as tk
from tkinter import messagebox, scrolledtext

def fetch_data():
    url = "https://devapi.beyondchats.com/api/get_message_with_sources"

    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        sources = data.get("data", {}).get("data", [])

        citations = []
        for item in sources:
            for source in item.get("source", []):
                if source.get("id") and source.get("link"):
                    citation = {
                        "id": source["id"],
                        "link": source["link"]
                    }
                    citations.append(citation)

        # Display citations in a user-friendly format
        display_citations(citations)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {e}")
    except json.decoder.JSONDecodeError:
        messagebox.showerror("Error", "Failed to decode JSON response")

def fetch_data_json():
    url = "https://devapi.beyondchats.com/api/get_message_with_sources"

    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        sources = data.get("data", {}).get("data", [])

        citations = []
        for item in sources:
            for source in item.get("source", []):
                if source.get("id") and source.get("link"):
                    citation = {
                        "id": source["id"],
                        "link": source["link"]
                    }
                    citations.append(citation)

        # Display citations in JSON format
        display_citations_json(citations)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {e}")
    except json.decoder.JSONDecodeError:
        messagebox.showerror("Error", "Failed to decode JSON response")

def display_citations(citations):
    text_widget.delete(1.0, tk.END) 
    if not citations:
        text_widget.insert(tk.END, "No citations found.")
        return

    # Enhanced formatting for readability
    formatted_citations = ""
    for citation in citations:
        formatted_citations += f"ID: {citation['id']}\nLink: {citation['link']}\n\n"

    text_widget.insert(tk.END, formatted_citations)

def display_citations_json(citations):
    text_widget.delete(1.0, tk.END)  # Clear the text widget

    if not citations:
        text_widget.insert(tk.END, "No citations found.")
        return

    # Insert the citations in JSON format
    citations_json = json.dumps(citations, indent=4)
    text_widget.insert(tk.END, citations_json)

# Create the main window
root = tk.Tk()
root.title("Citation Fetcher")

# Set the window size and make it non-resizable
root.geometry("800x600")
root.resizable(False, False)

# Create a stylish button to fetch data
fetch_button = tk.Button(
    root, 
    text="Click Me to Fetch Data", 
    command=fetch_data, 
    bg="#4CAF50",  # Button background color
    fg="white",  # Button text color
    font=("Helvetica", 14, "bold"),  # Font style
    padx=10,  
    pady=5,  
    relief="raised",  
    bd=3  # Border width
)
fetch_button.pack(pady=20)

# Create another stylish button to fetch data in JSON format
fetch_json_button = tk.Button(
    root, 
    text="Fetch Data in JSON Format", 
    command=fetch_data_json, 
    bg="#FF5733",  # Button background color
    fg="white",  # Button text color
    font=("Helvetica", 14, "bold"),  # Font style
    padx=10,  # Padding on the x-axis
    pady=5,  # Padding on the y-axis
    relief="raised",  # Button relief style
    bd=3  # Border width
)
fetch_json_button.pack(pady=20)

# Create a scrolled text widget to display citations
text_widget = scrolledtext.ScrolledText(root, width=80, height=20, font=("Helvetica", 12))
text_widget.pack(pady=10)

# Run the application
root.mainloop()



