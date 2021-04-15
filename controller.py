# -*- coding: utf-8 -*- 

from proxie import Proxie

class ControllerFormatProxie(object):
    def __init__(self, *args):
        ...

    """ This function start callback for format layout proxies """
    def proxie_layout(self, id_country):
        try:

            page = Proxie().get_page_html()
            layout = Proxie().format_layout(page, id_country)
            return layout
        
        except Exception as error:
            print(error)
            return {"status": 404, "error": str(error)}


