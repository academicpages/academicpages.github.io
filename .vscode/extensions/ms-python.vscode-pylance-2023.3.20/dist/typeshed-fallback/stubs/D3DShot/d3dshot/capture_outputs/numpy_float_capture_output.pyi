from d3dshot.capture_outputs.numpy_capture_output import NumpyCaptureOutput

# stub_uploader doesn't allow numpy because D3DShot doesn't declare it as a dependency
# this CaptureOutput should be float based
class NumpyFloatCaptureOutput(NumpyCaptureOutput): ...
