from setuptools import setup, find_packages
import os

version = '1.2'

setup(name='wm.chimpimport',
      version=version,
      description="automated way to import `role addresses` into mailchimp subscription lists",
      long_description=open("README.rst").read() + "\n\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='mailchimp import',
      author='Harald Friessnegger',
      author_email='harald at webmeisterei (dot) com',
      url='https://github.com/frisi/wm.chimpimport',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['wm'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          'chimpy',
          # -*- Extra requirements: -*-
      ],
      entry_points={
            'console_scripts': ['chimpimport = wm.chimpimport:main',]
            },
      )
