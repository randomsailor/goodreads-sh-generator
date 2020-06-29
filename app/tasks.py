from urllib import request
from bs4 import BeautifulSoup
import lxml
import ssl

# https://realpython.com/flask-by-example-part-3-text-processing-with-requests-beautifulsoup-nltk/

def get_book_details(book_url):
    # todo: remove this when pushed as a test
    ssl._create_default_https_context = ssl._create_unverified_context
    r = request.urlopen(book_url)   
    soup = BeautifulSoup(r.read().decode(), 'lxml')

    book_details = dict()
    temp = soup.find('h1', {'id':'bookTitle'}).contents
    book_details['title'] = temp[0].strip()
    book_details['title_id'] = soup.find('input', {'id':'book_id'})['value']
    # book_details['author'] = soup.find('meta', {'property':'books:author'})['content'].split('/show/')[1]
    author_details = soup.find('meta', {'property':'books:author'})['content'].split('/show/')[1]
    book_details['author_id'] = author_details.split('.')[0]
    book_details['author_name'] = author_details.split('.')[1].replace('_', ' ')

    book_details['pages'] = soup.find('meta', {'property':'books:page_count'})['content']
    if int(book_details['pages']) >= 400:
        book_details['pages_points'] = "5 points"
        book_details['misc_points'] = 5
    elif int(book_details['pages']) >= 300:
        book_details['pages_points'] = "4 points"   
        book_details['misc_points'] = 4
    elif int(book_details['pages']) >= 200:
        book_details['pages_points'] = "3 points"
        book_details['misc_points'] = 3
    elif int(book_details['pages']) >= 100:
        book_details['pages_points'] = "2 points"
        book_details['misc_points'] = 2
    elif int(book_details['pages']) >= 1:
        book_details['pages_points'] = "1 point"
        book_details['misc_points'] = 1
    else:
        book_details['pages_points'] = "??? point"
        book_details['misc_points'] = 0


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
        points += int(i.split(':')[0].split('-')[1])
    return points


def make_list(selected_content):
    final_list = list()
    for i in selected_content:
        point = i.split(':')[0].split('-')[1]
        value = i.split(':')[1]
        point_word = "points" if point != '1' else "point"

        final_list.append(f'{value}: {point} {point_word}')
    return final_list
