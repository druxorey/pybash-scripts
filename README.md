
<h1 align="center">PyBash Scripts</h1>

<p align="center">
<a href="#repository-structure"><img src="https://img.shields.io/badge/structure-BD93F9?style=for-the-badge"></a>
<a href="#how-to-execute-scripts"><img src="https://img.shields.io/badge/how%20to%20run-BD93F9?style=for-the-badge"></a>
</p>

<p align="center">A collection of multi-languages scripts to help in your daily tasks</p>

This is a dedicated space where we house a collection of scripts written in Bash and Python, plus other languages. These scripts serve a dual purpose, they are designed to automate various tasks, making your life easier, and they also serve as learning resources for those interested in getting to grips with Bash and Python scripting.

## Repository Structure

There is a directory for each programming language, and within each directory, there are different subdirectories for different types of scripts.

## How To Execute Scripts

### Bash

To execute a Bash script, navigate to the directory containing the script and use the following command:

    bash script-name.sh

### C++

To execute a C++ script, navigate to the directory containing the script and compile it with `g++` (or any other C++ compiler) using the following command:

    g++ script-name.cpp -o script-compiled

Then run it with the next command:

    ./script-name

### Golang

To execute a Go script, navigate to the directory containing the script and compile it with `go` using the following command:

    go build -o script-compiled script-name.cpp 

Then run it with the next command:

    ./script-name

### Python

To execute a Python script, navigate to the directory containing the script and use the following command:

    python3 script-name.py

### Rust

To execute a Rust script, navigate to the directory containing the script and compile it with `rust` using the following command:

    rustc script-name.rs -o script-compiled

Then run it with the next command:

    ./script-name

## Contribute

If you want to add new scripts or improve existing ones, follow these steps:

1. Open an issue to discuss the changes.
2. Fork this repository.
3. Create a new branch for your contribution: `git checkout -b your-branch-name`.
4. Make your changes.
5. Commit your changes, for example: `git commit -m 'fix(python): dirbyte output message.'`.
6. Push your changes to your forked repository: `git push origin your-branch-name`.
7. Open a Pull Request in this repository and reference the original issue.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for more details.
