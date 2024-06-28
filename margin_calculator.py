import tkinter as tk
from tkinter import messagebox

def calculate_selling_price():
    try:
        cost_price = float(cost_entry.get())
        quantity = int(quantity_entry.get())
        percentage_margin = float(margin_entry.get())

        # Calculate the price per quantity
        price_per_quantity = cost_price / quantity

        # Calculate the margin
        margin = price_per_quantity * (percentage_margin / 100)

        # Calculate the selling price
        selling_price = price_per_quantity + margin

        # Round up to the nearest whole number
        price_per_quantity_rounded = round(price_per_quantity)
        margin_rounded = round(margin)
        selling_price_rounded = round(selling_price)

        # Display the rounded results
        price_label.config(text=f"Price per Quantity: {price_per_quantity_rounded}")
        margin_label.config(text=f"Margin: {margin_rounded}")
        result_label.config(text=f"Selling Price: {selling_price_rounded}")

        # Clear the entry fields after calculation
        cost_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        margin_entry.delete(0, tk.END)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Selling Price Calculator")

# Create labels and entries for input
tk.Label(window, text="Cost Price:").grid(row=0, column=0, padx=10, pady=5)
cost_entry = tk.Entry(window)
cost_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Quantity:").grid(row=1, column=0, padx=10, pady=5)
quantity_entry = tk.Entry(window)
quantity_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Margin (%):").grid(row=2, column=0, padx=10, pady=5)
margin_entry = tk.Entry(window)
margin_entry.grid(row=2, column=1, padx=10, pady=5)

# Button to calculate selling price
calculate_button = tk.Button(window, text="Calculate", command=calculate_selling_price)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Labels to display the results
price_label = tk.Label(window, text="Price per Quantity: --")
price_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

margin_label = tk.Label(window, text="Margin: --")
margin_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(window, text="Selling Price: --")
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

def clear_fields():
    cost_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    margin_entry.delete(0, tk.END)
    price_label.config(text="Price per Quantity: --")
    margin_label.config(text="Margin: --")
    result_label.config(text="Selling Price: --")

# Button to clear fields
clear_button = tk.Button(window, text="Clear", command=clear_fields)
clear_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI main loop
window.mainloop()
