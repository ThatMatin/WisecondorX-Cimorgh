FROM conda/miniconda3
RUN conda install -f -c conda-forge -c bioconda wisecondorx
ENTRYPOINT [ "WisecondorX" ]
