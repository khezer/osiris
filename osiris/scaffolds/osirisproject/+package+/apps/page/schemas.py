from colander import MappingSchema, SchemaNode, String, Integer


class PageSchema(MappingSchema):
    title = SchemaNode(String())
    slug = SchemaNode(String())
    body = SchemaNode(String())
    meta_keywords = SchemaNode(String())
    meta_description = SchemaNode(String())
    status = SchemaNode(Integer())
