# mylab

soft_unicode method has been deprecated in markupsafe newer versions. To solve the error, run the `pip install markupsafe==2.0.1`.

## Pydantic

Data validation and settings management using Python type annotations.

It enforces type hints at runtime, and provides user friendly errors when data is invalid.

### Models

Untrusted data can be passed to a model, and after parsing and validation *pydantic* guarantees that the fields of the resultant model instance will conform to the field types defined on the model.

## FastAPI

Key features:
- Fast: on par with NodeJS and Go (thanks to Starlette and Pydantic)
- Fast to code
- Fewer bugs
- Intuitive
- Easy
- Short
- Robust
- Standards-based: based on OpenAPI and JSON Schema
- Dependency Injection
- Pydantic features

## hypothesis

## Protocols (Structural subtyping), ABC and Factories
[P, ABC and F](https://dev.to/meseta/factories-abstract-base-classes-and-python-s-new-protocols-structural-subtyping-20bm)


## OpenAPI

## JASON Schema
https://json-schema.org/understanding-json-schema/

### Understanding JSON Schema
The *type* keyword
`{"type": "string"}`
- `string`
  * `minLength`
  * `maxLength`
  * `pattern`

- `number`
  * `multipleOf`
  * `minimum`
  * `maximum`
  * `exclusiveMinimum`
  * `exclusiveMaximum`

- `integer`

- `object`
  * `properties`
  * `required`
- `array`
  * `items`
  * `uniqueItems`

- `boolean`
- `null`
- `enum`
- `const`

Declaring a JSON Schema
`{"$schema": "https://json-schema.org/draft/2000-12/schema"}`

Declaring a uniqie identifier
`{"$id": "http://yourdomain.com/schemas/myschema.json"}`

### jsonschema
https://github.com/python-jsonschema/jsonschema
`jsonschema` is an implementation of the JSON Schema specification for Python

## uvicorn

## orjson

## pyyaml

## install
pip install -e .[extra] --upgrade
