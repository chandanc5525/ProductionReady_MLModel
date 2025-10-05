# ML_ProductionCode_BootCamp

---

## Prepared By: Chandan Chaudhari

---

## BootCamp Introduction:

Machine Learning in Production

This repository is part of the ML in Production course, which focuses on deploying machine learning models in real-world, production environments.

---

## Course Overview

The course is designed to bridge the gap between building machine learning models and deploying them at scale. It emphasizes the transformation of ML models into operational microservices and explores the tools, practices, and infrastructure necessary for successful deployment and integration.

---

## What You'll Learn

- Best practices for model deployment

- Building ML services using modern frameworks

- Serving models via APIs (e.g., Flask, FastAPI)

- Model versioning and lifecycle management

- Monitoring and maintaining deployed models

- Working with Docker and container orchestration tools

- CI/CD pipelines for ML workflows


---


## Key Topics

- Model Serialization (Pickle, Joblib)

- REST API Development

- Containerization with Docker

- Deployment Strategies (Local, Cloud, Kubernetes)

- Data Ingestion and Preprocessing Pipelines

- Model Monitoring and Logging

- Reproducibility and Environment Management

---

## Poetry vs Conda – Dependency & Environment Management

This project uses [Poetry](https://python-poetry.org/) for managing dependencies, virtual environments, and packaging instead of Conda.

Below is a comparison to highlight the differences and explain why Poetry was chosen for this ML production code bootcamp.

---

## Comparison Table

| Feature                         | Poetry                                              | Conda                                             |
|---------------------------------|-----------------------------------------------------|---------------------------------------------------|
| Language Support                | Python-only                                         | Multi-language (Python, R, C/C++, etc.)           |
| Dependency Source               | PyPI (Python Package Index)                        | Conda Channels (e.g. conda-forge, defaults)       |
| Environment Management          | Built-in (virtualenv or system)                    | Built-in (conda environments)                     |
| Lockfile Support                | Yes (`poetry.lock`)                                | Yes (`environment.yml`, but looser pinning)       |
| Packaging & Publishing          | Full support for Python packaging                  | Not designed for packaging                        |
| Speed of Dependency Resolution  | Fast (especially with Poetry 1.5+)                  | Slower with complex environments                  |
| Binary/Non-Python Packages      | Limited                                             | Strong support (e.g., CUDA, OpenCV)               |
| Project Scripts / CLI Hooks     | Supported via `[tool.poetry.scripts]`              | Not supported natively                            |
| Reproducibility Across Systems  | Strong                                              | Good                                              |

---

## Why This Project Uses Poetry

- Clean and simple Python dependency management with `pyproject.toml`
- Reproducibility ensured via `poetry.lock`
- Faster setup for Python-only machine learning workflows
- Ideal for production-ready Python packaging and deployment
- Easy integration with development tools like `pytest`, `black`, and `mypy`
- Avoids system-level package dependencies when not required

---

## Project Setup Instructions

1. Install Poetry (only once):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
