import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Data Loading
df = pd.read_excel("earthquake_data.xlsx")

# Print column names to check for potential typos
print(df.columns)

# Merging date and time columns
df["DateTime"] = pd.to_datetime(df["Tarih"].astype(str) + " " + df["Saat"], format="%Y.%m.%d %H:%M:%S")

df.drop(["Tarih", "Saat"], axis=1, inplace=True)

# Analyzing the ML column
df["ML"] = pd.to_numeric(df["ML"], errors="coerce")  # Ignores numerical errors
print(f'Missing values in ML column: {df["ML"].isnull().sum()}')
# If there are missing values, let's drop them
df_clean = df.dropna(subset=["ML"])
print("Cleaned dataset size:", df_clean.shape)

# Earthquakes per day plot (Updated to remove palette warning)
plt.figure(figsize=(12, 6))
sns.countplot(data=df_clean, x=df_clean["DateTime"].dt.date)  # Removed palette to avoid FutureWarning
plt.xticks(rotation=45)
plt.title("Earthquakes Per Day")
plt.xlabel("Date")
plt.ylabel("Number of Earthquakes")

# Using subplots_adjust for better margin control instead of tight_layout
plt.subplots_adjust(bottom=0.2, top=0.95, left=0.1, right=0.95)
plt.show()

# Distribution of earthquake magnitudes
plt.figure(figsize=(8,6))
sns.histplot(df_clean["ML"], bins=50, kde=True, color="skyblue")
plt.title("Earthquake Magnitude Distribution")
plt.xlabel("Magnitude (ML)")
plt.ylabel("Frequency")
plt.subplots_adjust(bottom=0.2, top=0.95, left=0.1, right=0.95)
plt.show()

# Depth vs magnitude plot (Check column name and add hue correctly)
plt.figure(figsize=(16,12))

# Check if the correct column name for depth is used
if "Derinlik(km)" in df_clean.columns:
    sns.scatterplot(data=df_clean, x='Derinlik(km)', y='ML', hue='Yer', palette='deep')
    plt.title("Depth vs Magnitude of Earthquakes")
    plt.xlabel("Depth (km)")
    plt.ylabel("Magnitude (ML)")
    plt.legend(bbox_to_anchor=(1,1), loc="center")
    plt.subplots_adjust(bottom=0.2, top=0.95, left=0.1, right=0.95)
    plt.show()
else:
    print("Depth column 'Derinlik(km)' not found in the dataset.")

# Create interactive map
map_center=[38.0,35.0]
m = folium.Map(location=map_center, zoom_start=5)

# Adding each earthquake to the map
for idx, row in df_clean.iterrows():
    folium.CircleMarker(
        location=[row["Enlem(N)"], row["Boylam(E)"]],
        radius=row["ML"]*2,
        popup=f"Location: {row['Yer']}<br>Magnitude: {row['ML']}<br>Depth: {row['Derinlik(km)']} km",
        color='crimson',
        fill=True,
        fill_color="crimson"
    ).add_to(m)

m.save("earthquakes_map.html")
print("Process completed.")
