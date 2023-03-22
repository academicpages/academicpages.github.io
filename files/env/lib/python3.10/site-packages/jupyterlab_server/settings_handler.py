"""Tornado handlers for frontend config storage."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import json

from jsonschema import ValidationError
from jupyter_server.extension.handler import ExtensionHandlerJinjaMixin, ExtensionHandlerMixin
from tornado import web

from .settings_utils import SchemaHandler, get_settings, save_settings
from .translation_utils import translator


class SettingsHandler(ExtensionHandlerMixin, ExtensionHandlerJinjaMixin, SchemaHandler):
    """A settings API handler."""

    def initialize(
        self, name, app_settings_dir, schemas_dir, settings_dir, labextensions_path, **kwargs
    ):
        """Initialize the handler."""
        SchemaHandler.initialize(
            self, app_settings_dir, schemas_dir, settings_dir, labextensions_path
        )
        ExtensionHandlerMixin.initialize(self, name)

    @web.authenticated
    def get(self, schema_name=""):
        """Get setting(s)"""
        # Need to be update here as translator locale is not change when a new locale is put
        # from frontend
        locale = self.get_current_locale()
        translator.set_locale(locale)

        result, warnings = get_settings(
            self.app_settings_dir,
            self.schemas_dir,
            self.settings_dir,
            labextensions_path=self.labextensions_path,
            schema_name=schema_name,
            overrides=self.overrides,
            translator=translator.translate_schema,
        )

        # Print all warnings.
        for w in warnings:
            if w:
                self.log.warning(w)

        return self.finish(json.dumps(result))

    @web.authenticated
    def put(self, schema_name):
        """Update a setting"""
        overrides = self.overrides
        schemas_dir = self.schemas_dir
        settings_dir = self.settings_dir
        settings_error = "No current settings directory"
        invalid_json_error = "Failed parsing JSON payload: %s"
        invalid_payload_format_error = (
            "Invalid format for JSON payload. Must be in the form {'raw': ...}"
        )
        validation_error = "Failed validating input: %s"

        if not settings_dir:
            raise web.HTTPError(500, settings_error)

        raw_payload = self.request.body.strip().decode("utf-8")
        try:
            raw_settings = json.loads(raw_payload)["raw"]
            save_settings(
                schemas_dir,
                settings_dir,
                schema_name,
                raw_settings,
                overrides,
                self.labextensions_path,
            )
        except json.decoder.JSONDecodeError as e:
            raise web.HTTPError(400, invalid_json_error % str(e)) from None
        except (KeyError, TypeError):
            raise web.HTTPError(400, invalid_payload_format_error) from None
        except ValidationError as e:
            raise web.HTTPError(400, validation_error % str(e)) from None

        self.set_status(204)
