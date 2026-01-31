# ---------- INPUT & OUTPUT ----------

def print_line(char="-", length=30):
    print(char * length)


def print_title(title):
    print_line("=")
    print(title)
    print_line("=")


# ---------- STRING HANDLING ----------

def clean_string(text):
    return text.strip()


def is_empty(text):
    return clean_string(text) == ""


# ---------- VALIDATION ----------

def get_non_empty_input(msg):
    while True:
        value = input(msg)
        if not is_empty(value):
            return clean_string(value)
        print(" Input cannot be empty")


def get_yes_no(msg):
    while True:
        choice = input(msg + " (y/n): ").lower()
        if choice in ("y", "n"):
            return choice == "y"
        print(" Please enter y or n")


# ---------- SAFE INTEGER INPUT ----------

def get_int_input(msg, min_val=None, max_val=None):
    while True:
        try:
            num = int(input(msg))

            if min_val is not None and num < min_val:
                print(f" Number must be >= {min_val}")
                continue

            if max_val is not None and num > max_val:
                print(f" Number must be <= {max_val}")
                continue

            return num

        except ValueError:
            print(" Please enter a valid integer")


# ---------- MENU DISPLAY ----------

def show_menu(title, options):
    print_title(title)
    for i, option in enumerate(options, start=1):
        print(f"{i}) {option}")
    print_line()

   
# ---------- INPUT VALIDATION LOOPS ----------

def get_non_empty_input(msg):
    while True:
        value = input(msg).strip()
        if value != "":
            return value
        print(" Input cannot be empty, try again")


def get_int_input(msg, min_val=None, max_val=None):
    while True:
        try:
            num = int(input(msg))

            if min_val is not None and num < min_val:
                print(f" Number must be >= {min_val}")
                continue

            if max_val is not None and num > max_val:
                print(f" Number must be <= {max_val}")
                continue

            return num

        except ValueError:
            print(" Please enter a valid integer")


def get_yes_no(msg):
    while True:
        ans = input(msg + " (y/n): ").lower()
        if ans == "y" or ans == "n":
            return ans == "y"
        print(" Please enter y or n")




