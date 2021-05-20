# toucan_presentation


## Clone repository:
SSH:<br />
<code>git clone git@github.com:robwysze/toucan_presentation.git</code><br/>
HTTPS:<br />
<code>git clone --branch https://github.com/robwysze/toucan_presentation.git</code>

1. __Conda__:

  - __Linux__:
    - [Install conda on your Linux](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html "Install conda on your Linux").
    - Creating a conda environment using the attached yaml file.\
        <code>conda env create -f environment.yml</code>
- __Windows__:
  - [Install conda on your Windows](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html "Install conda on your Windows").
  - Remove *google-cloud-sdk* from dependencies in *environment.yml*
  - Creating a conda environment using the attached yaml file.\
    <code>conda env create -f environment.yml</code>
    
2. __DVC__:  
   <code> conda install -c conda-forge mamba # installs much faster than conda</code>  
   <code> mamba install -c conda-forge dvc </code>