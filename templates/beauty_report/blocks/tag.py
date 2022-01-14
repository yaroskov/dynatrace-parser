def template(tag="div", value="", params=None, double=True):
    params_line = ""
    if params:
        for param in params:
            params_line += f' {param}="{params[param]}"'

    results = f'\n<{tag}{params_line}>'
    if double:
        results += "\n" + value
        results += f'\n</{tag}>'

    return results
