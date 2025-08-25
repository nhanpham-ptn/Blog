from flask import Flask, render_template
import requests
from post import Post

posts = requests.get(url = "https://api.npoint.io/c790b4d5cab58020d391").json()
post_obj = []
for post in posts:
    blog = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_obj.append(blog)



app = Flask(__name__)

@app.route('/')
def home():
    blog_1 = post_obj[0]
    blog_2 = post_obj[1]
    blog_3 = post_obj[2]
    return render_template("index.html", title_1 = blog_1.get_title() , subtitle_1 = blog_1.get_subtitle(), title_2 = blog_2.get_title(),title_3 = blog_3.get_title(), subtitle_3 = blog_3.get_subtitle())

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/post_4.html')
def posts():
    return render_template("post_4.html" )

@app.route('/contact.html')
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)
