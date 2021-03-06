import os
from pynwb import load_namespaces, get_class

# Set path of the namespace.yaml file to the expected install location
ndx_cell_explorer_specpath = os.path.join(
    os.path.dirname(__file__),
    'spec',
    'ndx-cell-explorer.namespace.yaml'
)

# If the extension has not been installed yet but we are running directly from
# the git repo
if not os.path.exists(ndx_cell_explorer_specpath):
    ndx_cell_explorer_specpath = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', '..',
        'spec',
        'ndx-cell-explorer.namespace.yaml'
    ))

# Load the namespace
load_namespaces(ndx_cell_explorer_specpath)

# TODO: import your classes here or define your class using get_class to make
# them accessible at the package level
CellExplorerGeneral = get_class('CellExplorerGeneral', 'ndx-cell-explorer')
