from setuptools import setup, find_packages
# import pathlib
# import pkg_resources

# with pathlib.Path('requirements.txt').open() as requirements_txt:
#     install_requires = [
#         str(requirement)
#         for requirement
#         in pkg_resources.parse_requirements(requirements_txt)
#     ]

setup(
    name='detic',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "mss",
        "timm",
        "dataclasses",
        "ftfy",
        "regex",
        "fasttext-wheel",
        "scikit-learn",
        "lvis",
        "nltk",
        "clip @ git+https://github.com/openai/CLIP.git",
    ],
)