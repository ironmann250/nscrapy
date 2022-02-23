
# Nscrapy API  
a news scrapper packed with lots of AI features
-------------------------------------------------------------

### The Purpose

Nscrapy scraps news articles or any text posts and provides a summary,a front picture, a title, keywords, published date and so on

when it gets any url, it scraps it and find every part. It provides the results in json format. So, you can utilize it as means to any end of your purpose

### How to use it

*   Copy any link of an article or any text-containing site with an "**http**".
*   Then in yourbrowser or codes put "**nscrapy.herokuapp.com/?url=**" and paste the article's url.
*   Nscrapy also support multiple urls. To do it just add **","** without the quotes and put another article url as before **without /?url=**.
*   Having trouble? try [this](http://nscrapy.herokuapp.com/?url=http://cnn.com/2016/11/18/opinions/end-of-liberal-era-gardiner-opinion/index.html) (a live example)

Everything else such as to know authors, dates, broken links and error management or summaries are managed by Nscrapy

### The output

It outputs in a json format with each url data in its own array

Like this ...

\[{"keywords": {"word": frequency as float, "another word": frequency as float}, "summary": "sentence 1 \\n another sentence", "authors": \["an author name"\], "url": "the url you gave", "date": "the articles date", "title": "the title", "image\_url": "the cover image"\]}

### license

Opensource

### Contact the developers

email: Billy Byiringiro : byiringirobill@gmail.com  
email: Munyakabera jean claude (Stark): ironmann350@outlook.com

copyright:2017 Alright Reserved.
