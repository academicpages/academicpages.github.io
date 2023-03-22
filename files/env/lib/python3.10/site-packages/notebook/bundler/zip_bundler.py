# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import os
import io
import zipfile
import notebook.bundler.tools as tools

def _jupyter_bundlerextension_paths():
    """Metadata for notebook bundlerextension"""
    return [{
            'name': 'notebook_zip_download',
            'label': 'IPython Notebook bundle (.zip)',
            'module_name': 'notebook.bundler.zip_bundler',
            'group': 'download'
    }]

def bundle(handler, model):
    """Create a zip file containing the original notebook and files referenced
    from it. Retain the referenced files in paths relative to the notebook.
    Return the zip as a file download. 
    
    Assumes the notebook and other files are all on local disk.
    
    Parameters
    ----------
    handler : tornado.web.RequestHandler
        Handler that serviced the bundle request
    model : dict
        Notebook model from the configured ContentManager
    """
    abs_nb_path = os.path.join(handler.settings['contents_manager'].root_dir,
        model['path'])
    notebook_filename = model['name']
    notebook_name = os.path.splitext(notebook_filename)[0] 

    # Headers
    zip_filename = os.path.splitext(notebook_name)[0] + '.zip'
    handler.set_attachment_header(zip_filename)
    handler.set_header('Content-Type', 'application/zip')

    # Get associated files
    ref_filenames = tools.get_file_references(abs_nb_path, 4)

    # Prepare the zip file
    zip_buffer = io.BytesIO()
    zipf = zipfile.ZipFile(zip_buffer, mode='w', compression=zipfile.ZIP_DEFLATED)
    zipf.write(abs_nb_path, notebook_filename)

    notebook_dir = os.path.dirname(abs_nb_path)
    for nb_relative_filename in ref_filenames:
        # Build absolute path to file on disk
        abs_fn = os.path.join(notebook_dir, nb_relative_filename)
        # Store file under path relative to notebook 
        zipf.write(abs_fn, nb_relative_filename)

    zipf.close()

    # Return the buffer value as the response
    handler.finish(zip_buffer.getvalue())