#!/usr/bin/pyton3

import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_desc = fh.read()

setuptools.setup(
    name="slack-emoji-webscraper-upload-joe-rimsky", # Replace with your own username
    version="0.0.1",
    author="Joseph Rimsky",
    author_email="jrmedia@joerimsky.com",
    description="Tool used to populate a Slack workspace with emojis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoeRimsky/Slackmojis-Webscraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)