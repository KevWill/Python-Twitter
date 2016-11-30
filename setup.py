from distutils.core import setup

setup(name='Python-Twitter',
      version='1.0',
      description='Twitter Api wrapper code',
      author='Kevin Willemsen',
      author_email='kevin.willemsen@gmail.com',
      url='https://github.com/KevWill/Python-Twitter',
      install_requires=['requests>=2', 'requests_oauthlib',
                        'urllib'],
      classifiers=['Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',],
      download_url = 'https://github.com/KevWill/Python-Twitter',
      keywords = ['twitter'],
     )