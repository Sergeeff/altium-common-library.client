from setuptools import setup, find_packages

setup(
    name = "CSV",
    version = "0.1",
    description = """CSV Plugin""",
    author = 'Jack Krieger',
    #install_requires = ["Cheetah >= 1.0"],
    packages = ['csv'],
    entry_points = """
    [db.engine]
    instance = csv.csvfile:CSVWriter
    """)
