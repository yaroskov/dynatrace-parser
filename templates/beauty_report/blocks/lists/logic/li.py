def template(data, style):
    string = f"\n<li style=\"{style}\">"
    string += "\n" + data
    string += "\n</li>"

    return string
