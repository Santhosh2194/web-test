from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Set path where PDFs are stored
PDF_FOLDER = os.path.join(os.getcwd(), "static/pdfs")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip().lower()  # Get user input
    if not query:
        return jsonify([])  # Return empty list if no input

    # Get all PDFs that contain the query
    matching_pdfs = [f for f in os.listdir(PDF_FOLDER) if query in f.lower() and f.endswith('.pdf')]
    
    return jsonify(matching_pdfs)  # Return matching files as JSON

if __name__ == '__main__':
    app.run(debug=True)
