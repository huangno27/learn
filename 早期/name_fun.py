def get_formatted_name(first,last,middle=''):           #middle中间名改为可选
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ''  + middle + '' + last
    else:
        full_name = first + '' + '' + last
    return full_name.title()
