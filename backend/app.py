from flask import Flask, request, send_file, jsonify
import os
import tempfile
from crypto.file_encryptor import encrypt_file, decrypt_file

app = Flask(__name__)

@app.route("/")
def index():
    return {"status": "Blowfish API Ready"}

@app.route("/encrypt", methods=["POST"])
def encrypt_route():
    try:
        password = request.form.get("password")
        file = request.files.get("file")

        if not password or not file:
            return jsonify({"error": "Missing file or password"}), 400

        # Save temp input file
        temp_in = tempfile.NamedTemporaryFile(delete=False)
        file.save(temp_in.name)

        # Save temp output file
        temp_out = tempfile.NamedTemporaryFile(delete=False).name

        encrypt_file(temp_in.name, temp_out, password)

        return send_file(temp_out,
                         as_attachment=True,
                         download_name=file.filename + ".bf")

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/decrypt", methods=["POST"])
def decrypt_route():
    try:
        password = request.form.get("password")
        file = request.files.get("file")

        if not password or not file:
            return jsonify({"error": "Missing file or password"}), 400

        temp_in = tempfile.NamedTemporaryFile(delete=False)
        file.save(temp_in.name)

        temp_out = tempfile.NamedTemporaryFile(delete=False).name

        decrypt_file(temp_in.name, temp_out, password)

        return send_file(temp_out,
                         as_attachment=True,
                         download_name=file.filename.replace(".bf", ""))

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
