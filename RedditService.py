import requests
from RedditModel import RedditModel
import json
import datetime

class RedditService:
    @staticmethod
    def get_reddit_posts(url = "https://reddit.com/r/python/top/.json?t=", time = "day", num_results = None):
        url += time

        if num_results:
            url += f"&limit={num_results}"

        headers = {"User-Agent":"MyApp/0.0.1"}

        response = requests.get(url, headers=headers)

        if not response.ok:
            raise ValueError(response.content)

        data = response.json()

        root = data['data']['children']

        resp_list = []
        for parent in root:
            child = parent['data']
            obj = RedditModel(
                title =   child['title']
                , url =   child['url']
                , flairs = [flair['t'] for flair in child['link_flair_richtext'] if flair.get('t')][0]
                , upvotes = child['ups']
                , num_comments = child['num_comments']
                , created = str(datetime.timedelta(hours=-8) + datetime.datetime.utcfromtimestamp(float(child['created'])))
                , text =  child['selftext']
            )

            resp_list.append(obj)
            
        return resp_list
    
if __name__ == '__main__':
    rs = RedditService()
    print(rs.get_reddit_posts())