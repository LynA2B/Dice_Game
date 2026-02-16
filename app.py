from flask import Flask, render_template, request, session
from games.dice_game import DiceGame

app = Flask(__name__)
app.secret_key = "secret-key" # flask can store data in the session 

# App metadata
APP_NAME = "My Flask App"
APP_VERSION = "1.0"
APP_DESCRIPTION = "A basic Flask application"

@app.route("/", methods=["GET", "POST"])
def dice_game():
    # if no game exists, create a new one
    if "game" not in session:
        game = DiceGame()
        game.__dict__ = session["game"]
    else:
        # load the saved game from the session
        game = DiceGame()
        game.__dict__ = session["game"]

    # if user submitted the form
    if request.method == "POST":
        # get number typed by the user
        user_input = request.form.get("user_roll")

        if user_input:
            # convert input to an int
            roll = int(user_input)
        else:
            # if use didn't type anything, roll randomly
            roll = game.roll_dice()

        # play one turn of the game
        game.play_turn(roll)

        # save the updated game back into the session
        session["game"] = game.__dict__

    # show webpage
    return render_template("dice.html", game=DiceGame())

if __name__ == "__main__":
    app.run(debug=True)