#-*- coding: utf-8 -*-
import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk",
    version="0.0.1",

    description="The CDK stack for provisioning alarm-to-slack service",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "cdk"},
    packages=setuptools.find_packages(where="cdk"),

    install_requires=[
        "aws-cdk.core==1.120.0",
        "aws-cdk.aws_sns==1.120.0",
        "aws-cdk.aws_sns_subscriptions==1.120.0",
        "aws-cdk.aws_sqs==1.120.0",
        "aws-cdk.aws_lambda==1.120.0",
        "aws-cdk.aws_lambda_python==1.120.0",
        "python-dotenv"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
