import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "nishant696"
SRC_REPO = "Text-summarizer"
AUTHOR_EMAIL = "nishantsarita413@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/nishant696/Text-Summarizer",
   project_urls={
       "Bug Tracker": "https://github.com/nishant696/Text-Summarizer/issues",
   },
   package_dir={"": "src"},
   packages=setuptools.find_packages(where="src")
)