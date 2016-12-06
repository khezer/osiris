from pyramid_layout.panel import panel_config
from osiris.view import View
from .models import BlockModel


class BlockView(View):
    """ Block view class
    """
    __model__ = BlockModel()

    @panel_config(name='block', renderer='block/block.html')
    def blockview(self, delta):
        block = self.model.find_one({'delta': delta})
        if block is None:
            block = {
                'delta': '',
                'body': ''
            }
        return block
