<img src="PhonePe_Logo.jpg" alt="PhonePe Logo" width="300" height="200">

# PhonePe Pulse Data Visualization

## Overview

Welcome to the PhonePe Pulse Data Visualization project! This repository contains the source code for a user-friendly tool designed to visualize and explore PhonePe transaction and user data. The project leverages Streamlit and Plotly to create interactive charts and maps.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
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

## Usage

1. **Start the Streamlit app:**

    ```bash
    streamlit run 'PhonePe Main Project.py'
    ```

2. **Open your web browser:**

    Navigate to the provided Streamlit URL.

3. **Navigate through the app:**

    - Use the sidebar to switch between different sections: Home, Top Charts, and Analyze Data.
    - Customize your data analysis by selecting the type (Transaction or User) and specifying the year and quarter.

4. **Explore and gain insights:**

    - Visualize top charts based on your criteria in the "Top Charts" section.
    - Analyze transaction and user data on maps and charts in the "Analyze Data" section.

## Features

- **Top Charts:**
  - View top charts for transaction and user data, including charts for states, districts, and pincodes.

- **Map Visualization:**
  - Analyze transaction and user data on an interactive map of India.
  - Select specific states for detailed analysis.

- **Quarterly Analysis:**
  - Dynamically select the year and quarter for analyzing data, ensuring flexibility in exploring different time periods.

