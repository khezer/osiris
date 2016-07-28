from osiris.model import Model
from .schemas import BlockSchema


class BlockModel(Model):
    """ Stores blocks.
    sample:
        navigation menu
        footer
        or custom sidebar block
        ...

    fields:
        delta
        title
        body
        status
        user_id
        created
        changed
    """

    __collection__ = 'blocks'
    __schema__ = BlockSchema()
