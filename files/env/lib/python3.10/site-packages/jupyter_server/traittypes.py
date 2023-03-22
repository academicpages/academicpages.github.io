import inspect
from ast import literal_eval

from traitlets import ClassBasedTraitType, TraitError, Undefined
from traitlets.utils.descriptions import describe


class TypeFromClasses(ClassBasedTraitType):
    """A trait whose value must be a subclass of a class in a specified list of classes."""

    default_value: Undefined

    def __init__(self, default_value=Undefined, klasses=None, **kwargs):
        """Construct a Type trait
        A Type trait specifies that its values must be subclasses of
        a class in a list of possible classes.
        If only ``default_value`` is given, it is used for the ``klasses`` as
        well. If neither are given, both default to ``object``.
        Parameters
        ----------
        default_value : class, str or None
            The default value must be a subclass of klass.  If an str,
            the str must be a fully specified class name, like 'foo.bar.Bah'.
            The string is resolved into real class, when the parent
            :class:`HasTraits` class is instantiated.
        klasses : list of class, str [ default object ]
            Values of this trait must be a subclass of klass.  The klass
            may be specified in a string like: 'foo.bar.MyClass'.
            The string is resolved into real class, when the parent
            :class:`HasTraits` class is instantiated.
        allow_none : bool [ default False ]
            Indicates whether None is allowed as an assignable value.
        """
        if default_value is Undefined:
            new_default_value = object if (klasses is None) else klasses
        else:
            new_default_value = default_value

        if klasses is None:
            if (default_value is None) or (default_value is Undefined):
                klasses = [object]
            else:
                klasses = [default_value]

        # OneOfType requires a list of klasses to be specified (different than Type).
        if not isinstance(klasses, (list, tuple, set)):
            raise TraitError("`klasses` must be a list of class names (type is str) or classes.")

        for klass in klasses:
            if not (inspect.isclass(klass) or isinstance(klass, str)):
                raise TraitError("A OneOfType trait must specify a list of classes.")

        # Store classes.
        self.klasses = klasses

        super().__init__(new_default_value, **kwargs)

    def subclass_from_klasses(self, value):
        "Check that a given class is a subclasses found in the klasses list."
        return any(issubclass(value, klass) for klass in self.importable_klasses)

    def validate(self, obj, value):
        """Validates that the value is a valid object instance."""
        if isinstance(value, str):
            try:
                value = self._resolve_string(value)
            except ImportError:
                raise TraitError(
                    "The '%s' trait of %s instance must be a type, but "
                    "%r could not be imported" % (self.name, obj, value)
                )
        try:
            if self.subclass_from_klasses(value):
                return value
        except Exception:
            pass

        self.error(obj, value)

    def info(self):
        """Returns a description of the trait."""
        result = "a subclass of "
        for klass in self.klasses:
            if not isinstance(klass, str):
                klass = klass.__module__ + "." + klass.__name__
            result += f"{klass} or "
        # Strip the last "or"
        result = result.strip(" or ")  # noqa B005
        if self.allow_none:
            return result + " or None"
        return result

    def instance_init(self, obj):
        self._resolve_classes()
        super().instance_init(obj)

    def _resolve_classes(self):
        # Resolve all string names to actual classes.
        self.importable_klasses = []
        for klass in self.klasses:
            if isinstance(klass, str):
                # Try importing the classes to compare. Silently, ignore if not importable.
                try:
                    klass = self._resolve_string(klass)
                    self.importable_klasses.append(klass)
                except Exception:
                    pass
            else:
                self.importable_klasses.append(klass)

        if isinstance(self.default_value, str):
            self.default_value = self._resolve_string(self.default_value)

    def default_value_repr(self):
        value = self.default_value
        if isinstance(value, str):
            return repr(value)
        else:
            return repr(f"{value.__module__}.{value.__name__}")


class InstanceFromClasses(ClassBasedTraitType):
    """A trait whose value must be an instance of a class in a specified list of classes.
    The value can also be an instance of a subclass of the specified classes.
    Subclasses can declare default classes by overriding the klass attribute
    """

    def __init__(self, klasses=None, args=None, kw=None, **kwargs):
        """Construct an Instance trait.
        This trait allows values that are instances of a particular
        class or its subclasses.  Our implementation is quite different
        from that of enthough.traits as we don't allow instances to be used
        for klass and we handle the ``args`` and ``kw`` arguments differently.
        Parameters
        ----------
        klasses : list of classes or class_names (str)
            The class that forms the basis for the trait.  Class names
            can also be specified as strings, like 'foo.bar.Bar'.
        args : tuple
            Positional arguments for generating the default value.
        kw : dict
            Keyword arguments for generating the default value.
        allow_none : bool [ default False ]
            Indicates whether None is allowed as a value.
        Notes
        -----
        If both ``args`` and ``kw`` are None, then the default value is None.
        If ``args`` is a tuple and ``kw`` is a dict, then the default is
        created as ``klass(*args, **kw)``.  If exactly one of ``args`` or ``kw`` is
        None, the None is replaced by ``()`` or ``{}``, respectively.
        """
        # If class
        if klasses is None:
            self.klasses = klasses
        # Verify all elements are either classes or strings.
        elif all(inspect.isclass(k) or isinstance(k, str) for k in klasses):
            self.klasses = klasses
        else:
            raise TraitError(
                "The klasses attribute must be a list of class names or classes"
                " not: %r" % klasses
            )

        if (kw is not None) and not isinstance(kw, dict):
            raise TraitError("The 'kw' argument must be a dict or None.")
        if (args is not None) and not isinstance(args, tuple):
            raise TraitError("The 'args' argument must be a tuple or None.")

        self.default_args = args
        self.default_kwargs = kw

        super().__init__(**kwargs)

    def instance_from_importable_klasses(self, value):
        "Check that a given class is a subclasses found in the klasses list."
        return any(isinstance(value, klass) for klass in self.importable_klasses)

    def validate(self, obj, value):
        if self.instance_from_importable_klasses(value):
            return value
        else:
            self.error(obj, value)

    def info(self):
        result = "an instance of "
        assert self.klasses is not None
        for klass in self.klasses:
            if isinstance(klass, str):
                result += klass
            else:
                result += describe("a", klass)
            result += " or "
        result = result.strip(" or ")  # noqa B005
        if self.allow_none:
            result += " or None"
        return result

    def instance_init(self, obj):
        self._resolve_classes()
        super().instance_init(obj)

    def _resolve_classes(self):
        # Resolve all string names to actual classes.
        self.importable_klasses = []
        assert self.klasses is not None
        for klass in self.klasses:
            if isinstance(klass, str):
                # Try importing the classes to compare. Silently, ignore if not importable.
                try:
                    klass = self._resolve_string(klass)
                    self.importable_klasses.append(klass)
                except Exception:
                    pass
            else:
                self.importable_klasses.append(klass)

    def make_dynamic_default(self):
        if (self.default_args is None) and (self.default_kwargs is None):
            return None
        return self.klass(*(self.default_args or ()), **(self.default_kwargs or {}))

    def default_value_repr(self):
        return repr(self.make_dynamic_default())

    def from_string(self, s):
        return literal_eval(s)
