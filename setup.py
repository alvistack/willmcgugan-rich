# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rich']

package_data = \
{'': ['*']}

install_requires = \
['commonmark>=0.9.0,<0.10.0', 'pygments>=2.6.0,<3.0.0']

extras_require = \
{':python_version < "3.9"': ['typing-extensions>=4.0.0,<5.0'],
 'jupyter': ['ipywidgets>=7.5.1,<8.0.0']}

setup_kwargs = {
    'name': 'rich',
    'version': '13.0.1',
    'description': 'Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal',
    'author': 'Will McGugan',
    'author_email': 'willmcgugan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Textualize/rich',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.0',
}


setup(**setup_kwargs)
