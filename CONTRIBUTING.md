# Contributing to Remote Instrumentation Guide

Thank you for considering contributing to this project! Your help is greatly appreciated. Below is a guide to get you started with contributing effectively.

## How to Contribute

1. **Fork the repository:**  
   Fork this repository to your own GitHub account and clone it to your local machine.

2. **Set up the environment:**  
   Install the required dependencies by following the instructions below.

3. **Make your changes:**
   - Follow the existing documentation structure.
   - Ensure all example scripts are stored in the `src/` folder.
   - Ensure that all code examples and documentation are up to date with the latest version of QCoDeS.
   - If you’re adding new documentation pages, ensure they are linked in the `mkdocs.yml` file for easy navigation.

4. **Submit a Pull Request:**  
   When your changes are ready, submit a pull request with a clear description of what you’ve added or changed.

## Setting Up the Environment

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/barreralab/remote-instrumentation-guide.git
   ```

2. Navigate to the project directory:

   ```bash
   cd remote-instrumentation-guide
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Serve the documentation locally:

   ```bash
   mkdocs serve
   ```

   You can now view the documentation in your browser at `http://localhost:8000`.

## Code Style

- Ensure any code is well-commented and follows Python best practices (PEP 8).
- Python scripts should be formatted with tools like `black` and checked with `flake8`.

## Reporting Issues

If you encounter any bugs or issues, feel free to create an issue on GitHub and provide as much detail as possible.

## Code of Conduct

Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming environment for everyone.