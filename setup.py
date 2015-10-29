from setuptools import setup

entry_points = {
    'console_scripts': ['comcast-usage = comcastUsage:get_usage']
}

setup(name='comcast-usage',
      version="0.9.0",
      description='A simple script for checking your Comcast data usage',
      author='Anthony Fox',
      author_email='anthonyfox1988@gmail.com',
      license='MIT',
      url='https://github.com/wtfox/comcastUsage',
      modules=['comcastUsage'],
      install_requires=[
          'requests==2.8.1'
      ],
      entry_points=entry_points,
      keywords=['comcast', 'data usage', 'cli', 'script'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities'
      ])
