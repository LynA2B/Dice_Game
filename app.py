from flask import Flask, render_template, request, session, redirect, url_for
from games.dice_game import DiceGame

app = Flask(__name__)
app.secret_key = "secret-key" # flask can store data in the session 

# App metadata
APP_NAME = "Dice Game"
APP_VERSION = "1.0"
APP_DESCRIPTION = "Dice Game in Python"

@app.route("/", methods=["GET", "POST"])
def dice_game():
    # if no game exists, create a new one
    if "game" not in session:
        game = DiceGame()
        session["game"] = game.__dict__
    else:
        # load the saved game from the session
        game = DiceGame()
        game.__dict__ = session.get("game", {}) # safe loading

    # if user submitted the form
    if request.method == "POST":

        if request.form.get("random"):
            roll = game.roll_dice()
        else:
            # get number typed by user
            user_input = request.form.get("user_roll")

            # if user clicked Submit Roll with an empty box
            if not user_input:
                game.result = "Error: Please enter a number between 2 and 12."
                return render_template("dice.html", game=game)
            
            roll = int(user_input)

        # play one turn of the game
        game.play_turn(roll)

        # save the updated game back into the session
        session["game"] = game.__dict__

    # show webpage
    return render_template("dice.html", game=game)

# shown when clicked on Start New Game
@app.route("/new")
def new_game():
    session.pop("game", None)
    return redirect(url_for("dice_game"))

if __name__ == "__main__":
    app.run(debug=True)