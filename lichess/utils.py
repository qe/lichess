import re
VALID_REGEX = "^[A-Za-z0-9_-]*$"
VALID_RULES = re.compile(VALID_REGEX)


def valid_input(user_input):
    if isinstance(user_input, str):
        if VALID_RULES.match(user_input):
            return True
    return False

# validate params in list of strings
# True --> ALL GOOD
# False --> BAD!
# def val_liststr(list_str):
#     """
#     Takes a list of strings and makes sure all are valid
#     e.g. make sure "foo,bar,ismodes" .isalnum() and
#
#     :return:
#     """
#     invalid = [_ for _ in list_str if not _.isalnum()]
#     return len(invalid) == 0
#
#
# # makes sure list is not a nested list
# # True --> ALL GOOD (i.e. not nested)
# # False --> BAD!
# def not_nested(my_list):
#     return not any(isinstance(i, list) for i in my_list)

