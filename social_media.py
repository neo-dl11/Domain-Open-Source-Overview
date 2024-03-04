import praw

client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'
user_agent = 'APP_NAME'

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

def search_reddit_for_domain(domain_name, num_posts=10):
    posts = []
    try:
        search_results = reddit.subreddit("all").search(domain_name, limit=num_posts)
        for submission in search_results:
            posts.append(submission.title)
    except Exception as e:
        print(f"Error searching Reddit: {e}")
    return posts

