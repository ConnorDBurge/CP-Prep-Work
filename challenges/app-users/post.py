class Post:
    def __init__(self, author, title, text):
        self.author = author
        self.title = title
        self.text = text

    def __str__(self):
        return f'{self.text}'
