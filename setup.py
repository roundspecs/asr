import setuptools

setuptools.setup(
    name="asr",
    version="0.0.0",
    packages=setuptools.find_packages(),
    install_requires=["typer", "rich", "typing_extensions", "shellingham"],
    entry_points="""
    [console_scripts]
    asr=cli:app
    """,
)
