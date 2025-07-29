from setuptools import setup, find_packages 
setup(
    name = "Gen-Ai project",
    version  = '0.0.0',
    author = "Sumit kumar",
    author_email = "kumarsumit33688@gmail.com",
    description = "Gen-Ai project",
    packages = find_packages(where="src"),
    package_dir={"": "src"},
    install_requires = [
        "fastapi",
        "uvicorn",
    ]
)