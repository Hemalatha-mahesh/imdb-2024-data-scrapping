import pandas as pd
import plotly.express as px
import streamlit as st


# Streamlit page setup
st.set_page_config(page_title="IMDb Dashboard", layout="wide")
########## 1) TOP 10 MOVIES BY RATING AND VOTING COUNTS ########
st.title("1.IMDb Top 10 Movies Ratings and Votings")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("D:/Data scrapping and cleaning/cleaned_data.csv")   

df = load_data()

# Sidebar filter
genres = df["Genre"].dropna().unique()
selected_genre = st.sidebar.selectbox("Select Genre for Top 10 movies", ["All"] + list(genres))

# Filter dataset by Genre
if selected_genre != "All":
    filtered_df = df[df["Genre"] == selected_genre]
else:
    filtered_df = df

              #Top 10 Movies by Ratings#
top10_ratings = filtered_df.nlargest(10, "Ratings")
fig_ratings = px.bar(
    top10_ratings,
    x="Movie_Name",
    y="Ratings",
    color="Ratings",
    text="Ratings",
    title=f"Top 10 Movies by Ratings ({selected_genre})"
)
fig_ratings.update_traces(texttemplate='%{text:.2f}', textposition="outside")
fig_ratings.update_layout(xaxis_tickangle=-45, yaxis=dict(range=[0,10]))  # IMDb Ratings are out of 10

               #Top 10 Movies by Voting Counts#
top10_votes = filtered_df.nlargest(10, "Voting_counts")
fig_votes = px.bar(
    top10_votes,
    x="Movie_Name",
    y="Voting_counts",
    color="Voting_counts",
    text="Voting_counts",
    title=f"Top 10 Movies by Voting Counts ({selected_genre})"
)
fig_votes.update_traces(textposition="outside")
fig_votes.update_layout(xaxis_tickangle=-45)

# Layout side by side
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_ratings, width="stretch")
    st.dataframe(top10_ratings)
with col2:
    st.plotly_chart(fig_votes,  width="stretch")
    st.dataframe(top10_votes)


############# 2) IMDB MOVIES PER GENRE ############
st.title("2.IMDb Movies by Genre")

# Count movies per Genre
genre_counts = df["Genre"].value_counts().reset_index()
genre_counts.columns = ["Genre", "Movie_Count"]

# Plot bar chart
fig = px.bar(
    genre_counts,
    x="Genre",
    y="Movie_Count",
    color="Movie_Count",
    text="Movie_Count",
    title="Number of Movies by Genre"
)
fig.update_traces(textposition="outside")
fig.update_layout(xaxis_tickangle=-45)

# Show chart
st.plotly_chart(fig,  width="stretch")

# Show table
st.dataframe(genre_counts)

############## 3) AVERAGE MOVIE DURATION ################
st.title("3.Average Movie Duration per Genre")
# --- Average duration per genre ---
avg_duration = df.groupby("Genre")["Duration"].mean().reset_index()
avg_duration = avg_duration.sort_values(by="Duration", ascending=True)
# --- Plot horizontal bar chart ---
fig = px.bar(
    avg_duration,
    x="Duration",
    y="Genre",
    orientation="h",
    color="Duration",
    text=avg_duration["Duration"].round(1),
    title="Average Movie Duration per Genre (minutes)"
)
fig.update_traces(textposition="outside")
fig.update_layout(yaxis=dict(title="Genre"), xaxis=dict(title="Avg Duration (minutes)"))

# Show chart
st.plotly_chart(fig,  width="stretch")

# Show table
st.dataframe(avg_duration)

########## 4) AVERAGE VOTING COUNTS BY GENRE ########
st.title("4.Average Voting Counts by Genre")

#Average voting counts per genre
avg_votes = df.groupby("Genre")["Voting_counts"].mean().reset_index()
avg_votes = avg_votes.sort_values(by="Voting_counts", ascending=False)

#Bar chart 
fig = px.bar(
    avg_votes,
    x="Genre",
    y="Voting_counts",
    color="Voting_counts",
    text=avg_votes["Voting_counts"].round(0),
    title="Average Voting Counts across Genres"
)
fig.update_traces(textposition="outside")
fig.update_layout(xaxis_tickangle=-45, yaxis=dict(title="Avg Voting Counts"))

# Show chart
st.plotly_chart(fig, width="stretch")

# Show table
st.dataframe(avg_votes)

############ 5) DISTRIBUTION OF MOVIE RATINGS ###########
st.title("5.Distribution of Movie Ratings")

