
posts = []

def add_question(text):
    post_id = len(posts) + 1
    posts.append({
        "id": post_id,
        "text": text,
        "parent_id": None
    })
    return post_id
def add_answer(text, question_id):
    post_id = len(posts) + 1
    posts.append({
        "id": post_id,
        "text": text,
        "parent_id": question_id
    })


def get_answered_questions():
    answered = []

    for post in posts:
        if post["parent_id"] is None:  # سؤال
            for reply in posts:
                if reply["parent_id"] == post["id"]:
                    answered.append(post)
                    break

    return answered


def show_feed():
    feed = get_answered_questions()

    if not feed:
        print("\nNo answered questions yet.\n")
        return

    print("\n=== GLOBAL FEED ===\n")
    for q in feed:
        print(f"- {q['text']}")
        show_answers(q["id"])
        print()


def show_answers(question_id):
    for post in posts:
        if post["parent_id"] == question_id:
            print(f" {post['text']}")
