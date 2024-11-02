from flask import Flask, render_template
import util

# Create Flask application instance
app = Flask(__name__)

# Database credentials 
username = 'raywu1990'  
password = 'test'       
host = '127.0.0.1'
port = '5432'
database = 'dvdrental'  

# Route for updating basket_a with a new fruit "Cherry"
@app.route('/api/update_basket_a')
def update_basket_a():
    try:
        # Connect to the database
        cursor, connection = util.connect_to_db(username, password, host, port, database)
        
        # Insert "Cherry" into basket_a
        util.run_sql(cursor, "INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry') ON CONFLICT DO NOTHING;")
        
        # Commit the transaction
        connection.commit()
        
        # Disconnect from the database
        util.disconnect_from_db(connection, cursor)
        
        return "Success!"  # Display success message if no errors
    except Exception as e:
        return str(e), 500  # Display error message if an exception occurs

# Route for displaying unique fruits in basket_a and basket_b
@app.route('/api/unique')
def unique_fruits():
    try:
        # Connect to the database
        cursor, connection = util.connect_to_db(username, password, host, port, database)
        
        # Fetch fruits that are unique to basket_a
        fruits_a = util.run_and_fetch_sql(cursor, """
            SELECT DISTINCT fruit_a FROM basket_a
            WHERE fruit_a NOT IN (SELECT fruit_b FROM basket_b);
        """)
        
        # Fetch fruits that are unique to basket_b
        fruits_b = util.run_and_fetch_sql(cursor, """
            SELECT DISTINCT fruit_b FROM basket_b
            WHERE fruit_b NOT IN (SELECT fruit_a FROM basket_a);
        """)
        
        # Disconnect from the database
        util.disconnect_from_db(connection, cursor)

        # Calculate the maximum length of the lists
        max_length = max(len(fruits_a), len(fruits_b))

        # Render the HTML and pass fruits_a, fruits_b, and max_length
        return render_template('unique_fruits.html', fruits_a=fruits_a, fruits_b=fruits_b, max_length=max_length)
    except Exception as e:
        return str(e), 500  # Display error message if an exception occurs



# Run the Flask application
if __name__ == '__main__':
    app.debug = True  # Enable debug mode for development
    app.run(host='127.0.0.1', port=5000)  # Explicitly set port to 5000

