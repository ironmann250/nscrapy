# -*- coding: utf-8 -*-
#https://s3-us-west-2.amazonaws.com/jdimatteo-personal-public-readaccess/nltk-2.0.5-https-distribute.tar.gz nltk

from flask import Flask,request,current_app

app = Flask(__name__)

import re
import math

from collections import Counter

import settings

with open(settings.NLP_STOPWORDS_EN, 'r') as f:
    stopwords = set([w.strip() for w in f.readlines()])

ideal = 20.0

from newspaper import Article as article
import json,time,lsa_summly,punkt2

#punkt2.download() #enable if your host doesn't have punkt and you need to place it in memory everytime

def summarize(url,lan,len_):
        lsa_summly.LANGUAGE = lan
        lsa_summly.SENTENCES_COUNT=len_
        response=lsa_summly.summarize(url)
        return response
  

def split_words(text):
    """Split a string into array of words
    """
    try:
        text = re.sub(r'[^\w ]', '', text)  # strip special chars
        return [x.strip('.').lower() for x in text.split()]
    except TypeError:
        return None


def keywords(text):
    """Get the top 10 keywords and their frequency scores ignores blacklisted
    words in stopwords, counts the number of occurrences of each word, and
    sorts them in reverse natural order (so descending) by number of
    occurrences.
    """
    NUM_KEYWORDS = 10
    text = split_words(text)
    # of words before removing blacklist words
    if text:
        num_words = len(text)
        text = [x for x in text if x not in stopwords]
        freq = {}
        for word in text:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

        min_size = min(NUM_KEYWORDS, len(freq))
        keywords = sorted(freq.items(),
                          key=lambda x: (x[1], x[0]),
                          reverse=True)
        keywords = keywords[:min_size]
        keywords = dict((x, y) for x, y in keywords)

        for k in keywords:
            articleScore = keywords[k]*1.0 / max(num_words, 1)
            keywords[k] = articleScore * 1.5 + 1
        return dict(keywords)
    else:
        return dict()

def parse_article(url,lan='en', no_img=''): #if no images this is the image that will be shown
        if url not in ['',' ',None]: #get the url check if is valid and download ,parse , and does NLP it
                if url[:4]!='http':
                        url='http://'+url
                now=time.time()
                _article=article(url=url,language=lan)
                if True:
                        _article.download()
                        print ('download took',time.time()-now)
                        now=time.time()
                        _article.parse()
                        print ('parse took',time.time()-now)
                else:
                        return False
                if _article != False:
                        if _article.has_top_image():
                                  image_url=_article.top_image
                        else:
                                try:
                                        image_url=_article.images[0]
                                except:
                                        image_url=no_img
                        authors=_article.authors
                        title=_article.title
                        date=_article.publish_date
                        try:
                                print (title)
                        except:
                                pass
                        now=time.time()
                        summary=summarize(_article.text,'english',5)
                        keyword=keywords(_article.text)
                        print ('nlp took :',time.time()-now)
                        try:
                                date = [str(date.day),str(date.month),str(date.year)]
                                date=" ".join(date)
                        except:
                                date='UNKNOWN'
                        return {'url':url,'title':title,'summary':summary,'keywords':keyword,'authors':authors,'date':date,'image_url':image_url}


@app.route('/', methods=["GET","POST"])
def index():
	#help_msg was dimmed old and unprofessional but was done with all the love in the world ;)
	help_msg='''<html>
	<title>nscrapy</title>
	<p><h2>nscrapy -- a news scrapper packed with lots of AI --<h2></p>
	<p><h3><u>what does it do?</u></h3></p>
	<p>nscrapy scraps news articles or any text posts, it provides a summary,a front picture,title, keywords ,publish date and so on</p>
	<p>when given the url it scraps the url and on it's own find every part and give you all in a json format for whatever thing you wanna power</p>
	<p><h3><u>how does it work anyway?</u></h3></p>
	<p>
	<ul>
	<li>copy the link to your article or any text containing site with the <b>http</b> but if you leave it nscrapy will do that for you </li>
	<li>then in your browser or codes put <b>nscrapy.herokuapp.com/?url=</b> and then put the article url </li>
	<li>nscrapy also support multiple url just add <b> "," </b> without the quotes and put another article url as before <b>without /?url=</b></li>
	<li>having trouble? try <a href="/?url=http://cnn.com/2016/11/18/opinions/end-of-liberal-era-gardiner-opinion/index.html">this </a> live example</li>
	</ul>
	everything else like how it knows authors,how it gets dates and broken links and error management or summaries is all done
	by nscrapy
	</p>
	<p><h3><u>how does it return data</u></h3></p>
	<p>it outputs in a json format with each url data in its own array </p>
	<p>like this ...</p>
	<p>
	[{"keywords": {"word": frequency as float, "another word": frequency as float}, "summary": "sentence 1 \\n another sentence", "authors": ["an author name"], "url": "the url you gave", "date": "the articles date", "title": "the title", "image_url": "the cover image"]}
	</p>
	<p><h3><u>
	license:</u></h3>it is provided as is the develloper is not liable to any problem that may arise
	</p>x
	<p><h3><u>
	email:</u></h3> ironmann350@outlook.com - any problem that may arise or for anything else or just for help contact me
	</p>
	<p>
	<h3><u>
	copyright:</u></h3>done with all the love in the world at stark solutions in 2016 by a guy who beleive in the beauty of his dreams
	</p>
	</html>
	'''
	if True:
		if True:
			url = request.args.get('url')
			if url == None:
				return current_app.send_static_file('nscrapy.html')
		#url='http://cnn.com/2016/11/18/opinions/end-of-liberal-era-gardiner-opinion/index.html'
		print ('processing :',url)
		urls=url.split(',')
		base=[]
		error_titles=['Error']
		for url in urls:
			node=parse_article(url)
			if node in [False,None]:
				continue
			if node['title'] not in error_titles:
				base.append(node)
				print (' status: saved')
			else:
                                print (' status: not saved')
                        try:
                                print ('|'+'_'*(len(node['title'])+10)+'|')
                        except:
                                pass
                return json.dumps(base)
if __name__ == "__main__":
	print ('running')
	app.run()
