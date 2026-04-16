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