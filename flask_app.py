from flask import *
from pymongo import MongoClient
#from boto.s3.connection import S3Connection
import os

app = Flask(__name__)
#s3 = S3Connection(os.eviron['MONGO_URL'])
#client = MongoClient(os.environ.get("MONGO_URL", ""))

posts = [
	{
		"title": "Hi There",
		"snippet": "This is a test post...",
		"content": "This is a test post. ertgfegrbv ipbwvipwefhfiupreb wclekfhbugielqwhfev",
		"url": "./post/0"
	},
	{
		"title": "Lorem Ipsum",
		"snippet": "Lorem ipsum dolor sit amet, consectetur...",
		"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit pulvinar rhoncus. Nam dolor arcu, cursus venenatis malesuada at, dignissim sit amet tortor. Aliquam risus dui, dictum nec tellus a, feugiat blandit risus. Etiam bibendum condimentum tortor, vel eleifend mauris iaculis vitae. Aenean molestie rhoncus tincidunt. Nunc a vulputate urna. Praesent id purus metus. Pellentesque bibendum est in venenatis mollis.",
		"url": "./post/1"
	},
	{
		"title": "Hi There",
		"snippet": "This is a test post...",
		"content": "This is a test post. ertgfegrbv ipbwvipwefhfiupreb wclekfhbugielqwhfev",
		"url": "./post/2"
	},
	{
		"title": "Lorem Ipsum",
		"snippet": "Lorem ipsum dolor sit amet, consectetur...",
		"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec suscipit pulvinar rhoncus. Nam dolor arcu, cursus venenatis malesuada at, dignissim sit amet tortor. Aliquam risus dui, dictum nec tellus a, feugiat blandit risus. Etiam bibendum condimentum tortor, vel eleifend mauris iaculis vitae. Aenean molestie rhoncus tincidunt. Nunc a vulputate urna. Praesent id purus metus. Pellentesque bibendum est in venenatis mollis.",
		"url": "./post/3"
	},
]

@app.route('/')
def get_html():
    return render_template('index.html')

@app.route('/post/<int:post_id>')
def view_post(post_id):
	post = posts[post_id]
	print(post_id)
	return render_template('post.html', post=posts[post_id])

@app.route('/posts', methods=['GET'])
def get():
	data = json.dumps({
		"posts": posts
	})
	resp = Response(data, status=200, mimetype='application/json')
	return resp

@app.route('/submit-post', methods=["GET", "POST"])
def submit_post():
	print("yay")
	posts.append({
		"title": request.form.title
		"snippet": request.form.content[:50] + '...',
		"content": request.form.content,
		"url": "./post/" + str(len(posts))
	})
	return view_post(len(posts) - 1)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(os.environ.get("PORT")))
