from main import User, Tag, Post, db
import random
import datetime
user = User.query.get(1)
tag_one = Tag('Python')
tag_two = Tag('Flask')
tag_three = Tag('Jinja')

tag_list = [tag_one, tag_two, tag_three]

s = 'example text'

for i in xrange(100):
    new_post = Post("Post" + str(i))
    new_post.user = user
    new_post.publish_date = datetime.datetime.now()
    new_post.text = s
    new_post.tags = random.sample(tag_list, random.randint(1,2))
    db.session.add(new_post)

db.session.commit()