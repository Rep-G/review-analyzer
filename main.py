import requests
from bs4 import BeautifulSoup
debug = False
debugUrl = "https://www.imdb.com/title/tt11563598/reviews/?ref_=ttrt_sa_3"

def getSentiment(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find_all('div', class_='ipc-html-content-inner-div', role='presentation')
    
    posWords = {
        'great', 'good', 'happy', 'loved', 'amazing', 'perfect', 'awesome', 'wonderful', 'fantastic', 'incredible',
        'excellent', 'outstanding', 'superb', 'best', 'delightful', 'marvelous', 'enjoyable', 'positive', 'brilliant',
        'joyful', 'pleasing', 'uplifting', 'inspiring', 'charming', 'fabulous', 'heartwarming', 'admired', 'adored',
        'exciting', 'memorable', 'affectionate', 'lovable', 'praise', 'respect', 'commendable', 'treasured', 'satisfied',
        'supportive', 'caring', 'elevating', 'thrilled', 'ecstatic', 'elated', 'serene', 'peaceful', 'grateful', 'fortunate',
        'pleasant', 'joyous', 'breathtaking', 'blessed', 'harmonious', 'radiant', 'content', 'full-of-life', 'exuberant',
        'reassured', 'safe', 'admiring', 'chill', 'adoring'
    }

    negWords = {
        'embarassing', 'trash', 'horrible', 'bad', 'terrible', 'awful', 'dreadful', 'disappointing', 'horrendous',
        'atrocious', 'lousy', 'horrific', 'poor', 'pathetic', 'disgusting', 'repulsive', 'gross', 'unpleasant', 'unacceptable',
        'disastrous', 'unwanted', 'unsatisfactory', 'deplorable', 'vile', 'nasty', 'ugly', 'intolerable', 'unbearable',
        'wretched', 'sickening', 'frustrating', 'devastating', 'cringe', 'annoying', 'displeasing', 'grating', 'shameful',
        'nauseating', 'unfortunate', 'distasteful', 'discomforting', 'disturbing', 'unsettling', 'depressing', 'miserable',
        'offensive', 'repugnant', 'tragic', 'heartbreaking', 'pathetic', 'regrettable', 'unfortunate', 'painful', 'dismal',
        'dismaying', 'damaging', 'ugliness', 'low', 'sorrowful', 'toxic', 'unhealthy', 'off-putting', 'insulting', 'unfriendly',
        'inferior', 'cold', 'unwanted', 'boring', 'hopeless', 'exhausting', 'confusing', 'sucked', 'worse'
    }

    
    posCount = 0
    negCount = 0
    neutralCount = 0
    
    for div in divs:
        review = div.get_text().lower()
        reviewWords = set(review.split())

        posReviewWords = reviewWords.intersection(posWords)
        negReviewWords = reviewWords.intersection(negWords)


        if (len(negReviewWords) == 0):
            posCount += 1
        elif (0.5 <= len(posReviewWords) / len(negReviewWords) >= 1):
            neutralCount += 1
        elif (0 <= len(posReviewWords) / len(negReviewWords) > 0.5):
            negCount += 1
        else:
            posCount += 1
    if posCount > negCount and posCount > neutralCount:
        return "Overall Sentiment: Positive"
    elif negCount > posCount and negCount > neutralCount:
        return "Overall Sentiment: Negative"
    elif neutralCount >= posCount and neutralCount >= negCount:
        return "Overall Sentiment: Neutral"
    else:
        return "Overall Sentiment: Positive"
def main():
    if (debug):
        print(getSentiment(debugUrl))
    else:
        print(getSentiment(input("URL: ")))

if __name__ == "__main__":
    main()