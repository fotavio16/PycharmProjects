# Run with args: --page GoldenSongs (ou nome da page)

import json
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from wordcloud import WordCloud

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--page', default='GoldenSongs')
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    fname = "posts_{}.jsonl".format(args.page)

    all_posts = []

    with open(fname) as f:
        for line in f:
            post = json.loads(line)
            all_posts.append(post.get('message', ''))
    text = ' '.join(all_posts)
    stop_list = ['save', 'free', 'today', 'get', 'title', 'titles', 'bit', 'ly']
    stop_list.extend(stopwords.words('english'))
    wordcloud = WordCloud(stopwords=stop_list).generate(text)
    plt.imshow(wordcloud)
    plt.axis("off")
    image_fname = 'wordcloud_{}.png'.format(args.page)
    plt.savefig(image_fname)