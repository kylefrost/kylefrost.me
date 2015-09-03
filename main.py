from flask import Flask, render_template
import random, datetime

app = Flask(__name__)

# Load Index Page 
@app.route('/')
def index():
    color_array = ["#B71C1C", # DARK RED
                   #"#4A148C", # DARK PURPLE
                   #"#1A237E", # DARK INDIGO
                   #"#0D47A1", # DARK BLUE
                   "#006064", # DARK CYAN
                   "#009688", # TEAL
                   #"#1B5E20", # DARK GREEN
                   #"#FDD835", # MEDIUM YELLOW
                   #"#E65100", # DARK ORANGE
                   #"#3E2723", # DARK BROWN
                   "#424242", # DARK GRAY
                   "#263238"] # DARK BLUE GRAY
    color_choice = random.randrange(0, len(color_array) - 1)
    return render_template("index.html", color=color_array[color_choice], hovercolor="white", year=datetime.datetime.now().year)
    
# Load Search Page
@app.route('/search')
def search():
    return render_template("search.html")
    
# Run Flask app on load
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')