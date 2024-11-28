# from flask import Flask
# from app.routes import routes
#
# app = Flask(__name__)
# app.register_blueprint(routes)
#
# if __name__ == "__main__":
#     app.run(debug=True)

from app.game import RussianRoulette

if __name__ == "__main__":
    # Instanziere das Spiel
    game = RussianRoulette()
    game.start_game()