from setuptools import setup, find_packages

setup(
  name='show_graph_paths',
  version='0.1.0',
  packages=find_packages(where='show_graph_paths'),
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
      'show_graph_paths=show_grpah_paths.main:main',
    ],
  },
)
