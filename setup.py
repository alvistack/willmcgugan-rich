# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rich']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.0,<0.5.0',
 'commonmark>=0.9.0,<0.10.0',
 'pygments>=2.6.0,<3.0.0']

extras_require = \
{':python_version < "3.7"': ['dataclasses>=0.7,<0.9'],
 ':python_version < "3.8"': ['typing-extensions>=3.7.4,<5.0'],
 'jupyter': ['ipywidgets>=7.5.1,<8.0.0']}

setup_kwargs = {
    'name': 'rich',
    'version': '10.15.2',
    'description': 'Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal',
    'long_description': '[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0)](https://pypi.org/project/rich/) [![PyPI version](https://badge.fury.io/py/rich.svg)](https://badge.fury.io/py/rich)\n\n[![Downloads](https://pepy.tech/badge/rich/month)](https://pepy.tech/project/rich)\n[![codecov](https://codecov.io/gh/willmcgugan/rich/branch/master/graph/badge.svg)](https://codecov.io/gh/willmcgugan/rich)\n[![Rich blog](https://img.shields.io/badge/blog-rich%20news-yellowgreen)](https://www.willmcgugan.com/tag/rich/)\n[![Twitter Follow](https://img.shields.io/twitter/follow/willmcgugan.svg?style=social)](https://twitter.com/willmcgugan)\n\n![Logo](https://github.com/willmcgugan/rich/raw/master/imgs/logo.svg)\n\n[English readme](https://github.com/willmcgugan/rich/blob/master/README.md)\n • [中文 readme](https://github.com/willmcgugan/rich/blob/master/README.cn.md)\n • [Lengua española readme](https://github.com/willmcgugan/rich/blob/master/README.es.md)\n • [Deutsche readme](https://github.com/willmcgugan/rich/blob/master/README.de.md)\n • [Läs på svenska](https://github.com/willmcgugan/rich/blob/master/README.sv.md)\n • [日本語 readme](https://github.com/willmcgugan/rich/blob/master/README.ja.md)\n • [한국어 readme](https://github.com/willmcgugan/rich/blob/master/README.kr.md)\n • [Français readme](https://github.com/willmcgugan/rich/blob/master/README.fr.md)\n • [Schwizerdütsch readme](https://github.com/willmcgugan/rich/blob/master/README.de-ch.md)\n • [हिन्दी readme](https://github.com/willmcgugan/rich/blob/master/README.hi.md)\n • [Português brasileiro readme](https://github.com/willmcgugan/rich/blob/master/README.pt-br.md)\n • [Italian readme](https://github.com/willmcgugan/rich/blob/master/README.it.md)\n\nRich is a Python library for _rich_ text and beautiful formatting in the terminal.\n\nThe [Rich API](https://rich.readthedocs.io/en/latest/) makes it easy to add color and style to terminal output. Rich can also render pretty tables, progress bars, markdown, syntax highlighted source code, tracebacks, and more — out of the box.\n\n![Features](https://github.com/willmcgugan/rich/raw/master/imgs/features.png)\n\nFor a video introduction to Rich see [calmcode.io](https://calmcode.io/rich/introduction.html) by [@fishnets88](https://twitter.com/fishnets88).\n\nSee what [people are saying about Rich](https://www.willmcgugan.com/blog/pages/post/rich-tweets/).\n\n## Compatibility\n\nRich works with Linux, OSX, and Windows. True color / emoji works with new Windows Terminal, classic terminal is limited to 16 colors. Rich requires Python 3.6.1 or later.\n\nRich works with [Jupyter notebooks](https://jupyter.org/) with no additional configuration required.\n\n## Installing\n\nInstall with `pip` or your favorite PyPI package manager.\n\n```\npip install rich\n```\n\nRun the following to test Rich output on your terminal:\n\n```\npython -m rich\n```\n\n## Rich Print\n\nTo effortlessly add rich output to your application, you can import the [rich print](https://rich.readthedocs.io/en/latest/introduction.html#quick-start) method, which has the same signature as the builtin Python function. Try this:\n\n```python\nfrom rich import print\n\nprint("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())\n```\n\n![Hello World](https://github.com/willmcgugan/rich/raw/master/imgs/print.png)\n\n## Rich REPL\n\nRich can be installed in the Python REPL, so that any data structures will be pretty printed and highlighted.\n\n```python\n>>> from rich import pretty\n>>> pretty.install()\n```\n\n![REPL](https://github.com/willmcgugan/rich/raw/master/imgs/repl.png)\n\n## Using the Console\n\nFor more control over rich terminal content, import and construct a [Console](https://rich.readthedocs.io/en/latest/reference/console.html#rich.console.Console) object.\n\n```python\nfrom rich.console import Console\n\nconsole = Console()\n```\n\nThe Console object has a `print` method which has an intentionally similar interface to the builtin `print` function. Here\'s an example of use:\n\n```python\nconsole.print("Hello", "World!")\n```\n\nAs you might expect, this will print `"Hello World!"` to the terminal. Note that unlike the builtin `print` function, Rich will word-wrap your text to fit within the terminal width.\n\nThere are a few ways of adding color and style to your output. You can set a style for the entire output by adding a `style` keyword argument. Here\'s an example:\n\n```python\nconsole.print("Hello", "World!", style="bold red")\n```\n\nThe output will be something like the following:\n\n![Hello World](https://github.com/willmcgugan/rich/raw/master/imgs/hello_world.png)\n\nThat\'s fine for styling a line of text at a time. For more finely grained styling, Rich renders a special markup which is similar in syntax to [bbcode](https://en.wikipedia.org/wiki/BBCode). Here\'s an example:\n\n```python\nconsole.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")\n```\n\n![Console Markup](https://github.com/willmcgugan/rich/raw/master/imgs/where_there_is_a_will.png)\n\nYou can use a Console object to generate sophisticated output with minimal effort. See the [Console API](https://rich.readthedocs.io/en/latest/console.html) docs for details.\n\n## Rich Inspect\n\nRich has an [inspect](https://rich.readthedocs.io/en/latest/reference/init.html?highlight=inspect#rich.inspect) function which can produce a report on any Python object, such as class, instance, or builtin.\n\n```python\n>>> my_list = ["foo", "bar"]\n>>> from rich import inspect\n>>> inspect(my_list, methods=True)\n```\n\n![Log](https://github.com/willmcgugan/rich/raw/master/imgs/inspect.png)\n\nSee the [inspect docs](https://rich.readthedocs.io/en/latest/reference/init.html#rich.inspect) for details.\n\n# Rich Library\n\nRich contains a number of builtin _renderables_ you can use to create elegant output in your CLI and help you debug your code.\n\nClick the following headings for details:\n\n<details>\n<summary>Log</summary>\n\nThe Console object has a `log()` method which has a similar interface to `print()`, but also renders a column for the current time and the file and line which made the call. By default Rich will do syntax highlighting for Python structures and for repr strings. If you log a collection (i.e. a dict or a list) Rich will pretty print it so that it fits in the available space. Here\'s an example of some of these features.\n\n```python\nfrom rich.console import Console\nconsole = Console()\n\ntest_data = [\n    {"jsonrpc": "2.0", "method": "sum", "params": [None, 1, 2, 4, False, True], "id": "1",},\n    {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},\n    {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},\n]\n\ndef test_log():\n    enabled = False\n    context = {\n        "foo": "bar",\n    }\n    movies = ["Deadpool", "Rise of the Skywalker"]\n    console.log("Hello from", console, "!")\n    console.log(test_data, log_locals=True)\n\n\ntest_log()\n```\n\nThe above produces the following output:\n\n![Log](https://github.com/willmcgugan/rich/raw/master/imgs/log.png)\n\nNote the `log_locals` argument, which outputs a table containing the local variables where the log method was called.\n\nThe log method could be used for logging to the terminal for long running applications such as servers, but is also a very nice debugging aid.\n\n</details>\n<details>\n<summary>Logging Handler</summary>\n\nYou can also use the builtin [Handler class](https://rich.readthedocs.io/en/latest/logging.html) to format and colorize output from Python\'s logging module. Here\'s an example of the output:\n\n![Logging](https://github.com/willmcgugan/rich/raw/master/imgs/logging.png)\n\n</details>\n\n<details>\n<summary>Emoji</summary>\n\nTo insert an emoji in to console output place the name between two colons. Here\'s an example:\n\n```python\n>>> console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")\n😃 🧛 💩 👍 🦝\n```\n\nPlease use this feature wisely.\n\n</details>\n\n<details>\n<summary>Tables</summary>\n\nRich can render flexible [tables](https://rich.readthedocs.io/en/latest/tables.html) with unicode box characters. There is a large variety of formatting options for borders, styles, cell alignment etc.\n\n![table movie](https://github.com/willmcgugan/rich/raw/master/imgs/table_movie.gif)\n\nThe animation above was generated with [table_movie.py](https://github.com/willmcgugan/rich/blob/master/examples/table_movie.py) in the examples directory.\n\nHere\'s a simpler table example:\n\n```python\nfrom rich.console import Console\nfrom rich.table import Table\n\nconsole = Console()\n\ntable = Table(show_header=True, header_style="bold magenta")\ntable.add_column("Date", style="dim", width=12)\ntable.add_column("Title")\ntable.add_column("Production Budget", justify="right")\ntable.add_column("Box Office", justify="right")\ntable.add_row(\n    "Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"\n)\ntable.add_row(\n    "May 25, 2018",\n    "[red]Solo[/red]: A Star Wars Story",\n    "$275,000,000",\n    "$393,151,347",\n)\ntable.add_row(\n    "Dec 15, 2017",\n    "Star Wars Ep. VIII: The Last Jedi",\n    "$262,000,000",\n    "[bold]$1,332,539,889[/bold]",\n)\n\nconsole.print(table)\n```\n\nThis produces the following output:\n\n![table](https://github.com/willmcgugan/rich/raw/master/imgs/table.png)\n\nNote that console markup is rendered in the same way as `print()` and `log()`. In fact, anything that is renderable by Rich may be included in the headers / rows (even other tables).\n\nThe `Table` class is smart enough to resize columns to fit the available width of the terminal, wrapping text as required. Here\'s the same example, with the terminal made smaller than the table above:\n\n![table2](https://github.com/willmcgugan/rich/raw/master/imgs/table2.png)\n\n</details>\n\n<details>\n<summary>Progress Bars</summary>\n\nRich can render multiple flicker-free [progress](https://rich.readthedocs.io/en/latest/progress.html) bars to track long-running tasks.\n\nFor basic usage, wrap any sequence in the `track` function and iterate over the result. Here\'s an example:\n\n```python\nfrom rich.progress import track\n\nfor step in track(range(100)):\n    do_step(step)\n```\n\nIt\'s not much harder to add multiple progress bars. Here\'s an example taken from the docs:\n\n![progress](https://github.com/willmcgugan/rich/raw/master/imgs/progress.gif)\n\nThe columns may be configured to show any details you want. Built-in columns include percentage complete, file size, file speed, and time remaining. Here\'s another example showing a download in progress:\n\n![progress](https://github.com/willmcgugan/rich/raw/master/imgs/downloader.gif)\n\nTo try this out yourself, see [examples/downloader.py](https://github.com/willmcgugan/rich/blob/master/examples/downloader.py) which can download multiple URLs simultaneously while displaying progress.\n\n</details>\n\n<details>\n<summary>Status</summary>\n\nFor situations where it is hard to calculate progress, you can use the [status](https://rich.readthedocs.io/en/latest/reference/console.html#rich.console.Console.status) method which will display a \'spinner\' animation and message. The animation won\'t prevent you from using the console as normal. Here\'s an example:\n\n```python\nfrom time import sleep\nfrom rich.console import Console\n\nconsole = Console()\ntasks = [f"task {n}" for n in range(1, 11)]\n\nwith console.status("[bold green]Working on tasks...") as status:\n    while tasks:\n        task = tasks.pop(0)\n        sleep(1)\n        console.log(f"{task} complete")\n```\n\nThis generates the following output in the terminal.\n\n![status](https://github.com/willmcgugan/rich/raw/master/imgs/status.gif)\n\nThe spinner animations were borrowed from [cli-spinners](https://www.npmjs.com/package/cli-spinners). You can select a spinner by specifying the `spinner` parameter. Run the following command to see the available values:\n\n```\npython -m rich.spinner\n```\n\nThe above command generates the following output in the terminal:\n\n![spinners](https://github.com/willmcgugan/rich/raw/master/imgs/spinners.gif)\n\n</details>\n\n<details>\n<summary>Tree</summary>\n\nRich can render a [tree](https://rich.readthedocs.io/en/latest/tree.html) with guide lines. A tree is ideal for displaying a file structure, or any other hierarchical data.\n\nThe labels of the tree can be simple text or anything else Rich can render. Run the following for a demonstration:\n\n```\npython -m rich.tree\n```\n\nThis generates the following output:\n\n![markdown](https://github.com/willmcgugan/rich/raw/master/imgs/tree.png)\n\nSee the [tree.py](https://github.com/willmcgugan/rich/blob/master/examples/tree.py) example for a script that displays a tree view of any directory, similar to the linux `tree` command.\n\n</details>\n\n<details>\n<summary>Columns</summary>\n\nRich can render content in neat [columns](https://rich.readthedocs.io/en/latest/columns.html) with equal or optimal width. Here\'s a very basic clone of the (MacOS / Linux) `ls` command which displays a directory listing in columns:\n\n```python\nimport os\nimport sys\n\nfrom rich import print\nfrom rich.columns import Columns\n\ndirectory = os.listdir(sys.argv[1])\nprint(Columns(directory))\n```\n\nThe following screenshot is the output from the [columns example](https://github.com/willmcgugan/rich/blob/master/examples/columns.py) which displays data pulled from an API in columns:\n\n![columns](https://github.com/willmcgugan/rich/raw/master/imgs/columns.png)\n\n</details>\n\n<details>\n<summary>Markdown</summary>\n\nRich can render [markdown](https://rich.readthedocs.io/en/latest/markdown.html) and does a reasonable job of translating the formatting to the terminal.\n\nTo render markdown import the `Markdown` class and construct it with a string containing markdown code. Then print it to the console. Here\'s an example:\n\n```python\nfrom rich.console import Console\nfrom rich.markdown import Markdown\n\nconsole = Console()\nwith open("README.md") as readme:\n    markdown = Markdown(readme.read())\nconsole.print(markdown)\n```\n\nThis will produce output something like the following:\n\n![markdown](https://github.com/willmcgugan/rich/raw/master/imgs/markdown.png)\n\n</details>\n\n<details>\n<summary>Syntax Highlighting</summary>\n\nRich uses the [pygments](https://pygments.org/) library to implement [syntax highlighting](https://rich.readthedocs.io/en/latest/syntax.html). Usage is similar to rendering markdown; construct a `Syntax` object and print it to the console. Here\'s an example:\n\n```python\nfrom rich.console import Console\nfrom rich.syntax import Syntax\n\nmy_code = \'\'\'\ndef iter_first_last(values: Iterable[T]) -> Iterable[Tuple[bool, bool, T]]:\n    """Iterate and generate a tuple with a flag for first and last value."""\n    iter_values = iter(values)\n    try:\n        previous_value = next(iter_values)\n    except StopIteration:\n        return\n    first = True\n    for value in iter_values:\n        yield first, False, previous_value\n        first = False\n        previous_value = value\n    yield first, True, previous_value\n\'\'\'\nsyntax = Syntax(my_code, "python", theme="monokai", line_numbers=True)\nconsole = Console()\nconsole.print(syntax)\n```\n\nThis will produce the following output:\n\n![syntax](https://github.com/willmcgugan/rich/raw/master/imgs/syntax.png)\n\n</details>\n\n<details>\n<summary>Tracebacks</summary>\n\nRich can render [beautiful tracebacks](https://rich.readthedocs.io/en/latest/traceback.html) which are easier to read and show more code than standard Python tracebacks. You can set Rich as the default traceback handler so all uncaught exceptions will be rendered by Rich.\n\nHere\'s what it looks like on OSX (similar on Linux):\n\n![traceback](https://github.com/willmcgugan/rich/raw/master/imgs/traceback.png)\n\n</details>\n\nAll Rich renderables make use of the [Console Protocol](https://rich.readthedocs.io/en/latest/protocol.html), which you can also use to implement your own Rich content.\n\n# Rich for enterprise\n\nAvailable as part of the Tidelift Subscription.\n\nThe maintainers of Rich and thousands of other packages are working with Tidelift to deliver commercial support and maintenance for the open source packages you use to build your applications. Save time, reduce risk, and improve code health, while paying the maintainers of the exact packages you use. [Learn more.](https://tidelift.com/subscription/pkg/pypi-rich?utm_source=pypi-rich&utm_medium=referral&utm_campaign=enterprise&utm_term=repo)\n\n# Projects using Rich\n\nHere are a few projects using Rich:\n\n- [BrancoLab/BrainRender](https://github.com/BrancoLab/BrainRender)\n  a python package for the visualization of three dimensional neuro-anatomical data\n- [Ciphey/Ciphey](https://github.com/Ciphey/Ciphey)\n  Automated decryption tool\n- [emeryberger/scalene](https://github.com/emeryberger/scalene)\n  a high-performance, high-precision CPU and memory profiler for Python\n- [hedythedev/StarCli](https://github.com/hedythedev/starcli)\n  Browse GitHub trending projects from your command line\n- [intel/cve-bin-tool](https://github.com/intel/cve-bin-tool)\n  This tool scans for a number of common, vulnerable components (openssl, libpng, libxml2, expat and a few others) to let you know if your system includes common libraries with known vulnerabilities.\n- [nf-core/tools](https://github.com/nf-core/tools)\n  Python package with helper tools for the nf-core community.\n- [cansarigol/pdbr](https://github.com/cansarigol/pdbr)\n  pdb + Rich library for enhanced debugging\n- [plant99/felicette](https://github.com/plant99/felicette)\n  Satellite imagery for dummies.\n- [seleniumbase/SeleniumBase](https://github.com/seleniumbase/SeleniumBase)\n  Automate & test 10x faster with Selenium & pytest. Batteries included.\n- [smacke/ffsubsync](https://github.com/smacke/ffsubsync)\n  Automagically synchronize subtitles with video.\n- [tryolabs/norfair](https://github.com/tryolabs/norfair)\n  Lightweight Python library for adding real-time 2D object tracking to any detector.\n- [ansible/ansible-lint](https://github.com/ansible/ansible-lint) Ansible-lint checks playbooks for practices and behaviour that could potentially be improved\n- [ansible-community/molecule](https://github.com/ansible-community/molecule) Ansible Molecule testing framework\n- +[Many more](https://github.com/willmcgugan/rich/network/dependents)!\n\n<!-- This is a test, no need to translate -->\n',
    'author': 'Will McGugan',
    'author_email': 'willmcgugan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/willmcgugan/rich',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
