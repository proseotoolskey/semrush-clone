from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/keywords', methods=['GET'])
def get_keywords():
    query = request.args.get('q')
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={query}"
    response = requests.get(url)
    suggestions = response.json()[1]
    return jsonify(suggestions)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
