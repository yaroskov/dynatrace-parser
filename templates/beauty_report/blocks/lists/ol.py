from templates.beauty_report.blocks.lists.logic import list_logic


def template(lis, type_argument="", style="", li_style=""):
    return list_logic.template(
        list_type="ol",
        type_argument=type_argument,
        lis=lis,
        style=style,
        li_style=li_style
    )
