# Diamond Prices Data Analysis - Keeva Diamond

This project is designed for **Keeva Diamond** to analyze diamond prices based on various attributes like **carat, cut, clarity, color, impurity type**, and **price**. It provides an intuitive **Graphical User Interface (GUI)** that allows users to load diamond pricing data, apply filters, and generate visual analysis through summary statistics and plots.

## Features

- **Load Diamond Data**: The application can load data from a CSV file, which contains information about diamonds, including carat, cut, clarity, color, impurity, and price.
  
- **Filter by Attributes**: The application allows you to filter the data based on several characteristics:
  - **Cut**: Fair, Good, Very Good, Premium, Ideal.
  - **Clarity**: I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF.
  - **Impurity**: Type of impurity in the diamond.

- **View Summary Statistics**: You can view detailed summary statistics (e.g., mean, standard deviation, min, max) based on the applied filters. The summary will be presented in a pop-up window.

- **Generate Visual Plots**: Generate scatter plots to visualize the relationship between **Carat** and **Price** for the filtered diamonds.

- **Interactive GUI**: A user-friendly GUI built using **Tkinter** for loading the data, applying filters, viewing the results, and generating plots.

## Requirements

### Software
- **Python 3.x** must be installed on your system.
  
### Python Packages
You will need the following Python libraries, which are included in the `requirements.txt` file:
- `pandas`
- `matplotlib`
- `tkinter`

### Installation of Required Packages
To install the required Python packages, run the following command:

```bash
pip install -r requirements.txt
