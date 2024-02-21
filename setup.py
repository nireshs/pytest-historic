from setuptools import find_packages, setup

setup(
      name='pytest-historic',
      version="2.1.0",
      description='Custom report to display pytest historical execution records',
      long_description='Pytest Historic is custom report to display historical execution records using MySQL + Flask',
      classifiers=[
          'Framework :: Pytest',
          'Programming Language :: Python',
          'Topic :: Software Development :: Testing',
      ],
      keywords='pytest historical execution report',
      author='Niresh Shanmugam',
      author_email='niresh.shanmugam@gmail.com',
      url='https://github.com/nireshs/pytest-historic',
      license='MIT',

      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'pytest',
          'config',
          'flask',
          'flask-mysqldb'
      ],
      entry_points={
          'console_scripts': [
              'pytesthistoric=pytest_historic.app:main',
          ]
      },
)
