
class Post():
    def __init__(self, id, title, subtitle, body):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body

    def get_id(self):
        return self.id
    def get_title(self):
        return self.title
    def get_subtitle(self):
        return self.subtitle
    def get_body(self):
        return self.body
    
