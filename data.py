# Drop columns with too many NaNs
df = df.dropna(axis=1, thresh=len(df)*0.5)

# Drop rows missing key info
df = df.dropna(subset=['title', 'publish_time'])

# Convert dates
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df = df.dropna(subset=['publish_time'])
df['year'] = df['publish_time'].dt.year

# Example: Add abstract word count
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))
