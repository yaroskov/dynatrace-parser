from templates.beauty_report.blocks import tag
from templates.beauty_report.blocks.lists import ol


def template(input_data):
    string = tag.template(tag="!DOCTYPE html", double=False)
    head = tag.template(tag="meta", params={"charset": "UTF-8"}, double=False)
    head += tag.template("title", "Dynatrace Analyse")
    head += tag.template("style", "body {font-size: 14px; font-family: Arial, Helvetica, sans-serif;}")
    string += tag.template("head", head)
    string += tag.template(tag="div", params={"id": "header"})

    dyna_text = 'Dynatrace:'
    sections = ["Выявленные отказы:" + input_data, "Заведены новые дефекты:"]
    dyna_text += ol.template(sections)
    string += ol.template([dyna_text], type_argument="I")

    string = tag.template(tag="body", value=string, params={"id": "content"})
    string += tag.template(tag="div", params={"id": "bottom"})
    string = tag.template("body", string)
    string = tag.template("html", string)

    return string

