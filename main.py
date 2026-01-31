
# _______menu_______#
import utils
from sync import DataSync
from threading import Thread
from threads import add_question,add_reply,show_threads
from feed import show_feed,add_answer
utils.show_menu(
    "Main Menu",
    ["Login", "Sign Up", "Exit"]
)

choice = utils.get_int_input("Choose: ", 1, 3)
print("You chose:", choice)

#________nput Validation__________#
name = utils.get_non_empty_input("Enter your name: ")
allow = utils.get_yes_no("Allow anonymous questions?")


# ---------- INPUT VALIDATION LOOPS ----------

print("=== TEST INPUT VALIDATION ===")

name = utils.get_non_empty_input("Enter your name: ")
age = utils.get_int_input("Enter your age: ", 1, 120)
allow = utils.get_yes_no("Allow anonymous questions?")

print("\n--- Result ---")
print("Name:", name)
print("Age:", age)
print("Allow anonymous:", allow)

     #________data_sync________#
sync = DataSync() 

def user_activity(user_name, messages):
    for msg in messages:
        sync.add_message(user_name, msg)
if __name__ == "__main__":
    user1_msgs = ["Hi", "How are you?"]
    user2_msgs = ["Hello", "I am fine"]

    t1 = Thread(target=user_activity, args=("User1", user1_msgs))
    t2 = Thread(target=user_activity, args=("User2", user2_msgs))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nAll messages:")
    for user, msg in sync.get_messages():
        print(f"{user}: {msg}")
        #_______________theards_____________#

def main():
    print("=== Q&A Threaded System ===")

    
    q1 = add_question("What is Python?")

    add_reply("Python is easy to learn", q1)
    add_reply("It is used in AI and web", q1)

    
    add_reply("Yes, especially for beginners", 2)

    
    print("\nThreads:\n")
    show_threads()

if __name__ == "__main__":
    main()

    #_________feed_____________#

posts = []

def main():
    while True:
        print("\n1. Add Question")
        print("2. Add Answer")
        print("3. Show Global Feed")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            text = input("Question: ")
            add_question(text)

        elif choice == "2":
            q_id = int(input("Question ID: "))
            text = input("Answer: ")
            add_answer(text, q_id)

        elif choice == "3":
            show_feed()

        elif choice == "4":
            print("Bye")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


