def template(value, style=""):
    results = f'\n<span style="{style}">'
    results += "\n" + value
    results += '\n</span>'

    return results
