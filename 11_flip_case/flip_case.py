def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

    >>> flip_case('Aaaahhh', 'a')
    'aAAAhhh'

    >>> flip_case('Aaaahhh', 'A')
    'aAAAhhh'

    >>> flip_case('Aaaahhh', 'h')
    'AaaaHHH'

    """
    to_swap = to_swap.lower()
    out = ""

    for let in phrase:
        if let.lower() == to_swap:
            let = let.swapcase()
        out += let

    return out
