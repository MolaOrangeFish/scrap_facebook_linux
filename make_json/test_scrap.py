from facebook_scraper import get_posts
group_id = '197822284350539' #KMUTNB Community
for post in get_posts(group=group_id, pages=3, extra_info=True, option={"comment": False,"posts_per_page": 3,"reactors": True},credentials=("kittichet2000@hotmail.com","XXX")):#group=group_id, pages=20,cookies="from_browser", extra_info=True, option={"comment": False,"posts_per_page": 3,"reactors": True}
    print(post['images'])