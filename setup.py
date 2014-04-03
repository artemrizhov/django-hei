from setuptools import setup, find_packages

setup(
    author="Artem Rizhov, Sergey Kupriyanov",
    author_email="artem.rizhov@gmail.com",
    name='django-hei',
    description='Hide Error Info on Django error page in debug mode',
    license='MIT License',
    platforms=['OS Independent'],
    install_requires=[
    ],
    tests_require=[
    ],
    packages=find_packages(),
    include_package_data=True,
)
