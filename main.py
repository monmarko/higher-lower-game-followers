import random
from art import logo
from art import vs
from game_data import data


def get_random_account():
    return random.choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


def get_followers_amount(account):
    return account["follower_count"]


def follower_checking(followers_a_amount, followers_b_amount, user_guess):
    """
    Checks followers against user's guess and returns
    True if they got it right. Or False if they got it wrong.
    """

    if followers_a_amount > followers_b_amount:
        return user_guess == "a"
    else:
        return user_guess == "b"


def game():
    should_continue = True
    score = 0
    first_person = get_random_account()

    while should_continue:

        print(logo)

        second_person = get_random_account()

        if first_person == second_person:
            second_person = get_random_account()

        followers_a = get_followers_amount(first_person)
        followers_b = get_followers_amount(second_person)

        print(format_data(first_person))
        print(vs)
        print(format_data(second_person))

        user_guess = input("\nWho has more followers? Type A or B: ").lower()
        if follower_checking(followers_a, followers_b, user_guess):
            score += 1
            print(f"That's right, your score is {score}")
            if followers_b > followers_a:
                first_person = second_person
            should_continue = True
            # clear()

        else:
            print(f"Game over, your score is: {score}")
            should_continue = False


game()
