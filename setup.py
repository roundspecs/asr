from importlib.metadata import entry_points
import setuptools

setuptools.setup(
    name="asr",
    version="0.0.0",
    packages=setuptools.find_packages(),
    install_requires=['click', 'typing_extensions'],
    entry_points="""
    [console_scripts]
    asr=asr:main
    """
)