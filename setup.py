import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygranso",
    version="0.0.1",
    author="Tim Mitchell and Buyun Liang",
    author_email="liang664@umn.edu, tim@timmitchell.com",
    description="PyGRANSO: A PyTorch-enabled port of GRANSO with auto-differentiation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sun-umn/PyGRANSO",
    project_urls={
        "Bug Tracker": "https://github.com/sun-umn/PyGRANSO/issues",
    },
    package_dir={"": "pygranso"},
    packages=setuptools.find_packages(where="pygranso"),
    python_requires=">=3.9",
    install_requires=[
        "osqp >= 0.6.2",
        "numpy >= 1.20.3",
        "scipy >= 1.7.1",
        "pytorch >= 1.9.0",
        "notebook >= 6.4.5"
    ],
)