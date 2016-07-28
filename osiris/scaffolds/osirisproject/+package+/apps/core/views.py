from pyramid.view import view_config
from pyramid.view import notfound_view_config
from pyramid.view import forbidden_view_config
from pyramid_layout.layout import layout_config
from osiris.view import View


@layout_config(template='layout.html')
class LayoutView(View):
    """ Default layout
    """
    pass


class FrontPage(View):
    """ Front page view class
    """

    @view_config(route_name='frontpage', renderer='frontpage.html')
    def frontpage(self):
        return {}


class HttpExceptionsView(View):
    """ HTTP exceptions special pages
    """

    @notfound_view_config(renderer='404.html')
    def notfound(self):
        # self.request.response.status = 404
        return {}

    @forbidden_view_config(renderer='403.html')
    def forbidden(self):
        # self.request.response.status = 403
        return {}
