from setuptools import setup, find_packages

setup(
    name="clean_folder",
    version="0.0.6",
    description="Clean you'r PC",
    url="https://github.com/Chypas/clean_folder",
    author="Ovcharenko_04",
    author_email="Ovcharenko_04@example.com",
    license="MIT",
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    include_package_data=True,
    entry_points={"console_scripts": ["clean = clean_folder.clean:clean"]}
        
)