#Histogram of Ratings 
fig = px.histogram(
    df,
    x="Ratings",
    nbins=20,   # number of bins (adjust as needed)
    color_discrete_sequence=["#1f77b4"],  # blue bars
    title="Movie Ratings"
)

fig.update_layout(
    xaxis=dict(title="Ratings"),
    yaxis=dict(title="Number of Movies"),
    bargap=0.1
)

# Show chart
st.plotly_chart(fig, use_container_width=True)

############ 6) TOP RATED MOVIE FOR EACH GENRE ###########
st.title("6.Top Rated Movie for Each Genre")

#Find top rated movie per genre
top_movies = df.loc[df.groupby("Genre")["Ratings"].idxmax()].reset_index(drop=True)

# Optional: sort by Ratings descending
top_movies = top_movies.sort_values(by="Ratings", ascending=False)

# Display table
st.dataframe(top_movies)

############## 7) GENRES WITH HIGHEST TOTAL VOTING COUNTS ##########
st.title("7.Genres with Highest Total Voting Counts")

# Sum of voting counts per genre
votes_per_genre = df.groupby("Genre")["Voting_counts"].sum().reset_index()
votes_per_genre = votes_per_genre.sort_values(by="Voting_counts", ascending=False)

# Pie chart 
fig = px.pie(
    votes_per_genre,
    names="Genre",
    values="Voting_counts",
    title="Total Voting Counts by Genre",
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig.update_traces(textposition='inside', textinfo='percent+label')

# Display chart
st.plotly_chart(fig,  width="stretch")

# Display table
st.dataframe(votes_per_genre)

############# 8) SHORTEST AND LONGEST MOVIES ###########
st.title("8.Shortest and Longest Movies")

# Shortest movie
shortest_movie = df.loc[df["Duration"].idxmin()]

# Longest movie
longest_movie = df.loc[df["Duration"].idxmax()]


#display radiobar & table
movie_choice = st.sidebar.radio(
    "Movie length:",
    ["Both", "Shortest", "Longest"]
)

# Display table based on sidebar selection
if movie_choice == "Shortest":
    st.subheader("Shortest Movie")
    st.dataframe(pd.DataFrame([shortest_movie]).reset_index(drop=True))
elif movie_choice == "Longest":
    st.subheader("Longest Movie")
    st.dataframe(pd.DataFrame([longest_movie]).reset_index(drop=True))
else:
    st.subheader("Shortest and Longest Movies")
    combined_df = pd.DataFrame([shortest_movie, longest_movie]).reset_index(drop=True)
    st.dataframe(combined_df)

############### 9) RATINGS BY GENRE ################
st.title("9.Average Ratings Across Genres")

# Compute average ratings per genre
avg_ratings = df.groupby("Genre")["Ratings"].mean().reset_index()

# Heatmap using Plotly
# Compute average rating per genre
avg_ratings = df.groupby("Genre")["Ratings"].mean().reset_index()

# Create a heatmap-style horizontal bar chart
fig = px.bar(
    avg_ratings,
    x="Ratings",
    y="Genre",
    orientation='h',
    color="Ratings",
    text=avg_ratings["Ratings"].round(2),
    color_continuous_scale="Viridis",
    title="Average Movie Ratings by Genre"
)
fig.update_traces(textposition='outside')
fig.update_layout(xaxis=dict(title="Average Rating"), yaxis=dict(title="Genre"))

# Show chart
st.plotly_chart(fig, width="stretch")

################ 10) CORRELATION ANALYSIS ###########
st.title("10.Relationship Between Ratings and Voting Counts")

# Sidebar filter for Genre
st.sidebar.header("Filters")
genres = df["Genre"].dropna().unique()
selected_genre = st.sidebar.selectbox("Select Genre", ["All"] + list(genres))

# Filter dataset based on selection
if selected_genre != "All":
    filtered_df = df[df["Genre"] == selected_genre]
else:
    filtered_df = df

# Drop rows with missing values
filtered_df = filtered_df.dropna(subset=["Ratings", "Voting_counts"])

# Scatter plot
fig = px.scatter(
    filtered_df,
    x="Voting_counts",
    y="Ratings",
    size="Voting_counts",
    color="Ratings",
    hover_name="Movie_Name",
    title=f"IMDb Ratings vs Voting Counts ({selected_genre})",
    labels={"Voting_counts": "Voting Counts", "Ratings": "Ratings"},
    log_x=True  # log scale for votes
)

st.plotly_chart(fig, width="stretch")

# Duration
# Categorize runtime 
def categorize_runtime(minutes):
    if minutes < 120:
        return "<2 hrs"
    elif 120 <= minutes <= 180:
        return "2-3 hrs"
    else:
        return ">3 hrs"

df["Runtime_Category"] = df["Duration"].apply(categorize_runtime)

############ RUN TIME FILTER #############
st.title("IMDb Movies Runtime Filter")

# Dropdown for runtime category
runtime_filter = st.sidebar.selectbox(
    "Select Runtime Category:",
    ["All", "<2 hrs", "2-3 hrs", ">3 hrs"]
)

# Apply filter
if runtime_filter == "All":
    filtered_df = df
else:
    filtered_df = df[df["Runtime_Category"] == runtime_filter]

st.subheader(f"Movies in category: {runtime_filter}")
st.dataframe(filtered_df)

############# MOVIES FILTER BY RATINGS ############
st.title("IMDb Movies Filter by Ratings")

# Slider for minimum IMDb rating
rating_threshold = st.sidebar.slider(
    "Select Minimum IMDb Rating:",
    min_value=0.0,
    max_value=10.0,
    value=8.0,
    step=0.1
)

# Apply rating filter 
filtered_df = df[df["Ratings"] >= rating_threshold]

# Show results
st.subheader(f"Movies with IMDb Rating ≥ {rating_threshold}")
st.dataframe(filtered_df)

################ MOVIES FILTER BY VOTES #############
st.title("IMDb Movies Filter by Votes")

# Sidebar filter
st.sidebar.header("Filters")

votes_threshold = st.sidebar.number_input(
    "Minimum Number of Votes:",
    min_value=0,
    value=10000,   # default 10,000
    step=1000
)

# Apply votes filter
filtered_df = df[df["Voting_counts"] >= votes_threshold]

# Show results
st.subheader(f"Movies with ≥ {votes_threshold} votes")
st.dataframe(filtered_df)

################# MOVIES FILTER BY GENRE ###############
st.title("IMDb Movies Filter by Genre")

# Sidebar filter
st.sidebar.header("Filters")

# Get unique genres from DB
genres = df["Genre"].dropna().unique().tolist()

# Multi-select for genres
selected_genres = st.sidebar.multiselect(
    "Select Genre(s):",
    options=genres,
    default=[]
)

# Apply genre filter 
if selected_genres:
    filtered_df = df[df["Genre"].isin(selected_genres)]
else:
    filtered_df = df  # if nothing selected, show all

# Show results
if selected_genres:
    st.subheader(f"Movies in genres: {', '.join(selected_genres)}")
else:
    st.subheader("All Movies (no genre filter applied)")

st.dataframe(filtered_df)


# =============================
#        MOVIES FILTER
# =============================
st.title("IMDB Movies Filter")

# Sidebar Filters
st.sidebar.header("Filters")

# Genre Filter
genres = df['Genre'].dropna().unique().tolist()
selected_genres = st.sidebar.multiselect("Select Genres", genres)

# Ratings Filter
min_rating, max_rating = st.sidebar.slider("Select Ratings Range", 
                                           float(df['Ratings'].min()), 
                                           float(df['Ratings'].max()), 
                                           (float(df['Ratings'].min()), float(df['Ratings'].max())))

# Duration Filter
min_duration, max_duration = st.sidebar.slider("Select Duration (in minutes)", 
                                               int(df['Duration'].min()), 
                                               int(df['Duration'].max()), 
                                               (int(df['Duration'].min()), int(df['Duration'].max())))

# Voting Counts Filter
min_votes = st.sidebar.number_input("Minimum Voting Counts", 
                                    min_value=0, 
                                    max_value=int(df['Voting_counts'].max()), 
                                    value=0)


# Apply Filters
filtered_df = df.copy()

if selected_genres:
    filtered_df = filtered_df[filtered_df['Genre'].isin(selected_genres)]

filtered_df = filtered_df[
    (filtered_df['Ratings'] >= min_rating) &
    (filtered_df['Ratings'] <= max_rating) &
    (filtered_df['Duration'] >= min_duration) &
    (filtered_df['Duration'] <= max_duration) &
    (filtered_df['Voting_counts'] >= min_votes)
]

############ Display Dynamic DataFrame ################

st.subheader("Filtered Results")
st.write(f"Showing **{filtered_df.shape[0]} movies** after applying filters")

st.dataframe(filtered_df, width="stretch")

######### DOWNLOAD BUTTON ############
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode("utf-8")

csv = convert_df(filtered_df)
st.download_button("Download CSV", data=csv, file_name="filtered_movies.csv", mime="text/csv")

