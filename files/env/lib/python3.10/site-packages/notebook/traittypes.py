import inspect
from traitlets import ClassBasedTraitType, Undefined, warn

# Traitlet's 5.x includes a set of utilities for building
# description strings for objects. Traitlets 5.x does not
# support Python 3.6, but notebook does; instead
# notebook uses traitlets 4.3.x which doesn't have
# this `descriptions` submodule. This chunk in the except
# clause is a copy-and-paste from traitlets 5.0.5.
try:
    from traitlets.utils.descriptions import describe
except ImportError:
    import inspect
    import re
    import types

    def describe(article, value, name=None, verbose=False, capital=False):
        """Return string that describes a value
        Parameters
        ----------
        article : str or None
            A definite or indefinite article. If the article is
            indefinite (i.e. "a" or "an") the appropriate one
            will be infered. Thus, the arguments of ``describe``
            can themselves represent what the resulting string
            will actually look like. If None, then no article
            will be prepended to the result. For non-articled
            description, values that are instances are treated
            definitely, while classes are handled indefinitely.
        value : any
            The value which will be named.
        name : str or None (default: None)
            Only applies when ``article`` is "the" - this
            ``name`` is a definite reference to the value.
            By default one will be infered from the value's
            type and repr methods.
        verbose : bool (default: False)
            Whether the name should be concise or verbose. When
            possible, verbose names include the module, and/or
            class name where an object was defined.
        capital : bool (default: False)
            Whether the first letter of the article should
            be capitalized or not. By default it is not.
        Examples
        --------
        Indefinite description:
        >>> describe("a", object())
        'an object'
        >>> describe("a", object)
        'an object'
        >>> describe("a", type(object))
        'a type'
        Definite description:
        >>> describe("the", object())
        "the object at '0x10741f1b0'"
        >>> describe("the", object)
        "the type 'object'"
        >>> describe("the", type(object))
        "the type 'type'"
        Definitely named description:
        >>> describe("the", object(), "I made")
        'the object I made'
        >>> describe("the", object, "I will use")
        'the object I will use'
        """
        if isinstance(article, str):
            article = article.lower()

        if not inspect.isclass(value):
            typename = type(value).__name__
        else:
            typename = value.__name__
        if verbose:
            typename = _prefix(value) + typename

        if article == "the" or (article is None and not inspect.isclass(value)):
            if name is not None:
                result = f"{typename} {name}"
                if article is not None:
                    return add_article(result, True, capital)
                else:
                    return result
            else:
                tick_wrap = False
                if inspect.isclass(value):
                    name = value.__name__
                elif isinstance(value, types.FunctionType):
                    name = value.__name__
                    tick_wrap = True
                elif isinstance(value, types.MethodType):
                    name = value.__func__.__name__
                    tick_wrap = True
                elif type(value).__repr__ in (object.__repr__, type.__repr__):
                    name = f"at '{id(value):x}'"
                    verbose = False
                else:
                    name = repr(value)
                    verbose = False
                if verbose:
                    name = _prefix(value) + name
                if tick_wrap:
                    name = name.join("''")
                return describe(article, value, name=name,
                    verbose=verbose, capital=capital)
        elif article in ("a", "an") or article is None:
            if article is None:
                return typename
            return add_article(typename, False, capital)
        else:
            raise ValueError(
                f"The 'article' argument should be 'the', 'a', 'an', or None not {article!r}"
            )


    def add_article(name, definite=False, capital=False):
        """Returns the string with a prepended article.
        The input does not need to begin with a charater.
        Parameters
        ----------
        definite : bool (default: False)
            Whether the article is definite or not.
            Indefinite articles being 'a' and 'an',
            while 'the' is definite.
        capital : bool (default: False)
            Whether the added article should have
            its first letter capitalized or not.
        """
        if definite:
            result = "the " + name
        else:
            first_letters = re.compile(r'[\W_]+').sub('', name)
            if first_letters[:1].lower() in 'aeiou':
                result = 'an ' + name
            else:
                result = 'a ' + name
        if capital:
            return result[0].upper() + result[1:]
        else:
            return result


class TypeFromClasses(ClassBasedTraitType):
    """A trait whose value must be a subclass of a class in a specified list of classes."""

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
                    f"The '{self.name}' trait of {obj} instance must be a type, "
                    f"but {value!r} could not be imported"
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
                klass = klass.__module__ + '.' + klass.__name__
            result += f"{klass} or "
        # Strip the last "or"
        result = result.strip(" or ")
        if self.allow_none:
            return result + ' or None'
        return result

    def instance_init(self, obj):
        self._resolve_classes()
        super().instance_init(obj)

    def _resolve_classes(self):
        # Resolve all string names to actual classes.
        self.importable_klasses = []
        for klass in self.klasses:
            if isinstance(klass, str):
                try:
                    klass = self._resolve_string(klass)
                    self.importable_klasses.append(klass)
                except:
                    warn(f"{klass} is not importable. Is it installed?", ImportWarning)
            else:
                self.importable_klasses.append(klass)

        if isinstance(self.default_value, str):
            self.default_value = self._resolve_string(self.default_value)

    def default_value_repr(self):
        value = self.default_value
        if isinstance(value, str):
            return repr(value)
        else:
            return repr(f'{value.__module__}.{value.__name__}')


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
                f'The klasses attribute must be a list of class names or classes not: {klass!r}'
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
        for klass in self.klasses:
            if isinstance(klass, str):
                result += klass
            else:
                result += describe("a", klass)
            result += " or "
        result = result.strip(" or ")
        if self.allow_none:
            result += ' or None'
        return result

    def instance_init(self, obj):
        self._resolve_classes()
        super().instance_init(obj)

    def _resolve_classes(self):
        # Resolve all string names to actual classes.
        self.importable_klasses = []
        for klass in self.klasses:
            if isinstance(klass, str):
                try:
                    klass = self._resolve_string(klass)
                    self.importable_klasses.append(klass)
                except:
                    warn(f"{klass} is not importable. Is it installed?", ImportWarning)
            else:
                self.importable_klasses.append(klass)

    def make_dynamic_default(self):
        if (self.default_args is None) and (self.default_kwargs is None):
            return None
        return self.klass(*(self.default_args or ()),
                          **(self.default_kwargs or {}))

    def default_value_repr(self):
        return repr(self.make_dynamic_default())

    def from_string(self, s):
        return _safe_literal_eval(s)
