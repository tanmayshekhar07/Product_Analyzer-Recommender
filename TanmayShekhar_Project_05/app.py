import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
product_dict = pickle.load(open('products_dict.pkl','rb'))
products = pd.DataFrame(product_dict)

cosine_sim = pickle.load(open('cosine_sim.pkl','rb'))

balanced_df_dict = pickle.load(open('balanced_df_dict.pkl','rb'))
balanced_df = pd.DataFrame(balanced_df_dict)

def recommend_product(product_name):
    # Get the index of the product that matches the product name
    index = products[products['product_name'] == product_name].index[0]

    # Get the pairwise similarity scores of all products with that product
    distances = sorted(list(enumerate(cosine_sim[index])), reverse=True, key=lambda x: x[1])

    recommended_products = []
    recommended_product_posters = []

    # Print the top 5 similar products
    for i in distances[1:6]:
        recommended_products.append(products.iloc[i[0]].product_name)
        # fetch movie poster  url
        recommended_product_posters.append(fetch_image(products.iloc[i[0]].product_name))
    return recommended_products, recommended_product_posters

def fetch_image(product_name):
    # Filter the DataFrame for the given product name and retrieve the first image URL
    url = products[products['product_name'] == product_name]['image'].iloc[0]
    return url


def bar_chart(selected_product_name):
    # Filter the DataFrame for the given product name
    filtered_df = balanced_df[balanced_df['product_name'] == selected_product_name]
    
    # Count the sentiment values
    sentiment_counts = filtered_df['sentiment'].value_counts()
    
    # Start plotting
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('linen')

    sentiment_counts.plot(kind='bar', ax=ax, color=['#BB6464', '#81B622'])
    
    # Set the title and labels
    ax.set_title(f"Sentiment Counts for Product {selected_product_name}", fontsize=14)
    ax.set_xlabel('Sentiment', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.set_xticklabels(['Negative', 'Positive'], rotation=0)
    
    # Add some space before the bar chart
    st.write("\n")  # This adds a newline character to create some space
    st.write("\n")

    # Display the plot within a container with a background
    with st.container():
        st.pyplot(fig)





def get_product_details(product_name):
    # Retrieve details of the given product name
    product_row = products[products['product_name'] == product_name].iloc[0]
    details = {
        'image': product_row['image'],
        'price': product_row['price'],
        'avg_rating': product_row['avg_rating_per_item']
    }
    return details

# Image display dimensions
IMAGE_WIDTH = 150  # You can adjust this width as needed
IMAGE_HEIGHT = 150  # You can adjust this height as needed

st.header('Product Recommender System')

# Dropdown for product selection
selected_product_name = st.selectbox(
    "Type or select a product from the dropdown",
    [''] + list(products['product_name'].values),  # Add a blank option as the first choice
    index=0,
    placeholder="Type or select a product...",
)

if st.button('Show Details and Recommend'):
    if selected_product_name:  # Check if a product name is selected
        # Display the details of the selected product
        selected_product_details = get_product_details(selected_product_name)
        st.image(selected_product_details['image'], caption=selected_product_name, width=IMAGE_WIDTH, output_format='PNG')

        st.write(f"Price: {selected_product_details['price']}")
        st.write(f"Average Rating: {selected_product_details['avg_rating']}")

        # Get and display recommended products
        recommended_products, recommended_product_posters = recommend_product(selected_product_name)
        
        # Create columns for the recommended products
        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.text(recommended_products[i])
                st.image(recommended_product_posters[i], width=IMAGE_WIDTH, output_format='PNG')
        
        # Display the sentiment bar chart
        bar_chart(selected_product_name)
    else:
        # If no product is selected, display a message
        st.error('Please choose a product to get recommendations.')
