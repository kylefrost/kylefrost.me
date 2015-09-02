from flask import Flask, render_template
import random

app = Flask(__name__)

# Load Index page 
@app.route('/')
def index():
    color_array = ["#B71C1C", # DARK RED
                   "#4A148C", # DARK PURPLE
                   "#1A237E", # DARK INDIGO
                   "#0D47A1", # DARK BLUE
                   "#006064", # DARK CYAN
                   "#009688", # TEAL
                   "#1B5E20", # DARK GREEN
                   "#FDD835", # MEDIUM YELLOW
                   "#E65100", # DARK ORANGE
                   "#3E2723", # DARK BROWN
                   "#424242", # DARK GRAY
                   "#263238"] # DARK BLUE GRAY
    color_choice = random.randrange(0, 11)
    return render_template("index.html", color=color_array[color_choice], hovercolor="white")
    
# Run Flask app on load
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')