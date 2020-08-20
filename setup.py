from setuptools import find_packages, setup
from distutils.cmd import Command

class BdistWheelCommand(Command):
    """A class for "pip bdist_wheel"
    Raise exception to always disable wheel cache.
    See https://github.com/pypa/pip/issues/4720
    """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        raise Exception('bdist_wheel is not supported')


setup(
    name="alterego",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "torch",
        "torchvision",
        "backcall==0.2.0",
        "cffi==1.14.1",
        "cloudpickle==1.5.0",
        "colorama==0.4.3",
        "cycler==0.10.0",
        "dask==2.21.0",
        "decorator==4.4.2",
        "future==0.18.2",
        "imageio==2.9.0",
        "imageio-ffmpeg==0.4.2",
        "ipykernel==5.3.4",
        "ipython==7.16.1",
        "ipython-genutils==0.2.0",
        "jedi==0.17.2",
        "joblib==0.16.0",
        "jupyter-client==6.1.6",
        "jupyter-core==4.6.3",
        "kiwisolver==1.2.0",
        "matplotlib==3.3.0",
        "networkx==2.4",
        "numpy==1.19.1",
        "opencv-python==4.3.0.36",
        "pandas==1.0.5",
        "parso==0.7.1",
        "pickleshare==0.7.5",
        "Pillow==7.2.0",
        "prompt-toolkit==3.0.5",
        "pycparser==2.18",
        "pygit==0.1",
        "Pygments==2.6.1",
        "pyparsing==2.4.7",
        "python-dateutil==2.8.1",
        "pytz==2020.1",
        "PyWavelets==1.1.1",
        "pywin32==228",
        "PyYAML==5.3.1",
        "pyzmq==19.0.1",
        "scikit-image==0.17.2",
        "scikit-learn==0.23.1",
        "scipy==1.5.2",
        "six==1.15.0",
        "threadpoolctl==2.1.0",
        "tifffile==2020.7.24",
        "toolz==0.10.0",
        "tornado==6.0.4",
        "tqdm==4.48.0",
        "traitlets==4.3.3",
        "wcwidth==0.2.5"
    ],
    cmdclass={
      'bdist_wheel': BdistWheelCommand,
    },
)

