from setuptools import setup, find_packages

setup(
    name = "clean_folder",
    version = "0.0.5",
    description = "Clean you'r PC",
    url = "https://github.com/Chypas/Projects/tree/main/home_work_6",
    author = "Ovcharenko_04",
    author_email = "Ovcharenko_04@example.com",
    license = "MIT",
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
    ],
    package_dir = {"": "clean_folder"},
    packages = find_packages(where = "clean_folder"),
    pythor_requires = ">=3.7",
    include_package_data = True,
    entry_points = {"console_script" : ["clean = clean_folder.clean:clean"]}
        
)