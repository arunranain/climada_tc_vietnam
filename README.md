# climada_tc_vietnam
CLIMADA python repository with changes to core for implementation of Tropical Cyclone hazard across Vietnam

In order to replicate the results, or explore the risk of tropcial cyclones in Vietnam, please install CLIMADA-1.5.1 first from https://github.com/CLIMADA-project/climada_python/releases/tag/v1.5.1. Instructions of installation could be found via https://github.com/CLIMADA-project/climada_python/blob/main/doc/guide/install.rst

Based on the CLIMADA model, please implement the following changes:

IMPORTANT NOTE: Before making changes, backup of CLIMADA original files is strongly recommended.

1. Download the files provided here in the climada_tc_vietnam project

2. Open the folder named "climada/hazard". Copy the files inside and paste them under the directory "climada_python-1.5.1/climada/hazard", so the file "__init__.py", "tc_clim_change.py", and the folder "centroids" will be replaced, while a new file called "tc_surge" will be added.

3. Open the folder named "climada/util" downloaded from this "climada_tc_vietnam" project. Copt the files inside and paste them under the directory "climada_python-1.5.1/climada/util", so the files "constants.py" and "coordinates.py" are updated.

4. Open the folder named "data" and move the folder "addon" under the directory "climada_python-1.5.1/data".

Now you could initiate your Jupyter Notebook in the climada environment and run the codes stored in "CRA_VNM_JupyterNotebook".
