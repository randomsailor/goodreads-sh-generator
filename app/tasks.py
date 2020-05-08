from urllib import request
from bs4 import BeautifulSoup
import lxml


# https://realpython.com/flask-by-example-part-3-text-processing-with-requests-beautifulsoup-nltk/

def get_book_details(book_url):
    r = request.urlopen(book_url)
    soup = BeautifulSoup(r.read().decode(), 'lxml')

    book_details = dict()
    book_details['title'] = soup.find('meta', {'property':'og:title'})['content']
    # book_details['author'] = soup.find('meta', {'property':'books:author'})['content'].split('/show/')[1]
    book_details['pages'] = soup.find('meta', {'property':'books:page_count'})['content']
    author_details = soup.find('meta', {'property':'books:author'})['content'].split('/show/')[1]
    book_details['author_id'] = author_details.split('.')[0]
    book_details['author_name'] = author_details.split('.')[1].replace('_', ' ')

    return book_details

    # # https://www.goodreads.com/book/show/51172162-hideaway

    # [book:Hideaway|51172162] [author:Nora Roberts|625]
    # [bookcover:Hideaway|51172162]

    # todo: check if type changes for say anthology or whatever
    # <meta content='books.book' property='og:type'>
    # <meta content='Hideaway' property='og:title'>
    # <meta content='https://www.goodreads.com/author/show/625.Nora_Roberts' property='books:author'>
    # <meta content='9781250207104' property='books:isbn'>
    # <meta content='464' property='books:page_count'>


def get_points(selected_content):
    points = 0
    for i in selected_content:
        points += int(i.split('-')[1])
    return points