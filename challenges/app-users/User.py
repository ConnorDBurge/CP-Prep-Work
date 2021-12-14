import csv
import os
from post import Post
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "user.csv")
post_path = os.path.join(my_path, "posts.csv")


class User:
    users = {}

    def __init__(self, name, email_address, password):
        self.name = name
        self.email_address = email_address
        self.password = password
        self.posts = {}

    def __str__(self):
        return f'{self.name}: {self.posts}'

    def new_post(self, author, title, text):
        post = Post(author, title, text)
        self.posts[title] = post
        self.write_to_posts(post)

    def write_to_posts(self, post):
        fields = ['author', 'title', 'text']
        with open(post_path, 'a+', newline='') as file:
            writer = csv.DictWriter(file, fields)
            writer.writerow(post.__dict__)

    def delete_post(self, title):
        return self.posts.pop(title)

    @classmethod
    def get_user(cls, email):
        return User.users[email]

    @classmethod
    def load_all_users(cls):
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cls.users[row['email_address']] = User(**row)

    @classmethod
    def load_all_post(cls):
        with open(post_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                user = cls.users[row['author']]
                user.posts[row['title']] = Post(**row)


User.load_all_users()
User.load_all_post()
# for user in User.users:
#     print(user)
kyndall = User.get_user('kyndall.burge@gmail.com')
print(kyndall)
# kyndall.new_post(kyndall.email_address, 'Post 3', 'HEJFNJENK')
# print(kyndall)
