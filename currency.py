import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Variables
        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.result_var = tk.StringVar()

        # GUI Elements
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_entry = tk.Entry(root, textvariable=self.amount_var, width=10)

        self.from_currency_label = tk.Label(root, text="From Currency:")
        self.from_currency_combobox = ttk.Combobox(root, textvariable=self.from_currency_var, values=[])

        self.to_currency_label = tk.Label(root, text="To Currency:")
        self.to_currency_combobox = ttk.Combobox(root, textvariable=self.to_currency_var, values=[])

        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.result_label = tk.Label(root, textvariable=self.result_var)

        # Grid layout
        self.amount_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.from_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

        self.to_currency_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)

        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Initialize currencies
        self.currency_rates = CurrencyRates()
        self.currencies = self.currency_rates.get_rates("USD")
        self.currency_list = list(self.currencies.keys())

        self.from_currency_combobox["values"] = self.currency_list
        self.to_currency_combobox["values"] = self.currency_list

    def convert(self):
        amount = self.amount_var.get()
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()

        try:
            conversion_rate = self.currency_rates.get_rate(from_currency, to_currency)
            result = amount * conversion_rate
            self.result_var.set(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        except Exception as e:
            self.result_var.set("Error converting currencies. Check inputs and try again.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
