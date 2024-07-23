import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load dataset from CSV and remove rows with null values
df = pd.read_csv('movies.csv').dropna()

# Drop rows with any null values
print(df.head)
# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form['genre'].capitalize()  # Convert genre to capitalize first letter
    num_recommendations = int(request.form['num_recommendations'])
    
    # Filter movies by genre
    filtered_movies = df[df['genres'].str.contains(genre, case=False)]
    
    # Get top recommendations (since there's no vote_average, we can just return the filtered movies)
    recommended_movies = filtered_movies.head(num_recommendations)
    print(recommended_movies)
    return render_template('recommend.html', movies=recommended_movies.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)













