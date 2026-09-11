For trained model please find in https://ummoodle.um.edu.mo/mod/assign/view.php?id=1199216



pre-train datasets and trained models: 
# Get trained models
The model file is too large to upload to github or ummoodle. Please find these models and datasets from:
https://pan.quark.cn/s/df3b98bbca07 

Unzip the files and copy files inside CISC7021-Applied-NLP-Assignment1-models/ into models/ folder. Copy data file to ModelAndDatasets/data folder

# Start the project
## Create virtual environment
We highly suggest you to create a virtual environment to run this project.
```
python -m venv venv
venv\Scripts\activate
```
## Install requirements
```
pip install -r requirements.txt
```
Plese be notice that I am using cuda version 13.2. Please check your own cuda version and install the right pytorch with cuda.

## Start jupyter notebook
```
jupyter notebook
```
or 
```
jupyter server --ServerApp.allow_remote_access True
```
if you want to remotely access the jupyter notebook
