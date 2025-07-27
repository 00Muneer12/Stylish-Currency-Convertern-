import tkinter as tk
from tkinter import ttk
import requests

def convert():
    from_curr = from_currency.get()
    to_curr = to_currency.get()
    amount = float(amount_entry.get())

    url = f"https://api.exchangerate-api.com/v4/latest/{from_curr}"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"][to_curr]

    result = amount * rate
    result_label.config(text=f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
    
# Currency rates (1 unit in USD)
rates = {
    "USD": 1.0,
    "PKR": 277.5,
    "EUR": 0.91,
    "INR": 83.5,
    "GBP": 0.78,
    "AUD": 1.48,
    "CAD": 1.35
}

def convert():
    from_curr = from_currency.get()
    to_curr = to_currency.get()
    amount = float(amount_entry.get())

    usd = amount / rates[from_curr]
    result = usd * rates[to_curr]

    result_label.config(text=f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")

# App window
root = tk.Tk()
root.title("Stylish Currency Converter")
root.geometry("400x400")
root.config(bg="#2C3E50")

style = ttk.Style()
style.configure("TCombobox", padding=6, font=("Arial", 12))
style.configure("TButton", font=("Arial", 12), padding=6)

tk.Label(root, text="Currency Converter", font=("Arial", 20, "bold"), bg="#2C3E50", fg="white").pack(pady=20)

amount_entry = tk.Entry(root, font=("Arial", 14), justify="center", bd=2)
amount_entry.pack(pady=10)

from_currency = ttk.Combobox(root, values=list(rates.keys()), state="readonly", font=("Arial", 12))
from_currency.set("USD")
from_currency.pack(pady=5)

to_currency = ttk.Combobox(root, values=list(rates.keys()), state="readonly", font=("Arial", 12))
to_currency.set("PKR")
to_currency.pack(pady=5)

convert_btn = ttk.Button(root, text="Convert", command=convert)
convert_btn.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 16), bg="#2C3E50", fg="#F1C40F")
result_label.pack(pady=10)

root.mainloop()


