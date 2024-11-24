from name_function import get_formatted_name

"""
Unit test - verifies that one specific aspect of a function's behaviour is correct.
Test case - collection of unit tests that together prove that a function behaves as it's supposed to.
"""


# A passing test
def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == "Janis Joplin"  # An assertion is a claim about a condition


def test_first_middle_last_name():
    """Do names like 'Douglas Noel Adams' work?"""
    formatted_name = get_formatted_name(
        'douglas', "adams", "noel"
    )
    assert formatted_name == "Douglas Noel Adams"

# Run 'pytest' in a terminal
