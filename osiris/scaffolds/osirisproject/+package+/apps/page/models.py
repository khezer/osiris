from osiris.model import Model
from .schemas import PageSchema


class PageModel(Model):
    """ Stores website pages.
    sample:
        about us
        features
        ...

    fields:
        title
        slug
        body
        meta_keywords
        meta_description
        status
        user_id
        created
        changed
    """

    __collection__ = 'pages'
    __schema__ = PageSchema()
