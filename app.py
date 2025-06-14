from flask import Flask, request, jsonify
from scraper import scrape_discourse

app = Flask(__name__)

# Root route (so homepage doesn’t return 404)
@app.route('/')
def home():
    return "TDS Virtual TA API is running!"

# POST API endpoint
@app.route('/api/', methods=['POST'])
def answer_question():
    data = request.get_json()
    question = data.get('question', '')

    # Use scraped content if needed (you can replace with actual logic later)
    content = scrape_discourse("2025-01-01", "2025-04-14")

    # Return dummy static response for now
    response = {
        "answer": "You must use gpt-3.5-turbo-0125, even if the AI Proxy only supports gpt-4o-mini. Use the OpenAI API directly.",
        "links": [
            {
                "text": "Use the model that’s mentioned in the question.",
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4"
            },
            {
                "text": "Just use a tokenizer to get number of tokens and multiply that by the rate.",
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3"
            }
        ]
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
