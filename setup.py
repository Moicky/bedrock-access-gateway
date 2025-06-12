from setuptools import setup, find_packages

setup(
    name="bedrock-openai-proxy",
    version="1.0.0",
    description="OpenAI-compatible API proxy for AWS Bedrock",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.12",
    install_requires=[
        "fastapi",
        "uvicorn",
        "boto3",
        "botocore",
        "pydantic",
        "tiktoken",
        "numpy",
        "requests",
        "mangum",
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
            "mypy",
        ]
    },
    entry_points={
        "console_scripts": [
            "bedrock-proxy=api.app:main",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
)
