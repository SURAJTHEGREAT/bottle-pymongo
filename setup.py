from setuptools import setup,find_packages

setup(
    name='pymongo-blog',
    version=0.1,
    description='Pymongo-blog',
    author='Suraj',
    author_email='suraj.iot257@gmail.com',
    url='https://github.com/SURAJTHEGREAT/bottle-pymongo.git',
    license='Apache License (2.0)',
    download_url='https://github.com/SURAJTHEGREAT/bottle-pymongo.git',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],
    scripts=[],
    provides=['blog'],
    packages=find_packages(),
    install_requires=['pymongo','bottle','logging','oslo_config','pytest']
)



