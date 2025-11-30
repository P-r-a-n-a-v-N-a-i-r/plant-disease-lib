from setuptools import setup, find_packages
from pathlib import Path

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="plant_disease_lib",
    version="0.1.4",
    author="Pranav Nair",
    author_email="pranavshivannair@gmail.com",
    description="A library for plant disease detection using deep learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/P-r-a-n-a-v-N-a-i-r/plant-disease-lib",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.26.0",
        "pandas==1.2.4",
        "Pillow==8.2.0",
        "python-dateutil==2.8.1",
        "pytz==2021.1",
        "six==1.15.0",
        "typing-extensions==3.7.4.3",
        "torch==1.8.1+cpu",
        "torchvision==0.9.1+cpu"

    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    package_data={
        "plant_disease_lib": ["*.csv"],
    },
)
