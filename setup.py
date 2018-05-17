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
    scripts=[''],
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pymongo','bottle','logging','oslo_config','pytest'],
    data_files=[('app/views/',['app/views/blog_template.tpl','app/views/entry_template.tpl','app/views/error_template.tpl','app/views/login.tpl','app/views/newpost_template.tpl','app/views/signup.tpl','app/views/welcome.tpl'])], 
    zip_safe=False
)



