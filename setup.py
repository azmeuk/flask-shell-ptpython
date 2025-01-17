"""Replace the default ``flask shell`` command with a similar one running PTPython."""
from setuptools import setup


URL = "https://github.com/azmeuk/flask-shell-ptpython"

readme = open("README.rst").read()

setup_requires = [
    "autosemver>=0.5.3",
]

install_requires = [
    "Flask>=0.12.2",
    "click>=6.7",
    "ptpython>=0.41",
]

docs_require = []

tests_require = []

extras_require = {
    "docs": docs_require,
    "tests": tests_require,
}

extras_require["all"] = []
for name, reqs in extras_require.items():
    extras_require["all"].extend(reqs)

setup(
    name="flask-shell-ptpython2",
    autosemver={
        "bugtracker_url": URL + "/issues",
    },
    url=URL,
    license="MIT",
    author="Jacopo Notarstefano",
    author_email="jacopo.notarstefano@gmail.com",
    py_modules=["flask_shell_ptpython"],
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    description=__doc__,
    long_description=readme,
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    entry_points={
        "flask.commands": [
            "shell=flask_shell_ptpython:shell_command",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python",
    ],
)
