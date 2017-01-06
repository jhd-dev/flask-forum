from flask import *
from pymongo import MongoClient
import os

app = Flask(__name__)
client = MongoClient(os.environ.get("MONGO_URL"))
db = client.forumdata
posts = db.posts

def toArray(cursor):
	'''returns the documents from a cursor object as an array'''
	arr = []
	for doc in cursor:
		arr.append(doc)
	return arr

@app.route('/')
def get_html():
    return render_template('index.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
	post = posts.find_one({
		"_id": post_id
	})
	return render_template('post.html', post=post)

@app.route('/posts', methods=['GET'])
def get():
	data = json.dumps({
		"posts": toArray(posts.find())
	})
	resp = Response(data, status=200, mimetype='application/json')
	return resp

@app.route('/submit-post', methods=["GET", "POST"])
def submit_post():
	post_data = {
		"title": request.form["title"],
		"snippet": request.form["content"][:100] + '...',
		"content": request.form["content"]
	}
	post_id = posts.insert_one(post_data).inserted_id
	return view_post(post_id)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(os.environ.get("PORT")))
