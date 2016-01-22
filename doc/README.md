micronota documentation
=======================

This guide contains instructions for building the micronota documentation, as
well as guidelines for contributing to the documentation.

Building the documentation
--------------------------

To build the documentation, you'll need the following Python packages
installed:

- [Sphinx](http://sphinx-doc.org/) == 1.3.3

It may work on lower verions of Sphinx but it has not been tested.
Sphinx v1.3.3 supports both google-style and numpydoc-style docstrings
with the builtin napoleon extension.

An easy way to install the dependencies is via pip or conda:

    pip install sphinx==1.3.3
    conda install sphinx==1.3.3

Finally, you will need to install micronota.

**Important:** The documentation will be built for whatever version of
micronota is *currently installed* on your system (i.e., the version imported
by ```import skbio```). This may not match the code located in this repository.
You will need to either install this version of micronota somewhere (e.g., in
a virtualenv) or point your ```PYTHONPATH``` environment variable to this code,
*before* building the documentation.

To build the documentation, assuming you are at the top-level micronota
directory:

    make -C doc clean html

The built HTML documentation will be at ```doc/_build/html/index.html```.

Contributing to the documentation
---------------------------------

If you would like to contribute to the documentation, whether by adding
something entirely new or by modifying existing documentation, please first
review our [micronota contribution guide](../CONTRIBUTING.md).

Before submitting your changes, ensure that the documentation builds without
errors or warnings.

### Documentation guidelines

Most of micronota's API documentation is automatically generated from
[docstrings](http://legacy.python.org/dev/peps/pep-0257/#what-is-a-docstring).
The advantage to this approach is that users can access the documentation in an
interactive Python session or from our website as HTML. Other output formats
are also possible, such as PDF.

micronota docstrings follow the [numpydoc conventions](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt).
This ensures that the docstrings are easily readable both from the interpreter
and HTML, PDF, etc. Please read the numpydoc guidelines before continuing.

### Documenting a module in micronota

In addition to following the numpydoc conventions for docstrings, we have a few
more conventions that will ensure your documentation is correctly built and
linked within our website, and that it maintains consistency with the rest of
the micronota docs.

The easiest way to get started with documenting your code is to look at the
docstrings in existing micronota modules, such as ```micronota.bfillings```.
We've structured our docs in a similar way to
[SciPy's documentation](http://docs.scipy.org/doc/scipy/reference/) and
[scikit-bio](https://github.com/biocore/scikit-bio), so that
may be another good place to look for examples.

We'll take a top-down approach by discussing how to document a new module that
you'd like to add to micronota (let's call it ```micronota/example.py```).

#### Module docstring

The first thing you'll need to add is a docstring for the module. The docstring
must start at the first line of the file. It should start with a title for the
module:

    """
    Documentation examples
    ======================

Make sure that the title underline is the same length as the title.

We also need to include another Sphinx directive below this:

    .. currentmodule:: micronota.example

This directive tells Sphinx that other classes, functions, etc. that we will
reference are located in the ```micronota.example``` module.

Next, include a more detailed description of the module. For example:

    This module (:mod:`micronota.example`) consists of several
    example classes and functions to illustrate the micronota
    documentation system.

Following that, list any classes, functions, and exceptions that you'd like
documentation generated for. Note that you do *not* need to include every
single class, function, or exception that is defined in the module. Also, you
do not need to list class methods, as those will be automatically included in
the generated class documentation. Only include objects that should be exposed
as part of the public API.

For example:

    Classes
    -------

    .. autosummary::
       :toctree: _autosummary/

       ExampleClass1
       ExampleClass2

    Functions
    ---------

    .. autosummary::
       :toctree: _autosummary/

       example_function1
       example_function2

    Exceptions
    ----------

    .. autosummary::
       :toctree: _autosummary/

       ExampleError

The ```autosummary``` directives are important as they generate RST files in
the ```_autosummary/``` directory for each object. A single-line summary and link
to each object is inserted into the page for you.

After listing public module members, we encourage a usage example section
showing how to use some of the module's functionality. Examples should be
written in [doctest](http://docs.python.org/3/library/doctest.html) format so
that they can be automatically tested.

    Examples
    --------

    Run the ``example_function1`` function:

    >>> from micronota.example import example_function1
    >>> example_function1("hello", "world")
    hello world!

You can also embed the plots that an example generates into the built
documentation with the ```.. plot::``` directive. For example:

    .. plot::

       >>> from micronota.draw import boxplots
       >>> fig = boxplots([[2, 2, 1, 3, 4, 4.2, 7], [0, -1, 4, 5, 6, 7]])

This will include the plot, a link to the source code used to generate the
plot, and links to different image formats (e.g., PNG and PDF) so that users
can easily download the plot.

You're now ready to document the members of your module.

#### Documenting module members

When documenting the members of a module (e.g., classes, methods, attributes,
functions, and exceptions), follow the numpydoc conventions. In addition to
these conventions, there are a few things to keep in mind:

- When documenting a class, only public methods and attributes are included in
  the built documentation. If a method or attribute starts with an
  underscore, it is assumed to be private.

- When documenting a class, include the ```Parameters``` section in the class
  docstring, instead of in the ```__init__``` docstring. While numpydoc
  technically supports either form, ```__init__``` is not included in the list
  of methods by default and thus should have its documentation included in the
  class docstring.

#### Including the module in the docs

Until now, we've only been editing docstrings, which are attached to Python
code. The final step is to hook up this new module's docstrings to the
documentation build system:

1. Make sure you're within the ```micronota/doc``` directory.
2. Create a new file with the same name as your module under the ```source```
   directory. Do not include ```micronota``` as part of the name, and use
   ```.rst``` as the suffix. For example, ```source/example.rst```.
3. Add the following line to ```source/example.rst``` to have your module's
   docstring pulled into the document:

    ```
    .. automodule:: micronota.example
    ```
4. Add the following line to ```source/index.rst``` to add the new page to the
   top-level table of contents:

    ```
    example
    ```

That's it! You can now try building the documentation, which should include the
documentation for your new module!

### Documenting a subpackage in micronota

The process of documenting a subpackage is very similar to documenting a module
in micronota. The only difference is that the module docstring goes in the
subpackage's ```__init__.py```.

### Troubleshooting

If things aren't working correctly, try running ```make clean``` and then
rebuild the docs. If things still aren't working, try building the docs
*without* your changes, and see if there are any Sphinx errors or warnings.
Make note of these, and then see what new errors or warnings are generated when
you add your changes again.


### Acknowledgements

This documentation guide lines are adapted from ```scikit-bio```'s guide line.
