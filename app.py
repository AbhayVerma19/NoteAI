# from flask import Flask, render_template, request, url_for
# from scraper import scraper
# from wiki_summarizer import summarizer, estimated_reading_time

# app = Flask(__name__)
# app.config["JSON_AS_ASCII"] = False

# @app.route("/", methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         url = request.form.get('url')

#         try:
#             article_title, text = scraper(url)
#             summary = summarizer(text)
#             reading_time = estimated_reading_time(summary.split())
#             return render_template("index.html", article_title = article_title, reading_time = reading_time, summary = summary)
        
#         except TypeError:
#             print('Invalid url entered')

#     else: 
#         return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug = True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/youtube_summarizer")
# def youtube_summarizer():
#     return render_template("youtube_summarizer.html")

# @app.route("/youtube_qna")
# def youtube_qna():
#     return render_template("youtube_qna.html")

# @app.route("/wiki_tools")
# def wiki_tools():
#     return render_template("wiki_tools.html")

if __name__ == "__main__":
    app.run(debug=True)
