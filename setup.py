from setuptools import setup, find_packages

setup(
    name='k2test',
    version='1.0.0',
    description='Description of my project',
    author='Your Name',
    author_email='yourname@example.com',
    keywords="k2test, k2",
    python_requires=">=3.7, <=3.11.2",
    packages=['k2test'],
    package_data={  # Optional
        "k2test": ["static/style.css", "static/default.css", "templates/index.html", "templates/login.html"]    },
    install_requires=[
            beautifulsoup
    ],
)
