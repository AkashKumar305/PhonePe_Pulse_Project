import pandas as pd
import streamlit as st
import mysql.connector
import plotly.express as px
from PIL import Image
from streamlit_option_menu import option_menu

# Function to start MySQL connection
def start_mysql():
    mysql_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql',
        database='phonepe'
    )
    mysql_cursor = mysql_connection.cursor()
    return mysql_connection, mysql_cursor

# Function to execute MySQL query
def mysql_execute(query, params=None, columns=None):
    mysql_cursor.execute(query, params)
    return pd.DataFrame(mysql_cursor.fetchall(), columns=columns)

# Function to plot pie chart
def plot_pie_chart(df, values, names, title, hover_data):
    fig = px.pie(df, values=values, names=names, title=title, hover_data=hover_data)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

# Function to plot bar chart
def plot_bar_chart(df, x, y, color, title):
    fig = px.bar(df, x=x, y=y, color=color, title=title)
    return fig

# Function for map visualization
def map_viz(df, hover_data, title):
    fig = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='State',
        hover_data=hover_data,
        color_continuous_scale='Reds',
        title=title,
        width=800,
        height=800
    )
    fig.update_geos(fitbounds="locations", visible=True)
    return fig

# Function to close MySQL connection
def close_mysql():
    mysql_cursor.close()
    mysql_connection.close()

mysql_connection, mysql_cursor = start_mysql()

# Main Streamlit app
with st.sidebar:
    options = option_menu("Menu", ["Home", "Top Charts", "Analyze Data"])

    year = st.slider('Select the Year: ', 2018, 2023)
    
    if year != 2023:
        quarter = st.slider("Select the Quarter: ", 1, 4)
    else:
        quarter = st.slider("Select the Quarter: ", 1, 3)

    select = st.selectbox('Type: ', ['Transaction', 'User'])

if options == 'Home':
    # Home Page
    img = Image.open('PhonePe_Logo.jpg')
    st.image(img, width=400)
    st.title('PhonePe Pulse Data Visualization')
    st.subheader('Project Title: ')
    st.write('PhonePe Pulse Data Visualization and Exploration:A User-Friendly Tool Using Streamlit and Plotly')
    st.subheader('Technologies Used: ')
    st.write('Github Cloning, Python, Pandas, MySQL, Streamlit, Plotly')

if options == 'Top Charts':
    # Top Charts Page
    st.title('Top Charts')
    
    if select == 'Transaction':
        # Transaction Section
        st.markdown("### :violet[State]")

        query = "SELECT state, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from agg_trans where year = %s and quarter = %s group by state order by Total desc limit 10"
        df = mysql_execute(query, (year, quarter), ['State', 'Transactions_Count', 'Total_Amount'])
        st.plotly_chart(plot_pie_chart(df, 'Total_Amount', 'State', 'Top 10 States with Highest Transaction Amount', ['Transactions_Count']))

        st.markdown("### :violet[District]")

        query = 'SELECT district, state, sum(transaction_count) as total_count, sum(transaction_amount) as total_amount FROM map_trans WHERE year = %s AND quarter = %s GROUP BY district, state ORDER BY total_amount DESC LIMIT 10'
        df = mysql_execute(query, (year, quarter), ['District', 'State', 'Transaction_Count', 'Total_Amount'])
        st.plotly_chart(plot_pie_chart(df, 'Total_Amount', 'District', 'Top 10 Districts with Highest Transaction Amount', ['State']))

        st.markdown("### :violet[Pincode]")

        query = 'SELECT pincode, state, sum(transaction_count) as total_count, sum(transaction_amount) as total_amount FROM top_trans WHERE year = %s AND quarter = %s GROUP BY pincode, state ORDER BY total_amount DESC LIMIT 10'
        df = mysql_execute(query, (year, quarter), ['Pincode', 'State', 'Transaction_Count', 'Total_Amount'])
        st.plotly_chart(plot_pie_chart(df, 'Total_Amount', 'Pincode', 'Top 10 Pincodes with Highest Transaction Amount', ['State']))

    if select == 'User':
        # User Section
        st.markdown('### :violet[Brand]')
        if (year == 2022 and quarter in [2, 3, 4]) or (year == 2023):
            st.warning('No Available Data for Year 2022 (Quarter - 2,3,4) and 2023')
        else:
            query = 'SELECT brand_type, sum(brand_user_count) as Total_Users, avg(brand_user_percentage)*100 as Avg_Precentage FROM agg_user WHERE year = %s AND quarter = %s GROUP BY brand_type ORDER BY Total_Users DESC LIMIT 10'
            df = mysql_execute(query, (year, quarter), ['Brand_Type', 'Total_Users', 'Avg_Percentage'])
            st.plotly_chart(plot_pie_chart(df, 'Avg_Percentage', 'Brand_Type', 'Top 10 Brands with Highest User Count', ['Total_Users']))

        st.markdown('### :violet[App Opens - State]')
        if year == 2018 or (year == 2019 and quarter == 1):
            st.warning('No Available Data for Year 2018 and 2019 (Quarter - 1)')
        else:
            query = 'SELECT state, sum(registered_users) as Total_Users, sum(app_opens) as App_Opens FROM map_user WHERE year = %s AND quarter = %s GROUP BY state ORDER BY App_Opens DESC LIMIT 10'
            df = mysql_execute(query, (year, quarter), ['State', 'Total_Users', 'App_Opens'])
            st.plotly_chart(plot_pie_chart(df, 'App_Opens', 'State', 'Top 10 States with Highest App Opens', ['Total_Users']))

        st.markdown('### :violet[App Opens - District]')
        if year == 2018 or (year == 2019 and quarter == 1):
            st.warning('No Available Data for Year 2018 and 2019 (Quarter - 1)')
        else:
            query = 'SELECT district, sum(registered_users) as Total_Users, sum(app_opens) as App_Opens FROM map_user WHERE year = %s AND quarter = %s GROUP BY district ORDER BY App_Opens DESC LIMIT 10'
            df = mysql_execute(query, (year, quarter), ['District', 'Total_Users', 'App_Opens'])
            st.plotly_chart(plot_pie_chart(df, 'App_Opens', 'District', 'Top 10 Districts with Highest App Opens', ['Total_Users']))

        st.markdown('### :violet[Pincode]')
        query = 'SELECT pincode, state, sum(registered_users) as Total_Users FROM top_user WHERE year = %s AND quarter = %s GROUP BY pincode, state ORDER BY Total_Users DESC LIMIT 10'
        df = mysql_execute(query, (year, quarter), ['Pincode', 'State', 'Total_Users'])
        st.plotly_chart(plot_pie_chart(df, 'Total_Users', 'Pincode', 'Top 10 Pincodes with Highest Users', ['State']))

