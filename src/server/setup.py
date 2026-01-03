from setuptools import find_packages, setup


setup(
    name="Cadaver Exquisito Server",
    packages=find_packages(),
    author="Macarena Fernández Urquiza",
    author_email="m.fernanezurquiza@gmail.com",
    version="0.0.1",
    install_requires=["fastapi[standard]"],
    extras_require={},
    classifiers=["Programming Language :: Python :: 3"],
)
