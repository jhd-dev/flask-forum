from flask import *
from pymongo import MongoClient
import os

app = Flask(__name__)
client = MongoClient('mongodb://datauser:datapassword@ds151068.mlab.com:51068/forumdata')
db = client.forumdata
posts = db.posts

@app.route('/')
def get_html():
    return render_template('index.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
	post = posts.find_one({
		"index": post_id
	}, {"_id": False})
	return render_template('post.html', post=post)

@app.route('/posts', methods=['GET'])
def get():
	data = {
		"posts": list(posts.find({}, {"_id": False}))
	}
	print(data)
	resp = Response(data, status=200, mimetype='application/json')
	return jsonify(data)

@app.route('/submit-post', methods=["GET", "POST"])
def submit_post():
	count = posts.count()
	post_data = {
		"title": request.form["title"],
		"snippet": request.form["content"][:100] + '...',
		"content": request.form["content"],
		"index": count
	}
	posts.insert_one(post_data)
	return view_post(count)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(os.environ.get("PORT")))
	