# Zeitwerk



[![Gem Version](https://img.shields.io/gem/v/zeitwerk.svg?style=for-the-badge)](https://rubygems.org/gems/zeitwerk)
[![Build Status](https://img.shields.io/travis/com/fxn/zeitwerk/master?style=for-the-badge)](https://travis-ci.com/fxn/zeitwerk)

<!-- TOC -->

- [Introduction](#introduction)
- [Synopsis](#synopsis)
- [File structure](#file-structure)
    - [Implicit namespaces](#implicit-namespaces)
    - [Explicit namespaces](#explicit-namespaces)
    - [Collapsing directories](#collapsing-directories)
    - [Nested root directories](#nested-root-directories)
- [Usage](#usage)
    - [Setup](#setup)
        - [Generic](#generic)
        - [for_gem](#for_gem)
    - [Autoloading](#autoloading)
    - [Eager loading](#eager-loading)
    - [Reloading](#reloading)
    - [Inflection](#inflection)
        - [Zeitwerk::Inflector](#zeitwerkinflector)
        - [Zeitwerk::GemInflector](#zeitwerkgeminflector)
        - [Custom inflector](#custom-inflector)
    - [Logging](#logging)
        - [Loader tag](#loader-tag)
    - [Ignoring parts of the project](#ignoring-parts-of-the-project)
        - [Use case: Files that do not follow the conventions](#use-case-files-that-do-not-follow-the-conventions)
        - [Use case: The adapter pattern](#use-case-the-adapter-pattern)
        - [Use case: Test files mixed with implementation files](#use-case-test-files-mixed-with-implementation-files)
    - [Edge cases](#edge-cases)
    - [Reopening third-party namespaces](#reopening-third-party-namespaces)
    - [Rules of thumb](#rules-of-thumb)
    - [Debuggers](#debuggers)
        - [Break](#break)
        - [Byebug](#byebug)
- [Pronunciation](#pronunciation)
- [Supported Ruby versions](#supported-ruby-versions)
- [Testing](#testing)
- [Motivation](#motivation)
- [Thanks](#thanks)
- [License](#license)

<!-- /TOC -->

<a id="markdown-introduction" name="introduction"></a>
## Introduction

Zeitwerk is an efficient and thread-safe code loader for Ruby.

Given a [conventional file structure](#file-structure), Zeitwerk is able to load your project's classes and modules on demand (autoloading), or upfront (eager loading). You don't need to write `require` calls for your own files, rather, you can streamline your programming knowing that your classes and modules are available everywhere. This feature is efficient, thread-safe, and matches Ruby's semantics for constants.

Zeitwerk is also able to reload code, which may be handy while developing web applications. Coordination is needed to reload in a thread-safe manner. The documentation below explains how to do this.

The gem is designed so that any project, gem dependency, application, etc. can have their own independent loader, coexisting in the same process, managing their own project trees, and independent of each other. Each loader has its own configuration, inflector, and optional logger.

Internally, Zeitwerk issues `require` calls exclusively using absolute file names, so there are no costly file system lookups in `$LOAD_PATH`. Technically, the directories managed by Zeitwerk do not even need to be in `$LOAD_PATH`.

Furthermore, Zeitwerk does at most one single scan of the project tree, and it descends into subdirectories lazily, only if their namespaces are used.

<a id="markdown-synopsis" name="synopsis"></a>
## Synopsis

Main interface for gems:

```ruby
# lib/my_gem.rb (main file)

require "zeitwerk"
loader = Zeitwerk::Loader.for_gem
loader.setup # ready!

module MyGem
  # ...
end

loader.eager_load # optionally
```

Main generic interface:

```ruby
loader = Zeitwerk::Loader.new
loader.push_dir(...)
loader.setup # ready!
```

The `loader` variable can go out of scope. Zeitwerk keeps a registry with all of them, and so the object won't be garbage collected.

You can reload if you want to:

```ruby
loader = Zeitwerk::Loader.new
loader.push_dir(...)
loader.enable_reloading # you need to opt-in before setup
loader.setup
...
loader.reload
```

and you can eager load all the code:

```ruby
loader.eager_load
```

It is also possible to broadcast `eager_load` to all instances:

```ruby
Zeitwerk::Loader.eager_load_all
```

<a id="markdown-file-structure" name="file-structure"></a>
## File structure

To have a file structure Zeitwerk can work with, just name files and directories after the name of the classes and modules they define:

```
lib/my_gem.rb         -> MyGem
lib/my_gem/foo.rb     -> MyGem::Foo
lib/my_gem/bar_baz.rb -> MyGem::BarBaz
lib/my_gem/woo/zoo.rb -> MyGem::Woo::Zoo
```

Every directory configured with `push_dir` acts as root namespace. There can be several of them. For example, given

```ruby
loader.push_dir(Rails.root.join("app/models"))
loader.push_dir(Rails.root.join("app/controllers"))
```

Zeitwerk understands that their respective files and subdirectories belong to the root namespace:

```
app/models/user.rb                        -> User
app/controllers/admin/users_controller.rb -> Admin::UsersController
```

Alternatively, you can associate a custom namespace to a root directory by passing a class or module object in the optional `namespace` keyword argument.

For example, Active Job queue adapters have to define a constant after their name in `ActiveJob::QueueAdapters`.

So, if you declare

```ruby
require "active_job"
require "active_job/queue_adapters"
loader.push_dir("#{__dir__}/adapters", namespace: ActiveJob::QueueAdapters)
```

your adapter can be stored directly in that directory instead of the canonical `#{__dir__}/active_job/queue_adapters`.

Please, note that the given namespace must be non-reloadable, though autoloaded constants in that namespace can be. That is, if you associate `app/api` with an existing `Api` module, that module should not be reloadable. However, if the project defines and autoloads the class `Api::V2::Deliveries`, that one can be reloaded.

<a id="markdown-implicit-namespaces" name="implicit-namespaces"></a>
### Implicit namespaces

Directories without a matching Ruby file get modules autovivified automatically by Zeitwerk. For example, in

```
app/controllers/admin/users_controller.rb -> Admin::UsersController
```

`Admin` is autovivified as a module on demand, you do not need to define an `Admin` class or module in an `admin.rb` file explicitly.

<a id="markdown-explicit-namespaces" name="explicit-namespaces"></a>
### Explicit namespaces

Classes and modules that act as namespaces can also be explicitly defined, though. For instance, consider

```
app/models/hotel.rb         -> Hotel
app/models/hotel/pricing.rb -> Hotel::Pricing
```

There, `app/models/hotel.rb` defines `Hotel`, and thus Zeitwerk does not autovivify a module.

The classes and modules from the namespace are already available in the body of the class or module defining it:

```ruby
class Hotel < ApplicationRecord
  include Pricing # works
  ...
end
```

An explicit namespace must be managed by one single loader. Loaders that reopen namespaces owned by other projects are responsible for loading their constants before setup.

<a id="markdown-collapsing-directories" name="collapsing-directories"></a>
### Collapsing directories

Say some directories in a project exist for organizational purposes only, and you prefer not to have them as namespaces. For example, the `actions` subdirectory in the next example is not meant to represent a namespace, it is there only to group all actions related to bookings:

```
booking.rb                -> Booking
booking/actions/create.rb -> Booking::Create
```

To make it work that way, configure Zeitwerk to collapse said directory:

```ruby
loader.collapse("#{__dir__}/booking/actions")
```

This method accepts an arbitrary number of strings or `Pathname` objects, and also an array of them.

You can pass directories and glob patterns. Glob patterns are expanded when they are added, and again on each reload.

To illustrate usage of glob patterns, if `actions` in the example above is part of a standardized structure, you could use a wildcard:

```ruby
loader.collapse("#{__dir__}/*/actions")
```

<a id="markdown-nested-root-directories" name="nested-root-directories"></a>
### Nested root directories

Root directories should not be ideally nested, but Zeitwerk supports them because in Rails, for example, both `app/models` and `app/models/concerns` belong to the autoload paths.

Zeitwerk detects nested root directories, and treats them as roots only. In the example above, `concerns` is not considered to be a namespace below `app/models`. For example, the file:

```
app/models/concerns/geolocatable.rb
```

should define `Geolocatable`, not `Concerns::Geolocatable`.

<a id="markdown-usage" name="usage"></a>
## Usage

<a id="markdown-setup" name="setup"></a>
### Setup

<a id="markdown-generic" name="generic"></a>
#### Generic

Loaders are ready to load code right after calling `setup` on them:

```ruby
loader.setup
```

This method is synchronized and idempotent.

Customization should generally be done before that call. In particular, in the generic interface you may set the root directories from which you want to load files:

```ruby
loader.push_dir(...)
loader.push_dir(...)
loader.setup
```

<a id="markdown-for_gem" name="for_gem"></a>
#### for_gem

`Zeitwerk::Loader.for_gem` is a convenience shortcut for the common case in which a gem has its entry point directly under the `lib` directory:

```
lib/my_gem.rb         # MyGem
lib/my_gem/version.rb # MyGem::VERSION
lib/my_gem/foo.rb     # MyGem::Foo
```

Neither a gemspec nor a version file are technically required, this helper works as long as the code is organized using that standard structure.

If the entry point of your gem lives in a subdirectory of `lib` because it is reopening a namespace defined somewhere else, please use the generic API to setup the loader, and make sure you check the section [_Reopening third-party namespaces_](https://github.com/fxn/zeitwerk#reopening-third-party-namespaces) down below.

Conceptually, `for_gem` translates to:

```ruby
# lib/my_gem.rb

require "zeitwerk"
loader = Zeitwerk::Loader.new
loader.tag = File.basename(__FILE__, ".rb")
loader.inflector = Zeitwerk::GemInflector.new(__FILE__)
loader.push_dir(__dir__)
```

except that this method returns the same object in subsequent calls from the same file, in the unlikely case the gem wants to be able to reload.

If the main module references project constants at the top-level, Zeitwerk has to be ready to load them. Their definitions, in turn, may reference other project constants. And this is recursive. Therefore, it is important that the `setup` call happens above the main module definition:

```ruby
# lib/my_gem.rb (main file)

require "zeitwerk"
loader = Zeitwerk::Loader.for_gem
loader.setup

module MyGem
  # Since the setup has been performed, at this point we are already able
  # to reference project constants, in this case MyGem::MyLogger.
  include MyLogger
end
```

<a id="markdown-autoloading" name="autoloading"></a>
### Autoloading

After `setup`, you are able to reference classes and modules from the project without issuing `require` calls for them. They are all available everywhere, autoloading loads them on demand. This works even if the reference to the class or module is first hit in client code, outside your project.

Let's revisit the example above:

```ruby
# lib/my_gem.rb (main file)

require "zeitwerk"
loader = Zeitwerk::Loader.for_gem
loader.setup

module MyGem
  include MyLogger # (*)
end
```

That works, and there is no `require "my_gem/my_logger"`. When `(*)` is reached, Zeitwerk seamlessly autoloads `MyGem::MyLogger`.

If autoloading a file does not define the expected class or module, Zeitwerk raises `Zeitwerk::NameError`, which is a subclass of `NameError`.

<a id="markdown-eager-loading" name="eager-loading"></a>
### Eager loading

Zeitwerk instances are able to eager load their managed files:

```ruby
loader.eager_load
```

That skips [ignored files and directories](#ignoring-parts-of-the-project), and you can also tell Zeitwerk that certain files or directories are autoloadable, but should not be eager loaded:

```ruby
db_adapters = "#{__dir__}/my_gem/db_adapters"
loader.do_not_eager_load(db_adapters)
loader.setup
loader.eager_load # won't eager load the database adapters
```

In gems, the method needs to be invoked after the main namespace has been defined, as shown in [Synopsis](https://github.com/fxn/zeitwerk#synopsis).

Eager loading is synchronized and idempotent.

If eager loading a file does not define the expected class or module, Zeitwerk raises `Zeitwerk::NameError`, which is a subclass of `NameError`.

If you want to eager load yourself and all dependencies using Zeitwerk, you can broadcast the `eager_load` call to all instances:

```ruby
Zeitwerk::Loader.eager_load_all
```

This may be handy in top-level services, like web applications.

Note that thanks to idempotence `Zeitwerk::Loader.eager_load_all` won't eager load twice if any of the instances already eager loaded.

<a id="markdown-reloading" name="reloading"></a>
### Reloading

Zeitwerk is able to reload code, but you need to enable this feature:

```ruby
loader = Zeitwerk::Loader.new
loader.push_dir(...)
loader.enable_reloading # you need to opt-in before setup
loader.setup
...
loader.reload
```

There is no way to undo this, either you want to reload or you don't.

Enabling reloading after setup raises `Zeitwerk::Error`. Attempting to reload without having it enabled raises `Zeitwerk::ReloadingDisabledError`.

Generally speaking, reloading is useful while developing running services like web applications. Gems that implement regular libraries, so to speak, or services running in testing or production environments, won't normally have a use case for reloading. If reloading is not enabled, Zeitwerk is able to use less memory.

Reloading removes the currently loaded classes and modules and resets the loader so that it will pick whatever is in the file system now.

It is important to highlight that this is an instance method. Don't worry about project dependencies managed by Zeitwerk, their loaders are independent.

In order for reloading to be thread-safe, you need to implement some coordination. For example, a web framework that serves each request with its own thread may have a globally accessible RW lock. When a request comes in, the framework acquires the lock for reading at the beginning, and the code in the framework that calls `loader.reload` needs to acquire the lock for writing.

On reloading, client code has to update anything that would otherwise be storing a stale object. For example, if the routing layer of a web framework stores controller class objects or instances in internal structures, on reload it has to refresh them somehow, possibly reevaluating routes.

<a id="markdown-inflection" name="inflection"></a>
### Inflection

Each individual loader needs an inflector to figure out which constant path would a given file or directory map to. Zeitwerk ships with two basic inflectors.

<a id="markdown-zeitwerkinflector" name="zeitwerkinflector"></a>
#### Zeitwerk::Inflector

This is a very basic inflector that converts snake case to camel case:

```
user             -> User
users_controller -> UsersController
html_parser      -> HtmlParser
```

The camelize logic can be overridden easily for individual basenames:

```ruby
loader.inflector.inflect(
  "html_parser"   => "HTMLParser",
  "mysql_adapter" => "MySQLAdapter"
)
```

The `inflect` method can be invoked several times if you prefer this other style:

```ruby
loader.inflector.inflect "html_parser" => "HTMLParser"
loader.inflector.inflect "mysql_adapter" => "MySQLAdapter"
```

Overrides need to be configured before calling `setup`.

There are no inflection rules or global configuration that can affect this inflector. It is deterministic.

Loaders instantiated with `Zeitwerk::Loader.new` have an inflector of this type, independent of each other.

<a id="markdown-zeitwerkgeminflector" name="zeitwerkgeminflector"></a>
#### Zeitwerk::GemInflector

This inflector is like the basic one, except it expects `lib/my_gem/version.rb` to define `MyGem::VERSION`.

Loaders instantiated with `Zeitwerk::Loader.for_gem` have an inflector of this type, independent of each other.

<a id="markdown-custom-inflector" name="custom-inflector"></a>
#### Custom inflector

The inflectors that ship with Zeitwerk are deterministic and simple. But you can configure your own:

```ruby
# frozen_string_literal: true

class MyInflector < Zeitwerk::Inflector
  def camelize(basename, abspath)
    if basename =~ /\Ahtml_(.*)/
      "HTML" + super($1, abspath)
    else
      super
    end
  end
end
```

The first argument, `basename`, is a string with the basename of the file or directory to be inflected. In the case of a file, without extension. In the case of a directory, without trailing slash. The inflector needs to return this basename inflected. Therefore, a simple constant name without colons.

The second argument, `abspath`, is a string with the absolute path to the file or directory in case you need it to decide how to inflect the basename. Paths to directories don't have trailing slashes.

Then, assign the inflector:

```ruby
loader.inflector = MyInflector.new
```

This needs to be done before calling `setup`.

If a custom inflector definition in a gem takes too much space in the main file, you can extract it. For example, this is a simple pattern:

```ruby
# lib/my_gem/inflector.rb
module MyGem
  class Inflector < Zeitwerk::GemInflector
    ...
  end
end

# lib/my_gem.rb
require "zeitwerk"
require_relative "my_gem/inflector"

loader = Zeitwerk::Loader.for_gem
loader.inflector = MyGem::Inflector.new(__FILE__)
loader.setup

module MyGem
  # ...
end
```

Since `MyGem` is referenced before the namespace is defined in the main file, it is important to use this style:

```ruby
# Correct, effectively defines MyGem.
module MyGem
  class Inflector < Zeitwerk::GemInflector
    # ...
  end
end
```

instead of:

```ruby
# Raises uninitialized constant MyGem (NameError).
class MyGem::Inflector < Zeitwerk::GemInflector
  # ...
end
```

<a id="markdown-logging" name="logging"></a>
### Logging

Zeitwerk is silent by default, but you can ask loaders to trace their activity. Logging is meant just for troubleshooting, shouldn't normally be enabled.

The `log!` method is a quick shortcut to let the loader log to `$stdout`:

```
loader.log!
```

If you want more control, a logger can be configured as a callable

```ruby
loader.logger = method(:puts)
loader.logger = ->(msg) { ... }
```

as well as anything that responds to `debug`:

```ruby
loader.logger = Logger.new($stderr)
loader.logger = Rails.logger
```

In both cases, the corresponding methods are going to be passed exactly one argument with the message to be logged.

It is also possible to set a global default this way:

```ruby
Zeitwerk::Loader.default_logger = method(:puts)
```

If there is a logger configured, you'll see traces when autoloads are set, files loaded, and modules autovivified. While reloading, removed autoloads and unloaded objects are also traced.

As a curiosity, if your project has namespaces you'll notice in the traces Zeitwerk sets autoloads for _directories_. That's a technique used to be able to descend into subdirectories on demand, avoiding that way unnecessary tree walks.

<a id="markdown-loader-tag" name="loader-tag"></a>
#### Loader tag

Loaders have a tag that is printed in traces in order to be able to distinguish them in globally logged activity:

```
Zeitwerk@9fa54b: autoload set for User, to be loaded from ...
```

By default, a random tag like the one above is assigned, but you can change it:

```
loader.tag = "grep_me"
```

The tag of a loader returned by `for_gem` is the basename of the root file without extension:

```
Zeitwerk@my_gem: constant MyGem::Foo loaded from ...
```

<a id="markdown-ignoring-parts-of-the-project" name="ignoring-parts-of-the-project"></a>
### Ignoring parts of the project

Zeitwerk ignores automatically any file or directory whose name starts with a dot, and any files that do not have extension ".rb".

However, sometimes it might still be convenient to tell Zeitwerk to completely ignore some particular Ruby file or directory. That is possible with `ignore`, which accepts an arbitrary number of strings or `Pathname` objects, and also an array of them.

You can ignore file names, directory names, and glob patterns. Glob patterns are expanded when they are added and again on each reload.

Let's see some use cases.

<a id="markdown-use-case-files-that-do-not-follow-the-conventions" name="use-case-files-that-do-not-follow-the-conventions"></a>
#### Use case: Files that do not follow the conventions

Let's suppose that your gem decorates something in `Kernel`:

```ruby
# lib/my_gem/core_ext/kernel.rb

Kernel.module_eval do
  # ...
end
```

That file does not define a constant path after the path name and you need to tell Zeitwerk:

```ruby
kernel_ext = "#{__dir__}/my_gem/core_ext/kernel.rb"
loader.ignore(kernel_ext)
loader.setup
```

You can also ignore the whole directory:

```ruby
core_ext = "#{__dir__}/my_gem/core_ext"
loader.ignore(core_ext)
loader.setup
```

<a id="markdown-use-case-the-adapter-pattern" name="use-case-the-adapter-pattern"></a>
#### Use case: The adapter pattern

Another use case for ignoring files is the adapter pattern.

Let's imagine your project talks to databases, supports several, and has adapters for each one of them. Those adapters may have top-level `require` calls that load their respective drivers:

```ruby
# my_gem/db_adapters/postgresql.rb
require "pg"
```

but you don't want your users to install them all, only the one they are going to use.

On the other hand, if your code is eager loaded by you or a parent project (with `Zeitwerk::Loader.eager_load_all`), those `require` calls are going to be executed. Ignoring the adapters prevents that:

```ruby
db_adapters = "#{__dir__}/my_gem/db_adapters"
loader.ignore(db_adapters)
loader.setup
```

The chosen adapter, then, has to be loaded by hand somehow:

```ruby
require "my_gem/db_adapters/#{config[:db_adapter]}"
```

Note that since the directory is ignored, the required adapter can instantiate another loader to manage its subtree, if desired. Such loader would coexist with the main one just fine.

<a id="markdown-use-case-test-files-mixed-with-implementation-files" name="use-case-test-files-mixed-with-implementation-files"></a>
#### Use case: Test files mixed with implementation files

There are project layouts that put implementation files and test files together. To ignore the test files, you can use a glob pattern like this:

```ruby
tests = "#{__dir__}/**/*_test.rb"
loader.ignore(tests)
loader.setup
```

<a id="markdown-edge-cases" name="edge-cases"></a>
### Edge cases

A class or module that acts as a namespace:

```ruby
# trip.rb
class Trip
  include Geolocation
end

# trip/geolocation.rb
module Trip::Geolocation
  ...
end
```

has to be defined with the `class` or `module` keywords, as in the example above.

For technical reasons, raw constant assignment is not supported:

```ruby
# trip.rb
Trip = Class.new { ... }  # NOT SUPPORTED
Trip = Struct.new { ... } # NOT SUPPORTED
```

This only affects explicit namespaces, those idioms work well for any other ordinary class or module.

<a id="markdown-reopening-third-party-namespaces" name="reopening-third-party-namespaces"></a>
### Reopening third-party namespaces

Projects managed by Zeitwerk can work with namespaces defined by third-party libraries. However, they have to be loaded in memory before calling `setup`.

For example, let's imagine you're writing a gem that implements an adapter for [Active Job](https://guides.rubyonrails.org/active_job_basics.html) that uses AwesomeQueue as backend. By convention, your gem has to define a class called `ActiveJob::QueueAdapters::AwesomeQueue`, and it has to do so in a file with a matching path:

```ruby
# lib/active_job/queue_adapters/awesome_queue.rb
module ActiveJob
  module QueueAdapters
    class AwesomeQueue
      # ...
    end
  end
end
```

It is very important that your gem _reopens_ the modules `ActiveJob` and `ActiveJob::QueueAdapters` instead of _defining_ them. Because their proper definition lives in Active Job. Furthermore, if the project reloads, you do not want any of `ActiveJob` or `ActiveJob::QueueAdapters` to be reloaded.

Bottom line, Zeitwerk should not be managing those namespaces. Active Job owns them and defines them. Your gem needs to _reopen_ them.

In order to do so, you need to make sure those modules are loaded before calling `setup`. For instance, in the entry file for the gem:

```ruby
# Ensure these namespaces are reopened, not defined.
require "active_job"
require "active_job/queue_adapters"

require "zeitwerk"
loader = Zeitwerk::Loader.for_gem
loader.setup
```

With that, when Zeitwerk scans the file system and reaches the gem directories `lib/active_job` and `lib/active_job/queue_adapters`, it detects the corresponding modules already exist and therefore understands it does not have to manage them. The loader just descends into those directories. Eventually will reach `lib/active_job/queue_adapters/awesome_queue.rb`, and since `ActiveJob::QueueAdapters::AwesomeQueue` is unknown, Zeitwerk will manage it. Which is what happens regularly with the files in your gem. On reload, the namespaces are safe, won't be reloaded. The loader only reloads what it manages, which in this case is the adapter itself.

<a id="markdown-rules-of-thumb" name="rules-of-thumb"></a>
### Rules of thumb

1. Different loaders should manage different directory trees. It is an error condition to configure overlapping root directories in different loaders.

2. Think the mere existence of a file is effectively like writing a `require` call for them, which is executed on demand (autoload) or upfront (eager load).

3. In that line, if two loaders manage files that translate to the same constant in the same namespace, the first one wins, the rest are ignored. Similar to what happens with `require` and `$LOAD_PATH`, only the first occurrence matters.

4. Projects that reopen a namespace defined by some dependency have to ensure said namespace is loaded before setup. That is, the project has to make sure it reopens, rather than define. This is often accomplished just loading the dependency.

5. Objects stored in reloadable constants should not be cached in places that are not reloaded. For example, non-reloadable classes should not subclass a reloadable class, or mixin a reloadable module. Otherwise, after reloading, those classes or module objects would become stale. Referring to constants in dynamic places like method calls or lambdas is fine.

6. In a given process, ideally, there should be at most one loader with reloading enabled. Technically, you can have more, but it may get tricky if one refers to constants managed by the other one. Do that only if you know what you are doing.

<a id="markdown-debuggers" name="debuggers"></a>
### Debuggers

<a id="markdown-break" name="break"></a>
#### Break

Zeitwerk works fine with [@gsamokovarov](https://github.com/gsamokovarov)'s [Break](https://github.com/gsamokovarov/break) debugger.

<a id="markdown-byebug" name="byebug"></a>
#### Byebug

Zeitwerk and [Byebug](https://github.com/deivid-rodriguez/byebug) are incompatible, classes or modules that belong to [explicit namespaces](#explicit-namespaces) are not autoloaded inside a Byebug session. See [this issue](https://github.com/deivid-rodriguez/byebug/issues/564#issuecomment-499413606) for further details.

<a id="markdown-pronunciation" name="pronunciation"></a>
## Pronunciation

"Zeitwerk" is pronounced [this way](http://share.hashref.com/zeitwerk/zeitwerk_pronunciation.mp3).

<a id="markdown-supported-ruby-versions" name="supported-ruby-versions"></a>
## Supported Ruby versions

Zeitwerk works with MRI 2.4.4 and above.

<a id="markdown-testing" name="testing"></a>
## Testing

In order to run the test suite of Zeitwerk, `cd` into the project root and execute

```
bin/test
```

To run one particular suite, pass its file name as an argument:

```
bin/test test/lib/zeitwerk/test_eager_load.rb
```

Furthermore, the project has a development dependency on [`minitest-focus`](https://github.com/seattlerb/minitest-focus). To run an individual test mark it with `focus`:

```ruby
focus
test "capitalizes the first letter" do
  assert_equal "User", camelize("user")
end
```

and run `bin/test`.

<a id="markdown-motivation" name="motivation"></a>
## Motivation

Since `require` has global side-effects, and there is no static way to verify that you have issued the `require` calls for code that your file depends on, in practice it is very easy to forget some. That introduces bugs that depend on the load order. Zeitwerk provides a way to forget about `require` in your own code, just name things following conventions and done.

On the other hand, autoloading in Rails is based on `const_missing`, which lacks fundamental information like the nesting and the resolution algorithm that was being used. Because of that, Rails autoloading is not able to match Ruby's semantics and that introduces a series of gotchas. The original goal of this project was to bring a better autoloading mechanism for Rails 6.

<a id="markdown-thanks" name="thanks"></a>
## Thanks

I'd like to thank [@matthewd](https://github.com/matthewd) for the discussions we've had about this topic in the past years, I learned a couple of tricks used in Zeitwerk from him.

Also, would like to thank [@Shopify](https://github.com/Shopify), [@rafaelfranca](https://github.com/rafaelfranca), and [@dylanahsmith](https://github.com/dylanahsmith), for sharing [this PoC](https://github.com/Shopify/autoload_reloader). The technique Zeitwerk uses to support explicit namespaces was copied from that project.

Jean Boussier ([@casperisfine](https://github.com/casperisfine), [@byroot](https://github.com/byroot)) deserves special mention. Jean migrated autoloading in Shopify when Zeitwerk integration in Rails was yet unreleased. His work and positive attitude have been outstanding, and thanks to his feedback the interface and performance of Zeitwerk are way, way better. Kudos man ❤️.

Finally, many thanks to [@schurig](https://github.com/schurig) for recording an [audio file](http://share.hashref.com/zeitwerk/zeitwerk_pronunciation.mp3) with the pronunciation of "Zeitwerk" in perfect German. 💯

<a id="markdown-license" name="license"></a>
## License

Released under the MIT License, Copyright (c) 2019–<i>ω</i> Xavier Noria.
