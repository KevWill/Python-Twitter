from distutils.core import setup

setup(name='Python-Twitter',
      version='1.0',
      description='Twitter Api wrapper code',
      author='Kevin Willemsen',
      author_email='kevin.willemsen@gmail.com',
      install_requires=['requests>=2', 'requests_oauthlib'],
      classifiers=['Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',],
      url = 'https://github.com/KevWill/Python-Twitter',
      download_url = 'https://github.com/KevWill/Python-Twitter',
      packages = ['python_twitter'],
      keywords = ['twitter'],
     )