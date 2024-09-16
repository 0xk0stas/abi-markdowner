from setuptools import setup, find_packages

setup(
    name="abi-markdowner",
    version="0.1.15",
    description="A tool to convert MultiversX Smart Contract ABI files into Markdown documentation.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Kostas Tzoumpas",
    author_email="tzoumpas.ks@gmail.com",
    url="https://github.com/0xk0stas/abi-markdowner",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "toml>=0.10.2",  # For reading TOML files
        "pytest>=6.0"    # For testing
    ],
    entry_points={
        'console_scripts': [
            'abi-markdowner=abi_markdowner.main:main',
        ],
    },
)