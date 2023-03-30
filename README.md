# openai


env OPENAI_API_KEY={your_key}


conda create --name openai python=3.10
conda activate openai
conda install -c conda-forge jupyterlab
conda install -c conda-forge ipywidgets
conda install -c conda-forge openai



export OPENAI_API_KEY={you api key here}
jupyter-lab .

!pip install openai
%env OPENAI_API_KEY={your api key}