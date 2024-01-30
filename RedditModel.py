from typing import List, Dict
from datetime import datetime, timedelta

class RedditModel:
    def __init__(self,
                 title: str, 
                 url: str,
                 flairs: str, 
                 upvotes: int, 
                 num_comments: int, 
                 created: float, 
                 text: str,
                 current_time = None) -> None:
        self.title = title
        self.url = url
        self.flairs = flairs
        self.upvotes = upvotes
        self.num_comments = num_comments
        self.created = created
        self.text = text

        if current_time == None:
            current_time = str(datetime.now())
        
        self.current_time = current_time



if __name__ == '__main__':

    x = RedditModel('test','test.com',['test'],50,20, 46546543216, "Hello World")
    print(x.__dict__)