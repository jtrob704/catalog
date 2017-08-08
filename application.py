from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

@app.route('/')
@app.route('/catalog')
def items():
    return "Item Catalog Application"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
