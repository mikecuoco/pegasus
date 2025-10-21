import logging
import pandas as pd
from typing import Union
from pegasusio import MultimodalData, UnimodalData, timer

logger = logging.getLogger(__name__)


@timer(logger=logger)
def convert_to_seurat(
    data: Union[MultimodalData, UnimodalData],
    rds_filename: str,
) -> None:
    """Convert a Pegasus data object to a Seurat object and save it as an RDS file.
    
    This function converts a Pegasus/AnnData object to a Seurat object using rpy2 
    and saves it to an RDS file that can be loaded in R.

    Parameters
    ----------
    data: ``MultimodalData`` or ``UnimodalData``
        Annotated data matrix with rows for cells and columns for genes.

    rds_filename: ``str``
        Output filename for the RDS file containing the Seurat object.

    Returns
    -------
    ``None``

    The Seurat object is saved to the specified RDS file.

    Examples
    --------
    >>> pg.convert_to_seurat(data, "output.rds")
    
    Notes
    -----
    This function requires R to be installed with the SeuratObject package, 
    and the Python packages rpy2 to be installed.
    
    You can install the required Python package with::
    
        pip install rpy2
    
    And install the required R package with::
    
        R -e "install.packages('SeuratObject')"
    """
    try:
        from rpy2.robjects.packages import importr
        from rpy2.robjects import pandas2ri
        from rpy2.robjects.conversion import localconverter
    except ImportError:
        import sys
        logger.error("Need rpy2! Try 'pip install rpy2'.")
        sys.exit(-1)

    # Import R's 'base' and 'Seurat' packages as Python objects
    try:
        base = importr('base')
        seurat = importr('SeuratObject')
    except Exception as e:
        import sys
        logger.error(f"Failed to import R packages. Make sure R and SeuratObject are installed: {e}")
        sys.exit(-1)

    logger.info("Starting conversion from Pegasus to Seurat.")

    logger.info("Extracting data matrix, cell names, gene names, and metadata.")
    df = data.X.transpose().toarray()
    cells = data.obs.index.to_list()
    genes = data.var.index.to_list()
    metadata = data.obs

    # Use the localconverter context manager for the conversion
    logger.info("Converting data to R objects.")
    with localconverter(pandas2ri.converter):
        # The conversion from pandas to R happens safely inside this block
        rdf = pandas2ri.py2rpy(pd.DataFrame(df, index=genes, columns=cells))
        r_metadata = pandas2ri.py2rpy(metadata)

    # Create the Seurat object using the converted R objects
    logger.info("Creating Seurat object.")
    seurat_obj = seurat.CreateSeuratObject(
        counts=rdf, 
        meta_data=r_metadata
    )

    # Save the Seurat object to an RDS file
    logger.info(f"Saving Seurat object to {rds_filename}.")
    base.saveRDS(seurat_obj, file=rds_filename)
    logger.info("Conversion complete."),
