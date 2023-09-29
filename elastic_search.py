from flask import Flask, jsonify, request
import mysql.connector
from elasticsearch import Elasticsearch, ConnectionError

app = Flask(__name__)

# Replace the following variables with your MySQL database credentials
db_host = "localhost"
db_user = "root"
db_password = "sincostan"
db_name = "tribedb"

# Establish connection to MySQL
conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)

# Create a cursor to execute SQL queries
cursor = conn.cursor()
query = "SELECT srctxt, tgttxt FROM eng_hin"
cursor.execute(query)
data_from_mysql = cursor.fetchall()

# Close the MySQL connection
cursor.close()
conn.close()

# Connect to Elasticsearch
try:
    es = Elasticsearch(['http://localhost:9200'])
except ConnectionError as e:
    print(f"Error connecting to Elasticsearch: {e}")
    es = None

# Index name
index_name = "my_index"

# Define the index mapping (optional but recommended)
mapping = {
    "properties": {
        "srctxt": {"type": "text"},
        "tgttxt": {"type": "text"},
    }
}

# Create the index if it does not exist
if es and not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body={"mappings": mapping})

# Route to fetch data from Elasticsearch using search query
@app.route('/search', methods=['GET'])
def search_data():
    query = request.args.get('query', '')  # Get the 'query' parameter from the request
    if not query:
        return jsonify({'error': 'Please provide a query parameter "query".'}), 400

    if es:
        # Simple text-based search query
        search_query = {
            "query": {
                "match": {
                    "title": query
                }
            }
        }

        # Execute the search query
        try:
            result = es.search(index=index_name, body=search_query)
            hits = result['hits']['hits']
            search_results = [{"srctxt": hit['_source']['srctxt'], "tgttxt": hit['_source']['tgttxt']} for hit in hits]
            return jsonify(search_results)
        except Exception as e:
            return jsonify({'error': 'An error occurred while processing the search query.', 'details': str(e)}), 500
    else:
        return jsonify({'error': 'Connection to Elasticsearch could not be established.'}), 500

if __name__ == '__main__':
    app.run(debug=True)

