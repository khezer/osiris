# from cornice.schemas import CorniceSchema


class ResourceView(object):
    # __model__ = None
    # __schema__ = None

    def __init__(self, request):
        self.request = request

        # Accepted content_type of request
        self.content_type = "application/json"

        # Database connection
        if request.db:
            self.db = request.db

            # Model
            # if self.__model__ is not None:
            #     self.model = request.db[str(self.__model__)]
            #     self.model = self.__model__(request.db)

        else:
            self.db = None


        self._id = None
        if '_id' in self.request.matchdict:
            self._id = self.request.matchdict['_id']

        if request.method in ['POST', 'PUT', 'PATCH']:
            # Set self.json for POST, PUT, PATCH request method
            self.json = request.json

            # schema = None
            # if self.__schema__ is not None:
            #     schema = self.__schema__
            # elif self.__model__ is not None:
            #     schema = self.model.schema

            # # Data validation schema
            # if schema is not None:
            #     self.schema = CorniceSchema.from_colander(
            #         schema, bind_request=False)

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

    def __init__(self, request):
        self.request = request

        # Database connection
        if request.db:
            self.db = request.db

            # Model
            if self.__model__ is not None:
                self.model = request.db[str(self.__model__)]

        else:
            self.db = None

