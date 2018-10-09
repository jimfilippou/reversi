def who_plays_first():
    """
    Asks user if he/she wants to play first.
    Returns 'human' if human plays first and 'ai' if computer plays first.
    """
    ans = ''
    while str(ans).lower() != 'y' or str(ans).lower() != 'n':
        ans = input("Do you want to play first? [Y/N] ")
        if str(ans).lower() == 'y' or str(ans).lower() == 'n':
            break
    return 'human' if str(ans).lower() == 'y' else 'ai' 