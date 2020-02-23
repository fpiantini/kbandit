import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'kbandit',
    packages = setuptools.find_packages(),
    version = '1.0.0',
    license = 'MIT',
    author = 'Francesco Piantini',
    author_email = 'pf@fpiantini.it',
    description = 'A simple multi-armed bandit algorithm in Python',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/fpiantini/kbandit',
    download_url = '',
    install_requires=[
        'numpy',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",  # Chose between:
                                            # "3 - Alpha"
                                            # "4 - Beta"
                                            # "5 - Production/Stable"
    ],
    python_requires='>=3.6',
)

