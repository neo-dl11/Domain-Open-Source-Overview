from flask import Flask, render_template, request, redirect, url_for

from subdomains import get_subdomains
app = Flask(__name__)

from domain_tools import get_website_info, normalize_domain, get_socialmedia_infos

@app.route('/')
def index():
    domain = request.args.get('domain', 'example.com')
    normalized_domain = normalize_domain(domain)
    website_info = get_website_info(normalized_domain)
    social_media_info = get_socialmedia_infos(normalized_domain)
    if website_info:
        return render_template('index.html', website_info=website_info, social_media_info=social_media_info)
    else:
        return "Error fetching website information"

@app.route('/subdomains/<domain>')
def subdomains_list(domain):
    normalized_domain = normalize_domain(domain)
    return redirect(url_for('subdomains_list_normalized', normalized_domain=normalized_domain))

@app.route('/subdomains/list/<normalized_domain>')
def subdomains_list_normalized(normalized_domain):
    subdomains = get_subdomains(normalized_domain)
    if subdomains:
        return render_template('subdomains.html', subdomains=subdomains)
    else:
        return "Error fetching website information"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
