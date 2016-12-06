from bson import ObjectId


class Model(object):
    __collection__ = None
    __schema__ = None

    def __init__(self, request=None):
        self.collection = None
        if self.__collection__ is not None and request is not None:
            self.collection = request.db[str(self.__collection__)]

        self.schema = self.__schema__

    def __repr__(self):
        return self.__collection__

    def __str__(self):
        return self.__collection__

    def insert_one(self, document):
        return self.collection.insert_one(self.filter(document))

    def insert_many(self, documents, ordered=True):
        return self.collection.insert_many(self.filter_many(documents), ordered)

    def update_one_by_id(self, _id, update):
        return self.update_one({'_id': ObjectId(_id)}, self.filter(update))

    def update_one(self, filter, update, upsert=False):
        return self.collection.update_one(filter, self.filter(update), upsert)

    def update_many(self, filter, update):
        return self.collection.update_many(filter, self.filter(update))

    def delete_one_by_id(self, _id):
        return self.delete_one({'_id': ObjectId(_id)})

    def delete_one(self, filter):
        return self.collection.delete_one(filter)

    def delete_many(self, filter):
        return self.collection.delete_many(filter)

    def find_by_id(self, _id):
        document = self.find_one({'_id': ObjectId(_id)})
        return document

    def find_one(self, criteria, projection=None):
        if projection is not None:
            document = self.collection.find_one(criteria, projection)
        else:
            document = self.collection.find_one(criteria)

        if document:
            # Convert ObjectId to string
            document['_id'] = str(document['_id'])
            return document

        return None

    def find(self, criteria=None, projection=None):
        if criteria is not None and projection is not None:
            documents = self.collection.find(criteria, projection)
        elif criteria is not None:
            documents = self.collection.find(criteria)
        else:
            documents = self.collection.find()

        docs = list()
        for doc in documents:
            # Convert ObjectId to string
            if '_id' in doc:
                doc['_id'] = str(doc['_id'])
            docs.append(doc)
        return docs

    def count(self, filter=None, **kwargs):
        return self.collection.count(filter, kwargs)

    def filter(self, document):
        if self.schema is None:
            return document

        # Find defined schema node in schema of collection
        schema_nodes = list()
        for schema_node_object in self.schema.__all_schema_nodes__:
            schema_node = vars(schema_node_object)
            schema_nodes.append(schema_node['name'])

        # Filter document base on colander schema
        filtred_document = dict()
        for key, value in document.items():
            if key in schema_nodes:
                filtred_document[key] = value

        return filtred_document
