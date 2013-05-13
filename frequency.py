import sys
import json


def lines(fp):
    return str(len(fp.readlines()))


def tweetParse(tweet_file):
    tweet = []
    terms = {}
    for t in tweet_file.readlines():
        y= json.loads(t)
        #print str(y.encode("utf-8"))
        if y.has_key("text"):
            tweet.append(str(y["text"].encode("utf-8")).replace('\n',''))

    #print str(len(ss))
    #for r in ss:
       #print  r #str(r.encode("utf-8")),"\n\t------\n"
      # for w in r.split(' '):
       #    print str(w.encode("utf-8"))
  
    return tweet
           
             
            
def Calculate_frequency(tweet):
    terms = {}
    i = 0
    for t in tweet:
        for w in t.split(' '):            
            if w not in terms.keys():
                terms[w] = float(1)
            elif w.encode('utf-8', "ignore")in terms.keys(): #.encode('utf-8', "ignore") in terms.keys():
                terms[w] = float(terms[w] + 1)
            i = i + 1

    for term in terms:
        terms[term] = float(float(terms[term])/i)  
        print "%s %.3f"%(term,terms[term])

    
def main():
    tweet_file = open(sys.argv[1])


    #tweetParse(tweet_file)
    Calculate_frequency(tweetParse(tweet_file))
    
    #lines(sent_file)
    #lines(tweet_file)
    #print str(tweet_file.readlines(1,2))
    #print tweet_file[0]["text"].split()
    
    #for (x,y) in dic:
     #   print y

if __name__ == '__main__':
    main()
