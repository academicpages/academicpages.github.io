"""Implementation of configuration-related magic functions.
"""
#-----------------------------------------------------------------------------
#  Copyright (c) 2012 The IPython Development Team.
#
#  Distributed under the terms of the Modified BSD License.
#
#  The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Stdlib
import re

# Our own packages
from IPython.core.error import UsageError
from IPython.core.magic import Magics, magics_class, line_magic
from logging import error

#-----------------------------------------------------------------------------
# Magic implementation classes
#-----------------------------------------------------------------------------

reg = re.compile(r'^\w+\.\w+$')
@magics_class
class ConfigMagics(Magics):

    def __init__(self, shell):
        super(ConfigMagics, self).__init__(shell)
        self.configurables = []

    @line_magic
    def config(self, s):
        """configure IPython

            %config Class[.trait=value]

        This magic exposes most of the IPython config system. Any
        Configurable class should be able to be configured with the simple
        line::

            %config Class.trait=value

        Where `value` will be resolved in the user's namespace, if it is an
        expression or variable name.

        Examples
        --------

        To see what classes are available for config, pass no arguments::

            In [1]: %config
            Available objects for config:
                AliasManager
                DisplayFormatter
                HistoryManager
                IPCompleter
                LoggingMagics
                MagicsManager
                OSMagics
                PrefilterManager
                ScriptMagics
                TerminalInteractiveShell

        To view what is configurable on a given class, just pass the class
        name::

            In [2]: %config IPCompleter
            IPCompleter(Completer) options
            ----------------------------
            IPCompleter.backslash_combining_completions=<Bool>
                Enable unicode completions, e.g. \\alpha<tab> . Includes completion of latex
                commands, unicode names, and expanding unicode characters back to latex
                commands.
                Current: True
            IPCompleter.debug=<Bool>
                Enable debug for the Completer. Mostly print extra information for
                experimental jedi integration.
                Current: False
            IPCompleter.disable_matchers=<list-item-1>...
                List of matchers to disable.
                        The list should contain matcher identifiers (see
                :any:`completion_matcher`).
                Current: []
            IPCompleter.greedy=<Bool>
                Activate greedy completion
                        PENDING DEPRECATION. this is now mostly taken care of with Jedi.
                        This will enable completion on elements of lists, results of function calls, etc.,
                        but can be unsafe because the code is actually evaluated on TAB.
                Current: False
            IPCompleter.jedi_compute_type_timeout=<Int>
                Experimental: restrict time (in milliseconds) during which Jedi can compute types.
                        Set to 0 to stop computing types. Non-zero value lower than 100ms may hurt
                        performance by preventing jedi to build its cache.
                Current: 400
            IPCompleter.limit_to__all__=<Bool>
                DEPRECATED as of version 5.0.
                Instruct the completer to use __all__ for the completion
                Specifically, when completing on ``object.<tab>``.
                When True: only those names in obj.__all__ will be included.
                When False [default]: the __all__ attribute is ignored
                Current: False
            IPCompleter.merge_completions=<Bool>
                Whether to merge completion results into a single list
                        If False, only the completion results from the first non-empty
                        completer will be returned.
                        As of version 8.6.0, setting the value to ``False`` is an alias for:
                        ``IPCompleter.suppress_competing_matchers = True.``.
                Current: True
            IPCompleter.omit__names=<Enum>
                Instruct the completer to omit private method names
                        Specifically, when completing on ``object.<tab>``.
                        When 2 [default]: all names that start with '_' will be excluded.
                        When 1: all 'magic' names (``__foo__``) will be excluded.
                        When 0: nothing will be excluded.
                Choices: any of [0, 1, 2]
                Current: 2
            IPCompleter.profile_completions=<Bool>
                If True, emit profiling data for completion subsystem using cProfile.
                Current: False
            IPCompleter.profiler_output_dir=<Unicode>
                Template for path at which to output profile data for completions.
                Current: '.completion_profiles'
            IPCompleter.suppress_competing_matchers=<Union>
                Whether to suppress completions from other *Matchers*.
                When set to ``None`` (default) the matchers will attempt to auto-detect
                whether suppression of other matchers is desirable. For example, at the
                beginning of a line followed by `%` we expect a magic completion to be the
                only applicable option, and after ``my_dict['`` we usually expect a
                completion with an existing dictionary key.
                If you want to disable this heuristic and see completions from all matchers,
                set ``IPCompleter.suppress_competing_matchers = False``. To disable the
                heuristic for specific matchers provide a dictionary mapping:
                ``IPCompleter.suppress_competing_matchers = {'IPCompleter.dict_key_matcher':
                False}``.
                Set ``IPCompleter.suppress_competing_matchers = True`` to limit completions
                to the set of matchers with the highest priority; this is equivalent to
                ``IPCompleter.merge_completions`` and can be beneficial for performance, but
                will sometimes omit relevant candidates from matchers further down the
                priority list.
                Current: None
            IPCompleter.use_jedi=<Bool>
                Experimental: Use Jedi to generate autocompletions. Default to True if jedi
                is installed.
                Current: True

        but the real use is in setting values::

            In [3]: %config IPCompleter.greedy = True

        and these values are read from the user_ns if they are variables::

            In [4]: feeling_greedy=False

            In [5]: %config IPCompleter.greedy = feeling_greedy

        """
        from traitlets.config.loader import Config
        # some IPython objects are Configurable, but do not yet have
        # any configurable traits.  Exclude them from the effects of
        # this magic, as their presence is just noise:
        configurables = sorted(set([ c for c in self.shell.configurables
                                     if c.__class__.class_traits(config=True)
                                     ]), key=lambda x: x.__class__.__name__)
        classnames = [ c.__class__.__name__ for c in configurables ]

        line = s.strip()
        if not line:
            # print available configurable names
            print("Available objects for config:")
            for name in classnames:
                print("   ", name)
            return
        elif line in classnames:
            # `%config TerminalInteractiveShell` will print trait info for
            # TerminalInteractiveShell
            c = configurables[classnames.index(line)]
            cls = c.__class__
            help = cls.class_get_help(c)
            # strip leading '--' from cl-args:
            help = re.sub(re.compile(r'^--', re.MULTILINE), '', help)
            print(help)
            return
        elif reg.match(line):
            cls, attr = line.split('.')
            return getattr(configurables[classnames.index(cls)],attr)
        elif '=' not in line:
            msg = "Invalid config statement: %r, "\
                  "should be `Class.trait = value`."
            
            ll = line.lower()
            for classname in classnames:
                if ll == classname.lower():
                    msg = msg + '\nDid you mean %s (note the case)?' % classname
                    break

            raise UsageError( msg % line)

        # otherwise, assume we are setting configurables.
        # leave quotes on args when splitting, because we want
        # unquoted args to eval in user_ns
        cfg = Config()
        exec("cfg."+line, self.shell.user_ns, locals())

        for configurable in configurables:
            try:
                configurable.update_config(cfg)
            except Exception as e:
                error(e)
