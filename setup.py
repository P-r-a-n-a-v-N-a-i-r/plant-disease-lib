from setuptools import setup, find_packages

setup(
    name='plant_disease_lib',
    version='0.1.0',
    author='Pranav Nair',
    author_email='pranavshivannair@gmail.com',
    description='A library for plant disease detection using deep learning',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/P-r-a-n-a-v-N-a-i-r/plant-disease-lib',
    packages=find_packages(),
    install_requires=[
        'pillow',
        'numpy',
        'pandas',
        'torch',
        'torchvision'
    ],
    python_requires='>=3.7',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,
)
