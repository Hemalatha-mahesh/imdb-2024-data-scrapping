**IMDb Data Scraping, Storage & Visualization**<br/>
**Project Overview**<br/>

This project demonstrates how to scrape IMDb movie data, store it in a SQL database, and build an interactive dashboard using Streamlit for dynamic filtering and visualization.
It helps in analyzing movie trends based on ratings, genres, duration, and voting counts.

**Business Use Cases:<br/>**
**1.Top-Rated Movies:** Identify the top 10 movies with the highest ratings and voting counts.<br/>
**2.Genre Analysis:** Explore the distribution of genres in the 2024 movie list.<br/>
**3.Duration Insights:** Analyze the average duration of movies across genres.<br/>
**4.Voting Patterns:** Discover genres with the highest average voting counts.<br/>
**5.Popular Genres:** Identify the genres that dominate IMDb's 2024 list based on movie count.<br/>
**6.Rating Distribution:** Analyze the distribution of ratings across all movies.<br/>
**7.Genre vs. Ratings:** Compare the average ratings for each genre.<br/>
**8.Duration Extremes:** Identify the shortest and longest movies in 2024.<br/>
**9.Top-Voted Movies:** Find the top 10 movies with the highest voting counts.<br/>
**10.Interactive Filtering:** Allow users to filter movies by ratings, duration, votes, and genre and view the results in a tabular DataFrame format.<br/><br/>
**Approach:**<br/>
**1. Data Scraping and Storage**<br/>
**Data Source:** IMDb 2024 Movies page.<br/>
**Scraping Method:** Use Selenium to extract the following fields:<br/>
Movie Name<br/>
Genre<br/>
Ratings<br/>
Voting Counts<br/>
**Duration**
**Genre-wise Storage: **Save extracted data as individual CSV files for each genre.<br/>
**Combine Data:** Merge all genre-wise CSVs into a single DataFrame.<br/>
**SQL Storage:** Store the merged dataset into an SQL database for querying and future analysis.<br/>

**2. Data Analysis, Visualization, and Filtration<br/>**
**Interactive Visualizations<br/>**
Using Python and Streamlit, create dynamic visualizations for:<br/>
**1.Top 10 Movies by Rating and Voting Counts:** Identify movies with the highest ratings and significant voting engagement.<br/>
**2.Genre Distribution:** Plot the count of movies for each genre in a bar chart.<br/>
**3.Average Duration by Genre:** Show the average movie duration per genre in a horizontal bar chart.<br/>
**4.Voting Trends by Genre:** Visualize average voting counts across different genres.<br/>
**5.Rating Distribution:** Display a histogram or boxplot of movie ratings.<br/>
**6.Genre-Based Rating Leaders:** Highlight the top-rated movie for each genre in a table.<br/>
**7.Most Popular Genres by Voting:** Identify genres with the highest total voting counts in a pie chart.<br/>
**8.Duration Extremes:** Use a table or card display to show the shortest and longest movies.<br/>
**9.Ratings by Genre:** Use a heatmap to compare average ratings across genres.<br/>
**10.Correlation Analysis:** Analyze the relationship between ratings and voting counts using a scatter plot.<br/>

**Interactive Filtering Functionality**<br/>
**Allow users to filter the dataset based on the following criteria:<br/>**
**Duration (Hrs):** Filter movies based on their runtime (e.g., < 2 hrs, 2–3 hrs, > 3 hrs).<br/>
**Ratings:** Filter movies based on IMDb ratings (e.g., > 8.0).<br/>
**Voting Counts:** Filter based on the number of votes received (e.g., > 10,000 votes).<br/>
**Genre:** Filter movies within specific genres (e.g., Action, Drama).<br/>
Display the filtered results in a dynamic DataFrame within the Streamlit app.<br/>
Combine filtering options so users can apply multiple filters simultaneously for customized insights.<br/>
**Example Use Case:<br/>**
Users can filter for Action Movies with ratings above 8.0, duration between 2-3 hours, and voting counts greater than 50,000, and the results will be displayed dynamically as a table.<br/>

**Technical Tags**<br/>
**Languages:** Python<br/>
**Database:** MySQL/PostgreSQL<br/>
**Visualization Tools:** Streamlit<br/>
**Libraries:** Pandas, Selenium, Matplotlib, SQLAlchemy, Seaborn<br/><br/>
**Project Deliverables**<br/>
**SQL Database:** Contains the complete movie dataset.<br/>
**Python Scripts:** For data scraping, cleaning, merging, and database interaction.<br/>
**Streamlit Application:** Interactive dashboard showcasing visualizations, insights, and filtering functionality.<br/>
**CSV Files:** Genre-wise datasets for each genre in the IMDb list.<br/>
**Streamlit Application:** Interactive dashboard for real-time analysis.<br/><br/>
**Project Guidelines:<br/>**
**1.Follow coding standards:** Consistent naming conventions, modular code.<br/>
**2.Data validation:** Ensure all data is accurate and complete.<br/>
**3.Optimized queries:** Efficient SQL queries for large datasets.<br/>
**4.Documentation:** Well-documented code and a detailed project report.<br/>
