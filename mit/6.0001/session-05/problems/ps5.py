# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
import re
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz

import urllib3
import certifi

#-----------------------------------------------------------------------

http = urllib3.PoolManager(
    cert_reqs = 'CERT_REQUIRED',
    ca_certs = certifi.where()
)

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

# Ran into SSL issues, hence urllib3 and modifications

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """

    res = http.request('GET', url)

    #feed = feedparser.parse(url)

    feed = feedparser.parse(res.data)

    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2

class PhraseTrigger(Trigger):
    punctuation_reg_ex = r"[" + re.escape(string.punctuation) + "]"

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.phrase_reg_ex = r"^.*\b" + self.phrase + r"\b.*$"

    def has_phrase(self, text):
        cleaned_text = re.sub(
            r"\s+",
            ' ',
            re.sub(self.punctuation_reg_ex, ' ', text.lower())
        )

        test = re.match(self.phrase_reg_ex, cleaned_text)
        
        if test == None:
            return False
        else:
            return True


# Problem 3

class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        return self.has_phrase(story.get_title())


# Problem 4

class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        return self.has_phrase(story.get_description())


# TIME TRIGGERS

# Problem 5
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, time):
        self.time = datetime \
            .strptime(time, '%d %b %Y %H:%M:%S') \
            .replace(tzinfo = pytz.timezone('EST'))


# Problem 6

class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)

    def evaluate(self, story):
        return self.is_before(story.get_pubdate())

    def is_before(self, pubdate):
        pubdate = pubdate.replace(tzinfo = pytz.timezone('EST'))
        return pubdate < self.time
        

class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        TimeTrigger.__init__(self, time)

    def evaluate(self, story):
        return self.is_after(story.get_pubdate())

    def is_after(self, pubdate):
        pubdate = pubdate.replace(tzinfo = pytz.timezone('EST'))
        return pubdate > self.time


# COMPOSITE TRIGGERS

# Problem 7

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)


# Problem 8

class AndTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)


# Problem 9

class OrTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def evaluate(self, story):
        return self.t1.evaluate(story) or self.t2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """

    results = []

    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                results.append(story)

    return results



#======================
# User-Specified Triggers
#======================

# Problem 11

def handle_trigger_command(triggers, trigger_list, trigger_config):
    split_config = trigger_config.split(',')
    print(split_config)
    trigger_name = split_config[0]
    trigger_type = split_config[1]
    trigger_arg = split_config[2]
    trigger = None

    if trigger_name == 'ADD':
        for t in split_config[1:]:
            trigger_list.append(triggers[t])

        return

    if trigger_type == 'TITLE':
        trigger = TitleTrigger(trigger_arg)
    elif trigger_type == 'DESCRIPTION':
        trigger = DescriptionTrigger(trigger_arg)
    elif trigger_type == 'AFTER':
        trigger = AfterTrigger(trigger_arg)
    elif trigger_type == 'BEFORE':
        trigger = BeforeTrigger(trigger_arg)
    elif trigger_type == 'AND':
        trigger = AndTrigger(
            triggers[trigger_arg], 
            triggers[split_config[3]] 
        )
    elif trigger_type == 'OR':
        trigger = OrTrigger(
           triggers[trigger_arg], 
           triggers[split_config[3]] 
        )
    else:
        trigger = NotTrigger(triggers[trigger_arg])

    triggers[trigger_name] = trigger


def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    triggers = {}
    trigger_list = []

    for l in lines:
        handle_trigger_command(triggers, trigger_list, l)

    return trigger_list


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list
    # you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("softbank")
        t2 = DescriptionTrigger("iphone")
        t3 = DescriptionTrigger("ipad")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []

        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, '\n')
                cont.insert(END, 'LINK: ' + newstory.get_link())
                cont.insert(END, '\n')
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            #stories = process("http://news.google.com/news?output=rss")

            # Google Tech
            stories = process("https://news.google.com/news/rss/headlines/section/topic/TECHNOLOGY?ned=us&hl=en&gl=US")

            # Google Business
            stories.extend(process("https://news.google.com/news/rss/headlines/section/topic/BUSINESS?ned=us&hl=en&gl=US"))

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

