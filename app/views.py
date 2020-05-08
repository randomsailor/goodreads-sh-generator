from app import app
from app.tasks import get_book_details

from flask import render_template, request

@app.route("/")
def index():
    return "hello world"

@app.route("/add-task", methods=["GET", "POST"])
def add_task():

    print(request.method)
    message = 'nothing'
    book_details = None
    
    # if request.args:
#         url = request.args.get("url")
#         if url.startswith("https://www.goodreads.com/book/show/"):

#             book_details = get_book_details(url)
# # todo add a full format (like book code, same link etc, so only those get accepted)
#             message = f"Got url {url}"
#         else:
#             message = f"Invalid URL, needs to be like 'https://www.goodreads.com/book/show/'"


    if  request.args:
    # if request.args:
        message ='get'
        # print(request.form)
        # if request.form['submit'] == 'submit':
    
        selected_items = request.args.getlist('item')
        selected_locations = request.args.getlist('location')
        selected_actions = request.args.getlist('action')
        selected_covers = request.args.getlist('cover')
        selected_themes = request.args.getlist('theme')


        # any_selected = bool(selected)
        print(selected_items)
        
        # message = request.form.getlist('item')
    # else:
    #     message = f"Invalid URL, needs to be like 'https://www.goodreads.com/book/show/'"

    return render_template("add_task.html", message=message, book_details=book_details)