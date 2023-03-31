from setuptools import setup

if __name__ == "__main__":
  print("Running setup.py")
  setup(
    name='pylogger_discord',
    version='0.0.122',
    requires=[
      'dotenv',
      'requests'
    ],
    author='Sebastian Tuyu',
    author_email='contact@sebastiantuyu.com',
    description='A simple logger for production apps',
    license='MIT',
    keywords=['DISCORD', 'LOGGER', 'CONSOLE'],
    package_dir={"pylogger":"src"},
    packages=["pylogger"]
  )