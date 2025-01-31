from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the CSV data into a Pandas DataFrame
df = pd.read_csv("student_data.csv")

@app.route("/mrec", methods=["GET", "POST"])
def index():
    student_details = None
    if request.method == "POST":
        student_id = request.form.get("student_id")
        if student_id and student_id.isdigit():
            # Find the student details by StudentID
            student_details = df[df["StudentID"] == int(student_id)].to_dict(orient="records")
            if not student_details:
                student_details = "Student ID not found."
        else:
             student_details = "Invalid Student ID."
    
    return render_template("index.html", student_details=student_details)

@app.route("/blog")
def home():
    return render_template("blog.html",name="Balaji", popular_posts=['gucci','voi','puma'])

if __name__ == "__main__":
    app.run(debug=True)
