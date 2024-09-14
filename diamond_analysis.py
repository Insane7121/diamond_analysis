import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.filedialog import askopenfilename

import matplotlib.pyplot as plt
import pandas as pd


# Load Data Function
def load_data():
    file_path = askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(file_path)
            if set(['Carat', 'Cut', 'Clarity', 'Color', 'Price', 'Impurity']).issubset(df.columns):
                return df
            else:
                messagebox.showerror("Error", "CSV file must contain the required columns: Carat, Cut, Clarity, Color, Price, and Impurity")
                return None
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")
            return None
    return None

# Class for GUI Application
class DiamondAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diamond Prices Data Analysis - Keeva Diamond")
        
        self.data = None
        
        # Create Load Data Button
        self.load_btn = ttk.Button(root, text="Load Data", command=self.load_data)
        self.load_btn.grid(row=0, column=0, padx=10, pady=10)
        
        # Label for Filters
        self.lbl_filters = ttk.Label(root, text="Filters")
        self.lbl_filters.grid(row=1, column=0, padx=10, pady=10)
        
        # Combobox for Cut Filter
        self.lbl_cut = ttk.Label(root, text="Cut:")
        self.lbl_cut.grid(row=2, column=0, padx=10, pady=5)
        self.cut_var = tk.StringVar()
        self.cut_combobox = ttk.Combobox(root, textvariable=self.cut_var)
        self.cut_combobox.grid(row=2, column=1, padx=10, pady=5)
        
        # Combobox for Clarity Filter
        self.lbl_clarity = ttk.Label(root, text="Clarity:")
        self.lbl_clarity.grid(row=3, column=0, padx=10, pady=5)
        self.clarity_var = tk.StringVar()
        self.clarity_combobox = ttk.Combobox(root, textvariable=self.clarity_var)
        self.clarity_combobox.grid(row=3, column=1, padx=10, pady=5)
        
        # Combobox for Impurity Filter
        self.lbl_impurity = ttk.Label(root, text="Impurity:")
        self.lbl_impurity.grid(row=4, column=0, padx=10, pady=5)
        self.impurity_var = tk.StringVar()
        self.impurity_combobox = ttk.Combobox(root, textvariable=self.impurity_var)
        self.impurity_combobox.grid(row=4, column=1, padx=10, pady=5)
        
        # Analysis Buttons
        self.btn_summary = ttk.Button(root, text="View Summary", command=self.show_summary)
        self.btn_summary.grid(row=5, column=0, padx=10, pady=10)
        
        self.btn_plot = ttk.Button(root, text="Generate Plot", command=self.generate_plot)
        self.btn_plot.grid(row=5, column=1, padx=10, pady=10)
    
    # Load Data and Update Filters
    def load_data(self):
        self.data = load_data()
        if self.data is not None:
            self.update_filters()

    # Update Filter Options Based on Data
    def update_filters(self):
        # Update Cut Combobox
        self.cut_combobox['values'] = ['All'] + sorted(self.data['Cut'].unique().tolist())
        self.cut_combobox.set('All')
        
        # Update Clarity Combobox
        self.clarity_combobox['values'] = ['All'] + sorted(self.data['Clarity'].unique().tolist())
        self.clarity_combobox.set('All')
        
        # Update Impurity Combobox
        self.impurity_combobox['values'] = ['All'] + sorted(self.data['Impurity'].unique().tolist())
        self.impurity_combobox.set('All')

    # Show Summary Statistics
    def show_summary(self):
        if self.data is None:
            messagebox.showerror("Error", "No data loaded.")
            return
        
        cut = self.cut_var.get()
        clarity = self.clarity_var.get()
        impurity = self.impurity_var.get()

        # Filter the data based on selected filters
        filtered_data = self.data
        if cut != 'All':
            filtered_data = filtered_data[filtered_data['Cut'] == cut]
        if clarity != 'All':
            filtered_data = filtered_data[filtered_data['Clarity'] == clarity]
        if impurity != 'All':
            filtered_data = filtered_data[filtered_data['Impurity'] == impurity]

        if filtered_data.empty:
            messagebox.showinfo("No Data", "No data available for the selected filters.")
            return
        
        summary = filtered_data.describe(include='all')
        print(summary)
        messagebox.showinfo("Summary", str(summary))

    # Generate a Plot
    def generate_plot(self):
        if self.data is None:
            messagebox.showerror("Error", "No data loaded.")
            return
        
        cut = self.cut_var.get()
        clarity = self.clarity_var.get()
        impurity = self.impurity_var.get()

        # Filter the data based on selected filters
        filtered_data = self.data
        if cut != 'All':
            filtered_data = filtered_data[filtered_data['Cut'] == cut]
        if clarity != 'All':
            filtered_data = filtered_data[filtered_data['Clarity'] == clarity]
        if impurity != 'All':
            filtered_data = filtered_data[filtered_data['Impurity'] == impurity]

        if filtered_data.empty:
            messagebox.showinfo("No Data", "No data available for the selected filters.")
            return
        
        # Plot Carat vs Price
        plt.scatter(filtered_data['Carat'], filtered_data['Price'], c='blue', label='Price')
        plt.title("Carat vs Price")
        plt.xlabel("Carat")
        plt.ylabel("Price (in USD)")
        plt.grid(True)
        plt.show()

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = DiamondAnalysisApp(root)
    root.mainloop()
