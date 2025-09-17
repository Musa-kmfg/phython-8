import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load cleaned dataset
df = pd.read_csv('cleaned_metadata.csv', parse_dates=['publish_time'])

st.title("CORD-19 Data Explorer")
st.write("Explore trends in COVID-19 research papers")

# Year filter
min_year, max_year = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select publication year range", min_year, max_year, (min_year, max_year))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write(f"Showing {len(filtered_df)} papers from {year_range[0]} to {year_range[1]}")
st.dataframe(filtered_df[['title', 'journal', 'publish_time']].head(20))

# Plot publications per year
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title("Publications by Year")
st.pyplot(fig)

# Word cloud
text = " ".join(filtered_df['title'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)
