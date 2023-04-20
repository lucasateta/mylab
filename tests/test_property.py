import pytest

from XYZThings.models.value import Value
from XYZThings.models.property import Property, PropertyError

from XYZThings.models.errors import PropertyError

def test_name():
    p = Property("my_property", 1)
    assert p.name == "my_property"

def test_repr():
    p = Property("my_property", 1)
    assert p.__repr__() == "(Property my_property)"

def test_description():
    p = Property("my_property", Value(1))
    assert p.description == {
        'links': [
            {
                'href': '/properties/my_property', 
                'mediaType': 'application/json',
                'rel': 'property'
            }
        ]}

def test_href():
    p = Property("my_property", Value(1))
    assert p.href == "/properties/my_property"

def test_href_prefix():
    p = Property("my_property", Value(1))
    assert p.href_prefix == ""

@pytest.mark.asyncio
async def test_set_get_value():
    p = Property("my_property", Value(1))
    await p.set_value(2)

    assert await p.get_value() == 2
    
@pytest.mark.asyncio
async def test_property_error():
    metadata={
        "@type": "OnOffProperty",
        "title": "On/Off",
        "type": "boolean",
        "description": "Whether the lamp is turned on",
    }
    p = Property(
        "my_property",
        Value(True),
        metadata=metadata,
    )

    with pytest.raises(PropertyError, match='Invalid property value 1'):
        await p.set_value(1)

    assert await p.get_value() == True