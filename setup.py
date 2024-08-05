from setuptools import setup, find_packages

setup(
    name="image-sequence-gif",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Pillow",
    ],
    entry_points={
        "console_scripts": [
            "image-sequence-gif = image_sequence_gif.image_sequence_gif:main",
        ],
    },
    author="Emmanuel Pilande",
    author_email="epilande@gmail.com",
    description="A script to create a GIF from a directory of images.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/epilande/image-sequence-gif",
    python_requires=">=3.6",
)
