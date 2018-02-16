import sys

from colors import red, black, blue


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " ["+blue("y") + "/" + red("n") + "] "
    elif default == "yes":
        prompt = " ["+blue("Y") + "/" + red("n") + "] "
    elif default == "no":
        prompt = " ["+blue("y") + "/" + red("N") + "] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def progressBar(value, endvalue, color, bar_length=20):
    """
    \r move the cursor back to the beginning of the line
    \b apply backspace
    # for i in range(11):
    #     progressBar(i,10,50)
    #     time.sleep(1)
    # sys.exit(1)
    :param value:
    :param endvalue:
    :param bar_length:
    :return:
    """
    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write(color("\rProgress: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100)))))
    sys.stdout.flush()
