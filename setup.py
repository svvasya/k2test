from setuptools import setup, find_packages

#setup(
#    name='k2test',
#    version='1.0.0',
#    description='Description of my project',
#    author='Your Name',
#    author_email='yourname@example.com',
#    packages=find_packages(),  
#    package_data={'k2test': ['views.py']},
#    install_requires=[

 #   ],
#)
setup(
    name='k2test',
    version='1.0.0',
    packages=['k2test'],
    include_package_data=True,
    install_requires=[
        
    ],
)
