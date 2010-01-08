from setuptools import setup, find_packages

version = '1.0'

setup(name='collective.sharerizer',
      version=version,
      description="A package to inject Web 2.0 style sharing buttons into a Plone 3.x's portal_actions.",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone',
      author='ONE/Northwest',
      author_email='jonb@onenw.org',
      url='http://svn.plone.org/svn/collective/collective.sharerizer',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      )
