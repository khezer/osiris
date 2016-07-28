from colander import MappingSchema, SchemaNode, String


class BlockSchema(MappingSchema):
    delta = SchemaNode(String())
    body = SchemaNode(String())
