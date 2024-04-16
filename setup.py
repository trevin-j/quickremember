from setuptools import setup, find_packages

setup(
    name='remember',
    version='0.1',
    description='Quicly remember things for later',
    url='https://github.com/trevin-j/quickremember',
    author='Trevin Jones',
    author_email='trevindjones@gmail.com',
    license='MIT',
    install_requires=['thefuzz'],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=[
            'remember=src.remember:consolemain',
            'forget=src.forget:consolemain'
        ]
    )
)