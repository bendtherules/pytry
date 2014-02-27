from flask import Flask
from flask import *
from urllib2 import unquote,quote
import redis

app=Flask(__name__)

global list_shortened_links
list_shortened_links=[]

db=redis.Redis()
db.client_setname("Url_shortener")
db_list_name= "shortened_links"

@app.route("/")
def show_form():
    return render_template("form.html")

@app.route("/submit")
def make_shortened_url():
    dict_args=request.args.to_dict()
    if dict_args.has_key("url"):
        link_to_commit=unquote(dict_args["url"])
        #list_shortened_links.append(link_to_commit)

        db.rpush(db_list_name,link_to_commit)
        #len_list=len(list_shortened_links)
        len_list=db.llen(db_list_name)
        return render_template("submit.html",short_code=str(len_list))
    else:
        return redirect(r"./")

@app.route("/view/<short_code>")
def show_shortened_url(short_code):
    short_code=int(short_code)
    #len_list=len(list_shortened_links)

    len_list=db.llen(db_list_name)

    if len_list>=short_code:
        #return_url= list_shortened_links[short_code-1]
        return_url=db.lindex(db_list_name,short_code-1)
        return render_template("view.html",return_url=return_url)
    else:
        return "Invalid short url"

app.run()
