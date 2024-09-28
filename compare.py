import xmlschema
import xml.etree.ElementTree as ET

# Load and parse the XSD schema
schema = xmlschema.XMLSchema('schemat.xsd')

# Generate a sample XML document based on the schema
# Create an empty data structure that corresponds to the XSD schema
data = schema.create_element('root')  # Adjust 'root' to match your schema's root element

# Create an XML tree from the data
root = ET.Element('root')  # Adjust root element to match your schema
tree = ET.ElementTree(root)

# Add example data according to the schema
for element in data:
    child = ET.SubElement(root, element.tag)
    child.text = 'Sample data'  # Fill with actual data based on your needs

# Write the XML document to a file
tree.write('output.xml', encoding='utf-8', xml_declaration=True)

print("XML file generated successfully!")