if options == 'Analyze Data':
    # Analyze Data Page
    st.title('Map Visualization')

    if select == 'Transaction':
        # Transaction Section
        query = "SELECT state, sum(transaction_count) as Total_Count, sum(transaction_amount) as Total_amount FROM map_trans WHERE year = %s AND quarter = %s GROUP BY state ORDER BY state"
        df = mysql_execute(query, (year, quarter), ['State', 'Total_Count', 'Total_amount'])
        df_states = pd.read_csv('Statenames.csv')
        df.State = df_states
       
        st.plotly_chart(map_viz(df, ['Total_Count', 'Total_amount'], 'Total Transaction Amount by State'))

        query = 'SELECT transaction_type, sum(transaction_count) as Total_Count, sum(transaction_amount) as Total_Amount FROM agg_trans WHERE year = %s AND quarter = %s GROUP BY transaction_type ORDER BY transaction_type'
        df = mysql_execute(query, (year, quarter), ['Transaction_Type', 'Total_Count', 'Total_Amount'])
        st.plotly_chart(plot_bar_chart(df, 'Transaction_Type', 'Total_Count', 'Total_Amount', 'Transaction Type vs Total Count'))

        selected_state = st.selectbox("",
                                      ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam',
                                       'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                                       'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
                                       'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                       'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha',
                                       'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana',
                                       'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal'))

        mysql_cursor.execute(
            f"SELECT State, District, sum(transaction_count) as Total_Transactions, sum(transaction_amount) as Total_amount FROM map_trans WHERE year = {year} AND quarter = {quarter} AND State = '{selected_state}' GROUP BY State, District ORDER BY state, district")
        df = pd.DataFrame(mysql_cursor.fetchall(), columns=['State', 'District', 'Total_Transactions', 'Total_amount'])
        st.plotly_chart(plot_bar_chart(df, "District", "Total_Transactions", 'Total_amount', 'Districts vs Total Transactions'))

    if select == 'User':
        # User Section
        query = "SELECT state, sum(registered_users) as Total_Users, sum(app_opens) as App_opens FROM map_user WHERE year = %s AND quarter = %s GROUP BY state ORDER BY state"
        df = mysql_execute(query, (year, quarter), ['State', 'Total_Users', 'App_opens'])
        df_states = pd.read_csv('Statenames.csv')
        df.State = df_states

        st.plotly_chart(map_viz(df, ['Total_Users', 'App_opens'], 'Total Registered Users by State'))

        selected_state = st.selectbox("",
                                      ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam',
                                       'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                                       'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
                                       'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                       'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha',
                                       'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana',
                                       'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal'))

        mysql_cursor.execute(
            f"SELECT state, district, sum(registered_users) as Total_Users, sum(app_opens) as Total_Appopens FROM map_user WHERE year  = {year} AND quarter = {quarter} AND state = '{selected_state}' GROUP BY state, district ORDER BY state, district")
        df = pd.DataFrame(mysql_cursor.fetchall(), columns=['State', 'District', 'Total_Users', 'Total_Appopens'])
        st.plotly_chart(plot_bar_chart(df, "District", "Total_Users", 'Total_Appopens', 'Districts vs Total Users'))

# Close MySQL connection
close_mysql()
