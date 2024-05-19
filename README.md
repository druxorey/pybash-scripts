## PyBash Scripts

Welcome to the 'pybash-scripts' repository. This is a dedicated space where we house a collection of scripts written in Bash and Python. These scripts serve a dual purpose - they are designed to automate various tasks, making your life easier, and they also serve as learning resources for those interested in getting to grips with Bash and Python scripting.

## Repository Structure

- `bash/`: Contains Bash scripts. 
- `c++/`: Contains C++ scripts. 
- `golang/`: Contains Go scripts. 
- `python/`: Contains Python scripts. 
- `rust/`: Contains Rust scripts. 

The `learning` folder contains scripts for understanding the language.

## How to Execute Scripts

### Bash Scripts

To execute a Bash script, navigate to the directory containing the script and use the following command:

    bash script-name.sh

or

    sh script-name.sh

### C++ Scripts

To execute a C++ script, navigate to the directory containing the script and comile it with the 'g++' package using the following command:

    g++ script-name.cpp -o script-compiled

Then run it with the next command:

    ./script-name

### Go Scripts

To execute a Go script, navigate to the directory containing the script and comile it with the 'go' package using the following command:

    go build -o script-compiled script-name.cpp 

Then run it with the next command:

    ./script-name

### Python Scripts

To execute a Python script, navigate to the directory containing the script and use the following command:

    python3 script-name.py

### Python scripts with a requirements.txt file

Some Python scripts have a requirements.txt file. These scripts should be run in a virtual environment with the specified packages installed. Here’s a quick tutorial:

1) Create a virtual environment:
    
        python -m venv env

2) Activate the virtual environment:
   
    - On Windows: `.\env\Scripts\activate`

    - On Unix or MacOS: `source env/bin/activate`

3) Install the required packages:

        pip install -r requirements.txt

Now you can run your script:

    python3 script-name.py

**WARNING:** Some programs may not work correctly on Windows as they execute Unix commands. They may need to be modified for correct execution.

### Rust Scripts

To execute a Rust script, navigate to the directory containing the script and comile it with the 'rust' package using the following command:

    rustc script-name.rs -o script-compiled

Then run it with the next command:

    ./script-name

## License

This project is licensed under the GPL-3.0 License. See the LICENSE file for more details.
