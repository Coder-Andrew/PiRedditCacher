import json
from RedditModel import RedditModel
from os.path import exists

class JsonFileStore:
    def __init__(self, filename = 'cache.json'):
        self.filename = filename
        self.objects = []
        self.read()

    def read(self):
        if exists(self.filename):           
            with open(self.filename, 'r') as f:
                file_contents = f.read()
                if file_contents:
                    self.objects = [RedditModel(**item) for item in json.loads(file_contents)]
                else:
                    self.objects = []
                return self.objects
        else:
            with open(self.filename, "w"):
                pass
            
    def write(self, json_obj: RedditModel):
        if isinstance(json_obj, list):
            self.objects += json_obj
        else:
            self.objects.append(json_obj)

        with open(self.filename, "w") as f:
            f.write(json.dumps([item.__dict__ for item in self.objects], indent=4))

    def return_clear(self):
        data = self.objects
        self.objects = []
        
        with open(self.filename, 'w') as f:
            f.write(json.dumps([], indent=4))
        
        return data
    
    def __len__(self):
        return len(self.objects)


if __name__ == '__main__':
    js = JsonFileStore('test2.json')

    js.write({'test': 4229})
    #print(js.objects)

    #print(js.return_clear())

