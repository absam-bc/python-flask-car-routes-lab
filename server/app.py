from flask import Flask

app = Flask(__name__)

# List of car models available in our fleet
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


# Welcome route for the car company
@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'


# Route for checking whether a car model exists
@app.route('/<model>')
def car_model(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'


if __name__ == '__main__':
    app.run(debug=True)