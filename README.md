# Domain Open Source Overview

The goal of the project is to create a tool capable of quickly recovering all the
information linked to a domain name from opensource content, then display them in
a more readable format.

## List of information to retrieve

* infos from the Whois
* SSL informations
* Informations retrieved from the site
* DNS records information(s)
* subdomains list
* if the domain was reported in a phishing list 
* some posts retrieved from social networks containing the domain name

PS : some features require API keys, so you will need to replace the contents of the variables with your own keys
(phishing > go on google safe browsing, social media content > reddit)


## How to start application

* you can find all the necessary libs to install in the requirements.txt file
* then you can run : ``` python3 -m flask run  ```

* after that you can access the page with your localhost adress

