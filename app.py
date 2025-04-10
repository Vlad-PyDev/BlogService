from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
app = Flask(__name__)

posts = []
post_id = 1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    global post_id
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        posts.append({'id': post_id, 'title': title, 'content': content, 'timestamp': timestamp})
        post_id += 1
    return render_template('main.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)