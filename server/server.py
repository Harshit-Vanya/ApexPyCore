from flask import Flask, render_template, request, jsonify
import util
from util import app

if __name__ == '__main__':
    util.load_artifacts()
    app.run(host='0.0.0.0', port=5000, debug=True)