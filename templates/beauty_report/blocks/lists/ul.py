from templates.beauty_report.blocks.lists.logic import list_logic


def template(lis, style="", li_style=""):
    return list_logic.template(
        list_type="ul",
        type_argument="",
        lis=lis,
        style=style,
        li_style=li_style
    )
