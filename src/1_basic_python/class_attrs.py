from datetime import datetime


class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs["created_at"] = datetime.now()
        return super().__new__(cls, name, bases, attrs)


class Post(metaclass=MyMeta):
    pass


print(Post.created_at)
