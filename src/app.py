from flask import Flask, render_template, abort

app = Flask(__name__)

# Blog posts
posts = [
    {
        "id": 1,
        "title": "Welcome to My Blog",
        "content": "This is the first post on my Flask blog!"
    },
    {
        "id": 2,
        "title": "Dockerized Flask Apps",
        "content": "Nothing to see here for now, I'm just learning how to deploy Flask apps with Bash scripts, Docker and Nginx.  Thanks for coming by!"
    },
    {
        "id": 3,
        "title": "Automation Scripts",
        "content": "Automate your deployments using Bash scripts!"
    }
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post_item = next((p for p in posts if p["id"] == post_id), None)
    if post_item:
        return render_template("post.html", post=post_item)
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
