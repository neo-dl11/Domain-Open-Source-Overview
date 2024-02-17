from flask import Flask, render_template, request
app = Flask(__name__)

from info import get_website_info  

@app.route('/')
def index():
    domain = request.args.get('domain', 'example.com')
    website_info = get_website_info(domain)
    if website_info:
        return render_template('index.html', website_info=website_info)
    else:
        return "Error fetching website information"

if __name__ == '__main__':
    app.run(debug=True)
