from setuptools import setup, find_packages

setup(
  name='show_graph_paths',
  version='0.1.2',
  packages=find_packages(),
  include_package_data=True,
  description='Extracts subgraph based on regex filters from nx DiGraphs',
  author='Reuven Peleg',
  author_email='your_email@example.com',
  install_requires=[
    'networkx',
    'gravis',
    'scipy'
  ],
  entry_points={
    'console_scripts': [
      'show_graph_paths=show_graph_paths.__main__:main',
    ],
  },
)
