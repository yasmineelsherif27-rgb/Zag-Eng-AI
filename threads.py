
posts = []  


def add_question(text):
    post_id = len(posts) + 1
    posts.append({
        "id": post_id,
        "text": text,
        "parent_id": None
    })
    return post_id


def add_reply(text, parent_id):
    post_id = len(posts) + 1
    posts.append({
        "id": post_id,
        "text": text,
        "parent_id": parent_id
    })


def show_threads(parent_id=None, level=0):
    for post in posts:
        if post["parent_id"] == parent_id:
            print("  " * level + "- " + post["text"])
            show_threads(post["id"], level + 1)
            