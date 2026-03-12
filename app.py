from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")

def home():

    df = pd.read_csv("data/map_ready_data.csv")

    total = len(df)

    locations = df.dropna(
        subset=["lat","lon"]
    ).to_dict(orient="records")

    return render_template(
        "index.html",
        total=total,
        locations=locations
    )

if __name__ == "__main__":

    app.run(debug=True)