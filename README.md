# E-Commerce Data Analytics Dashboard

This project contains a Streamlit-based interactive dashboard to analyze e-commerce data, including customer behavior, order trends, product analysis, customer reviews, geolocation, and correlation analysis.

## Prerequisites

Ensure that you have the following installed:

- Python 3.8 or above
- Streamlit
- Required libraries in `requirements.txt`

## Setup Instructions

### 1. Navigate to the `dashboard` folder

```bash
cd dashboard
```

### 2. Install required dependencies

Install all necessary Python packages by running the following command:

```bash
pip install -r requirements.txt
```

### 3. Run the dashboard

Once the required packages are installed, you can run the dashboard using the following command:

```bash
streamlit run dashboard.py
```

This will start the Streamlit server, and you can view the dashboard by opening the provided local URL (e.g., `http://localhost:8501`) in your web browser.

## Features of the Dashboard

- **Customer Analysis**: View customer distribution by state.
- **Order Analysis**: Examine order trends and status distribution.
- **Product Analysis**: Analyze product categories and view revenue from the top 10 categories.
- **Customer Reviews**: Insights into review scores and breakdown of positive/negative reviews.
- **Geolocation**: Visualize customer and seller locations on a map.
- **Correlation Analysis**: Explore the correlation between delivery time and customer satisfaction.

## Data

Make sure to place the necessary datasets (e.g., `customers_dataset.csv`, `orders_dataset.csv`, etc.) in the `data` folder as referenced in the script.
