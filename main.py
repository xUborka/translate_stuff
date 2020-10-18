# import argparse
from flask import Flask, render_template, request, redirect, url_for
from parser_class import ParserClass

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html", name="Dominika")


@app.route('/url_parser/', methods=['POST'])
def form_post():
    url = request.form['url']
    return redirect('/url_parser/' + url)


@app.route('/url_parser/<url>')
def hello_name(url):
    url_parser = ParserClass(url)
    return_string = "Hello {}!<br>".format(url)
    print(url_parser.stats)
    for i in url_parser.stats:
        return_string += str(i) + '<br>'
    return return_string


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Process webpages.')
    # parser.add_argument('--url', help='Link to webpage')
    # args = parser.parse_args()
    #
    # my_parser = ParserClass(args.url)
    app.run(host='127.0.0.1', port=8080, debug=True)
