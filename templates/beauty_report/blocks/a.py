def template(value, href="", style=""):
    results = f'\n<a href="{href}" style="{style}">'
    results += "\n" + value
    results += '\n</a>'

    return results
