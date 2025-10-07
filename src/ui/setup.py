from setuptools import find_packages, setup


setup(
    name="Cadaver Exquisito UI",
    packages=find_packages(),
    author="Macarena Fernández Urquiza",
    author_email="m.fernanezurquiza@gmail.com",
    version="0.0.1",
    install_requires=[
        "streamlit==1.45.1"
    ],
    extras_require={},
    classifiers=["Programming Language :: Python :: 3"],
)
