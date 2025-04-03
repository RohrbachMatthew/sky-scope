from flask import Flask, render_template, redirect, url_for
from app import create_app


app = create_app() 

@app.route('/')
def main_menu():
    return render_template('index.html')  

if __name__ == "__main__":
    app.run(debug=True)
