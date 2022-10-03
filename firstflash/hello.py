from flask import Flask,url_for,request,render_template,abort, redirect
from markupsafe import escape


app = Flask(__name__)









@app.route("/")
def index():
    return "<p>Hello, 管延雪!</p>"




@app.route('/hello',methods=['GET', 'POST'])
@app.route('/hello/<name>')
def hello(name=None):
   print(request.method)
   #return 'hello,吉林师范大学'
   return render_template('hello.html',name=name)

@app.errorhandler(404)
def index(error):
    return render_template('404.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return f'用户:{username}'  

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'POST:{post_id}'   

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}' 

with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('show_user_profile',username='吉林四平'))

if __name__ == '__main__':
       app.run()