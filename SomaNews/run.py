# Have installed pip flask

from flask import Flask, render_template
from newsapi import NewsApiClient #Import the API and import it here.
app = Flask(__name__)


#Creating a route function @approute and rendering the html template.
@app.route("/")
def home():

    newsapi = NewsApiClient(api_key="44216e90102b4e7bbc548343f8cdc3ea")

#Code-block for getting the top stories from the API
    top_headlines = newsapi.get_top_headlines(sources = "bbc-news") #source to help us from where to get the news by API.

#code-block to fetch headlines
    t_articles = top_headlines['articles']


#We make a list of the items to display on our application
    news = []
    desc = []
    img = []
    p_date = []
    url = []

#Code block using a for-loop to fetch the contents of articles.
    for i in range(len(t_articles)): 
        main_article = t_articles[i]

        news.append(main_article['title'])  #To append the title into the list.
        desc.append(main_article['description'])  #To append the description into the list.
        img.append(main_article['urlToImage'])  #Append the urlToImage into the list.
        p_date.append(main_article['publishedAt'])  #Append the published date into the list.
        url.append(main_article['url'])  #Append the url into the list.

#To store the contents gotten above.
        contents = zip(news, desc,img,p_date,url)

#To get all articles:
    all_articles = newsapi.get_everything(sources = "bbc-news")
#code-block to fetch all articles
    a_articles = all_articles['articles']
#We make a list of the items to display on our application
    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []   
    url_all = []

    for j in range(len(a_articles)): 
        a_article = a_articles[j]   

        news_all.append(a_article['title'])
        desc_all.append(a_article['description'])
        img_all.append(a_article['urlToImage'])
        p_date_all.append(a_article['publishedAt'])
        url_all.append(a_article['url'])
        
        all = zip( news_all,desc_all,img_all,p_date_all,url_all)
#To store all the articles gotten above.
        all = zip(news_all, desc_all,img_all,p_date_all,url_all)


#Passing in the contents variable into the file we are rendering.

    return render_template('home.html', contents=contents, all=all)




#Creating a route function @approute and rendering the html template.
@app.route("/cnn")
def cnn():

    newsapi = NewsApiClient(api_key="44216e90102b4e7bbc548343f8cdc3ea")

#Code-block for getting the top stories from the API
    ctop_headlines = newsapi.get_top_headlines(sources = "cnn") #source to help us from where to get the news by API.

#code-block to fetch headlines
    c_articles = ctop_headlines['articles']


#We make a list of the items to display on our application
    cnews = []
    cdesc = []
    cimg = []
    cp_date = []
    curl = []

#Code block using a for-loop to fetch the contents of articles.
    for i in range(len(c_articles)): 
        cmain_article = c_articles[i]

        cnews.append(cmain_article['title'])  #To append the title into the list.
        cdesc.append(cmain_article['description'])  #To append the description into the list.
        cimg.append(cmain_article['urlToImage'])  #Append the urlToImage into the list.
        cp_date.append(cmain_article['publishedAt'])  #Append the published date into the list.
        curl.append(cmain_article['url'])  #Append the url into the list.

#To store the contents gotten above.
        cnn_contents = zip(cnews, cdesc,cimg,cp_date,curl)
        return render_template('cnn.html', cnn_contents=cnn_contents)




if __name__ == '__main__':
    app.run(debug=True)

