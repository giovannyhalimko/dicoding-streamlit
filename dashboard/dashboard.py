import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
customer_df = pd.read_csv('./data/customers_dataset.csv')
order_df = pd.read_csv('./data/orders_dataset.csv')
order_items_df = pd.read_csv('./data/order_items_dataset.csv')
products_df = pd.read_csv('./data/products_dataset.csv')
product_category_df = pd.read_csv('./data/product_category_name_translation.csv')
order_reviews_df = pd.read_csv('./data/order_reviews_dataset.csv')
order_payments_df = pd.read_csv('./data/order_payments_dataset.csv')
geolocation_df = pd.read_csv('./data/geolocation_dataset.csv')
sellers_df = pd.read_csv('./data/sellers_dataset.csv')

# Dashboard Title
st.title("E-Commerce Data Analytics Dashboard")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.selectbox("Choose a section:", ["Customer Analysis", "Order Analysis", "Product Analysis", "Customer Reviews", "Geolocation", "Correlation Analysis"])

# Customer Analysis
if options == "Customer Analysis":
    st.header("Customer Distribution")
    st.write(customer_df.head())

    # Plotting customer distribution
    customer_state_dist = customer_df['customer_state'].value_counts()
    plt.figure(figsize=(10,6))
    sns.barplot(x=customer_state_dist.index, y=customer_state_dist.values, palette="Blues_d")
    plt.xticks(rotation=90)
    plt.title("Customer Distribution by State")
    st.pyplot(plt)

# Order Analysis
if options == "Order Analysis":
    st.header("Order Trends")
    st.write(order_df.head())
    
    # Example: showing order status distribution
    order_status_dist = order_df['order_status'].value_counts()
    st.bar_chart(order_status_dist)

    # Example: showing orders over time (assuming order_df has a date column)
    st.line_chart(order_df.groupby('order_purchase_timestamp').size())

# Product Analysis
# Product Analysis
if options == "Product Analysis":
    st.header("Product Category Analysis")
    st.write(products_df.head())
    
    # Calculate revenue per product category
    # Merging datasets: order_items, products, and product_category_name_translation
    merged_products = pd.merge(order_items_df, products_df, on='product_id')
    merged_products = pd.merge(merged_products, product_category_df, on='product_category_name')

    # Calculate total revenue per product category
    merged_products['revenue'] = merged_products['price'] * merged_products['order_item_id']
    category_revenue = merged_products.groupby('product_category_name_english')['revenue'].sum().sort_values(ascending=False)

    # Show top 10 categories by revenue
    st.subheader("Top 10 Product Categories by Revenue")
    st.bar_chart(category_revenue.head(10))

    # Show detailed table for top 10 categories
    st.write(category_revenue.head(10))

# Customer Reviews
if options == "Customer Reviews":
    st.header("Customer Review Analysis")
    st.write(order_reviews_df.head())
    
    # Example: Showing distribution of review scores
    review_score_dist = order_reviews_df['review_score'].value_counts()
    st.bar_chart(review_score_dist)

    # Showing positive vs negative reviews
    positive_reviews = order_reviews_df[order_reviews_df['review_score'] >= 4].shape[0]
    negative_reviews = order_reviews_df[order_reviews_df['review_score'] <= 2].shape[0]
    
    st.write(f"Positive reviews: {positive_reviews}")
    st.write(f"Negative reviews: {negative_reviews}")

# Geolocation
if options == "Geolocation":
    st.header("Geolocation of Customers and Sellers")

    # Rename columns to match Streamlit's expected format for map data
    geolocation_df = geolocation_df.rename(columns={
        'geolocation_lat': 'latitude', 
        'geolocation_lng': 'longitude'
    })

    # Display the map with customer/seller locations
    st.map(geolocation_df[['latitude', 'longitude']])

# Correlation Analysis
if options == "Correlation Analysis":
    st.header("Correlation Analysis: Delivery Time and Customer Satisfaction")

    # Calculating delivery time
    order_df['delivery_time'] = pd.to_datetime(order_df['order_delivered_customer_date']) - pd.to_datetime(order_df['order_purchase_timestamp'])
    order_df['delivery_time'] = order_df['delivery_time'].dt.days  # convert to number of days

    # Merging with reviews
    merged_df = pd.merge(order_df, order_reviews_df, on='order_id')
    
    # Correlation between delivery time and review scores
    correlation = merged_df[['delivery_time', 'review_score']].corr()

    st.write("Correlation between Delivery Time and Customer Satisfaction:")
    st.write(correlation)

    # Visualization of the correlation
    plt.figure(figsize=(8,6))
    sns.scatterplot(x='delivery_time', y='review_score', data=merged_df)
    plt.title("Delivery Time vs Customer Satisfaction")
    plt.xlabel("Delivery Time (days)")
    plt.ylabel("Review Score")
    st.pyplot(plt)

# Footer
st.sidebar.markdown("Developed by Giovanny Halimko")
