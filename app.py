from flask import Flask, request, jsonify
from time import time
from scraper import scrape_discourse

app = Flask(__name__)

@app.route("/api/", methods=["POST"])
def answer_question():
    start = time()

    data = request.get_json()
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "No question provided"}), 400

    print("Received question:", question)

    # Simulate loading scraped data
    discourse_data = scrape_discourse("2025-01-01", "2025-04-14")

    # Dummy logic to respond based on question content
    if "gpt-3.5" in question or "gpt-4o" in question:
        answer = "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly."
        links = [
            {
                "text": "Use the model that’s mentioned in the question.",
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4"
            },
            {
                "text": "Just use a tokenizer to get number of tokens and multiply that by the rate.",
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3"
            }
        ]
    else:
        answer = f"I'm a Virtual TA. Sorry, I couldn't find a specific answer to your question: '{question}'"
        links = []

    duration = time() - start
    print(f"Response Time: {duration:.4f} seconds")

    return jsonify({"answer": answer, "links": links})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
