# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
"""
Common validator wrapper to provide a uniform usage of other schema validation
libraries.
"""

import os

import fastjsonschema
import jsonschema
from fastjsonschema import JsonSchemaException as _JsonSchemaException
from jsonschema import Draft4Validator as _JsonSchemaValidator
from jsonschema import ErrorTree, ValidationError


class JsonSchemaValidator:
    name = "jsonschema"

    def __init__(self, schema):
        self._schema = schema
        self._default_validator = _JsonSchemaValidator(schema)  # Default
        self._validator = self._default_validator

    def validate(self, data):
        self._default_validator.validate(data)

    def iter_errors(self, data, schema=None):
        if schema is None:
            return self._default_validator.iter_errors(data)
        if hasattr(self._default_validator, "evolve"):
            return self._default_validator.evolve(schema=schema).iter_errors(data)
        return self._default_validator.iter_errors(data, schema)

    def error_tree(self, errors):
        return ErrorTree(errors=errors)


class FastJsonSchemaValidator(JsonSchemaValidator):
    name = "fastjsonschema"

    def __init__(self, schema):
        super().__init__(schema)
        self._validator = fastjsonschema.compile(schema)

    def validate(self, data):
        try:
            self._validator(data)
        except _JsonSchemaException as error:
            raise ValidationError(str(error), schema_path=error.path)

    def iter_errors(self, data, schema=None):
        if schema is not None:
            return super().iter_errors(data, schema)

        errors = []
        validate_func = self._validator
        try:
            validate_func(data)
        except _JsonSchemaException as error:
            errors = [ValidationError(str(error), schema_path=error.path)]

        return errors

    def error_tree(self, errors):
        # fastjsonschema's exceptions don't contain the same information that the jsonschema ValidationErrors
        # do. This method is primarily used for introspecting metadata schema failures so that we can strip
        # them if asked to do so in `nbformat.validate`.
        # Another way forward for compatibility: we could distill both validator errors into a custom collection
        # for this data. Since implementation details of ValidationError is used elsewhere, we would probably
        # just use this data for schema introspection.
        raise NotImplementedError("JSON schema error introspection not enabled for fastjsonschema")


_VALIDATOR_MAP = [
    ("fastjsonschema", fastjsonschema, FastJsonSchemaValidator),
    ("jsonschema", jsonschema, JsonSchemaValidator),
]
VALIDATORS = [item[0] for item in _VALIDATOR_MAP]


def _validator_for_name(validator_name):
    if validator_name not in VALIDATORS:
        raise ValueError(
            f"Invalid validator '{validator_name}' value!\nValid values are: {VALIDATORS}"
        )

    for (name, module, validator_cls) in _VALIDATOR_MAP:
        if module and validator_name == name:
            return validator_cls
    # we always return something.
    raise ValueError(f"Missing validator for {repr(validator_name)}")


def get_current_validator():
    """
    Return the default validator based on the value of an environment variable.
    """
    validator_name = os.environ.get("NBFORMAT_VALIDATOR", "fastjsonschema")
    return _validator_for_name(validator_name)
