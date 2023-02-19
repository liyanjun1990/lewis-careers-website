from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Brisbane',
    'salary':'$70,000'
  },
  {
    'id':2,
    'title': 'Data Scientist',
    'location': 'Brisbane, Queensland',
    'salary':'$80,000'
  },
  {
    'id':3,
    'title': 'Fronted Engineer',
    'location': 'Remote'
  },
  {
    'id':4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary':'$200,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Lewis')

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)

