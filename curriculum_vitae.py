from flask import Flask
from curriculum_vitae_routes import curriculum_vitae

app = Flask(__name__)
app.register_blueprint(curriculum_vitae)

if __name__ == '__main__':
    app.run(debug=True)
