from templates.beauty_report.blocks.lists.logic import li


def template(list_type, type_argument, lis, style, li_style):
    string = f"\n<{list_type} type=\"{type_argument}\" style=\"{style}\">"

    for li_block in lis:
        string += li.template(li_block, li_style)

    string += f"\n</{list_type}>"

    return string
