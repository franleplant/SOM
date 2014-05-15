SOM
===

This is a result of a Research Project made in 2014 in UTN FRD Argentina (Universidad Tecnologica Nacional Facultad Regional Delta).

## Getting Started

### Environment setting

We are using Python and Scipy packages.
We've found that all-in-one installer are the easiest and simpler to install.


- Download and Install [Enthought Canopy Free](https://www.enthought.com/downloads/).
- Download and Install [Git](http://git-scm.com/download)


And you are all set! (Checkout advanced settings section)


> Other options include [Anaconda](http://continuum.io/downloads), but
use Entought Canopy to promote smooth team work.

### Dealing with previously installed Python versions

You might have another Python installed previously, Enthought already comes with
Python packaged and that Python will definetively play nice with the other packages
so you want to use that one.

You have two solutions:

#### 1. Uninstall all previous Python installations
#### 2. Change environment variable (on Windows)

> Work in progress

1. Type `Win` command
2. Search `Variable` and select `Edit Environment variables`. Optionally look for this option inside Win Control Panel (Look for it).
3. Make sure that `Path` environment variable points to the directory where Enthought has the `python.exe`: `C:\Users\your_user_name\AppData\Local\Enthought\Canopy\User\Scripts`

### Download and run the code 

Make you sure you have git installed, open `git bash` in windows (or a regular terminal in Linux / Unix system) and type:

````bash
git clone https://github.com/franleplant/SOM SOM
cd SOM
```

Run any of the `.py` files

````bash
python file.py
```

You'll see the result if any in the CLI (Command Line Interface)


Its a good idea lo learn git. Here it is a summary of a [common workflow](https://github.com/franleplant/git-101).
It also contains some useful links and tutorials.

## Docs

We are using the [wiki](https://github.com/franleplant/SOM/wiki) intensively. Please check it up.

We are going to be using Scipy heavily, please refer to
[Scipy Docs](http://www.scipy.org/docs.html).
Scipy is a Python meta-package that includes other Scientific and Mathematics packages, the most important are:

- [Numpy](http://docs.scipy.org/doc/numpy/): Fast N-Array package.
- [Matplotlib](http://matplotlib.org/contents.html): Comprehensive 2D Plotting
- [Scipy itself](http://docs.scipy.org/doc/scipy/reference/): Fundamental library for scientific computing
- Others


## Resources

Throw in here any link that you think that is relevant or useful.

- [Scipy Getting started example. Use this to check Scipy package install](http://scipy.org/getting-started.html#an-example-session)
- [SOM implementation in Python](http://www.pymvpa.org/examples/som.html)
- [Som implementation in Python source](https://github.com/PyMVPA/PyMVPA/blob/c9ed9d71a425fe4b8b2ebaa7e6def71d62449764/mvpa2/mappers/som.py)


# Copyright

Copyright 2014 Dario Huggenberger, Pedro Araujo, Francisco Guijarro
