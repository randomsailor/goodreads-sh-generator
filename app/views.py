from app import app
from app.tasks import get_book_details, get_points, make_list

from flask import render_template, request

@app.route("/")
def index():
    return "hello world"

@app.route("/add-task", methods=["GET", "POST"])
def add_task():

    print(request.method)
    message = None
    book_details = dict()
    item_list = list()
    location_list = list()
    action_list = list()
    cover_list = list()
    themes_list = list()
    misc_list = list()


    if  request.args:
        url = request.args.get("url")
        if url.startswith("https://www.goodreads.com/book/show/"):
            book_details = get_book_details(url)
            message = f"Got url {url}"
        # else:
        #     message = f"Invalid URL, needs to be like 'https://www.goodreads.com/book/show/'"
        
        selected_items = request.args.getlist('item')
        book_details['item_points'] = get_points(selected_items)
        item_list = make_list(selected_items)

        selected_locations = request.args.getlist('location')
        book_details['location_points'] = get_points(selected_locations)
        location_list = make_list(selected_locations)

        selected_actions = request.args.getlist('action')
        book_details['action_points'] = get_points(selected_actions)
        action_list = make_list(selected_actions)

        selected_covers = request.args.getlist('cover')
        book_details['cover_points'] = get_points(selected_covers)
        cover_list = make_list(selected_covers)

        selected_themes = request.args.getlist('theme')
        book_details['theme_points'] = get_points(selected_themes)
        themes_list = make_list(selected_themes)


        selected_misc = request.args.getlist('misc')
        book_details['misc_points'] += get_points(selected_misc)
        misc_list = make_list(selected_misc)
        
        # message = request.form.getlist('item')
    # else:
    #     message = f"Invalid URL, needs to be like 'https://www.goodreads.com/book/show/'"

        book_details['total_points'] = book_details['item_points'] + book_details['location_points'] + \
            book_details['action_points'] + book_details['cover_points'] + book_details['theme_points'] + book_details['misc_points'] 

        return render_template("add_task.html", message=message, book_details=book_details, item_list=item_list,
        location_list=location_list, action_list=action_list, cover_list=cover_list, themes_list=themes_list)
    return render_template("add_task.html", message=message, book_details=None)