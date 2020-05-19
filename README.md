# N of one
Self-experimentation.

## Setup
First make sure you have python3 , pip and virtualenv installed.
### setting up a virtual environment
Execute the following commands:
```
virtualenv -p python3 venv
```
by now you have a `venv` file containing the python environment. To activate it use:
```
source venv/bin/activate
```

### setting up requirements`
```
pip install -r requirements.txt
```
### setting up notebook
install `ipykernel
```
python -m ipykernel install --user --name=nofone
```
You can replace `nofone` by another name.

You can now run jupyter using:
```
jupyter notebook
```
To start a new notebook, make sure you choose the right environment `nofone` or whichever name you chose in the ipykernel command above.
