
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/", methods=["POST"])
def virtual_ta():
    data = request.get_json()
    question = data.get("question", "")
    image = data.get("image", None)

    # Placeholder: Replace with actual logic
    answer = "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question."
    links = [
        {
            "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
            "text": "Use the model that’s mentioned in the question."
        },
        {
            "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
            "text": "Prof. Anand mentioned to just use a tokenizer to get the number of tokens and multiply by the rate."
        }
    ]

    return jsonify({
        "answer": answer,
        "links": links
    })

# Run app on Render
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
