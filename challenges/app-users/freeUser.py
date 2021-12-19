from post import Post


class Free_User:
    def __init__(self, name, email_address, password):
        super().__init__(name, email_address, password)
        self.posts = 0

    def new_post(self, author, title, text):
        if self.posts < 2:
            self.posts += 1
            post = Post(author, title, text)
            self.posts[title] = post
            self.write_to_posts(post)
