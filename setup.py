from setuptools import find_packages, setup

setup(
    name="alterego",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "torch",
        "torchvision",
        "imageio",
        "imageio-ffmpeg",
        "matplotlib",
        "numpy",
        "opencv-python",
        "pandas",
        "PyYAML",
        "scipy",
        "tqdm",
        "scikit-image",
        "scikit-learn",
    ],
)
