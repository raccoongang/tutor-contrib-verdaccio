import io
import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutorverdaccio", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-contrib-verdaccio",
    version=ABOUT["__version__"],
    url="https://github.com/raccoongang/tutor-contrib-verdaccio",
    project_urls={
        "Code": "https://github.com/raccoongang/tutor-contrib-verdaccio",
        "Issue tracker": "https://github.com/raccoongang/tutor-contrib-verdaccio/issues",
    },
    license="AGPLv3",
    author="Max Sokolski",
    author_email="maksim.sokolskiy@raccoongang.com",
    description="verdaccio plugin for Tutor",
    long_description=load_readme(),
    long_description_content_type="text/x-rst",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["tutor>=17.0.0,<18.0.0"],
    extras_require={
        "dev": [
            "tutor[dev]>=17.0.0,<18.0.0",
        ]
    },
    entry_points={
        "tutor.plugin.v1": [
            "verdaccio = tutorverdaccio.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
