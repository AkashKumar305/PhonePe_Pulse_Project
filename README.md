<img src="PhonePe_Logo.jpg" alt="PhonePe Logo" width="500" height="180">

# PhonePe Pulse Data Visualization

## Overview

Welcome to the PhonePe Pulse Data Visualization project! This repository contains the source code for a user-friendly tool designed to visualize and explore PhonePe transaction and user data. The project leverages Streamlit and Plotly to create interactive charts and maps.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Workflow](#workflow)
- [Usage](#usage)
- [Features](#features)

## Getting Started

### Prerequisites

Make sure you have the following installed on your system:

- Python 3
- MySQL
- Streamlit
- Plotly
- Pandas
- Json

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/PhonePe/pulse.git
   ```
2. **Set up MySQL Database**

## Workflow 

### Step 1: Set Up MySQL Connection
- The project starts by establishing a connection to the MySQL database using the `start_mysql()` function.

### Step 2: Execute MySQL Queries
- Functions like `mysql_execute()` are utilized to execute MySQL queries and retrieve data for analysis.

### Step 3: Visualization Functions
- Several functions are defined to create different types of visualizations using Plotly, including pie charts, bar charts, and choropleth maps.

### Step 4: Main Streamlit App
- The main Streamlit app is created using the `st.sidebar` for navigation and various input widgets such as sliders and select boxes.

### Step 5: Home Page
- If the user selects the 'Home' option, a brief overview of the project, including the project title and technologies used, is displayed.

### Step 6: Top Charts Page
- If the user selects the 'Top Charts' option, the page displays top charts related to transactions or user data based on the selected type.

### Step 7: Analyze Data Page
- If the user selects the 'Analyze Data' option, map visualizations and bar charts are presented for further analysis.

### Step 8: MySQL Connection Closing
- The MySQL connection is closed using the `close_mysql()` function at the end of the workflow.

## Usage
1. Clone the GitHub repository.
2. Ensure that the required Python libraries are installed (Pandas, Streamlit, MySQL Connector, Plotly, PIL).
3. Update MySQL connection details in the `start_mysql()` function.
4. Run the Streamlit app using the command `streamlit run your_script.py`.

## Features

- **Top Charts:**
  - View top charts for transaction and user data, including charts for states, districts, and pincodes.

- **Map Visualization:**
  - Analyze transaction and user data on an interactive map of India.
  - Select specific states for detailed analysis.

- **Quarterly Analysis:**
  - Dynamically select the year and quarter for analyzing data, ensuring flexibility in exploring different time periods.

