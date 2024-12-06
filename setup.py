from setuptools import setup, find_packages

setup(
    name="hackathon_project",  # Replace with your project name
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "sentence-transformers==2.2.2",
        "langchain",
        "flask",
        "pypdf",
        "python-dotenv",
        "pinecone[grpc]",
        "langchain-pinecone",
        "langchain_community",
        "langchain_openai",
        "langchain_experimental",
    ],
)