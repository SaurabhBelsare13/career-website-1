from flask import Flask, render_template, jsonify
app = Flask (__name__)  

JOBS =[
{
  'id': 1,
  'title':'Data analyst',
  'location':'Bengluru, India',
  'salary': 'Rs 10,00,000'
},
  {
  'id': 2,
  'title':'Data scientist',
  'location':'Delhi, India',
  'salary': 'Rs 15,00,000'
},
  {
  'id': 3,
  'title':'software engineer',
  'location':'San francisco, USA',

},
  {
  'id': 4,
  'title':'frontend engineer',
  'location':'mumbai, India',
  'salary': 'Rs 10,50,000'
}
]

@app.route("/")

def hello_world():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)