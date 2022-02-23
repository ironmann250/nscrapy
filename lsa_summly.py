#from __future__ import absolute_import
#from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer as Summarizer1
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 5


def summarize(url):
    global LANGUAGE
    global SENTENCES_COUNT
    #"http://cnn.com/2016/11/18/opinions/end-of-liberal-era-gardiner-opinion/index.html"
    #parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    parser = PlaintextParser.from_string(url, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    summary=''
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        tmp=str(sentence)
        summary=tmp+'\n'+summary
    return summary       
