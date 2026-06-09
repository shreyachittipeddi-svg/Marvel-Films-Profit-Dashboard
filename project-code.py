import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Box Office Dashboard", page_icon = ":bar_chart:", layout = "wide")
st.title("MCU Films From 2008 to 2019")
marvel = pd.read_csv("/Users/shreyachittipeddi/Downloads/mcu_films.csv")

with st.expander('About Box Office Dashboard'):
    st.header("About the MCU Films Dataset")
    st.write("This dataset is a public dataset from Kaggle which has data from 2008 to 2019 about the box office profits on each film's opening weekend, as well as U.S. and international total box office profits.")
    st.image("/Users/shreyachittipeddi/Downloads/marvel.png")


st.header("Opening Weekend Profits by Movie")
st.bar_chart(data = marvel, x = "movie", y = "opening_weekend_us", x_label = "Movie Title", y_label = "Opening Weekend Profits", color = "#F0141E", horizontal = True)
st.header("Gross Domestic and International Profits by Movie")
st.line_chart(data = marvel, x = "movie", y = ["gross_us", "gross_world"], x_label = "Movie Title", y_label = "gross_profits", color = ["#F7D027", "#00991f"])