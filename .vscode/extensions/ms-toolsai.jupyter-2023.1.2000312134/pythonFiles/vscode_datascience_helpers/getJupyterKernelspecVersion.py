# Check whether kernelspec module exists.
import sys
import jupyter_client
import jupyter_client.kernelspec

sys.stdout.write(jupyter_client.__version__)
sys.stdout.flush()
