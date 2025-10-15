# Lifestyle Data Dashboard - Data Analysis with Python

# https://www.kaggle.com/datasets/jockeroika/life-style-data

This is an interactive web application built with Streamlit that provides a comprehensive analysis of a lifestyle dataset. The dashboard allows users to explore relationships between physical attributes, workout routines, dietary habits, and health metrics like BMI and calories burned.

The application features interactive filters and a wide range of data visualizations created with Plotly, offering insights into how different factors like gender, age, and diet impact an individual's health and fitness profile.

  <!-- It's recommended to replace this with an actual screenshot of your dashboard -->

## 📋 Table of Contents

- [Features](#-features)
- [Dataset](#-dataset)
- [Installation](#-installation)
- [Usage](#-usage)
- [Script Overview](#-script-overview)
- [Dependencies](#-dependencies)

## ✨ Features

-   **Interactive Filters**: Filter data by Gender, Age Group, and Diet Type to dynamically update all visualizations.
-   **General Metrics**: At-a-glance cards showing key statistics like total records, average age, average BMI, and average calories burned.
-   **Gender-Based Analysis**: Comparative charts for BMI, calories burned, workout types, and water intake between genders.
-   **Age Group Analysis**: Visualizations showing trends in BMI, macronutrient intake, and fat percentage across different age groups.
-   **Diet and Workout Insights**: Pie charts and bar graphs displaying the distribution of diet types, workout difficulty levels, and most popular exercises.
-   **Advanced Correlation Analysis**: Scatter plots and box plots to explore relationships between variables like BMI vs. Calories Burned and Water Intake vs. Fat Percentage.
-   **Raw Data View**: A dynamic table that allows users to view the filtered data and select which columns to display.

## 📂 Dataset

The dashboard uses a CSV file named `Final_data.csv`. This dataset is expected to contain anonymized lifestyle and fitness data.

**Key columns used in the analysis:**
*   `Age`, `Gender`, `Weight (kg)`, `Height (m)`
*   `Workout`, `Target Muscle Group`, `Difficulty Level`
*   `Calories_Burned`, `Burns_Calories_Bin`
*   `BMI`, `Fat_Percentage`
*   `Water_Intake (liters)`, `diet_type`, `Carbs`, `Proteins`, `Fats`
*   `Daily meals frequency`

The script performs initial data exploration by printing basic information, statistical summaries, and characteristics grouped by gender and age to the console before launching the web app.

## ⚙️ Installation

To run this dashboard locally, you need to have Python installed. Follow these steps to set it up.

1.  **Clone the repository (or download the script):**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    A `requirements.txt` file is recommended for listing dependencies. If you don't have one, you can create it and add the libraries listed in the [Dependencies](#-dependencies) section.
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

1.  Make sure the `Final_data.csv` file is in the same directory as the Python script.

2.  Run the Streamlit application from your terminal:
    ```bash
    streamlit run your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your file).

3.  The application will open in a new tab in your default web browser. Use the filters in the sidebar to explore the data.

## 📜 Script Overview

The script is divided into two main parts:

1.  **Initial Data Analysis (Console Output)**:
    *   Loads the `Final_data.csv` dataset using `pandas`.
    *   Prints descriptive statistics, column names, missing values, and unique value counts.
    *   Calculates and prints aggregated characteristics for each gender and for predefined age groups. This part is useful for a quick, static analysis in a terminal environment.

2.  **Streamlit Dashboard (Web Application)**:
    *   Sets up the page configuration for a wide layout.
    *   Creates a sidebar with filters for gender, age group, and diet type.
    *   Displays general metrics in a series of columns.
    *   Generates over 15 different interactive plots using `plotly.express` and `plotly.graph_objects`, organized into logical sections.
    *   Includes a data table viewer with a multi-select widget for choosing columns.
    *   Implements error handling for cases where the data file is not found.

## 📦 Dependencies

This project relies on the following Python libraries:

*   **pandas**: For data manipulation and analysis.
*   **streamlit**: For creating and running the interactive web application.
*   **plotly**: For creating rich, interactive data visualizations.

You can install them all with pip:
```bash
pip install pandas streamlit plotly
```

---