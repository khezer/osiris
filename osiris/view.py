from cornice.schemas import CorniceSchema


class ResourceView(object):
    __model__ = None
    __schema__ = None

    def __init__(self, context, request):
        self.context = context
        self.request = request

        # Accepted content_type of request
        self.content_type = "application/json"

        # Database connection
        self.db = request.db

        # Model
        if self.__model__ is not None:
            self.model = request.db[str(self.__model__)]

        self._id = None
        if '_id' in self.request.matchdict:
            self._id = self.request.matchdict['_id']

        if request.method != 'GET' or \
                (self._id is not None and request.method == 'DELETE'):
            # Set self.json for POST, PUT, PATCH, DELETE request method
            self.json = request.json

            if self.__schema__ is not None:
                schema = self.__schema__
            else:
                schema = self.model.schema

            # Data validation schema
            self.schema = CorniceSchema.from_colander(
                schema, bind_request=False)

    def collection_get(self):
        return {}

    def collection_post(self):
        return {}

    def collection_put(self):
        return {}

    def collection_patch(self):
        return {}

    def collection_delete(self):
        return {}

    def get(self):
        return {}

    def post(self):
        return {}

    def put(self):
        return {}

    def patch(self):
        return {}

    def delete(self):
        return {}


class View(object):
    __model__ = None

    def __init__(self, context, request):
        self.context = context
        self.request = request

        # Database connection
        self.db = request.db

        # Model
        if self.__model__ is not None:
            self.model = request.db[str(self.__model__)]
