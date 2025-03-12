from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)  # Ensure this variable name is 'app'
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    query = data.get("query")

    if not query:
        return jsonify({"error": "Missing query parameter"}), 400

    # AI Content Generation for Full-Length Marketing Video Script
    prompt = f"Generate a professional, full-length marketing video script for the trending topic: {query}. Include an engaging opening, product/service introduction, key benefits, customer testimonials (if applicable), a call-to-action, and a strong closing."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI specializing in digital marketing content creation."},
                  {"role": "user", "content": prompt}]
    )

    return jsonify({
        "query": query,
        "marketing_video_script": response['choices'][0]['message']['content']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Ensure the correct app variable is used
