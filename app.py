from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Azure SQL Server configurations
server = 'natureproduct.database.windows.net'
database = 'nature'
username = 'welcome'
password = 'Azure@12345'
driver = '{ODBC Driver 18 for SQL Server}'

# Establishing connection to SQL Server
def get_db_connection():
    try:
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        return conn
    except Exception as e:
        print(str(e))
        return None

# API endpoint to fetch data from SQL Server
@app.route('/data', methods=['GET'])
def get_data():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM YourTable")  # Replace YourTable with your actual table name
        data = cursor.fetchall()
        connection.close()
        return jsonify(data)
    else:
        return jsonify({"message": "Failed to connect to the database"}), 500

if __name__ == '__main__':
    app.run(debug=True)
