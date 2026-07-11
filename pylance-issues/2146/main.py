 # SCENARIO: extract method should preserve the multi-line except tuple formatting
 # TARGET: select the try/except block between the two printed prompts
 # TRIGGER: run "Extract method" on the selected block
 # EXPECT: the extracted method keeps the multi-line `(KeyError, ValueError)` formatting
 # VERIFY: if the tuple collapses or reformats incorrectly, the bug still reproduces
 # RECOVER: undo the refactoring or reload the file

def main():
    """Demo of the bug"""

    print('Select from here')

    try:
        raise ValueError('This is a test')
    except (
        KeyError,
        ValueError,
    ) as e:
        print(e)

    print('...to here and select "Extract method" in the light bulb menu.')

    return 0