from app import app
from app.tasks import get_book_details
from app.tasks import get_points

from flask import render_template, request

@app.route("/")
def index():
    return "hello world"

@app.route("/add-task", methods=["GET", "POST"])
def add_task():

    print(request.method)
    message = None
    book_details = dict()

    if  request.args:
        url = request.args.get("url")
        if url.startswith("https://www.goodreads.com/book/show/"):
            book_details = get_book_details(url)
            message = f"Got url {url}"
        # else:
        #     message = f"Invalid URL, needs to be like 'https://www.goodreads.com/book/show/'"
        
        selected_items = request.args.getlist('item')
        selected_locations = request.args.getlist('location')
        selected_actions = request.args.getlist('action')
        selected_covers = request.args.getlist('cover')
        selected_themes = request.args.getlist('theme')
        selected_misc = request.args.getlist('misc')

        book_details['item_points'] = get_points(selected_items)
        book_details['location_points'] = get_points(selected_locations)
        book_details['action_points'] = get_points(selected_actions)
        book_details['cover_points'] = get_points(selected_covers)
        book_details['theme_points'] = get_points(selected_themes)
        
        # message = request.form.getlist('item')
    # else:
    #     message = f"Invalid URL, needs to be like 'https://www.goodreads.com/book/show/'"

        return render_template("add_task.html", message=message, book_details=book_details)
    return render_template("add_task.html", message=message, book_details=None)