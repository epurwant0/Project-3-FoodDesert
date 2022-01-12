from flask import Flask, render_template
from config import USERNAME, PASSWORD

# Import our psycopg2 library, which lets us connect our Flask app to our Postgres database.
import sqlalchemy

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
connection_string = f"{USERNAME}:{PASSWORD}@localhost:5433/FoodDesertDB"

# Pass connection url to the sqlalchemy create_engine method
engine = sqlalchemy.create_engine(f'postgresql://{connection_string}')

# Set route
@app.route('/')
def index():
    # Store the entire footwear collection in a list
    counties = engine.execute("SELECT * FROM counties")

    # Return the template with the footwear list passed in
    return render_template('index.html', counties=counties)


if __name__ == "__main__":
    app.run(debug=True)
