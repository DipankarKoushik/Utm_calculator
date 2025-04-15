import math
import tkinter as tk
from tkinter import messagebox

def get_utm_zone(longitude):
    return math.ceil((longitude + 180) / 6)

def get_hemisphere(latitude):
    return "Northern Hemisphere" if latitude >= 0 else "Southern Hemisphere"

def calculate_utm():
    try:
        lat = float(entry_lat.get())
        lon = float(entry_lon.get())
        zone = get_utm_zone(lon)
        hemi = get_hemisphere(lat)
        result_label.config(text=f"UTM Zone: {zone}\n{hemi}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for latitude and longitude.")

# Create GUI window
root = tk.Tk()
root.title("UTM Zone Finder")

tk.Label(root, text="Latitude:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_lat = tk.Entry(root)
entry_lat.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Longitude:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_lon = tk.Entry(root)
entry_lon.grid(row=1, column=1, padx=10, pady=5)

calc_button = tk.Button(root, text="Calculate UTM Zone", command=calculate_utm)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
