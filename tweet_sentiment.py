import sys
import json


def lines(fp):
    return str(len(fp.readlines()))


def tweetParse(tweet_file):
    ss = []
    for t in tweet_file.readlines():
        y= json.loads(t)
        #print str(y.encode("utf-8"))
        if y.has_key("text"):
            ss.append(str(y["text"].encode("utf-8")))

    #print str(len(ss))
    #for r in ss:
       #print  r #str(r.encode("utf-8")),"\n\t------\n"
      # for w in r.split(' '):
       #    print str(w.encode("utf-8"))
    return ss
           

def Calculate(tweet,dic):
    for t in tweet:
        val = 0.0
        for w in t.split(' '):
            if w not in dic.keys():
                val = val +float(dic[w])
        print float(val)
                
            
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    dic = {}
    for d in sent_file.readlines():
        word, score = d.split("\t")
        #dic.append((y[0], y[1]))
        dic[word] = float(score)

    #tweetParse(tweet_file)
    Calculate(tweetParse(tweet_file),dic)
    
    #lines(sent_file)
    #lines(tweet_file)
    #print str(tweet_file.readlines(1,2))
    #print tweet_file[0]["text"].split()
    
    #for (x,y) in dic:
     #   print y

if __name__ == '__main__':
    main()
