import xmlschema
from pprint import pprint
schema = xmlschema.XMLSchema('./dane/schemat.xsd')
schema.types
pprint(dict(schema.elements))
schema.get_schema()
