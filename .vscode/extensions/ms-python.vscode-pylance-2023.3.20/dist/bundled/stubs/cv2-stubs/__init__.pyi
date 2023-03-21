# Python: 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
# Library: cv2, version: 4.4.0
# Module: cv2.cv2, version: 4.4.0
import typing
import builtins as _mod_builtins
import cv2 as _mod_cv2
import numpy as np

Mat = np.ndarray[int, np.dtype[np.generic]]

ACCESS_FAST: int
ACCESS_MASK: int
ACCESS_READ: int
ACCESS_RW: int
ACCESS_WRITE: int
ADAPTIVE_THRESH_GAUSSIAN_C: int
ADAPTIVE_THRESH_MEAN_C: int
AGAST_FEATURE_DETECTOR_AGAST_5_8: int
AGAST_FEATURE_DETECTOR_AGAST_7_12D: int
AGAST_FEATURE_DETECTOR_AGAST_7_12S: int
AGAST_FEATURE_DETECTOR_NONMAX_SUPPRESSION: int
AGAST_FEATURE_DETECTOR_OAST_9_16: int
AGAST_FEATURE_DETECTOR_THRESHOLD: int
AKAZE = _mod_cv2.AKAZE
AKAZE_DESCRIPTOR_KAZE: int
AKAZE_DESCRIPTOR_KAZE_UPRIGHT: int
AKAZE_DESCRIPTOR_MLDB: int
AKAZE_DESCRIPTOR_MLDB_UPRIGHT: int
def AKAZE_create(descriptor_type=..., descriptor_size=..., descriptor_channels=..., threshold=..., nOctaves=..., nOctaveLayers=..., diffusivity=...) -> typing.Any:
    'AKAZE_create([, descriptor_type[, descriptor_size[, descriptor_channels[, threshold[, nOctaves[, nOctaveLayers[, diffusivity]]]]]]]) -> retval\n.   @brief The AKAZE constructor\n.   \n.       @param descriptor_type Type of the extracted descriptor: DESCRIPTOR_KAZE,\n.       DESCRIPTOR_KAZE_UPRIGHT, DESCRIPTOR_MLDB or DESCRIPTOR_MLDB_UPRIGHT.\n.       @param descriptor_size Size of the descriptor in bits. 0 -\\> Full size\n.       @param descriptor_channels Number of channels in the descriptor (1, 2, 3)\n.       @param threshold Detector response threshold to accept point\n.       @param nOctaves Maximum octave evolution of the image\n.       @param nOctaveLayers Default number of sublevels per scale level\n.       @param diffusivity Diffusivity type. DIFF_PM_G1, DIFF_PM_G2, DIFF_WEICKERT or\n.       DIFF_CHARBONNIER'
    ...

AgastFeatureDetector = _mod_cv2.AgastFeatureDetector
AgastFeatureDetector_AGAST_5_8: int
AgastFeatureDetector_AGAST_7_12d: int
AgastFeatureDetector_AGAST_7_12s: int
AgastFeatureDetector_NONMAX_SUPPRESSION: int
AgastFeatureDetector_OAST_9_16: int
AgastFeatureDetector_THRESHOLD: int
def AgastFeatureDetector_create(threshold=..., nonmaxSuppression=..., type=...) -> typing.Any:
    'AgastFeatureDetector_create([, threshold[, nonmaxSuppression[, type]]]) -> retval\n.'
    ...

Algorithm = _mod_cv2.Algorithm
AlignExposures = _mod_cv2.AlignExposures
AlignMTB = _mod_cv2.AlignMTB
AsyncArray = _mod_cv2.AsyncArray
BFMatcher = _mod_cv2.BFMatcher
def BFMatcher_create(normType: int = ..., crossCheck=...) -> typing.Any:
    "BFMatcher_create([, normType[, crossCheck]]) -> retval\n.   @brief Brute-force matcher create method.\n.       @param normType One of NORM_L1, NORM_L2, NORM_HAMMING, NORM_HAMMING2. L1 and L2 norms are\n.       preferable choices for SIFT and SURF descriptors, NORM_HAMMING should be used with ORB, BRISK and\n.       BRIEF, NORM_HAMMING2 should be used with ORB when WTA_K==3 or 4 (see ORB::ORB constructor\n.       description).\n.       @param crossCheck If it is false, this is will be default BFMatcher behaviour when it finds the k\n.       nearest neighbors for each query descriptor. If crossCheck==true, then the knnMatch() method with\n.       k=1 will only return pairs (i,j) such that for i-th query descriptor the j-th descriptor in the\n.       matcher's collection is the nearest and vice versa, i.e. the BFMatcher will only return consistent\n.       pairs. Such technique usually produces best results with minimal number of outliers when there are\n.       enough matches. This is alternative to the ratio test, used by D. Lowe in SIFT paper."
    ...

BORDER_CONSTANT: int
BORDER_DEFAULT: int
BORDER_ISOLATED: int
BORDER_REFLECT: int
BORDER_REFLECT101: int
BORDER_REFLECT_101: int
BORDER_REPLICATE: int
BORDER_TRANSPARENT: int
BORDER_WRAP: int
BOWImgDescriptorExtractor = _mod_cv2.BOWImgDescriptorExtractor
BOWKMeansTrainer = _mod_cv2.BOWKMeansTrainer
BOWTrainer = _mod_cv2.BOWTrainer
BRISK = _mod_cv2.BRISK
def BRISK_create(thresh=..., octaves=..., patternScale=...) -> typing.Any:
    'BRISK_create([, thresh[, octaves[, patternScale]]]) -> retval\n.   @brief The BRISK constructor\n.   \n.       @param thresh AGAST detection threshold score.\n.       @param octaves detection octaves. Use 0 to do single scale.\n.       @param patternScale apply this scale to the pattern used for sampling the neighbourhood of a\n.       keypoint.\n\n\n\nBRISK_create(radiusList, numberList[, dMax[, dMin[, indexChange]]]) -> retval\n.   @brief The BRISK constructor for a custom pattern\n.   \n.       @param radiusList defines the radii (in pixels) where the samples around a keypoint are taken (for\n.       keypoint scale 1).\n.       @param numberList defines the number of sampling points on the sampling circle. Must be the same\n.       size as radiusList..\n.       @param dMax threshold for the short pairings used for descriptor formation (in pixels for keypoint\n.       scale 1).\n.       @param dMin threshold for the long pairings used for orientation determination (in pixels for\n.       keypoint scale 1).\n.   @param indexChange index remapping of the bits.\n\n\n\nBRISK_create(thresh, octaves, radiusList, numberList[, dMax[, dMin[, indexChange]]]) -> retval\n.   @brief The BRISK constructor for a custom pattern, detection threshold and octaves\n.   \n.       @param thresh AGAST detection threshold score.\n.       @param octaves detection octaves. Use 0 to do single scale.\n.       @param radiusList defines the radii (in pixels) where the samples around a keypoint are taken (for\n.       keypoint scale 1).\n.       @param numberList defines the number of sampling points on the sampling circle. Must be the same\n.       size as radiusList..\n.       @param dMax threshold for the short pairings used for descriptor formation (in pixels for keypoint\n.       scale 1).\n.       @param dMin threshold for the long pairings used for orientation determination (in pixels for\n.       keypoint scale 1).\n.   @param indexChange index remapping of the bits.'
    ...

BackgroundSubtractor = _mod_cv2.BackgroundSubtractor
BackgroundSubtractorKNN = _mod_cv2.BackgroundSubtractorKNN
BackgroundSubtractorMOG2 = _mod_cv2.BackgroundSubtractorMOG2
BaseCascadeClassifier = _mod_cv2.BaseCascadeClassifier
CALIB_CB_ACCURACY: int
CALIB_CB_ADAPTIVE_THRESH: int
CALIB_CB_ASYMMETRIC_GRID: int
CALIB_CB_CLUSTERING: int
CALIB_CB_EXHAUSTIVE: int
CALIB_CB_FAST_CHECK: int
CALIB_CB_FILTER_QUADS: int
CALIB_CB_LARGER: int
CALIB_CB_MARKER: int
CALIB_CB_NORMALIZE_IMAGE: int
CALIB_CB_SYMMETRIC_GRID: int
CALIB_FIX_ASPECT_RATIO: int
CALIB_FIX_FOCAL_LENGTH: int
CALIB_FIX_INTRINSIC: int
CALIB_FIX_K1: int
CALIB_FIX_K2: int
CALIB_FIX_K3: int
CALIB_FIX_K4: int
CALIB_FIX_K5: int
CALIB_FIX_K6: int
CALIB_FIX_PRINCIPAL_POINT: int
CALIB_FIX_S1_S2_S3_S4: int
CALIB_FIX_TANGENT_DIST: int
CALIB_FIX_TAUX_TAUY: int
CALIB_HAND_EYE_ANDREFF: int
CALIB_HAND_EYE_DANIILIDIS: int
CALIB_HAND_EYE_HORAUD: int
CALIB_HAND_EYE_PARK: int
CALIB_HAND_EYE_TSAI: int
CALIB_NINTRINSIC: int
CALIB_RATIONAL_MODEL: int
CALIB_SAME_FOCAL_LENGTH: int
CALIB_THIN_PRISM_MODEL: int
CALIB_TILTED_MODEL: int
CALIB_USE_EXTRINSIC_GUESS: int
CALIB_USE_INTRINSIC_GUESS: int
CALIB_USE_LU: int
CALIB_USE_QR: int
CALIB_ZERO_DISPARITY: int
CALIB_ZERO_TANGENT_DIST: int
CAP_ANDROID: int
CAP_ANY: int
CAP_ARAVIS: int
CAP_AVFOUNDATION: int
CAP_CMU1394: int
CAP_DC1394: int
CAP_DSHOW: int
CAP_FFMPEG: int
CAP_FIREWARE: int
CAP_FIREWIRE: int
CAP_GIGANETIX: int
CAP_GPHOTO2: int
CAP_GSTREAMER: int
CAP_IEEE1394: int
CAP_IMAGES: int
CAP_INTELPERC: int
CAP_INTELPERC_DEPTH_GENERATOR: int
CAP_INTELPERC_DEPTH_MAP: int
CAP_INTELPERC_GENERATORS_MASK: int
CAP_INTELPERC_IMAGE: int
CAP_INTELPERC_IMAGE_GENERATOR: int
CAP_INTELPERC_IR_GENERATOR: int
CAP_INTELPERC_IR_MAP: int
CAP_INTELPERC_UVDEPTH_MAP: int
CAP_INTEL_MFX: int
CAP_MSMF: int
CAP_OPENCV_MJPEG: int
CAP_OPENNI: int
CAP_OPENNI2: int
CAP_OPENNI2_ASUS: int
CAP_OPENNI_ASUS: int
CAP_OPENNI_BGR_IMAGE: int
CAP_OPENNI_DEPTH_GENERATOR: int
CAP_OPENNI_DEPTH_GENERATOR_BASELINE: int
CAP_OPENNI_DEPTH_GENERATOR_FOCAL_LENGTH: int
CAP_OPENNI_DEPTH_GENERATOR_PRESENT: int
CAP_OPENNI_DEPTH_GENERATOR_REGISTRATION: int
CAP_OPENNI_DEPTH_GENERATOR_REGISTRATION_ON: int
CAP_OPENNI_DEPTH_MAP: int
CAP_OPENNI_DISPARITY_MAP: int
CAP_OPENNI_DISPARITY_MAP_32F: int
CAP_OPENNI_GENERATORS_MASK: int
CAP_OPENNI_GRAY_IMAGE: int
CAP_OPENNI_IMAGE_GENERATOR: int
CAP_OPENNI_IMAGE_GENERATOR_OUTPUT_MODE: int
CAP_OPENNI_IMAGE_GENERATOR_PRESENT: int
CAP_OPENNI_IR_GENERATOR: int
CAP_OPENNI_IR_GENERATOR_PRESENT: int
CAP_OPENNI_IR_IMAGE: int
CAP_OPENNI_POINT_CLOUD_MAP: int
CAP_OPENNI_QVGA_30HZ: int
CAP_OPENNI_QVGA_60HZ: int
CAP_OPENNI_SXGA_15HZ: int
CAP_OPENNI_SXGA_30HZ: int
CAP_OPENNI_VALID_DEPTH_MASK: int
CAP_OPENNI_VGA_30HZ: int
CAP_PROP_APERTURE: int
CAP_PROP_ARAVIS_AUTOTRIGGER: int
CAP_PROP_AUTOFOCUS: int
CAP_PROP_AUTO_EXPOSURE: int
CAP_PROP_AUTO_WB: int
CAP_PROP_BACKEND: int
CAP_PROP_BACKLIGHT: int
CAP_PROP_BITRATE: int
CAP_PROP_BRIGHTNESS: int
CAP_PROP_BUFFERSIZE: int
CAP_PROP_CHANNEL: int
CAP_PROP_CODEC_PIXEL_FORMAT: int
CAP_PROP_CONTRAST: int
CAP_PROP_CONVERT_RGB: int
CAP_PROP_DC1394_MAX: int
CAP_PROP_DC1394_MODE_AUTO: int
CAP_PROP_DC1394_MODE_MANUAL: int
CAP_PROP_DC1394_MODE_ONE_PUSH_AUTO: int
CAP_PROP_DC1394_OFF: int
CAP_PROP_EXPOSURE: int
CAP_PROP_EXPOSUREPROGRAM: int
CAP_PROP_FOCUS: int
CAP_PROP_FORMAT: int
CAP_PROP_FOURCC: int
CAP_PROP_FPS: int
CAP_PROP_FRAME_COUNT: int
CAP_PROP_FRAME_HEIGHT: int
CAP_PROP_FRAME_WIDTH: int
CAP_PROP_GAIN: int
CAP_PROP_GAMMA: int
CAP_PROP_GIGA_FRAME_HEIGH_MAX: int
CAP_PROP_GIGA_FRAME_OFFSET_X: int
CAP_PROP_GIGA_FRAME_OFFSET_Y: int
CAP_PROP_GIGA_FRAME_SENS_HEIGH: int
CAP_PROP_GIGA_FRAME_SENS_WIDTH: int
CAP_PROP_GIGA_FRAME_WIDTH_MAX: int
CAP_PROP_GPHOTO2_COLLECT_MSGS: int
CAP_PROP_GPHOTO2_FLUSH_MSGS: int
CAP_PROP_GPHOTO2_PREVIEW: int
CAP_PROP_GPHOTO2_RELOAD_CONFIG: int
CAP_PROP_GPHOTO2_RELOAD_ON_CHANGE: int
CAP_PROP_GPHOTO2_WIDGET_ENUMERATE: int
CAP_PROP_GSTREAMER_QUEUE_LENGTH: int
CAP_PROP_GUID: int
CAP_PROP_HUE: int
CAP_PROP_IMAGES_BASE: int
CAP_PROP_IMAGES_LAST: int
CAP_PROP_INTELPERC_DEPTH_CONFIDENCE_THRESHOLD: int
CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_HORZ: int
CAP_PROP_INTELPERC_DEPTH_FOCAL_LENGTH_VERT: int
CAP_PROP_INTELPERC_DEPTH_LOW_CONFIDENCE_VALUE: int
CAP_PROP_INTELPERC_DEPTH_SATURATION_VALUE: int
CAP_PROP_INTELPERC_PROFILE_COUNT: int
CAP_PROP_INTELPERC_PROFILE_IDX: int
CAP_PROP_IOS_DEVICE_EXPOSURE: int
CAP_PROP_IOS_DEVICE_FLASH: int
CAP_PROP_IOS_DEVICE_FOCUS: int
CAP_PROP_IOS_DEVICE_TORCH: int
CAP_PROP_IOS_DEVICE_WHITEBALANCE: int
CAP_PROP_IRIS: int
CAP_PROP_ISO_SPEED: int
CAP_PROP_MODE: int
CAP_PROP_MONOCHROME: int
CAP_PROP_OPENNI2_MIRROR: int
CAP_PROP_OPENNI2_SYNC: int
CAP_PROP_OPENNI_APPROX_FRAME_SYNC: int
CAP_PROP_OPENNI_BASELINE: int
CAP_PROP_OPENNI_CIRCLE_BUFFER: int
CAP_PROP_OPENNI_FOCAL_LENGTH: int
CAP_PROP_OPENNI_FRAME_MAX_DEPTH: int
CAP_PROP_OPENNI_GENERATOR_PRESENT: int
CAP_PROP_OPENNI_MAX_BUFFER_SIZE: int
CAP_PROP_OPENNI_MAX_TIME_DURATION: int
CAP_PROP_OPENNI_OUTPUT_MODE: int
CAP_PROP_OPENNI_REGISTRATION: int
CAP_PROP_OPENNI_REGISTRATION_ON: int
CAP_PROP_PAN: int
CAP_PROP_POS_AVI_RATIO: int
CAP_PROP_POS_FRAMES: int
CAP_PROP_POS_MSEC: int
CAP_PROP_PVAPI_BINNINGX: int
CAP_PROP_PVAPI_BINNINGY: int
CAP_PROP_PVAPI_DECIMATIONHORIZONTAL: int
CAP_PROP_PVAPI_DECIMATIONVERTICAL: int
CAP_PROP_PVAPI_FRAMESTARTTRIGGERMODE: int
CAP_PROP_PVAPI_MULTICASTIP: int
CAP_PROP_PVAPI_PIXELFORMAT: int
CAP_PROP_RECTIFICATION: int
CAP_PROP_ROLL: int
CAP_PROP_SAR_DEN: int
CAP_PROP_SAR_NUM: int
CAP_PROP_SATURATION: int
CAP_PROP_SETTINGS: int
CAP_PROP_SHARPNESS: int
CAP_PROP_SPEED: int
CAP_PROP_TEMPERATURE: int
CAP_PROP_TILT: int
CAP_PROP_TRIGGER: int
CAP_PROP_TRIGGER_DELAY: int
CAP_PROP_VIEWFINDER: int
CAP_PROP_WB_TEMPERATURE: int
CAP_PROP_WHITE_BALANCE_BLUE_U: int
CAP_PROP_WHITE_BALANCE_RED_V: int
CAP_PROP_XI_ACQ_BUFFER_SIZE: int
CAP_PROP_XI_ACQ_BUFFER_SIZE_UNIT: int
CAP_PROP_XI_ACQ_FRAME_BURST_COUNT: int
CAP_PROP_XI_ACQ_TIMING_MODE: int
CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_COMMIT: int
CAP_PROP_XI_ACQ_TRANSPORT_BUFFER_SIZE: int
CAP_PROP_XI_AEAG: int
CAP_PROP_XI_AEAG_LEVEL: int
CAP_PROP_XI_AEAG_ROI_HEIGHT: int
CAP_PROP_XI_AEAG_ROI_OFFSET_X: int
CAP_PROP_XI_AEAG_ROI_OFFSET_Y: int
CAP_PROP_XI_AEAG_ROI_WIDTH: int
CAP_PROP_XI_AE_MAX_LIMIT: int
CAP_PROP_XI_AG_MAX_LIMIT: int
CAP_PROP_XI_APPLY_CMS: int
CAP_PROP_XI_AUTO_BANDWIDTH_CALCULATION: int
CAP_PROP_XI_AUTO_WB: int
CAP_PROP_XI_AVAILABLE_BANDWIDTH: int
CAP_PROP_XI_BINNING_HORIZONTAL: int
CAP_PROP_XI_BINNING_PATTERN: int
CAP_PROP_XI_BINNING_SELECTOR: int
CAP_PROP_XI_BINNING_VERTICAL: int
CAP_PROP_XI_BPC: int
CAP_PROP_XI_BUFFERS_QUEUE_SIZE: int
CAP_PROP_XI_BUFFER_POLICY: int
CAP_PROP_XI_CC_MATRIX_00: int
CAP_PROP_XI_CC_MATRIX_01: int
CAP_PROP_XI_CC_MATRIX_02: int
CAP_PROP_XI_CC_MATRIX_03: int
CAP_PROP_XI_CC_MATRIX_10: int
CAP_PROP_XI_CC_MATRIX_11: int
CAP_PROP_XI_CC_MATRIX_12: int
CAP_PROP_XI_CC_MATRIX_13: int
CAP_PROP_XI_CC_MATRIX_20: int
CAP_PROP_XI_CC_MATRIX_21: int
CAP_PROP_XI_CC_MATRIX_22: int
CAP_PROP_XI_CC_MATRIX_23: int
CAP_PROP_XI_CC_MATRIX_30: int
CAP_PROP_XI_CC_MATRIX_31: int
CAP_PROP_XI_CC_MATRIX_32: int
CAP_PROP_XI_CC_MATRIX_33: int
CAP_PROP_XI_CHIP_TEMP: int
CAP_PROP_XI_CMS: int
CAP_PROP_XI_COLOR_FILTER_ARRAY: int
CAP_PROP_XI_COLUMN_FPN_CORRECTION: int
CAP_PROP_XI_COOLING: int
CAP_PROP_XI_COUNTER_SELECTOR: int
CAP_PROP_XI_COUNTER_VALUE: int
CAP_PROP_XI_DATA_FORMAT: int
CAP_PROP_XI_DEBOUNCE_EN: int
CAP_PROP_XI_DEBOUNCE_POL: int
CAP_PROP_XI_DEBOUNCE_T0: int
CAP_PROP_XI_DEBOUNCE_T1: int
CAP_PROP_XI_DEBUG_LEVEL: int
CAP_PROP_XI_DECIMATION_HORIZONTAL: int
CAP_PROP_XI_DECIMATION_PATTERN: int
CAP_PROP_XI_DECIMATION_SELECTOR: int
CAP_PROP_XI_DECIMATION_VERTICAL: int
CAP_PROP_XI_DEFAULT_CC_MATRIX: int
CAP_PROP_XI_DEVICE_MODEL_ID: int
CAP_PROP_XI_DEVICE_RESET: int
CAP_PROP_XI_DEVICE_SN: int
CAP_PROP_XI_DOWNSAMPLING: int
CAP_PROP_XI_DOWNSAMPLING_TYPE: int
CAP_PROP_XI_EXPOSURE: int
CAP_PROP_XI_EXPOSURE_BURST_COUNT: int
CAP_PROP_XI_EXP_PRIORITY: int
CAP_PROP_XI_FFS_ACCESS_KEY: int
CAP_PROP_XI_FFS_FILE_ID: int
CAP_PROP_XI_FFS_FILE_SIZE: int
CAP_PROP_XI_FRAMERATE: int
CAP_PROP_XI_FREE_FFS_SIZE: int
CAP_PROP_XI_GAIN: int
CAP_PROP_XI_GAIN_SELECTOR: int
CAP_PROP_XI_GAMMAC: int
CAP_PROP_XI_GAMMAY: int
CAP_PROP_XI_GPI_LEVEL: int
CAP_PROP_XI_GPI_MODE: int
CAP_PROP_XI_GPI_SELECTOR: int
CAP_PROP_XI_GPO_MODE: int
CAP_PROP_XI_GPO_SELECTOR: int
CAP_PROP_XI_HDR: int
CAP_PROP_XI_HDR_KNEEPOINT_COUNT: int
CAP_PROP_XI_HDR_T1: int
CAP_PROP_XI_HDR_T2: int
CAP_PROP_XI_HEIGHT: int
CAP_PROP_XI_HOUS_BACK_SIDE_TEMP: int
CAP_PROP_XI_HOUS_TEMP: int
CAP_PROP_XI_HW_REVISION: int
CAP_PROP_XI_IMAGE_BLACK_LEVEL: int
CAP_PROP_XI_IMAGE_DATA_BIT_DEPTH: int
CAP_PROP_XI_IMAGE_DATA_FORMAT: int
CAP_PROP_XI_IMAGE_DATA_FORMAT_RGB32_ALPHA: int
CAP_PROP_XI_IMAGE_IS_COLOR: int
CAP_PROP_XI_IMAGE_PAYLOAD_SIZE: int
CAP_PROP_XI_IS_COOLED: int
CAP_PROP_XI_IS_DEVICE_EXIST: int
CAP_PROP_XI_KNEEPOINT1: int
CAP_PROP_XI_KNEEPOINT2: int
CAP_PROP_XI_LED_MODE: int
CAP_PROP_XI_LED_SELECTOR: int
CAP_PROP_XI_LENS_APERTURE_VALUE: int
CAP_PROP_XI_LENS_FEATURE: int
CAP_PROP_XI_LENS_FEATURE_SELECTOR: int
CAP_PROP_XI_LENS_FOCAL_LENGTH: int
CAP_PROP_XI_LENS_FOCUS_DISTANCE: int
CAP_PROP_XI_LENS_FOCUS_MOVE: int
CAP_PROP_XI_LENS_FOCUS_MOVEMENT_VALUE: int
CAP_PROP_XI_LENS_MODE: int
CAP_PROP_XI_LIMIT_BANDWIDTH: int
CAP_PROP_XI_LUT_EN: int
CAP_PROP_XI_LUT_INDEX: int
CAP_PROP_XI_LUT_VALUE: int
CAP_PROP_XI_MANUAL_WB: int
CAP_PROP_XI_OFFSET_X: int
CAP_PROP_XI_OFFSET_Y: int
CAP_PROP_XI_OUTPUT_DATA_BIT_DEPTH: int
CAP_PROP_XI_OUTPUT_DATA_PACKING: int
CAP_PROP_XI_OUTPUT_DATA_PACKING_TYPE: int
CAP_PROP_XI_RECENT_FRAME: int
CAP_PROP_XI_REGION_MODE: int
CAP_PROP_XI_REGION_SELECTOR: int
CAP_PROP_XI_ROW_FPN_CORRECTION: int
CAP_PROP_XI_SENSOR_BOARD_TEMP: int
CAP_PROP_XI_SENSOR_CLOCK_FREQ_HZ: int
CAP_PROP_XI_SENSOR_CLOCK_FREQ_INDEX: int
CAP_PROP_XI_SENSOR_DATA_BIT_DEPTH: int
CAP_PROP_XI_SENSOR_FEATURE_SELECTOR: int
CAP_PROP_XI_SENSOR_FEATURE_VALUE: int
CAP_PROP_XI_SENSOR_MODE: int
CAP_PROP_XI_SENSOR_OUTPUT_CHANNEL_COUNT: int
CAP_PROP_XI_SENSOR_TAPS: int
CAP_PROP_XI_SHARPNESS: int
CAP_PROP_XI_SHUTTER_TYPE: int
CAP_PROP_XI_TARGET_TEMP: int
CAP_PROP_XI_TEST_PATTERN: int
CAP_PROP_XI_TEST_PATTERN_GENERATOR_SELECTOR: int
CAP_PROP_XI_TIMEOUT: int
CAP_PROP_XI_TRANSPORT_PIXEL_FORMAT: int
CAP_PROP_XI_TRG_DELAY: int
CAP_PROP_XI_TRG_SELECTOR: int
CAP_PROP_XI_TRG_SOFTWARE: int
CAP_PROP_XI_TRG_SOURCE: int
CAP_PROP_XI_TS_RST_MODE: int
CAP_PROP_XI_TS_RST_SOURCE: int
CAP_PROP_XI_USED_FFS_SIZE: int
CAP_PROP_XI_WB_KB: int
CAP_PROP_XI_WB_KG: int
CAP_PROP_XI_WB_KR: int
CAP_PROP_XI_WIDTH: int
CAP_PROP_ZOOM: int
CAP_PVAPI: int
CAP_PVAPI_DECIMATION_2OUTOF16: int
CAP_PVAPI_DECIMATION_2OUTOF4: int
CAP_PVAPI_DECIMATION_2OUTOF8: int
CAP_PVAPI_DECIMATION_OFF: int
CAP_PVAPI_FSTRIGMODE_FIXEDRATE: int
CAP_PVAPI_FSTRIGMODE_FREERUN: int
CAP_PVAPI_FSTRIGMODE_SOFTWARE: int
CAP_PVAPI_FSTRIGMODE_SYNCIN1: int
CAP_PVAPI_FSTRIGMODE_SYNCIN2: int
CAP_PVAPI_PIXELFORMAT_BAYER16: int
CAP_PVAPI_PIXELFORMAT_BAYER8: int
CAP_PVAPI_PIXELFORMAT_BGR24: int
CAP_PVAPI_PIXELFORMAT_BGRA32: int
CAP_PVAPI_PIXELFORMAT_MONO16: int
CAP_PVAPI_PIXELFORMAT_MONO8: int
CAP_PVAPI_PIXELFORMAT_RGB24: int
CAP_PVAPI_PIXELFORMAT_RGBA32: int
CAP_QT: int
CAP_REALSENSE: int
CAP_UNICAP: int
CAP_V4L: int
CAP_V4L2: int
CAP_VFW: int
CAP_WINRT: int
CAP_XIAPI: int
CAP_XINE: int
CASCADE_DO_CANNY_PRUNING: int
CASCADE_DO_ROUGH_SEARCH: int
CASCADE_FIND_BIGGEST_OBJECT: int
CASCADE_SCALE_IMAGE: int
CCL_DEFAULT: int
CCL_GRANA: int
CCL_WU: int
CC_STAT_AREA: int
CC_STAT_HEIGHT: int
CC_STAT_LEFT: int
CC_STAT_MAX: int
CC_STAT_TOP: int
CC_STAT_WIDTH: int
CHAIN_APPROX_NONE: int
CHAIN_APPROX_SIMPLE: int
CHAIN_APPROX_TC89_KCOS: int
CHAIN_APPROX_TC89_L1: int
CIRCLES_GRID_FINDER_PARAMETERS_ASYMMETRIC_GRID: int
CIRCLES_GRID_FINDER_PARAMETERS_SYMMETRIC_GRID: int
CLAHE = _mod_cv2.CLAHE
CMP_EQ: int
CMP_GE: int
CMP_GT: int
CMP_LE: int
CMP_LT: int
CMP_NE: int
COLORMAP_AUTUMN: int
COLORMAP_BONE: int
COLORMAP_CIVIDIS: int
COLORMAP_COOL: int
COLORMAP_DEEPGREEN: int
COLORMAP_HOT: int
COLORMAP_HSV: int
COLORMAP_INFERNO: int
COLORMAP_JET: int
COLORMAP_MAGMA: int
COLORMAP_OCEAN: int
COLORMAP_PARULA: int
COLORMAP_PINK: int
COLORMAP_PLASMA: int
COLORMAP_RAINBOW: int
COLORMAP_SPRING: int
COLORMAP_SUMMER: int
COLORMAP_TURBO: int
COLORMAP_TWILIGHT: int
COLORMAP_TWILIGHT_SHIFTED: int
COLORMAP_VIRIDIS: int
COLORMAP_WINTER: int
COLOR_BAYER_BG2BGR: int
COLOR_BAYER_BG2BGRA: int
COLOR_BAYER_BG2BGR_EA: int
COLOR_BAYER_BG2BGR_VNG: int
COLOR_BAYER_BG2GRAY: int
COLOR_BAYER_BG2RGB: int
COLOR_BAYER_BG2RGBA: int
COLOR_BAYER_BG2RGB_EA: int
COLOR_BAYER_BG2RGB_VNG: int
COLOR_BAYER_GB2BGR: int
COLOR_BAYER_GB2BGRA: int
COLOR_BAYER_GB2BGR_EA: int
COLOR_BAYER_GB2BGR_VNG: int
COLOR_BAYER_GB2GRAY: int
COLOR_BAYER_GB2RGB: int
COLOR_BAYER_GB2RGBA: int
COLOR_BAYER_GB2RGB_EA: int
COLOR_BAYER_GB2RGB_VNG: int
COLOR_BAYER_GR2BGR: int
COLOR_BAYER_GR2BGRA: int
COLOR_BAYER_GR2BGR_EA: int
COLOR_BAYER_GR2BGR_VNG: int
COLOR_BAYER_GR2GRAY: int
COLOR_BAYER_GR2RGB: int
COLOR_BAYER_GR2RGBA: int
COLOR_BAYER_GR2RGB_EA: int
COLOR_BAYER_GR2RGB_VNG: int
COLOR_BAYER_RG2BGR: int
COLOR_BAYER_RG2BGRA: int
COLOR_BAYER_RG2BGR_EA: int
COLOR_BAYER_RG2BGR_VNG: int
COLOR_BAYER_RG2GRAY: int
COLOR_BAYER_RG2RGB: int
COLOR_BAYER_RG2RGBA: int
COLOR_BAYER_RG2RGB_EA: int
COLOR_BAYER_RG2RGB_VNG: int
COLOR_BGR2BGR555: int
COLOR_BGR2BGR565: int
COLOR_BGR2BGRA: int
COLOR_BGR2GRAY: int
COLOR_BGR2HLS: int
COLOR_BGR2HLS_FULL: int
COLOR_BGR2HSV: int
COLOR_BGR2HSV_FULL: int
COLOR_BGR2LAB: int
COLOR_BGR2LUV: int
COLOR_BGR2Lab: int
COLOR_BGR2Luv: int
COLOR_BGR2RGB: int
COLOR_BGR2RGBA: int
COLOR_BGR2XYZ: int
COLOR_BGR2YCR_CB: int
COLOR_BGR2YCrCb: int
COLOR_BGR2YUV: int
COLOR_BGR2YUV_I420: int
COLOR_BGR2YUV_IYUV: int
COLOR_BGR2YUV_YV12: int
COLOR_BGR5552BGR: int
COLOR_BGR5552BGRA: int
COLOR_BGR5552GRAY: int
COLOR_BGR5552RGB: int
COLOR_BGR5552RGBA: int
COLOR_BGR5652BGR: int
COLOR_BGR5652BGRA: int
COLOR_BGR5652GRAY: int
COLOR_BGR5652RGB: int
COLOR_BGR5652RGBA: int
COLOR_BGRA2BGR: int
COLOR_BGRA2BGR555: int
COLOR_BGRA2BGR565: int
COLOR_BGRA2GRAY: int
COLOR_BGRA2RGB: int
COLOR_BGRA2RGBA: int
COLOR_BGRA2YUV_I420: int
COLOR_BGRA2YUV_IYUV: int
COLOR_BGRA2YUV_YV12: int
COLOR_BayerBG2BGR: int
COLOR_BayerBG2BGRA: int
COLOR_BayerBG2BGR_EA: int
COLOR_BayerBG2BGR_VNG: int
COLOR_BayerBG2GRAY: int
COLOR_BayerBG2RGB: int
COLOR_BayerBG2RGBA: int
COLOR_BayerBG2RGB_EA: int
COLOR_BayerBG2RGB_VNG: int
COLOR_BayerGB2BGR: int
COLOR_BayerGB2BGRA: int
COLOR_BayerGB2BGR_EA: int
COLOR_BayerGB2BGR_VNG: int
COLOR_BayerGB2GRAY: int
COLOR_BayerGB2RGB: int
COLOR_BayerGB2RGBA: int
COLOR_BayerGB2RGB_EA: int
COLOR_BayerGB2RGB_VNG: int
COLOR_BayerGR2BGR: int
COLOR_BayerGR2BGRA: int
COLOR_BayerGR2BGR_EA: int
COLOR_BayerGR2BGR_VNG: int
COLOR_BayerGR2GRAY: int
COLOR_BayerGR2RGB: int
COLOR_BayerGR2RGBA: int
COLOR_BayerGR2RGB_EA: int
COLOR_BayerGR2RGB_VNG: int
COLOR_BayerRG2BGR: int
COLOR_BayerRG2BGRA: int
COLOR_BayerRG2BGR_EA: int
COLOR_BayerRG2BGR_VNG: int
COLOR_BayerRG2GRAY: int
COLOR_BayerRG2RGB: int
COLOR_BayerRG2RGBA: int
COLOR_BayerRG2RGB_EA: int
COLOR_BayerRG2RGB_VNG: int
COLOR_COLORCVT_MAX: int
COLOR_GRAY2BGR: int
COLOR_GRAY2BGR555: int
COLOR_GRAY2BGR565: int
COLOR_GRAY2BGRA: int
COLOR_GRAY2RGB: int
COLOR_GRAY2RGBA: int
COLOR_HLS2BGR: int
COLOR_HLS2BGR_FULL: int
COLOR_HLS2RGB: int
COLOR_HLS2RGB_FULL: int
COLOR_HSV2BGR: int
COLOR_HSV2BGR_FULL: int
COLOR_HSV2RGB: int
COLOR_HSV2RGB_FULL: int
COLOR_LAB2BGR: int
COLOR_LAB2LBGR: int
COLOR_LAB2LRGB: int
COLOR_LAB2RGB: int
COLOR_LBGR2LAB: int
COLOR_LBGR2LUV: int
COLOR_LBGR2Lab: int
COLOR_LBGR2Luv: int
COLOR_LRGB2LAB: int
COLOR_LRGB2LUV: int
COLOR_LRGB2Lab: int
COLOR_LRGB2Luv: int
COLOR_LUV2BGR: int
COLOR_LUV2LBGR: int
COLOR_LUV2LRGB: int
COLOR_LUV2RGB: int
COLOR_Lab2BGR: int
COLOR_Lab2LBGR: int
COLOR_Lab2LRGB: int
COLOR_Lab2RGB: int
COLOR_Luv2BGR: int
COLOR_Luv2LBGR: int
COLOR_Luv2LRGB: int
COLOR_Luv2RGB: int
COLOR_M_RGBA2RGBA: int
COLOR_RGB2BGR: int
COLOR_RGB2BGR555: int
COLOR_RGB2BGR565: int
COLOR_RGB2BGRA: int
COLOR_RGB2GRAY: int
COLOR_RGB2HLS: int
COLOR_RGB2HLS_FULL: int
COLOR_RGB2HSV: int
COLOR_RGB2HSV_FULL: int
COLOR_RGB2LAB: int
COLOR_RGB2LUV: int
COLOR_RGB2Lab: int
COLOR_RGB2Luv: int
COLOR_RGB2RGBA: int
COLOR_RGB2XYZ: int
COLOR_RGB2YCR_CB: int
COLOR_RGB2YCrCb: int
COLOR_RGB2YUV: int
COLOR_RGB2YUV_I420: int
COLOR_RGB2YUV_IYUV: int
COLOR_RGB2YUV_YV12: int
COLOR_RGBA2BGR: int
COLOR_RGBA2BGR555: int
COLOR_RGBA2BGR565: int
COLOR_RGBA2BGRA: int
COLOR_RGBA2GRAY: int
COLOR_RGBA2M_RGBA: int
COLOR_RGBA2RGB: int
COLOR_RGBA2YUV_I420: int
COLOR_RGBA2YUV_IYUV: int
COLOR_RGBA2YUV_YV12: int
COLOR_RGBA2mRGBA: int
COLOR_XYZ2BGR: int
COLOR_XYZ2RGB: int
COLOR_YCR_CB2BGR: int
COLOR_YCR_CB2RGB: int
COLOR_YCrCb2BGR: int
COLOR_YCrCb2RGB: int
COLOR_YUV2BGR: int
COLOR_YUV2BGRA_I420: int
COLOR_YUV2BGRA_IYUV: int
COLOR_YUV2BGRA_NV12: int
COLOR_YUV2BGRA_NV21: int
COLOR_YUV2BGRA_UYNV: int
COLOR_YUV2BGRA_UYVY: int
COLOR_YUV2BGRA_Y422: int
COLOR_YUV2BGRA_YUNV: int
COLOR_YUV2BGRA_YUY2: int
COLOR_YUV2BGRA_YUYV: int
COLOR_YUV2BGRA_YV12: int
COLOR_YUV2BGRA_YVYU: int
COLOR_YUV2BGR_I420: int
COLOR_YUV2BGR_IYUV: int
COLOR_YUV2BGR_NV12: int
COLOR_YUV2BGR_NV21: int
COLOR_YUV2BGR_UYNV: int
COLOR_YUV2BGR_UYVY: int
COLOR_YUV2BGR_Y422: int
COLOR_YUV2BGR_YUNV: int
COLOR_YUV2BGR_YUY2: int
COLOR_YUV2BGR_YUYV: int
COLOR_YUV2BGR_YV12: int
COLOR_YUV2BGR_YVYU: int
COLOR_YUV2GRAY_420: int
COLOR_YUV2GRAY_I420: int
COLOR_YUV2GRAY_IYUV: int
COLOR_YUV2GRAY_NV12: int
COLOR_YUV2GRAY_NV21: int
COLOR_YUV2GRAY_UYNV: int
COLOR_YUV2GRAY_UYVY: int
COLOR_YUV2GRAY_Y422: int
COLOR_YUV2GRAY_YUNV: int
COLOR_YUV2GRAY_YUY2: int
COLOR_YUV2GRAY_YUYV: int
COLOR_YUV2GRAY_YV12: int
COLOR_YUV2GRAY_YVYU: int
COLOR_YUV2RGB: int
COLOR_YUV2RGBA_I420: int
COLOR_YUV2RGBA_IYUV: int
COLOR_YUV2RGBA_NV12: int
COLOR_YUV2RGBA_NV21: int
COLOR_YUV2RGBA_UYNV: int
COLOR_YUV2RGBA_UYVY: int
COLOR_YUV2RGBA_Y422: int
COLOR_YUV2RGBA_YUNV: int
COLOR_YUV2RGBA_YUY2: int
COLOR_YUV2RGBA_YUYV: int
COLOR_YUV2RGBA_YV12: int
COLOR_YUV2RGBA_YVYU: int
COLOR_YUV2RGB_I420: int
COLOR_YUV2RGB_IYUV: int
COLOR_YUV2RGB_NV12: int
COLOR_YUV2RGB_NV21: int
COLOR_YUV2RGB_UYNV: int
COLOR_YUV2RGB_UYVY: int
COLOR_YUV2RGB_Y422: int
COLOR_YUV2RGB_YUNV: int
COLOR_YUV2RGB_YUY2: int
COLOR_YUV2RGB_YUYV: int
COLOR_YUV2RGB_YV12: int
COLOR_YUV2RGB_YVYU: int
COLOR_YUV420P2BGR: int
COLOR_YUV420P2BGRA: int
COLOR_YUV420P2GRAY: int
COLOR_YUV420P2RGB: int
COLOR_YUV420P2RGBA: int
COLOR_YUV420SP2BGR: int
COLOR_YUV420SP2BGRA: int
COLOR_YUV420SP2GRAY: int
COLOR_YUV420SP2RGB: int
COLOR_YUV420SP2RGBA: int
COLOR_YUV420p2BGR: int
COLOR_YUV420p2BGRA: int
COLOR_YUV420p2GRAY: int
COLOR_YUV420p2RGB: int
COLOR_YUV420p2RGBA: int
COLOR_YUV420sp2BGR: int
COLOR_YUV420sp2BGRA: int
COLOR_YUV420sp2GRAY: int
COLOR_YUV420sp2RGB: int
COLOR_YUV420sp2RGBA: int
COLOR_mRGBA2RGBA: int
CONTOURS_MATCH_I1: int
CONTOURS_MATCH_I2: int
CONTOURS_MATCH_I3: int
COVAR_COLS: int
COVAR_NORMAL: int
COVAR_ROWS: int
COVAR_SCALE: int
COVAR_SCRAMBLED: int
COVAR_USE_AVG: int
CV_16S: int
CV_16SC1: int
CV_16SC2: int
CV_16SC3: int
CV_16SC4: int
CV_16U: int
CV_16UC1: int
CV_16UC2: int
CV_16UC3: int
CV_16UC4: int
CV_32F: int
CV_32FC1: int
CV_32FC2: int
CV_32FC3: int
CV_32FC4: int
CV_32S: int
CV_32SC1: int
CV_32SC2: int
CV_32SC3: int
CV_32SC4: int
CV_64F: int
CV_64FC1: int
CV_64FC2: int
CV_64FC3: int
CV_64FC4: int
CV_8S: int
CV_8SC1: int
CV_8SC2: int
CV_8SC3: int
CV_8SC4: int
CV_8U: int
CV_8UC1: int
CV_8UC2: int
CV_8UC3: int
CV_8UC4: int
CalibrateCRF = _mod_cv2.CalibrateCRF
CalibrateDebevec = _mod_cv2.CalibrateDebevec
CalibrateRobertson = _mod_cv2.CalibrateRobertson
def CamShift(probImage, window, criteria) -> typing.Any:
    'CamShift(probImage, window, criteria) -> retval, window\n.   @brief Finds an object center, size, and orientation.\n.   \n.   @param probImage Back projection of the object histogram. See calcBackProject.\n.   @param window Initial search window.\n.   @param criteria Stop criteria for the underlying meanShift.\n.   returns\n.   (in old interfaces) Number of iterations CAMSHIFT took to converge\n.   The function implements the CAMSHIFT object tracking algorithm @cite Bradski98 . First, it finds an\n.   object center using meanShift and then adjusts the window size and finds the optimal rotation. The\n.   function returns the rotated rectangle structure that includes the object position, size, and\n.   orientation. The next position of the search window can be obtained with RotatedRect::boundingRect()\n.   \n.   See the OpenCV sample camshiftdemo.c that tracks colored objects.\n.   \n.   @note\n.   -   (Python) A sample explaining the camshift tracking algorithm can be found at\n.       opencv_source_code/samples/python/camshift.py'
    ...

def Canny(image: Mat, threshold1, threshold2, edges=..., apertureSize=..., L2gradient=...) -> typing.Any:
    'Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) -> edges\n.   @brief Finds edges in an image using the Canny algorithm @cite Canny86 .\n.   \n.   The function finds edges in the input image and marks them in the output map edges using the\n.   Canny algorithm. The smallest value between threshold1 and threshold2 is used for edge linking. The\n.   largest value is used to find initial segments of strong edges. See\n.   <http://en.wikipedia.org/wiki/Canny_edge_detector>\n.   \n.   @param image 8-bit input image.\n.   @param edges output edge map; single channels 8-bit image, which has the same size as image .\n.   @param threshold1 first threshold for the hysteresis procedure.\n.   @param threshold2 second threshold for the hysteresis procedure.\n.   @param apertureSize aperture size for the Sobel operator.\n.   @param L2gradient a flag, indicating whether a more accurate \\f$L_2\\f$ norm\n.   \\f$=\\sqrt{(dI/dx)^2 + (dI/dy)^2}\\f$ should be used to calculate the image gradient magnitude (\n.   L2gradient=true ), or whether the default \\f$L_1\\f$ norm \\f$=|dI/dx|+|dI/dy|\\f$ is enough (\n.   L2gradient=false ).\n\n\n\nCanny(dx, dy, threshold1, threshold2[, edges[, L2gradient]]) -> edges\n.   \\overload\n.   \n.   Finds edges in an image using the Canny algorithm with custom image gradient.\n.   \n.   @param dx 16-bit x derivative of input image (CV_16SC1 or CV_16SC3).\n.   @param dy 16-bit y derivative of input image (same type as dx).\n.   @param edges output edge map; single channels 8-bit image, which has the same size as image .\n.   @param threshold1 first threshold for the hysteresis procedure.\n.   @param threshold2 second threshold for the hysteresis procedure.\n.   @param L2gradient a flag, indicating whether a more accurate \\f$L_2\\f$ norm\n.   \\f$=\\sqrt{(dI/dx)^2 + (dI/dy)^2}\\f$ should be used to calculate the image gradient magnitude (\n.   L2gradient=true ), or whether the default \\f$L_1\\f$ norm \\f$=|dI/dx|+|dI/dy|\\f$ is enough (\n.   L2gradient=false ).'
    ...

CascadeClassifier = _mod_cv2.CascadeClassifier
def CascadeClassifier_convert(oldcascade, newcascade) -> typing.Any:
    'CascadeClassifier_convert(oldcascade, newcascade) -> retval\n.'
    ...

CirclesGridFinderParameters = _mod_cv2.CirclesGridFinderParameters
CirclesGridFinderParameters_ASYMMETRIC_GRID: int
CirclesGridFinderParameters_SYMMETRIC_GRID: int
DCT_INVERSE: int
DCT_ROWS: int
DECOMP_CHOLESKY: int
DECOMP_EIG: int
DECOMP_LU: int
DECOMP_NORMAL: int
DECOMP_QR: int
DECOMP_SVD: int
DESCRIPTOR_MATCHER_BRUTEFORCE: int
DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING: int
DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMINGLUT: int
DESCRIPTOR_MATCHER_BRUTEFORCE_L1: int
DESCRIPTOR_MATCHER_BRUTEFORCE_SL2: int
DESCRIPTOR_MATCHER_FLANNBASED: int
DFT_COMPLEX_INPUT: int
DFT_COMPLEX_OUTPUT: int
DFT_INVERSE: int
DFT_REAL_OUTPUT: int
DFT_ROWS: int
DFT_SCALE: int
DISOPTICAL_FLOW_PRESET_FAST: int
DISOPTICAL_FLOW_PRESET_MEDIUM: int
DISOPTICAL_FLOW_PRESET_ULTRAFAST: int
DISOpticalFlow = _mod_cv2.DISOpticalFlow
DISOpticalFlow_PRESET_FAST: int
DISOpticalFlow_PRESET_MEDIUM: int
DISOpticalFlow_PRESET_ULTRAFAST: int
def DISOpticalFlow_create(preset=...) -> typing.Any:
    'DISOpticalFlow_create([, preset]) -> retval\n.   @brief Creates an instance of DISOpticalFlow\n.   \n.       @param preset one of PRESET_ULTRAFAST, PRESET_FAST and PRESET_MEDIUM'
    ...

DIST_C: int
DIST_FAIR: int
DIST_HUBER: int
DIST_L1: int
DIST_L12: int
DIST_L2: int
DIST_LABEL_CCOMP: int
DIST_LABEL_PIXEL: int
DIST_MASK_3: int
DIST_MASK_5: int
DIST_MASK_PRECISE: int
DIST_USER: int
DIST_WELSCH: int
DMatch = _mod_cv2.DMatch
DRAW_MATCHES_FLAGS_DEFAULT: int
DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG: int
DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS: int
DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS: int
DenseOpticalFlow = _mod_cv2.DenseOpticalFlow
DescriptorMatcher = _mod_cv2.DescriptorMatcher
DescriptorMatcher_BRUTEFORCE: int
DescriptorMatcher_BRUTEFORCE_HAMMING: int
DescriptorMatcher_BRUTEFORCE_HAMMINGLUT: int
DescriptorMatcher_BRUTEFORCE_L1: int
DescriptorMatcher_BRUTEFORCE_SL2: int
DescriptorMatcher_FLANNBASED: int
def DescriptorMatcher_create(descriptorMatcherType) -> typing.Any:
    'DescriptorMatcher_create(descriptorMatcherType) -> retval\n.   @brief Creates a descriptor matcher of a given type with the default parameters (using default\n.       constructor).\n.   \n.       @param descriptorMatcherType Descriptor matcher type. Now the following matcher types are\n.       supported:\n.       -   `BruteForce` (it uses L2 )\n.       -   `BruteForce-L1`\n.       -   `BruteForce-Hamming`\n.       -   `BruteForce-Hamming(2)`\n.       -   `FlannBased`\n\n\n\nDescriptorMatcher_create(matcherType) -> retval\n.'
    ...

DrawMatchesFlags_DEFAULT: int
DrawMatchesFlags_DRAW_OVER_OUTIMG: int
DrawMatchesFlags_DRAW_RICH_KEYPOINTS: int
DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS: int
def EMD(signature1, signature2, distType, cost=..., lowerBound=..., flow=...) -> typing.Any:
    'EMD(signature1, signature2, distType[, cost[, lowerBound[, flow]]]) -> retval, lowerBound, flow\n.   @brief Computes the "minimal work" distance between two weighted point configurations.\n.   \n.   The function computes the earth mover distance and/or a lower boundary of the distance between the\n.   two weighted point configurations. One of the applications described in @cite RubnerSept98,\n.   @cite Rubner2000 is multi-dimensional histogram comparison for image retrieval. EMD is a transportation\n.   problem that is solved using some modification of a simplex algorithm, thus the complexity is\n.   exponential in the worst case, though, on average it is much faster. In the case of a real metric\n.   the lower boundary can be calculated even faster (using linear-time algorithm) and it can be used\n.   to determine roughly whether the two signatures are far enough so that they cannot relate to the\n.   same object.\n.   \n.   @param signature1 First signature, a \\f$\\texttt{size1}\\times \\texttt{dims}+1\\f$ floating-point matrix.\n.   Each row stores the point weight followed by the point coordinates. The matrix is allowed to have\n.   a single column (weights only) if the user-defined cost matrix is used. The weights must be\n.   non-negative and have at least one non-zero value.\n.   @param signature2 Second signature of the same format as signature1 , though the number of rows\n.   may be different. The total weights may be different. In this case an extra "dummy" point is added\n.   to either signature1 or signature2. The weights must be non-negative and have at least one non-zero\n.   value.\n.   @param distType Used metric. See #DistanceTypes.\n.   @param cost User-defined \\f$\\texttt{size1}\\times \\texttt{size2}\\f$ cost matrix. Also, if a cost matrix\n.   is used, lower boundary lowerBound cannot be calculated because it needs a metric function.\n.   @param lowerBound Optional input/output parameter: lower boundary of a distance between the two\n.   signatures that is a distance between mass centers. The lower boundary may not be calculated if\n.   the user-defined cost matrix is used, the total weights of point configurations are not equal, or\n.   if the signatures consist of weights only (the signature matrices have a single column). You\n.   **must** initialize \\*lowerBound . If the calculated distance between mass centers is greater or\n.   equal to \\*lowerBound (it means that the signatures are far enough), the function does not\n.   calculate EMD. In any case \\*lowerBound is set to the calculated distance between mass centers on\n.   return. Thus, if you want to calculate both distance between mass centers and EMD, \\*lowerBound\n.   should be set to 0.\n.   @param flow Resultant \\f$\\texttt{size1} \\times \\texttt{size2}\\f$ flow matrix: \\f$\\texttt{flow}_{i,j}\\f$ is\n.   a flow from \\f$i\\f$ -th point of signature1 to \\f$j\\f$ -th point of signature2 .'
    ...

EVENT_FLAG_ALTKEY: int
EVENT_FLAG_CTRLKEY: int
EVENT_FLAG_LBUTTON: int
EVENT_FLAG_MBUTTON: int
EVENT_FLAG_RBUTTON: int
EVENT_FLAG_SHIFTKEY: int
EVENT_LBUTTONDBLCLK: int
EVENT_LBUTTONDOWN: int
EVENT_LBUTTONUP: int
EVENT_MBUTTONDBLCLK: int
EVENT_MBUTTONDOWN: int
EVENT_MBUTTONUP: int
EVENT_MOUSEHWHEEL: int
EVENT_MOUSEMOVE: int
EVENT_MOUSEWHEEL: int
EVENT_RBUTTONDBLCLK: int
EVENT_RBUTTONDOWN: int
EVENT_RBUTTONUP: int
FAST_FEATURE_DETECTOR_FAST_N: int
FAST_FEATURE_DETECTOR_NONMAX_SUPPRESSION: int
FAST_FEATURE_DETECTOR_THRESHOLD: int
FAST_FEATURE_DETECTOR_TYPE_5_8: int
FAST_FEATURE_DETECTOR_TYPE_7_12: int
FAST_FEATURE_DETECTOR_TYPE_9_16: int
FILE_NODE_EMPTY: int
FILE_NODE_FLOAT: int
FILE_NODE_FLOW: int
FILE_NODE_INT: int
FILE_NODE_MAP: int
FILE_NODE_NAMED: int
FILE_NODE_NONE: int
FILE_NODE_REAL: int
FILE_NODE_SEQ: int
FILE_NODE_STR: int
FILE_NODE_STRING: int
FILE_NODE_TYPE_MASK: int
FILE_NODE_UNIFORM: int
FILE_STORAGE_APPEND: int
FILE_STORAGE_BASE64: int
FILE_STORAGE_FORMAT_AUTO: int
FILE_STORAGE_FORMAT_JSON: int
FILE_STORAGE_FORMAT_MASK: int
FILE_STORAGE_FORMAT_XML: int
FILE_STORAGE_FORMAT_YAML: int
FILE_STORAGE_INSIDE_MAP: int
FILE_STORAGE_MEMORY: int
FILE_STORAGE_NAME_EXPECTED: int
FILE_STORAGE_READ: int
FILE_STORAGE_UNDEFINED: int
FILE_STORAGE_VALUE_EXPECTED: int
FILE_STORAGE_WRITE: int
FILE_STORAGE_WRITE_BASE64: int
FILLED: int
FILTER_SCHARR: int
FLOODFILL_FIXED_RANGE: int
FLOODFILL_MASK_ONLY: int
FM_7POINT: int
FM_8POINT: int
FM_LMEDS: int
FM_RANSAC: int
FONT_HERSHEY_COMPLEX: int
FONT_HERSHEY_COMPLEX_SMALL: int
FONT_HERSHEY_DUPLEX: int
FONT_HERSHEY_PLAIN: int
FONT_HERSHEY_SCRIPT_COMPLEX: int
FONT_HERSHEY_SCRIPT_SIMPLEX: int
FONT_HERSHEY_SIMPLEX: int
FONT_HERSHEY_TRIPLEX: int
FONT_ITALIC: int
FORMATTER_FMT_C: int
FORMATTER_FMT_CSV: int
FORMATTER_FMT_DEFAULT: int
FORMATTER_FMT_MATLAB: int
FORMATTER_FMT_NUMPY: int
FORMATTER_FMT_PYTHON: int
FarnebackOpticalFlow = _mod_cv2.FarnebackOpticalFlow
def FarnebackOpticalFlow_create(numLevels=..., pyrScale=..., fastPyramids=..., winSize=..., numIters=..., polyN=..., polySigma=..., flags: int = ...) -> typing.Any:
    'FarnebackOpticalFlow_create([, numLevels[, pyrScale[, fastPyramids[, winSize[, numIters[, polyN[, polySigma[, flags]]]]]]]]) -> retval\n.'
    ...

FastFeatureDetector = _mod_cv2.FastFeatureDetector
FastFeatureDetector_FAST_N: int
FastFeatureDetector_NONMAX_SUPPRESSION: int
FastFeatureDetector_THRESHOLD: int
FastFeatureDetector_TYPE_5_8: int
FastFeatureDetector_TYPE_7_12: int
FastFeatureDetector_TYPE_9_16: int
def FastFeatureDetector_create(threshold=..., nonmaxSuppression=..., type=...) -> typing.Any:
    'FastFeatureDetector_create([, threshold[, nonmaxSuppression[, type]]]) -> retval\n.'
    ...

Feature2D = _mod_cv2.Feature2D
FileNode = _mod_cv2.FileNode
FileNode_EMPTY: int
FileNode_FLOAT: int
FileNode_FLOW: int
FileNode_INT: int
FileNode_MAP: int
FileNode_NAMED: int
FileNode_NONE: int
FileNode_REAL: int
FileNode_SEQ: int
FileNode_STR: int
FileNode_STRING: int
FileNode_TYPE_MASK: int
FileNode_UNIFORM: int
FileStorage = _mod_cv2.FileStorage
FileStorage_APPEND: int
FileStorage_BASE64: int
FileStorage_FORMAT_AUTO: int
FileStorage_FORMAT_JSON: int
FileStorage_FORMAT_MASK: int
FileStorage_FORMAT_XML: int
FileStorage_FORMAT_YAML: int
FileStorage_INSIDE_MAP: int
FileStorage_MEMORY: int
FileStorage_NAME_EXPECTED: int
FileStorage_READ: int
FileStorage_UNDEFINED: int
FileStorage_VALUE_EXPECTED: int
FileStorage_WRITE: int
FileStorage_WRITE_BASE64: int
FlannBasedMatcher = _mod_cv2.FlannBasedMatcher
def FlannBasedMatcher_create() -> typing.Any:
    'FlannBasedMatcher_create() -> retval\n.'
    ...

Formatter_FMT_C: int
Formatter_FMT_CSV: int
Formatter_FMT_DEFAULT: int
Formatter_FMT_MATLAB: int
Formatter_FMT_NUMPY: int
Formatter_FMT_PYTHON: int
GC_BGD: int
GC_EVAL: int
GC_EVAL_FREEZE_MODEL: int
GC_FGD: int
GC_INIT_WITH_MASK: int
GC_INIT_WITH_RECT: int
GC_PR_BGD: int
GC_PR_FGD: int
GEMM_1_T: int
GEMM_2_T: int
GEMM_3_T: int
GFTTDetector = _mod_cv2.GFTTDetector
def GFTTDetector_create(maxCorners=..., qualityLevel=..., minDistance=..., blockSize=..., useHarrisDetector=..., k=...) -> typing.Any:
    'GFTTDetector_create([, maxCorners[, qualityLevel[, minDistance[, blockSize[, useHarrisDetector[, k]]]]]]) -> retval\n.   \n\n\n\nGFTTDetector_create(maxCorners, qualityLevel, minDistance, blockSize, gradiantSize[, useHarrisDetector[, k]]) -> retval\n.'
    ...

def GaussianBlur(src: Mat, ksize, sigmaX, dts: Mat = ..., sigmaY=..., borderType=...) -> typing.Any:
    "GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst\n.   @brief Blurs an image using a Gaussian filter.\n.   \n.   The function convolves the source image with the specified Gaussian kernel. In-place filtering is\n.   supported.\n.   \n.   @param src input image; the image can have any number of channels, which are processed\n.   independently, but the depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.\n.   @param dst output image of the same size and type as src.\n.   @param ksize Gaussian kernel size. ksize.width and ksize.height can differ but they both must be\n.   positive and odd. Or, they can be zero's and then they are computed from sigma.\n.   @param sigmaX Gaussian kernel standard deviation in X direction.\n.   @param sigmaY Gaussian kernel standard deviation in Y direction; if sigmaY is zero, it is set to be\n.   equal to sigmaX, if both sigmas are zeros, they are computed from ksize.width and ksize.height,\n.   respectively (see #getGaussianKernel for details); to fully control the result regardless of\n.   possible future modifications of all this semantics, it is recommended to specify all of ksize,\n.   sigmaX, and sigmaY.\n.   @param borderType pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not supported.\n.   \n.   @sa  sepFilter2D, filter2D, blur, boxFilter, bilateralFilter, medianBlur"
    ...

GeneralizedHough = _mod_cv2.GeneralizedHough
GeneralizedHoughBallard = _mod_cv2.GeneralizedHoughBallard
GeneralizedHoughGuil = _mod_cv2.GeneralizedHoughGuil
HISTCMP_BHATTACHARYYA: int
HISTCMP_CHISQR: int
HISTCMP_CHISQR_ALT: int
HISTCMP_CORREL: int
HISTCMP_HELLINGER: int
HISTCMP_INTERSECT: int
HISTCMP_KL_DIV: int
HOGDESCRIPTOR_DEFAULT_NLEVELS: int
HOGDESCRIPTOR_DESCR_FORMAT_COL_BY_COL: int
HOGDESCRIPTOR_DESCR_FORMAT_ROW_BY_ROW: int
HOGDESCRIPTOR_L2HYS: int
HOGDescriptor = _mod_cv2.HOGDescriptor
HOGDescriptor_DEFAULT_NLEVELS: int
HOGDescriptor_DESCR_FORMAT_COL_BY_COL: int
HOGDescriptor_DESCR_FORMAT_ROW_BY_ROW: int
HOGDescriptor_L2Hys: int
def HOGDescriptor_getDaimlerPeopleDetector() -> typing.Any:
    'HOGDescriptor_getDaimlerPeopleDetector() -> retval\n.   @brief Returns coefficients of the classifier trained for people detection (for 48x96 windows).'
    ...

def HOGDescriptor_getDefaultPeopleDetector() -> typing.Any:
    'HOGDescriptor_getDefaultPeopleDetector() -> retval\n.   @brief Returns coefficients of the classifier trained for people detection (for 64x128 windows).'
    ...

HOUGH_GRADIENT: int
HOUGH_GRADIENT_ALT: int
HOUGH_MULTI_SCALE: int
HOUGH_PROBABILISTIC: int
HOUGH_STANDARD: int
def HoughCircles(image: Mat, method: int, dp, minDist, circles=..., param1=..., param2=..., minRadius=..., maxRadius=...) -> typing.Any:
    'HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) -> circles\n.   @brief Finds circles in a grayscale image using the Hough transform.\n.   \n.   The function finds circles in a grayscale image using a modification of the Hough transform.\n.   \n.   Example: :\n.   @include snippets/imgproc_HoughLinesCircles.cpp\n.   \n.   @note Usually the function detects the centers of circles well. However, it may fail to find correct\n.   radii. You can assist to the function by specifying the radius range ( minRadius and maxRadius ) if\n.   you know it. Or, in the case of #HOUGH_GRADIENT method you may set maxRadius to a negative number\n.   to return centers only without radius search, and find the correct radius using an additional procedure.\n.   \n.   It also helps to smooth image a bit unless it\'s already soft. For example,\n.   GaussianBlur() with 7x7 kernel and 1.5x1.5 sigma or similar blurring may help.\n.   \n.   @param image 8-bit, single-channel, grayscale input image.\n.   @param circles Output vector of found circles. Each vector is encoded as  3 or 4 element\n.   floating-point vector \\f$(x, y, radius)\\f$ or \\f$(x, y, radius, votes)\\f$ .\n.   @param method Detection method, see #HoughModes. The available methods are #HOUGH_GRADIENT and #HOUGH_GRADIENT_ALT.\n.   @param dp Inverse ratio of the accumulator resolution to the image resolution. For example, if\n.   dp=1 , the accumulator has the same resolution as the input image. If dp=2 , the accumulator has\n.   half as big width and height. For #HOUGH_GRADIENT_ALT the recommended value is dp=1.5,\n.   unless some small very circles need to be detected.\n.   @param minDist Minimum distance between the centers of the detected circles. If the parameter is\n.   too small, multiple neighbor circles may be falsely detected in addition to a true one. If it is\n.   too large, some circles may be missed.\n.   @param param1 First method-specific parameter. In case of #HOUGH_GRADIENT and #HOUGH_GRADIENT_ALT,\n.   it is the higher threshold of the two passed to the Canny edge detector (the lower one is twice smaller).\n.   Note that #HOUGH_GRADIENT_ALT uses #Scharr algorithm to compute image derivatives, so the threshold value\n.   shough normally be higher, such as 300 or normally exposed and contrasty images.\n.   @param param2 Second method-specific parameter. In case of #HOUGH_GRADIENT, it is the\n.   accumulator threshold for the circle centers at the detection stage. The smaller it is, the more\n.   false circles may be detected. Circles, corresponding to the larger accumulator values, will be\n.   returned first. In the case of #HOUGH_GRADIENT_ALT algorithm, this is the circle "perfectness" measure.\n.   The closer it to 1, the better shaped circles algorithm selects. In most cases 0.9 should be fine.\n.   If you want get better detection of small circles, you may decrease it to 0.85, 0.8 or even less.\n.   But then also try to limit the search range [minRadius, maxRadius] to avoid many false circles.\n.   @param minRadius Minimum circle radius.\n.   @param maxRadius Maximum circle radius. If <= 0, uses the maximum image dimension. If < 0, #HOUGH_GRADIENT returns\n.   centers without finding the radius. #HOUGH_GRADIENT_ALT always computes circle radiuses.\n.   \n.   @sa fitEllipse, minEnclosingCircle'
    ...

def HoughLines(image: Mat, rho, theta, threshold, lines=..., srn=..., stn=..., min_theta=..., max_theta=...) -> typing.Any:
    'HoughLines(image, rho, theta, threshold[, lines[, srn[, stn[, min_theta[, max_theta]]]]]) -> lines\n.   @brief Finds lines in a binary image using the standard Hough transform.\n.   \n.   The function implements the standard or standard multi-scale Hough transform algorithm for line\n.   detection. See <http://homepages.inf.ed.ac.uk/rbf/HIPR2/hough.htm> for a good explanation of Hough\n.   transform.\n.   \n.   @param image 8-bit, single-channel binary source image. The image may be modified by the function.\n.   @param lines Output vector of lines. Each line is represented by a 2 or 3 element vector\n.   \\f$(\\rho, \\theta)\\f$ or \\f$(\\rho, \\theta, \\textrm{votes})\\f$ . \\f$\\rho\\f$ is the distance from the coordinate origin \\f$(0,0)\\f$ (top-left corner of\n.   the image). \\f$\\theta\\f$ is the line rotation angle in radians (\n.   \\f$0 \\sim \\textrm{vertical line}, \\pi/2 \\sim \\textrm{horizontal line}\\f$ ).\n.   \\f$\\textrm{votes}\\f$ is the value of accumulator.\n.   @param rho Distance resolution of the accumulator in pixels.\n.   @param theta Angle resolution of the accumulator in radians.\n.   @param threshold Accumulator threshold parameter. Only those lines are returned that get enough\n.   votes ( \\f$>\\texttt{threshold}\\f$ ).\n.   @param srn For the multi-scale Hough transform, it is a divisor for the distance resolution rho .\n.   The coarse accumulator distance resolution is rho and the accurate accumulator resolution is\n.   rho/srn . If both srn=0 and stn=0 , the classical Hough transform is used. Otherwise, both these\n.   parameters should be positive.\n.   @param stn For the multi-scale Hough transform, it is a divisor for the distance resolution theta.\n.   @param min_theta For standard and multi-scale Hough transform, minimum angle to check for lines.\n.   Must fall between 0 and max_theta.\n.   @param max_theta For standard and multi-scale Hough transform, maximum angle to check for lines.\n.   Must fall between min_theta and CV_PI.'
    ...

def HoughLinesP(image: Mat, rho, theta, threshold, lines=..., minLineLength=..., maxLineGap=...) -> typing.Any:
    'HoughLinesP(image, rho, theta, threshold[, lines[, minLineLength[, maxLineGap]]]) -> lines\n.   @brief Finds line segments in a binary image using the probabilistic Hough transform.\n.   \n.   The function implements the probabilistic Hough transform algorithm for line detection, described\n.   in @cite Matas00\n.   \n.   See the line detection example below:\n.   @include snippets/imgproc_HoughLinesP.cpp\n.   This is a sample picture the function parameters have been tuned for:\n.   \n.   ![image](pics/building.jpg)\n.   \n.   And this is the output of the above program in case of the probabilistic Hough transform:\n.   \n.   ![image](pics/houghp.png)\n.   \n.   @param image 8-bit, single-channel binary source image. The image may be modified by the function.\n.   @param lines Output vector of lines. Each line is represented by a 4-element vector\n.   \\f$(x_1, y_1, x_2, y_2)\\f$ , where \\f$(x_1,y_1)\\f$ and \\f$(x_2, y_2)\\f$ are the ending points of each detected\n.   line segment.\n.   @param rho Distance resolution of the accumulator in pixels.\n.   @param theta Angle resolution of the accumulator in radians.\n.   @param threshold Accumulator threshold parameter. Only those lines are returned that get enough\n.   votes ( \\f$>\\texttt{threshold}\\f$ ).\n.   @param minLineLength Minimum line length. Line segments shorter than that are rejected.\n.   @param maxLineGap Maximum allowed gap between points on the same line to link them.\n.   \n.   @sa LineSegmentDetector'
    ...

def HoughLinesPointSet(_point, lines_max, threshold, min_rho, max_rho, rho_step, min_theta, max_theta, theta_step, _lines=...) -> typing.Any:
    "HoughLinesPointSet(_point, lines_max, threshold, min_rho, max_rho, rho_step, min_theta, max_theta, theta_step[, _lines]) -> _lines\n.   @brief Finds lines in a set of points using the standard Hough transform.\n.   \n.   The function finds lines in a set of points using a modification of the Hough transform.\n.   @include snippets/imgproc_HoughLinesPointSet.cpp\n.   @param _point Input vector of points. Each vector must be encoded as a Point vector \\f$(x,y)\\f$. Type must be CV_32FC2 or CV_32SC2.\n.   @param _lines Output vector of found lines. Each vector is encoded as a vector<Vec3d> \\f$(votes, rho, theta)\\f$.\n.   The larger the value of 'votes', the higher the reliability of the Hough line.\n.   @param lines_max Max count of hough lines.\n.   @param threshold Accumulator threshold parameter. Only those lines are returned that get enough\n.   votes ( \\f$>\\texttt{threshold}\\f$ )\n.   @param min_rho Minimum Distance value of the accumulator in pixels.\n.   @param max_rho Maximum Distance value of the accumulator in pixels.\n.   @param rho_step Distance resolution of the accumulator in pixels.\n.   @param min_theta Minimum angle value of the accumulator in radians.\n.   @param max_theta Maximum angle value of the accumulator in radians.\n.   @param theta_step Angle resolution of the accumulator in radians."
    ...

def HuMoments(m, hu=...) -> typing.Any:
    'HuMoments(m[, hu]) -> hu\n.   @overload'
    ...

IMREAD_ANYCOLOR: int
IMREAD_ANYDEPTH: int
IMREAD_COLOR: int
IMREAD_GRAYSCALE: int
IMREAD_IGNORE_ORIENTATION: int
IMREAD_LOAD_GDAL: int
IMREAD_REDUCED_COLOR_2: int
IMREAD_REDUCED_COLOR_4: int
IMREAD_REDUCED_COLOR_8: int
IMREAD_REDUCED_GRAYSCALE_2: int
IMREAD_REDUCED_GRAYSCALE_4: int
IMREAD_REDUCED_GRAYSCALE_8: int
IMREAD_UNCHANGED: int
IMWRITE_EXR_TYPE: int
IMWRITE_EXR_TYPE_FLOAT: int
IMWRITE_EXR_TYPE_HALF: int
IMWRITE_JPEG2000_COMPRESSION_X1000: int
IMWRITE_JPEG_CHROMA_QUALITY: int
IMWRITE_JPEG_LUMA_QUALITY: int
IMWRITE_JPEG_OPTIMIZE: int
IMWRITE_JPEG_PROGRESSIVE: int
IMWRITE_JPEG_QUALITY: int
IMWRITE_JPEG_RST_INTERVAL: int
IMWRITE_PAM_FORMAT_BLACKANDWHITE: int
IMWRITE_PAM_FORMAT_GRAYSCALE: int
IMWRITE_PAM_FORMAT_GRAYSCALE_ALPHA: int
IMWRITE_PAM_FORMAT_NULL: int
IMWRITE_PAM_FORMAT_RGB: int
IMWRITE_PAM_FORMAT_RGB_ALPHA: int
IMWRITE_PAM_TUPLETYPE: int
IMWRITE_PNG_BILEVEL: int
IMWRITE_PNG_COMPRESSION: int
IMWRITE_PNG_STRATEGY: int
IMWRITE_PNG_STRATEGY_DEFAULT: int
IMWRITE_PNG_STRATEGY_FILTERED: int
IMWRITE_PNG_STRATEGY_FIXED: int
IMWRITE_PNG_STRATEGY_HUFFMAN_ONLY: int
IMWRITE_PNG_STRATEGY_RLE: int
IMWRITE_PXM_BINARY: int
IMWRITE_TIFF_COMPRESSION: int
IMWRITE_TIFF_RESUNIT: int
IMWRITE_TIFF_XDPI: int
IMWRITE_TIFF_YDPI: int
IMWRITE_WEBP_QUALITY: int
INPAINT_NS: int
INPAINT_TELEA: int
INTERSECT_FULL: int
INTERSECT_NONE: int
INTERSECT_PARTIAL: int
INTER_AREA: int
INTER_BITS: int
INTER_BITS2: int
INTER_CUBIC: int
INTER_LANCZOS4: int
INTER_LINEAR: int
INTER_LINEAR_EXACT: int
INTER_MAX: int
INTER_NEAREST: int
INTER_TAB_SIZE: int
INTER_TAB_SIZE2: int
KAZE = _mod_cv2.KAZE
KAZE_DIFF_CHARBONNIER: int
KAZE_DIFF_PM_G1: int
KAZE_DIFF_PM_G2: int
KAZE_DIFF_WEICKERT: int
def KAZE_create(extended=..., upright=..., threshold=..., nOctaves=..., nOctaveLayers=..., diffusivity=...) -> typing.Any:
    'KAZE_create([, extended[, upright[, threshold[, nOctaves[, nOctaveLayers[, diffusivity]]]]]]) -> retval\n.   @brief The KAZE constructor\n.   \n.       @param extended Set to enable extraction of extended (128-byte) descriptor.\n.       @param upright Set to enable use of upright descriptors (non rotation-invariant).\n.       @param threshold Detector response threshold to accept point\n.       @param nOctaves Maximum octave evolution of the image\n.       @param nOctaveLayers Default number of sublevels per scale level\n.       @param diffusivity Diffusivity type. DIFF_PM_G1, DIFF_PM_G2, DIFF_WEICKERT or\n.       DIFF_CHARBONNIER'
    ...

KMEANS_PP_CENTERS: int
KMEANS_RANDOM_CENTERS: int
KMEANS_USE_INITIAL_LABELS: int
KalmanFilter = _mod_cv2.KalmanFilter
KeyPoint = _mod_cv2.KeyPoint
def KeyPoint_convert(keypoints, keypointIndexes=...) -> typing.Any:
    'KeyPoint_convert(keypoints[, keypointIndexes]) -> points2f\n.   This method converts vector of keypoints to vector of points or the reverse, where each keypoint is\n.       assigned the same size and the same orientation.\n.   \n.       @param keypoints Keypoints obtained from any feature detection algorithm like SIFT/SURF/ORB\n.       @param points2f Array of (x,y) coordinates of each keypoint\n.       @param keypointIndexes Array of indexes of keypoints to be converted to points. (Acts like a mask to\n.       convert only specified keypoints)\n\n\n\nKeyPoint_convert(points2f[, size[, response[, octave[, class_id]]]]) -> keypoints\n.   @overload\n.       @param points2f Array of (x,y) coordinates of each keypoint\n.       @param keypoints Keypoints obtained from any feature detection algorithm like SIFT/SURF/ORB\n.       @param size keypoint diameter\n.       @param response keypoint detector response on the keypoint (that is, strength of the keypoint)\n.       @param octave pyramid octave in which the keypoint has been detected\n.       @param class_id object id'
    ...

def KeyPoint_overlap(kp1, kp2) -> typing.Any:
    "KeyPoint_overlap(kp1, kp2) -> retval\n.   This method computes overlap for pair of keypoints. Overlap is the ratio between area of keypoint\n.       regions' intersection and area of keypoint regions' union (considering keypoint region as circle).\n.       If they don't overlap, we get zero. If they coincide at same location with same size, we get 1.\n.       @param kp1 First keypoint\n.       @param kp2 Second keypoint"
    ...

LDR_SIZE: int
LINE_4: int
LINE_8: int
LINE_AA: int
LMEDS: int
LSD_REFINE_ADV: int
LSD_REFINE_NONE: int
LSD_REFINE_STD: int
def LUT(src: Mat, lut, dts: Mat = ...) -> typing.Any:
    'LUT(src, lut[, dst]) -> dst\n.   @brief Performs a look-up table transform of an array.\n.   \n.   The function LUT fills the output array with values from the look-up table. Indices of the entries\n.   are taken from the input array. That is, the function processes each element of src as follows:\n.   \\f[\\texttt{dst} (I)  \\leftarrow \\texttt{lut(src(I) + d)}\\f]\n.   where\n.   \\f[d =  \\fork{0}{if \\(\\texttt{src}\\) has depth \\(\\texttt{CV_8U}\\)}{128}{if \\(\\texttt{src}\\) has depth \\(\\texttt{CV_8S}\\)}\\f]\n.   @param src input array of 8-bit elements.\n.   @param lut look-up table of 256 elements; in case of multi-channel input array, the table should\n.   either have a single channel (in this case the same table is used for all channels) or the same\n.   number of channels as in the input array.\n.   @param dst output array of the same size and number of channels as src, and the same depth as lut.\n.   @sa  convertScaleAbs, Mat::convertTo'
    ...

def Laplacian(src: Mat, ddepth, dts: Mat = ..., ksize=..., scale=..., delta=..., borderType=...) -> typing.Any:
    'Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst\n.   @brief Calculates the Laplacian of an image.\n.   \n.   The function calculates the Laplacian of the source image by adding up the second x and y\n.   derivatives calculated using the Sobel operator:\n.   \n.   \\f[\\texttt{dst} =  \\Delta \\texttt{src} =  \\frac{\\partial^2 \\texttt{src}}{\\partial x^2} +  \\frac{\\partial^2 \\texttt{src}}{\\partial y^2}\\f]\n.   \n.   This is done when `ksize > 1`. When `ksize == 1`, the Laplacian is computed by filtering the image\n.   with the following \\f$3 \\times 3\\f$ aperture:\n.   \n.   \\f[\\vecthreethree {0}{1}{0}{1}{-4}{1}{0}{1}{0}\\f]\n.   \n.   @param src Source image.\n.   @param dst Destination image of the same size and the same number of channels as src .\n.   @param ddepth Desired depth of the destination image.\n.   @param ksize Aperture size used to compute the second-derivative filters. See #getDerivKernels for\n.   details. The size must be positive and odd.\n.   @param scale Optional scale factor for the computed Laplacian values. By default, no scaling is\n.   applied. See #getDerivKernels for details.\n.   @param delta Optional delta value that is added to the results prior to storing them in dst .\n.   @param borderType Pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not supported.\n.   @sa  Sobel, Scharr'
    ...

LineSegmentDetector = _mod_cv2.LineSegmentDetector
MARKER_CROSS: int
MARKER_DIAMOND: int
MARKER_SQUARE: int
MARKER_STAR: int
MARKER_TILTED_CROSS: int
MARKER_TRIANGLE_DOWN: int
MARKER_TRIANGLE_UP: int
MAT_AUTO_STEP: int
MAT_CONTINUOUS_FLAG: int
MAT_DEPTH_MASK: int
MAT_MAGIC_MASK: int
MAT_MAGIC_VAL: int
MAT_SUBMATRIX_FLAG: int
MAT_TYPE_MASK: int
MIXED_CLONE: int
MONOCHROME_TRANSFER: int
MORPH_BLACKHAT: int
MORPH_CLOSE: int
MORPH_CROSS: int
MORPH_DILATE: int
MORPH_ELLIPSE: int
MORPH_ERODE: int
MORPH_GRADIENT: int
MORPH_HITMISS: int
MORPH_OPEN: int
MORPH_RECT: int
MORPH_TOPHAT: int
MOTION_AFFINE: int
MOTION_EUCLIDEAN: int
MOTION_HOMOGRAPHY: int
MOTION_TRANSLATION: int
MSER = _mod_cv2.MSER
def MSER_create(_delta=..., _min_area=..., _max_area=..., _max_variation=..., _min_diversity=..., _max_evolution=..., _area_threshold=..., _min_margin=..., _edge_blur_size=...) -> typing.Any:
    'MSER_create([, _delta[, _min_area[, _max_area[, _max_variation[, _min_diversity[, _max_evolution[, _area_threshold[, _min_margin[, _edge_blur_size]]]]]]]]]) -> retval\n.   @brief Full constructor for %MSER detector\n.   \n.       @param _delta it compares \\f$(size_{i}-size_{i-delta})/size_{i-delta}\\f$\n.       @param _min_area prune the area which smaller than minArea\n.       @param _max_area prune the area which bigger than maxArea\n.       @param _max_variation prune the area have similar size to its children\n.       @param _min_diversity for color image, trace back to cut off mser with diversity less than min_diversity\n.       @param _max_evolution  for color image, the evolution steps\n.       @param _area_threshold for color image, the area threshold to cause re-initialize\n.       @param _min_margin for color image, ignore too small margin\n.       @param _edge_blur_size for color image, the aperture size for edge blur'
    ...

def Mahalanobis(v1, v2, icovar) -> typing.Any:
    'Mahalanobis(v1, v2, icovar) -> retval\n.   @brief Calculates the Mahalanobis distance between two vectors.\n.   \n.   The function cv::Mahalanobis calculates and returns the weighted distance between two vectors:\n.   \\f[d( \\texttt{vec1} , \\texttt{vec2} )= \\sqrt{\\sum_{i,j}{\\texttt{icovar(i,j)}\\cdot(\\texttt{vec1}(I)-\\texttt{vec2}(I))\\cdot(\\texttt{vec1(j)}-\\texttt{vec2(j)})} }\\f]\n.   The covariance matrix may be calculated using the #calcCovarMatrix function and then inverted using\n.   the invert function (preferably using the #DECOMP_SVD method, as the most accurate).\n.   @param v1 first 1D input vector.\n.   @param v2 second 1D input vector.\n.   @param icovar inverse covariance matrix.'
    ...

Mat_AUTO_STEP: int
Mat_CONTINUOUS_FLAG: int
Mat_DEPTH_MASK: int
Mat_MAGIC_MASK: int
Mat_MAGIC_VAL: int
Mat_SUBMATRIX_FLAG: int
Mat_TYPE_MASK: int
MergeDebevec = _mod_cv2.MergeDebevec
MergeExposures = _mod_cv2.MergeExposures
MergeMertens = _mod_cv2.MergeMertens
MergeRobertson = _mod_cv2.MergeRobertson
NORMAL_CLONE: int
NORMCONV_FILTER: int
NORM_HAMMING: int
NORM_HAMMING2: int
NORM_INF: int
NORM_L1: int
NORM_L2: int
NORM_L2SQR: int
NORM_MINMAX: int
NORM_RELATIVE: int
NORM_TYPE_MASK: int
OPTFLOW_FARNEBACK_GAUSSIAN: int
OPTFLOW_LK_GET_MIN_EIGENVALS: int
OPTFLOW_USE_INITIAL_FLOW: int
ORB = _mod_cv2.ORB
ORB_FAST_SCORE: int
ORB_HARRIS_SCORE: int
def ORB_create(nfeatures=..., scaleFactor=..., nlevels=..., edgeThreshold=..., firstLevel=..., WTA_K=..., scoreType=..., patchSize=..., fastThreshold=...) -> typing.Any:
    'ORB_create([, nfeatures[, scaleFactor[, nlevels[, edgeThreshold[, firstLevel[, WTA_K[, scoreType[, patchSize[, fastThreshold]]]]]]]]]) -> retval\n.   @brief The ORB constructor\n.   \n.       @param nfeatures The maximum number of features to retain.\n.       @param scaleFactor Pyramid decimation ratio, greater than 1. scaleFactor==2 means the classical\n.       pyramid, where each next level has 4x less pixels than the previous, but such a big scale factor\n.       will degrade feature matching scores dramatically. On the other hand, too close to 1 scale factor\n.       will mean that to cover certain scale range you will need more pyramid levels and so the speed\n.       will suffer.\n.       @param nlevels The number of pyramid levels. The smallest level will have linear size equal to\n.       input_image_linear_size/pow(scaleFactor, nlevels - firstLevel).\n.       @param edgeThreshold This is size of the border where the features are not detected. It should\n.       roughly match the patchSize parameter.\n.       @param firstLevel The level of pyramid to put source image to. Previous layers are filled\n.       with upscaled source image.\n.       @param WTA_K The number of points that produce each element of the oriented BRIEF descriptor. The\n.       default value 2 means the BRIEF where we take a random point pair and compare their brightnesses,\n.       so we get 0/1 response. Other possible values are 3 and 4. For example, 3 means that we take 3\n.       random points (of course, those point coordinates are random, but they are generated from the\n.       pre-defined seed, so each element of BRIEF descriptor is computed deterministically from the pixel\n.       rectangle), find point of maximum brightness and output index of the winner (0, 1 or 2). Such\n.       output will occupy 2 bits, and therefore it will need a special variant of Hamming distance,\n.       denoted as NORM_HAMMING2 (2 bits per bin). When WTA_K=4, we take 4 random points to compute each\n.       bin (that will also occupy 2 bits with possible values 0, 1, 2 or 3).\n.       @param scoreType The default HARRIS_SCORE means that Harris algorithm is used to rank features\n.       (the score is written to KeyPoint::score and is used to retain best nfeatures features);\n.       FAST_SCORE is alternative value of the parameter that produces slightly less stable keypoints,\n.       but it is a little faster to compute.\n.       @param patchSize size of the patch used by the oriented BRIEF descriptor. Of course, on smaller\n.       pyramid layers the perceived image area covered by a feature will be larger.\n.       @param fastThreshold the fast threshold'
    ...

PARAM_ALGORITHM: int
PARAM_BOOLEAN: int
PARAM_FLOAT: int
PARAM_INT: int
PARAM_MAT: int
PARAM_MAT_VECTOR: int
PARAM_REAL: int
PARAM_SCALAR: int
PARAM_STRING: int
PARAM_UCHAR: int
PARAM_UINT64: int
PARAM_UNSIGNED_INT: int
def PCABackProject(data, mean, eigenvectors, result=...) -> typing.Any:
    'PCABackProject(data, mean, eigenvectors[, result]) -> result\n.   wrap PCA::backProject'
    ...

def PCACompute(data, mean, eigenvectors=..., maxComponents=...) -> typing.Any:
    'PCACompute(data, mean[, eigenvectors[, maxComponents]]) -> mean, eigenvectors\n.   wrap PCA::operator()\n\n\n\nPCACompute(data, mean, retainedVariance[, eigenvectors]) -> mean, eigenvectors\n.   wrap PCA::operator()'
    ...

def PCACompute2(data, mean, eigenvectors=..., eigenvalues=..., maxComponents=...) -> typing.Any:
    'PCACompute2(data, mean[, eigenvectors[, eigenvalues[, maxComponents]]]) -> mean, eigenvectors, eigenvalues\n.   wrap PCA::operator() and add eigenvalues output parameter\n\n\n\nPCACompute2(data, mean, retainedVariance[, eigenvectors[, eigenvalues]]) -> mean, eigenvectors, eigenvalues\n.   wrap PCA::operator() and add eigenvalues output parameter'
    ...

def PCAProject(data, mean, eigenvectors, result=...) -> typing.Any:
    'PCAProject(data, mean, eigenvectors[, result]) -> result\n.   wrap PCA::project'
    ...

PCA_DATA_AS_COL: int
PCA_DATA_AS_ROW: int
PCA_USE_AVG: int
PROJ_SPHERICAL_EQRECT: int
PROJ_SPHERICAL_ORTHO: int
def PSNR(src1: Mat, src2: Mat, R=...) -> typing.Any:
    'PSNR(src1, src2[, R]) -> retval\n.   @brief Computes the Peak Signal-to-Noise Ratio (PSNR) image quality metric.\n.   \n.   This function calculates the Peak Signal-to-Noise Ratio (PSNR) image quality metric in decibels (dB),\n.   between two input arrays src1 and src2. The arrays must have the same type.\n.   \n.   The PSNR is calculated as follows:\n.   \n.   \\f[\n.   \\texttt{PSNR} = 10 \\cdot \\log_{10}{\\left( \\frac{R^2}{MSE} \\right) }\n.   \\f]\n.   \n.   where R is the maximum integer value of depth (e.g. 255 in the case of CV_8U data)\n.   and MSE is the mean squared error between the two arrays.\n.   \n.   @param src1 first input array.\n.   @param src2 second input array of the same size as src1.\n.   @param R the maximum pixel value (255 by default)'
    ...

Param_ALGORITHM: int
Param_BOOLEAN: int
Param_FLOAT: int
Param_INT: int
Param_MAT: int
Param_MAT_VECTOR: int
Param_REAL: int
Param_SCALAR: int
Param_STRING: int
Param_UCHAR: int
Param_UINT64: int
Param_UNSIGNED_INT: int
PyRotationWarper = _mod_cv2.PyRotationWarper
QRCodeDetector = _mod_cv2.QRCodeDetector
QT_CHECKBOX: int
QT_FONT_BLACK: int
QT_FONT_BOLD: int
QT_FONT_DEMIBOLD: int
QT_FONT_LIGHT: int
QT_FONT_NORMAL: int
QT_NEW_BUTTONBAR: int
QT_PUSH_BUTTON: int
QT_RADIOBOX: int
QT_STYLE_ITALIC: int
QT_STYLE_NORMAL: int
QT_STYLE_OBLIQUE: int
RANSAC: int
RECURS_FILTER: int
REDUCE_AVG: int
REDUCE_MAX: int
REDUCE_MIN: int
REDUCE_SUM: int
RETR_CCOMP: int
RETR_EXTERNAL: int
RETR_FLOODFILL: int
RETR_LIST: int
RETR_TREE: int
RHO: int
RNG_NORMAL: int
RNG_UNIFORM: int
ROTATE_180: int
ROTATE_90_CLOCKWISE: int
ROTATE_90_COUNTERCLOCKWISE: int
def RQDecomp3x3(src: Mat, mtxR=..., mtxQ=..., Qx=..., Qy=..., Qz=...) -> typing.Any:
    'RQDecomp3x3(src[, mtxR[, mtxQ[, Qx[, Qy[, Qz]]]]]) -> retval, mtxR, mtxQ, Qx, Qy, Qz\n.   @brief Computes an RQ decomposition of 3x3 matrices.\n.   \n.   @param src 3x3 input matrix.\n.   @param mtxR Output 3x3 upper-triangular matrix.\n.   @param mtxQ Output 3x3 orthogonal matrix.\n.   @param Qx Optional output 3x3 rotation matrix around x-axis.\n.   @param Qy Optional output 3x3 rotation matrix around y-axis.\n.   @param Qz Optional output 3x3 rotation matrix around z-axis.\n.   \n.   The function computes a RQ decomposition using the given rotations. This function is used in\n.   decomposeProjectionMatrix to decompose the left 3x3 submatrix of a projection matrix into a camera\n.   and a rotation matrix.\n.   \n.   It optionally returns three rotation matrices, one for each axis, and the three Euler angles in\n.   degrees (as the return value) that could be used in OpenGL. Note, there is always more than one\n.   sequence of rotations about the three principal axes that results in the same orientation of an\n.   object, e.g. see @cite Slabaugh . Returned tree rotation matrices and corresponding three Euler angles\n.   are only one of the possible solutions.'
    ...

def Rodrigues(src: Mat, dts: Mat = ..., jacobian=...) -> typing.Any:
    'Rodrigues(src[, dst[, jacobian]]) -> dst, jacobian\n.   @brief Converts a rotation matrix to a rotation vector or vice versa.\n.   \n.   @param src Input rotation vector (3x1 or 1x3) or rotation matrix (3x3).\n.   @param dst Output rotation matrix (3x3) or rotation vector (3x1 or 1x3), respectively.\n.   @param jacobian Optional output Jacobian matrix, 3x9 or 9x3, which is a matrix of partial\n.   derivatives of the output array components with respect to the input array components.\n.   \n.   \\f[\\begin{array}{l} \\theta \\leftarrow norm(r) \\\\ r  \\leftarrow r/ \\theta \\\\ R =  \\cos(\\theta) I + (1- \\cos{\\theta} ) r r^T +  \\sin(\\theta) \\vecthreethree{0}{-r_z}{r_y}{r_z}{0}{-r_x}{-r_y}{r_x}{0} \\end{array}\\f]\n.   \n.   Inverse transformation can be also done easily, since\n.   \n.   \\f[\\sin ( \\theta ) \\vecthreethree{0}{-r_z}{r_y}{r_z}{0}{-r_x}{-r_y}{r_x}{0} = \\frac{R - R^T}{2}\\f]\n.   \n.   A rotation vector is a convenient and most compact representation of a rotation matrix (since any\n.   rotation matrix has just 3 degrees of freedom). The representation is used in the global 3D geometry\n.   optimization procedures like @ref calibrateCamera, @ref stereoCalibrate, or @ref solvePnP .\n.   \n.   @note More information about the computation of the derivative of a 3D rotation matrix with respect to its exponential coordinate\n.   can be found in:\n.       - A Compact Formula for the Derivative of a 3-D Rotation in Exponential Coordinates, Guillermo Gallego, Anthony J. Yezzi @cite Gallego2014ACF\n.   \n.   @note Useful information on SE(3) and Lie Groups can be found in:\n.       - A tutorial on SE(3) transformation parameterizations and on-manifold optimization, Jose-Luis Blanco @cite blanco2010tutorial\n.       - Lie Groups for 2D and 3D Transformation, Ethan Eade @cite Eade17\n.       - A micro Lie theory for state estimation in robotics, Joan Sol&#224;, J&#233;r&#233;mie Deray, Dinesh Atchuthan @cite Sol2018AML'
    ...

SIFT = _mod_cv2.SIFT
def SIFT_create(nfeatures=..., nOctaveLayers=..., contrastThreshold=..., edgeThreshold=..., sigma=...) -> typing.Any:
    'SIFT_create([, nfeatures[, nOctaveLayers[, contrastThreshold[, edgeThreshold[, sigma]]]]]) -> retval\n.   @param nfeatures The number of best features to retain. The features are ranked by their scores\n.       (measured in SIFT algorithm as the local contrast)\n.   \n.       @param nOctaveLayers The number of layers in each octave. 3 is the value used in D. Lowe paper. The\n.       number of octaves is computed automatically from the image resolution.\n.   \n.       @param contrastThreshold The contrast threshold used to filter out weak features in semi-uniform\n.       (low-contrast) regions. The larger the threshold, the less features are produced by the detector.\n.   \n.       @note The contrast threshold will be divided by nOctaveLayers when the filtering is applied. When\n.       nOctaveLayers is set to default and if you want to use the value used in D. Lowe paper, 0.03, set\n.       this argument to 0.09.\n.   \n.       @param edgeThreshold The threshold used to filter out edge-like features. Note that the its meaning\n.       is different from the contrastThreshold, i.e. the larger the edgeThreshold, the less features are\n.       filtered out (more features are retained).\n.   \n.       @param sigma The sigma of the Gaussian applied to the input image at the octave \\#0. If your image\n.       is captured with a weak camera with soft lenses, you might want to reduce the number.'
    ...

SOLVELP_MULTI: int
SOLVELP_SINGLE: int
SOLVELP_UNBOUNDED: int
SOLVELP_UNFEASIBLE: int
SOLVEPNP_AP3P: int
SOLVEPNP_DLS: int
SOLVEPNP_EPNP: int
SOLVEPNP_IPPE: int
SOLVEPNP_IPPE_SQUARE: int
SOLVEPNP_ITERATIVE: int
SOLVEPNP_MAX_COUNT: int
SOLVEPNP_P3P: int
SOLVEPNP_UPNP: int
SORT_ASCENDING: int
SORT_DESCENDING: int
SORT_EVERY_COLUMN: int
SORT_EVERY_ROW: int
SPARSE_MAT_HASH_BIT: int
SPARSE_MAT_HASH_SCALE: int
SPARSE_MAT_MAGIC_VAL: int
SPARSE_MAT_MAX_DIM: int
STEREO_BM_PREFILTER_NORMALIZED_RESPONSE: int
STEREO_BM_PREFILTER_XSOBEL: int
STEREO_MATCHER_DISP_SCALE: int
STEREO_MATCHER_DISP_SHIFT: int
STEREO_SGBM_MODE_HH: int
STEREO_SGBM_MODE_HH4: int
STEREO_SGBM_MODE_SGBM: int
STEREO_SGBM_MODE_SGBM_3WAY: int
STITCHER_ERR_CAMERA_PARAMS_ADJUST_FAIL: int
STITCHER_ERR_HOMOGRAPHY_EST_FAIL: int
STITCHER_ERR_NEED_MORE_IMGS: int
STITCHER_OK: int
STITCHER_PANORAMA: int
STITCHER_SCANS: int
SUBDIV2D_NEXT_AROUND_DST: int
SUBDIV2D_NEXT_AROUND_LEFT: int
SUBDIV2D_NEXT_AROUND_ORG: int
SUBDIV2D_NEXT_AROUND_RIGHT: int
SUBDIV2D_PREV_AROUND_DST: int
SUBDIV2D_PREV_AROUND_LEFT: int
SUBDIV2D_PREV_AROUND_ORG: int
SUBDIV2D_PREV_AROUND_RIGHT: int
SUBDIV2D_PTLOC_ERROR: int
SUBDIV2D_PTLOC_INSIDE: int
SUBDIV2D_PTLOC_ON_EDGE: int
SUBDIV2D_PTLOC_OUTSIDE_RECT: int
SUBDIV2D_PTLOC_VERTEX: int
def SVBackSubst(w, u, vt, rhs, dts: Mat = ...) -> typing.Any:
    'SVBackSubst(w, u, vt, rhs[, dst]) -> dst\n.   wrap SVD::backSubst'
    ...

SVD_FULL_UV: int
SVD_MODIFY_A: int
SVD_NO_UV: int
def SVDecomp(src: Mat, w=..., u=..., vt=..., flags: int = ...) -> typing.Any:
    'SVDecomp(src[, w[, u[, vt[, flags]]]]) -> w, u, vt\n.   wrap SVD::compute'
    ...

def Scharr(src: Mat, ddepth, dx, dy, dts: Mat = ..., scale=..., delta=..., borderType=...) -> typing.Any:
    'Scharr(src, ddepth, dx, dy[, dst[, scale[, delta[, borderType]]]]) -> dst\n.   @brief Calculates the first x- or y- image derivative using Scharr operator.\n.   \n.   The function computes the first x- or y- spatial image derivative using the Scharr operator. The\n.   call\n.   \n.   \\f[\\texttt{Scharr(src, dst, ddepth, dx, dy, scale, delta, borderType)}\\f]\n.   \n.   is equivalent to\n.   \n.   \\f[\\texttt{Sobel(src, dst, ddepth, dx, dy, FILTER_SCHARR, scale, delta, borderType)} .\\f]\n.   \n.   @param src input image.\n.   @param dst output image of the same size and the same number of channels as src.\n.   @param ddepth output image depth, see @ref filter_depths "combinations"\n.   @param dx order of the derivative x.\n.   @param dy order of the derivative y.\n.   @param scale optional scale factor for the computed derivative values; by default, no scaling is\n.   applied (see #getDerivKernels for details).\n.   @param delta optional delta value that is added to the results prior to storing them in dst.\n.   @param borderType pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not supported.\n.   @sa  cartToPolar'
    ...

SimpleBlobDetector = _mod_cv2.SimpleBlobDetector
SimpleBlobDetector_Params = _mod_cv2.SimpleBlobDetector_Params
def SimpleBlobDetector_create(parameters=...) -> typing.Any:
    'SimpleBlobDetector_create([, parameters]) -> retval\n.'
    ...

def Sobel(src: Mat, ddepth, dx, dy, dts: Mat = ..., ksize=..., scale=..., delta=..., borderType=...) -> typing.Any:
    'Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) -> dst\n.   @brief Calculates the first, second, third, or mixed image derivatives using an extended Sobel operator.\n.   \n.   In all cases except one, the \\f$\\texttt{ksize} \\times \\texttt{ksize}\\f$ separable kernel is used to\n.   calculate the derivative. When \\f$\\texttt{ksize = 1}\\f$, the \\f$3 \\times 1\\f$ or \\f$1 \\times 3\\f$\n.   kernel is used (that is, no Gaussian smoothing is done). `ksize = 1` can only be used for the first\n.   or the second x- or y- derivatives.\n.   \n.   There is also the special value `ksize = #FILTER_SCHARR (-1)` that corresponds to the \\f$3\\times3\\f$ Scharr\n.   filter that may give more accurate results than the \\f$3\\times3\\f$ Sobel. The Scharr aperture is\n.   \n.   \\f[\\vecthreethree{-3}{0}{3}{-10}{0}{10}{-3}{0}{3}\\f]\n.   \n.   for the x-derivative, or transposed for the y-derivative.\n.   \n.   The function calculates an image derivative by convolving the image with the appropriate kernel:\n.   \n.   \\f[\\texttt{dst} =  \\frac{\\partial^{xorder+yorder} \\texttt{src}}{\\partial x^{xorder} \\partial y^{yorder}}\\f]\n.   \n.   The Sobel operators combine Gaussian smoothing and differentiation, so the result is more or less\n.   resistant to the noise. Most often, the function is called with ( xorder = 1, yorder = 0, ksize = 3)\n.   or ( xorder = 0, yorder = 1, ksize = 3) to calculate the first x- or y- image derivative. The first\n.   case corresponds to a kernel of:\n.   \n.   \\f[\\vecthreethree{-1}{0}{1}{-2}{0}{2}{-1}{0}{1}\\f]\n.   \n.   The second case corresponds to a kernel of:\n.   \n.   \\f[\\vecthreethree{-1}{-2}{-1}{0}{0}{0}{1}{2}{1}\\f]\n.   \n.   @param src input image.\n.   @param dst output image of the same size and the same number of channels as src .\n.   @param ddepth output image depth, see @ref filter_depths "combinations"; in the case of\n.       8-bit input images it will result in truncated derivatives.\n.   @param dx order of the derivative x.\n.   @param dy order of the derivative y.\n.   @param ksize size of the extended Sobel kernel; it must be 1, 3, 5, or 7.\n.   @param scale optional scale factor for the computed derivative values; by default, no scaling is\n.   applied (see #getDerivKernels for details).\n.   @param delta optional delta value that is added to the results prior to storing them in dst.\n.   @param borderType pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not supported.\n.   @sa  Scharr, Laplacian, sepFilter2D, filter2D, GaussianBlur, cartToPolar'
    ...

SparseMat_HASH_BIT: int
SparseMat_HASH_SCALE: int
SparseMat_MAGIC_VAL: int
SparseMat_MAX_DIM: int
SparseOpticalFlow = _mod_cv2.SparseOpticalFlow
SparsePyrLKOpticalFlow = _mod_cv2.SparsePyrLKOpticalFlow
def SparsePyrLKOpticalFlow_create(winSize=..., maxLevel=..., crit=..., flags: int = ..., minEigThreshold=...) -> typing.Any:
    'SparsePyrLKOpticalFlow_create([, winSize[, maxLevel[, crit[, flags[, minEigThreshold]]]]]) -> retval\n.'
    ...

StereoBM = _mod_cv2.StereoBM
StereoBM_PREFILTER_NORMALIZED_RESPONSE: int
StereoBM_PREFILTER_XSOBEL: int
def StereoBM_create(numDisparities=..., blockSize=...) -> typing.Any:
    'StereoBM_create([, numDisparities[, blockSize]]) -> retval\n.   @brief Creates StereoBM object\n.   \n.       @param numDisparities the disparity search range. For each pixel algorithm will find the best\n.       disparity from 0 (default minimum disparity) to numDisparities. The search range can then be\n.       shifted by changing the minimum disparity.\n.       @param blockSize the linear size of the blocks compared by the algorithm. The size should be odd\n.       (as the block is centered at the current pixel). Larger block size implies smoother, though less\n.       accurate disparity map. Smaller block size gives more detailed disparity map, but there is higher\n.       chance for algorithm to find a wrong correspondence.\n.   \n.       The function create StereoBM object. You can then call StereoBM::compute() to compute disparity for\n.       a specific stereo pair.'
    ...

StereoMatcher = _mod_cv2.StereoMatcher
StereoMatcher_DISP_SCALE: int
StereoMatcher_DISP_SHIFT: int
StereoSGBM = _mod_cv2.StereoSGBM
StereoSGBM_MODE_HH: int
StereoSGBM_MODE_HH4: int
StereoSGBM_MODE_SGBM: int
StereoSGBM_MODE_SGBM_3WAY: int
def StereoSGBM_create(minDisparity=..., numDisparities=..., blockSize=..., P1=..., P2=..., disp12MaxDiff=..., preFilterCap=..., uniquenessRatio=..., speckleWindowSize=..., speckleRange=..., mode=...) -> typing.Any:
    'StereoSGBM_create([, minDisparity[, numDisparities[, blockSize[, P1[, P2[, disp12MaxDiff[, preFilterCap[, uniquenessRatio[, speckleWindowSize[, speckleRange[, mode]]]]]]]]]]]) -> retval\n.   @brief Creates StereoSGBM object\n.   \n.       @param minDisparity Minimum possible disparity value. Normally, it is zero but sometimes\n.       rectification algorithms can shift images, so this parameter needs to be adjusted accordingly.\n.       @param numDisparities Maximum disparity minus minimum disparity. The value is always greater than\n.       zero. In the current implementation, this parameter must be divisible by 16.\n.       @param blockSize Matched block size. It must be an odd number \\>=1 . Normally, it should be\n.       somewhere in the 3..11 range.\n.       @param P1 The first parameter controlling the disparity smoothness. See below.\n.       @param P2 The second parameter controlling the disparity smoothness. The larger the values are,\n.       the smoother the disparity is. P1 is the penalty on the disparity change by plus or minus 1\n.       between neighbor pixels. P2 is the penalty on the disparity change by more than 1 between neighbor\n.       pixels. The algorithm requires P2 \\> P1 . See stereo_match.cpp sample where some reasonably good\n.       P1 and P2 values are shown (like 8\\*number_of_image_channels\\*blockSize\\*blockSize and\n.       32\\*number_of_image_channels\\*blockSize\\*blockSize , respectively).\n.       @param disp12MaxDiff Maximum allowed difference (in integer pixel units) in the left-right\n.       disparity check. Set it to a non-positive value to disable the check.\n.       @param preFilterCap Truncation value for the prefiltered image pixels. The algorithm first\n.       computes x-derivative at each pixel and clips its value by [-preFilterCap, preFilterCap] interval.\n.       The result values are passed to the Birchfield-Tomasi pixel cost function.\n.       @param uniquenessRatio Margin in percentage by which the best (minimum) computed cost function\n.       value should "win" the second best value to consider the found match correct. Normally, a value\n.       within the 5-15 range is good enough.\n.       @param speckleWindowSize Maximum size of smooth disparity regions to consider their noise speckles\n.       and invalidate. Set it to 0 to disable speckle filtering. Otherwise, set it somewhere in the\n.       50-200 range.\n.       @param speckleRange Maximum disparity variation within each connected component. If you do speckle\n.       filtering, set the parameter to a positive value, it will be implicitly multiplied by 16.\n.       Normally, 1 or 2 is good enough.\n.       @param mode Set it to StereoSGBM::MODE_HH to run the full-scale two-pass dynamic programming\n.       algorithm. It will consume O(W\\*H\\*numDisparities) bytes, which is large for 640x480 stereo and\n.       huge for HD-size pictures. By default, it is set to false .\n.   \n.       The first constructor initializes StereoSGBM with all the default parameters. So, you only have to\n.       set StereoSGBM::numDisparities at minimum. The second constructor enables you to set each parameter\n.       to a custom value.'
    ...

Stitcher = _mod_cv2.Stitcher
Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL: int
Stitcher_ERR_HOMOGRAPHY_EST_FAIL: int
Stitcher_ERR_NEED_MORE_IMGS: int
Stitcher_OK: int
Stitcher_PANORAMA: int
Stitcher_SCANS: int
def Stitcher_create(mode=...) -> typing.Any:
    'Stitcher_create([, mode]) -> retval\n.   @brief Creates a Stitcher configured in one of the stitching modes.\n.   \n.       @param mode Scenario for stitcher operation. This is usually determined by source of images\n.       to stitch and their transformation. Default parameters will be chosen for operation in given\n.       scenario.\n.       @return Stitcher class instance.'
    ...

Subdiv2D = _mod_cv2.Subdiv2D
Subdiv2D_NEXT_AROUND_DST: int
Subdiv2D_NEXT_AROUND_LEFT: int
Subdiv2D_NEXT_AROUND_ORG: int
Subdiv2D_NEXT_AROUND_RIGHT: int
Subdiv2D_PREV_AROUND_DST: int
Subdiv2D_PREV_AROUND_LEFT: int
Subdiv2D_PREV_AROUND_ORG: int
Subdiv2D_PREV_AROUND_RIGHT: int
Subdiv2D_PTLOC_ERROR: int
Subdiv2D_PTLOC_INSIDE: int
Subdiv2D_PTLOC_ON_EDGE: int
Subdiv2D_PTLOC_OUTSIDE_RECT: int
Subdiv2D_PTLOC_VERTEX: int
TERM_CRITERIA_COUNT: int
TERM_CRITERIA_EPS: int
TERM_CRITERIA_MAX_ITER: int
THRESH_BINARY: int
THRESH_BINARY_INV: int
THRESH_MASK: int
THRESH_OTSU: int
THRESH_TOZERO: int
THRESH_TOZERO_INV: int
THRESH_TRIANGLE: int
THRESH_TRUNC: int
TM_CCOEFF: int
TM_CCOEFF_NORMED: int
TM_CCORR: int
TM_CCORR_NORMED: int
TM_SQDIFF: int
TM_SQDIFF_NORMED: int
TermCriteria_COUNT: int
TermCriteria_EPS: int
TermCriteria_MAX_ITER: int
TickMeter = _mod_cv2.TickMeter
Tonemap = _mod_cv2.Tonemap
TonemapDrago = _mod_cv2.TonemapDrago
TonemapMantiuk = _mod_cv2.TonemapMantiuk
TonemapReinhard = _mod_cv2.TonemapReinhard
UMAT_AUTO_STEP: int
UMAT_CONTINUOUS_FLAG: int
UMAT_DATA_ASYNC_CLEANUP: int
UMAT_DATA_COPY_ON_MAP: int
UMAT_DATA_DEVICE_COPY_OBSOLETE: int
UMAT_DATA_DEVICE_MEM_MAPPED: int
UMAT_DATA_HOST_COPY_OBSOLETE: int
UMAT_DATA_TEMP_COPIED_UMAT: int
UMAT_DATA_TEMP_UMAT: int
UMAT_DATA_USER_ALLOCATED: int
UMAT_DEPTH_MASK: int
UMAT_MAGIC_MASK: int
UMAT_MAGIC_VAL: int
UMAT_SUBMATRIX_FLAG: int
UMAT_TYPE_MASK: int
UMat = _mod_cv2.UMat
UMatData_ASYNC_CLEANUP: int
UMatData_COPY_ON_MAP: int
UMatData_DEVICE_COPY_OBSOLETE: int
UMatData_DEVICE_MEM_MAPPED: int
UMatData_HOST_COPY_OBSOLETE: int
UMatData_TEMP_COPIED_UMAT: int
UMatData_TEMP_UMAT: int
UMatData_USER_ALLOCATED: int
UMat_AUTO_STEP: int
UMat_CONTINUOUS_FLAG: int
UMat_DEPTH_MASK: int
UMat_MAGIC_MASK: int
UMat_MAGIC_VAL: int
UMat_SUBMATRIX_FLAG: int
UMat_TYPE_MASK: int
def UMat_context() -> typing.Any:
    'UMat_context() -> retval\n.'
    ...

def UMat_queue() -> typing.Any:
    'UMat_queue() -> retval\n.'
    ...

USAGE_ALLOCATE_DEVICE_MEMORY: int
USAGE_ALLOCATE_HOST_MEMORY: int
USAGE_ALLOCATE_SHARED_MEMORY: int
USAGE_DEFAULT: int
VIDEOWRITER_PROP_FRAMEBYTES: int
VIDEOWRITER_PROP_IS_COLOR: int
VIDEOWRITER_PROP_NSTRIPES: int
VIDEOWRITER_PROP_QUALITY: int
VariationalRefinement = _mod_cv2.VariationalRefinement
def VariationalRefinement_create() -> typing.Any:
    'VariationalRefinement_create() -> retval\n.   @brief Creates an instance of VariationalRefinement'
    ...

VideoCapture = _mod_cv2.VideoCapture
VideoWriter = _mod_cv2.VideoWriter
def VideoWriter_fourcc(c1, c2, c3, c4) -> typing.Any:
    'VideoWriter_fourcc(c1, c2, c3, c4) -> retval\n.   @brief Concatenates 4 chars to a fourcc code\n.   \n.       @return a fourcc code\n.   \n.       This static method constructs the fourcc code of the codec to be used in the constructor\n.       VideoWriter::VideoWriter or VideoWriter::open.'
    ...

WARP_FILL_OUTLIERS: int
WARP_INVERSE_MAP: int
WARP_POLAR_LINEAR: int
WARP_POLAR_LOG: int
WINDOW_AUTOSIZE: int
WINDOW_FREERATIO: int
WINDOW_FULLSCREEN: int
WINDOW_GUI_EXPANDED: int
WINDOW_GUI_NORMAL: int
WINDOW_KEEPRATIO: int
WINDOW_NORMAL: int
WINDOW_OPENGL: int
WND_PROP_ASPECT_RATIO: int
WND_PROP_AUTOSIZE: int
WND_PROP_FULLSCREEN: int
WND_PROP_OPENGL: int
WND_PROP_TOPMOST: int
WND_PROP_VISIBLE: int
WarperCreator = _mod_cv2.WarperCreator
_INPUT_ARRAY_CUDA_GPU_MAT: int
_INPUT_ARRAY_CUDA_HOST_MEM: int
_INPUT_ARRAY_EXPR: int
_INPUT_ARRAY_FIXED_SIZE: int
_INPUT_ARRAY_FIXED_TYPE: int
_INPUT_ARRAY_KIND_MASK: int
_INPUT_ARRAY_KIND_SHIFT: int
_INPUT_ARRAY_MAT: int
_INPUT_ARRAY_MATX: int
_INPUT_ARRAY_NONE: int
_INPUT_ARRAY_OPENGL_BUFFER: int
_INPUT_ARRAY_STD_ARRAY: int
_INPUT_ARRAY_STD_ARRAY_MAT: int
_INPUT_ARRAY_STD_BOOL_VECTOR: int
_INPUT_ARRAY_STD_VECTOR: int
_INPUT_ARRAY_STD_VECTOR_CUDA_GPU_MAT: int
_INPUT_ARRAY_STD_VECTOR_MAT: int
_INPUT_ARRAY_STD_VECTOR_UMAT: int
_INPUT_ARRAY_STD_VECTOR_VECTOR: int
_INPUT_ARRAY_UMAT: int
_InputArray_CUDA_GPU_MAT: int
_InputArray_CUDA_HOST_MEM: int
_InputArray_EXPR: int
_InputArray_FIXED_SIZE: int
_InputArray_FIXED_TYPE: int
_InputArray_KIND_MASK: int
_InputArray_KIND_SHIFT: int
_InputArray_MAT: int
_InputArray_MATX: int
_InputArray_NONE: int
_InputArray_OPENGL_BUFFER: int
_InputArray_STD_ARRAY: int
_InputArray_STD_ARRAY_MAT: int
_InputArray_STD_BOOL_VECTOR: int
_InputArray_STD_VECTOR: int
_InputArray_STD_VECTOR_CUDA_GPU_MAT: int
_InputArray_STD_VECTOR_MAT: int
_InputArray_STD_VECTOR_UMAT: int
_InputArray_STD_VECTOR_VECTOR: int
_InputArray_UMAT: int
_OUTPUT_ARRAY_DEPTH_MASK_16F: int
_OUTPUT_ARRAY_DEPTH_MASK_16S: int
_OUTPUT_ARRAY_DEPTH_MASK_16U: int
_OUTPUT_ARRAY_DEPTH_MASK_32F: int
_OUTPUT_ARRAY_DEPTH_MASK_32S: int
_OUTPUT_ARRAY_DEPTH_MASK_64F: int
_OUTPUT_ARRAY_DEPTH_MASK_8S: int
_OUTPUT_ARRAY_DEPTH_MASK_8U: int
_OUTPUT_ARRAY_DEPTH_MASK_ALL: int
_OUTPUT_ARRAY_DEPTH_MASK_ALL_16F: int
_OUTPUT_ARRAY_DEPTH_MASK_ALL_BUT_8S: int
_OUTPUT_ARRAY_DEPTH_MASK_FLT: int
_OutputArray_DEPTH_MASK_16F: int
_OutputArray_DEPTH_MASK_16S: int
_OutputArray_DEPTH_MASK_16U: int
_OutputArray_DEPTH_MASK_32F: int
_OutputArray_DEPTH_MASK_32S: int
_OutputArray_DEPTH_MASK_64F: int
_OutputArray_DEPTH_MASK_8S: int
_OutputArray_DEPTH_MASK_8U: int
_OutputArray_DEPTH_MASK_ALL: int
_OutputArray_DEPTH_MASK_ALL_16F: int
_OutputArray_DEPTH_MASK_ALL_BUT_8S: int
_OutputArray_DEPTH_MASK_FLT: int
__UMAT_USAGE_FLAGS_32BIT: int
__doc__: str
__file__: str
__name__: str
__package__: str
__version__: str
def absdiff(src1: Mat, src2: Mat, dts: Mat = ...) -> typing.Any:
    'absdiff(src1, src2[, dst]) -> dst\n.   @brief Calculates the per-element absolute difference between two arrays or between an array and a scalar.\n.   \n.   The function cv::absdiff calculates:\n.   *   Absolute difference between two arrays when they have the same\n.       size and type:\n.       \\f[\\texttt{dst}(I) =  \\texttt{saturate} (| \\texttt{src1}(I) -  \\texttt{src2}(I)|)\\f]\n.   *   Absolute difference between an array and a scalar when the second\n.       array is constructed from Scalar or has as many elements as the\n.       number of channels in `src1`:\n.       \\f[\\texttt{dst}(I) =  \\texttt{saturate} (| \\texttt{src1}(I) -  \\texttt{src2} |)\\f]\n.   *   Absolute difference between a scalar and an array when the first\n.       array is constructed from Scalar or has as many elements as the\n.       number of channels in `src2`:\n.       \\f[\\texttt{dst}(I) =  \\texttt{saturate} (| \\texttt{src1} -  \\texttt{src2}(I) |)\\f]\n.       where I is a multi-dimensional index of array elements. In case of\n.       multi-channel arrays, each channel is processed independently.\n.   @note Saturation is not applied when the arrays have the depth CV_32S.\n.   You may even get a negative value in the case of overflow.\n.   @param src1 first input array or a scalar.\n.   @param src2 second input array or a scalar.\n.   @param dst output array that has the same size and type as input arrays.\n.   @sa cv::abs(const Mat&)'
    ...

def accumulate(src: Mat, dts: Mat, mask: Mat = ...) -> typing.Any:
    'accumulate(src, dst[, mask]) -> dst\n.   @brief Adds an image to the accumulator image.\n.   \n.   The function adds src or some of its elements to dst :\n.   \n.   \\f[\\texttt{dst} (x,y)  \\leftarrow \\texttt{dst} (x,y) +  \\texttt{src} (x,y)  \\quad \\text{if} \\quad \\texttt{mask} (x,y)  \\ne 0\\f]\n.   \n.   The function supports multi-channel images. Each channel is processed independently.\n.   \n.   The function cv::accumulate can be used, for example, to collect statistics of a scene background\n.   viewed by a still camera and for the further foreground-background segmentation.\n.   \n.   @param src Input image of type CV_8UC(n), CV_16UC(n), CV_32FC(n) or CV_64FC(n), where n is a positive integer.\n.   @param dst %Accumulator image with the same number of channels as input image, and a depth of CV_32F or CV_64F.\n.   @param mask Optional operation mask.\n.   \n.   @sa  accumulateSquare, accumulateProduct, accumulateWeighted'
    ...

def accumulateProduct(src1: Mat, src2: Mat, dts: Mat, mask: Mat = ...) -> typing.Any:
    'accumulateProduct(src1, src2, dst[, mask]) -> dst\n.   @brief Adds the per-element product of two input images to the accumulator image.\n.   \n.   The function adds the product of two images or their selected regions to the accumulator dst :\n.   \n.   \\f[\\texttt{dst} (x,y)  \\leftarrow \\texttt{dst} (x,y) +  \\texttt{src1} (x,y)  \\cdot \\texttt{src2} (x,y)  \\quad \\text{if} \\quad \\texttt{mask} (x,y)  \\ne 0\\f]\n.   \n.   The function supports multi-channel images. Each channel is processed independently.\n.   \n.   @param src1 First input image, 1- or 3-channel, 8-bit or 32-bit floating point.\n.   @param src2 Second input image of the same type and the same size as src1 .\n.   @param dst %Accumulator image with the same number of channels as input images, 32-bit or 64-bit\n.   floating-point.\n.   @param mask Optional operation mask.\n.   \n.   @sa  accumulate, accumulateSquare, accumulateWeighted'
    ...

def accumulateSquare(src: Mat, dts: Mat, mask: Mat = ...) -> typing.Any:
    'accumulateSquare(src, dst[, mask]) -> dst\n.   @brief Adds the square of a source image to the accumulator image.\n.   \n.   The function adds the input image src or its selected region, raised to a power of 2, to the\n.   accumulator dst :\n.   \n.   \\f[\\texttt{dst} (x,y)  \\leftarrow \\texttt{dst} (x,y) +  \\texttt{src} (x,y)^2  \\quad \\text{if} \\quad \\texttt{mask} (x,y)  \\ne 0\\f]\n.   \n.   The function supports multi-channel images. Each channel is processed independently.\n.   \n.   @param src Input image as 1- or 3-channel, 8-bit or 32-bit floating point.\n.   @param dst %Accumulator image with the same number of channels as input image, 32-bit or 64-bit\n.   floating-point.\n.   @param mask Optional operation mask.\n.   \n.   @sa  accumulateSquare, accumulateProduct, accumulateWeighted'
    ...

def accumulateWeighted(src: Mat, dts: Mat, alpha, mask: Mat = ...) -> typing.Any:
    'accumulateWeighted(src, dst, alpha[, mask]) -> dst\n.   @brief Updates a running average.\n.   \n.   The function calculates the weighted sum of the input image src and the accumulator dst so that dst\n.   becomes a running average of a frame sequence:\n.   \n.   \\f[\\texttt{dst} (x,y)  \\leftarrow (1- \\texttt{alpha} )  \\cdot \\texttt{dst} (x,y) +  \\texttt{alpha} \\cdot \\texttt{src} (x,y)  \\quad \\text{if} \\quad \\texttt{mask} (x,y)  \\ne 0\\f]\n.   \n.   That is, alpha regulates the update speed (how fast the accumulator "forgets" about earlier images).\n.   The function supports multi-channel images. Each channel is processed independently.\n.   \n.   @param src Input image as 1- or 3-channel, 8-bit or 32-bit floating point.\n.   @param dst %Accumulator image with the same number of channels as input image, 32-bit or 64-bit\n.   floating-point.\n.   @param alpha Weight of the input image.\n.   @param mask Optional operation mask.\n.   \n.   @sa  accumulate, accumulateSquare, accumulateProduct'
    ...

def adaptiveThreshold(src: Mat, maxValue, adaptiveMethod, thresholdType, blockSize, C, dts: Mat = ...) -> typing.Any:
    'adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst\n.   @brief Applies an adaptive threshold to an array.\n.   \n.   The function transforms a grayscale image to a binary image according to the formulae:\n.   -   **THRESH_BINARY**\n.       \\f[dst(x,y) =  \\fork{\\texttt{maxValue}}{if \\(src(x,y) > T(x,y)\\)}{0}{otherwise}\\f]\n.   -   **THRESH_BINARY_INV**\n.       \\f[dst(x,y) =  \\fork{0}{if \\(src(x,y) > T(x,y)\\)}{\\texttt{maxValue}}{otherwise}\\f]\n.   where \\f$T(x,y)\\f$ is a threshold calculated individually for each pixel (see adaptiveMethod parameter).\n.   \n.   The function can process the image in-place.\n.   \n.   @param src Source 8-bit single-channel image.\n.   @param dst Destination image of the same size and the same type as src.\n.   @param maxValue Non-zero value assigned to the pixels for which the condition is satisfied\n.   @param adaptiveMethod Adaptive thresholding algorithm to use, see #AdaptiveThresholdTypes.\n.   The #BORDER_REPLICATE | #BORDER_ISOLATED is used to process boundaries.\n.   @param thresholdType Thresholding type that must be either #THRESH_BINARY or #THRESH_BINARY_INV,\n.   see #ThresholdTypes.\n.   @param blockSize Size of a pixel neighborhood that is used to calculate a threshold value for the\n.   pixel: 3, 5, 7, and so on.\n.   @param C Constant subtracted from the mean or weighted mean (see the details below). Normally, it\n.   is positive but may be zero or negative as well.\n.   \n.   @sa  threshold, blur, GaussianBlur'
    ...

def add(src1: Mat, src2: Mat, dts: Mat = ..., mask: Mat = ..., dtype=...) -> typing.Any:
    'add(src1, src2[, dst[, mask[, dtype]]]) -> dst\n.   @brief Calculates the per-element sum of two arrays or an array and a scalar.\n.   \n.   The function add calculates:\n.   - Sum of two arrays when both input arrays have the same size and the same number of channels:\n.   \\f[\\texttt{dst}(I) =  \\texttt{saturate} ( \\texttt{src1}(I) +  \\texttt{src2}(I)) \\quad \\texttt{if mask}(I) \\ne0\\f]\n.   - Sum of an array and a scalar when src2 is constructed from Scalar or has the same number of\n.   elements as `src1.channels()`:\n.   \\f[\\texttt{dst}(I) =  \\texttt{saturate} ( \\texttt{src1}(I) +  \\texttt{src2} ) \\quad \\texttt{if mask}(I) \\ne0\\f]\n.   - Sum of a scalar and an array when src1 is constructed from Scalar or has the same number of\n.   elements as `src2.channels()`:\n.   \\f[\\texttt{dst}(I) =  \\texttt{saturate} ( \\texttt{src1} +  \\texttt{src2}(I) ) \\quad \\texttt{if mask}(I) \\ne0\\f]\n.   where `I` is a multi-dimensional index of array elements. In case of multi-channel arrays, each\n.   channel is processed independently.\n.   \n.   The first function in the list above can be replaced with matrix expressions:\n.   @code{.cpp}\n.       dst = src1 + src2;\n.       dst += src1; // equivalent to add(dst, src1, dst);\n.   @endcode\n.   The input arrays and the output array can all have the same or different depths. For example, you\n.   can add a 16-bit unsigned array to a 8-bit signed array and store the sum as a 32-bit\n.   floating-point array. Depth of the output array is determined by the dtype parameter. In the second\n.   and third cases above, as well as in the first case, when src1.depth() == src2.depth(), dtype can\n.   be set to the default -1. In this case, the output array will have the same depth as the input\n.   array, be it src1, src2 or both.\n.   @note Saturation is not applied when the output array has the depth CV_32S. You may even get\n.   result of an incorrect sign in the case of overflow.\n.   @param src1 first input array or a scalar.\n.   @param src2 second input array or a scalar.\n.   @param dst output array that has the same size and number of channels as the input array(s); the\n.   depth is defined by dtype or src1/src2.\n.   @param mask optional operation mask - 8-bit single channel array, that specifies elements of the\n.   output array to be changed.\n.   @param dtype optional depth of the output array (see the discussion below).\n.   @sa subtract, addWeighted, scaleAdd, Mat::convertTo'
    ...

def addText(img: Mat, text, org, nameFont, pointSize=..., color=..., weight=..., style=..., spacing=...) -> typing.Any:
    'addText(img, text, org, nameFont[, pointSize[, color[, weight[, style[, spacing]]]]]) -> None\n.   @brief Draws a text on the image.\n.   \n.   @param img 8-bit 3-channel image where the text should be drawn.\n.   @param text Text to write on an image.\n.   @param org Point(x,y) where the text should start on an image.\n.   @param nameFont Name of the font. The name should match the name of a system font (such as\n.   *Times*). If the font is not found, a default one is used.\n.   @param pointSize Size of the font. If not specified, equal zero or negative, the point size of the\n.   font is set to a system-dependent default value. Generally, this is 12 points.\n.   @param color Color of the font in BGRA where A = 255 is fully transparent.\n.   @param weight Font weight. Available operation flags are : cv::QtFontWeights You can also specify a positive integer for better control.\n.   @param style Font style. Available operation flags are : cv::QtFontStyles\n.   @param spacing Spacing between characters. It can be negative or positive.'
    ...

def addWeighted(src1: Mat, alpha, src2: Mat, beta, gamma, dts: Mat = ..., dtype=...) -> typing.Any:
    'addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]]) -> dst\n.   @brief Calculates the weighted sum of two arrays.\n.   \n.   The function addWeighted calculates the weighted sum of two arrays as follows:\n.   \\f[\\texttt{dst} (I)= \\texttt{saturate} ( \\texttt{src1} (I)* \\texttt{alpha} +  \\texttt{src2} (I)* \\texttt{beta} +  \\texttt{gamma} )\\f]\n.   where I is a multi-dimensional index of array elements. In case of multi-channel arrays, each\n.   channel is processed independently.\n.   The function can be replaced with a matrix expression:\n.   @code{.cpp}\n.       dst = src1*alpha + src2*beta + gamma;\n.   @endcode\n.   @note Saturation is not applied when the output array has the depth CV_32S. You may even get\n.   result of an incorrect sign in the case of overflow.\n.   @param src1 first input array.\n.   @param alpha weight of the first array elements.\n.   @param src2 second input array of the same size and channel number as src1.\n.   @param beta weight of the second array elements.\n.   @param gamma scalar added to each sum.\n.   @param dst output array that has the same size and number of channels as the input arrays.\n.   @param dtype optional depth of the output array; when both input arrays have the same depth, dtype\n.   can be set to -1, which will be equivalent to src1.depth().\n.   @sa  add, subtract, scaleAdd, Mat::convertTo'
    ...

def applyColorMap(src: Mat, colormap, dts: Mat = ...) -> typing.Any:
    'applyColorMap(src, colormap[, dst]) -> dst\n.   @brief Applies a GNU Octave/MATLAB equivalent colormap on a given image.\n.   \n.   @param src The source image, grayscale or colored of type CV_8UC1 or CV_8UC3.\n.   @param dst The result is the colormapped source image. Note: Mat::create is called on dst.\n.   @param colormap The colormap to apply, see #ColormapTypes\n\n\n\napplyColorMap(src, userColor[, dst]) -> dst\n.   @brief Applies a user colormap on a given image.\n.   \n.   @param src The source image, grayscale or colored of type CV_8UC1 or CV_8UC3.\n.   @param dst The result is the colormapped source image. Note: Mat::create is called on dst.\n.   @param userColor The colormap to apply of type CV_8UC1 or CV_8UC3 and size 256'
    ...

def approxPolyDP(curve, epsilon, closed, approxCurve=...) -> typing.Any:
    'approxPolyDP(curve, epsilon, closed[, approxCurve]) -> approxCurve\n.   @brief Approximates a polygonal curve(s) with the specified precision.\n.   \n.   The function cv::approxPolyDP approximates a curve or a polygon with another curve/polygon with less\n.   vertices so that the distance between them is less or equal to the specified precision. It uses the\n.   Douglas-Peucker algorithm <http://en.wikipedia.org/wiki/Ramer-Douglas-Peucker_algorithm>\n.   \n.   @param curve Input vector of a 2D point stored in std::vector or Mat\n.   @param approxCurve Result of the approximation. The type should match the type of the input curve.\n.   @param epsilon Parameter specifying the approximation accuracy. This is the maximum distance\n.   between the original curve and its approximation.\n.   @param closed If true, the approximated curve is closed (its first and last vertices are\n.   connected). Otherwise, it is not closed.'
    ...

def arcLength(curve, closed) -> typing.Any:
    'arcLength(curve, closed) -> retval\n.   @brief Calculates a contour perimeter or a curve length.\n.   \n.   The function computes a curve length or a closed contour perimeter.\n.   \n.   @param curve Input vector of 2D points, stored in std::vector or Mat.\n.   @param closed Flag indicating whether the curve is closed or not.'
    ...

def arrowedLine(img: Mat, pt1, pt2, color, thickness=..., line_type=..., shift=..., tipLength=...) -> typing.Any:
    'arrowedLine(img, pt1, pt2, color[, thickness[, line_type[, shift[, tipLength]]]]) -> img\n.   @brief Draws a arrow segment pointing from the first point to the second one.\n.   \n.   The function cv::arrowedLine draws an arrow between pt1 and pt2 points in the image. See also #line.\n.   \n.   @param img Image.\n.   @param pt1 The point the arrow starts from.\n.   @param pt2 The point the arrow points to.\n.   @param color Line color.\n.   @param thickness Line thickness.\n.   @param line_type Type of the line. See #LineTypes\n.   @param shift Number of fractional bits in the point coordinates.\n.   @param tipLength The length of the arrow tip in relation to the arrow length'
    ...

def batchDistance(src1: Mat, src2: Mat, dtype, dist=..., nidx=..., normType: int = ..., K=..., mask: Mat = ..., update=..., crosscheck=...) -> typing.Any:
    'batchDistance(src1, src2, dtype[, dist[, nidx[, normType[, K[, mask[, update[, crosscheck]]]]]]]) -> dist, nidx\n.   @brief naive nearest neighbor finder\n.   \n.   see http://en.wikipedia.org/wiki/Nearest_neighbor_search\n.   @todo document'
    ...

def bilateralFilter(src: Mat, d, sigmaColor, sigmaSpace, dts: Mat = ..., borderType=...) -> typing.Any:
    'bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) -> dst\n.   @brief Applies the bilateral filter to an image.\n.   \n.   The function applies bilateral filtering to the input image, as described in\n.   http://www.dai.ed.ac.uk/CVonline/LOCAL_COPIES/MANDUCHI1/Bilateral_Filtering.html\n.   bilateralFilter can reduce unwanted noise very well while keeping edges fairly sharp. However, it is\n.   very slow compared to most filters.\n.   \n.   _Sigma values_: For simplicity, you can set the 2 sigma values to be the same. If they are small (\\<\n.   10), the filter will not have much effect, whereas if they are large (\\> 150), they will have a very\n.   strong effect, making the image look "cartoonish".\n.   \n.   _Filter size_: Large filters (d \\> 5) are very slow, so it is recommended to use d=5 for real-time\n.   applications, and perhaps d=9 for offline applications that need heavy noise filtering.\n.   \n.   This filter does not work inplace.\n.   @param src Source 8-bit or floating-point, 1-channel or 3-channel image.\n.   @param dst Destination image of the same size and type as src .\n.   @param d Diameter of each pixel neighborhood that is used during filtering. If it is non-positive,\n.   it is computed from sigmaSpace.\n.   @param sigmaColor Filter sigma in the color space. A larger value of the parameter means that\n.   farther colors within the pixel neighborhood (see sigmaSpace) will be mixed together, resulting\n.   in larger areas of semi-equal color.\n.   @param sigmaSpace Filter sigma in the coordinate space. A larger value of the parameter means that\n.   farther pixels will influence each other as long as their colors are close enough (see sigmaColor\n.   ). When d\\>0, it specifies the neighborhood size regardless of sigmaSpace. Otherwise, d is\n.   proportional to sigmaSpace.\n.   @param borderType border mode used to extrapolate pixels outside of the image, see #BorderTypes'
    ...

def bitwise_and(src1: Mat, src2: Mat, dts: Mat = ..., mask: Mat = ...) -> typing.Any:
    'bitwise_and(src1, src2[, dst[, mask]]) -> dst\n.   @brief computes bitwise conjunction of the two arrays (dst = src1 & src2)\n.   Calculates the per-element bit-wise conjunction of two arrays or an\n.   array and a scalar.\n.   \n.   The function cv::bitwise_and calculates the per-element bit-wise logical conjunction for:\n.   *   Two arrays when src1 and src2 have the same size:\n.       \\f[\\texttt{dst} (I) =  \\texttt{src1} (I)  \\wedge \\texttt{src2} (I) \\quad \\texttt{if mask} (I) \\ne0\\f]\n.   *   An array and a scalar when src2 is constructed from Scalar or has\n.       the same number of elements as `src1.channels()`:\n.       \\f[\\texttt{dst} (I) =  \\texttt{src1} (I)  \\wedge \\texttt{src2} \\quad \\texttt{if mask} (I) \\ne0\\f]\n.   *   A scalar and an array when src1 is constructed from Scalar or has\n.       the same number of elements as `src2.channels()`:\n.       \\f[\\texttt{dst} (I) =  \\texttt{src1}  \\wedge \\texttt{src2} (I) \\quad \\texttt{if mask} (I) \\ne0\\f]\n.   In case of floating-point arrays, their machine-specific bit\n.   representations (usually IEEE754-compliant) are used for the operation.\n.   In case of multi-channel arrays, each channel is processed\n.   independently. In the second and third cases above, the scalar is first\n.   converted to the array type.\n.   @param src1 first input array or a scalar.\n.   @param src2 second input array or a scalar.\n.   @param dst output array that has the same size and type as the input\n.   arrays.\n.   @param mask optional operation mask, 8-bit single channel array, that\n.   specifies elements of the output array to be changed.'
    ...

def bitwise_not(src: Mat, dts: Mat = ..., mask: Mat = ...) -> typing.Any:
    'bitwise_not(src[, dst[, mask]]) -> dst\n.   @brief  Inverts every bit of an array.\n.   \n.   The function cv::bitwise_not calculates per-element bit-wise inversion of the input\n.   array:\n.   \\f[\\texttt{dst} (I) =  \\neg \\texttt{src} (I)\\f]\n.   In case of a floating-point input array, its machine-specific bit\n.   representation (usually IEEE754-compliant) is used for the operation. In\n.   case of multi-channel arrays, each channel is processed independently.\n.   @param src input array.\n.   @param dst output array that has the same size and type as the input\n.   array.\n.   @param mask optional operation mask, 8-bit single channel array, that\n.   specifies elements of the output array to be changed.'
    ...

def bitwise_or(src1: Mat, src2: Mat, dts: Mat = ..., mask: Mat = ...) -> typing.Any:
    'bitwise_or(src1, src2[, dst[, mask]]) -> dst\n.   @brief Calculates the per-element bit-wise disjunction of two arrays or an\n.   array and a scalar.\n.   \n.   The function cv::bitwise_or calculates the per-element bit-wise logical disjunction for:\n.   *   Two arrays when src1 and src2 have the same size:\n.       \\f[\\texttt{dst} (I) =  \\texttt{src1} (I)  \\vee \\texttt{src2} (I) \\quad \\texttt{if mask} (I) \\ne0\\f]\n.   *   An array and a scalar when src2 is constructed from Scalar or has\n.       the same number of elements as `src1.channels()`:\n.       \\f[\\texttt{dst} (I) =  \\texttt{src1} (I)  \\vee \\texttt{src2} \\quad \\texttt{if mask} (I) \\ne0\\f]\n.   *   A scalar and an array when src1 is constructed from Scalar or has\n.       the same number of elements as `src2.channels()`:\n.       \\f[\\texttt{dst} (I) =  \\texttt{src1}  \\vee \\texttt{src2} (I) \\quad \\texttt{if mask} (I) \\ne0\\f]\n.   In case of floating-point arrays, their machine-specific bit\n.   representations (usually IEEE754-compliant) are used for the operation.\n.   In case of multi-channel arrays, each channel is processed\n.   independently. In the second and third cases above, the scalar is first\n.   converted to the array type.\n.   @param src1 first input array or a scalar.\n.   @param src2 second input array or a scalar.\n.   @param dst output array that has the same size and type as the input\n.   arrays.\n.   @param mask optional operation mask, 8-bit single channel array, that\n.   specifies elements of the output array to be changed.'
    ...

def bitwise_xor(src1: Mat, src2: Mat, dts: Mat = ..., mask: Mat = ...) -> typing.Any:
    'bitwise_xor(src1, src2[, dst[, mask]]) -> dst\n.   @brief Calculates the per-element bit-wise "exclusive or" operation on two\n.   arrays or an array and a scalar.\n.   \n.   The function cv::bitwise_xor calculates the per-element bit-wise logical "exclusive-or"\n.   operation for:\n.   *   Two arrays when src1 and src2 have the same size:\n.       \\f[\\texttt{dst} (I) =  \\texttt{src1} (I)  \\oplus \\texttt{src2} (I) \\quad \\texttt{if mask} (I) \\ne0\\f]\n.   *   An array and a scalar when src2 is constructed from Scalar or has\n.       the same number of elements as `src1.channels()`:\n.       \\f[\\texttt{dst} (I) =  \\texttt{src1} (I)  \\oplus \\texttt{src2} \\quad \\texttt{if mask} (I) \\ne0\\f]\n.   *   A scalar and an array when src1 is constructed from Scalar or has\n.       the same number of elements as `src2.channels()`:\n.       \\f[\\texttt{dst} (I) =  \\texttt{src1}  \\oplus \\texttt{src2} (I) \\quad \\texttt{if mask} (I) \\ne0\\f]\n.   In case of floating-point arrays, their machine-specific bit\n.   representations (usually IEEE754-compliant) are used for the operation.\n.   In case of multi-channel arrays, each channel is processed\n.   independently. In the 2nd and 3rd cases above, the scalar is first\n.   converted to the array type.\n.   @param src1 first input array or a scalar.\n.   @param src2 second input array or a scalar.\n.   @param dst output array that has the same size and type as the input\n.   arrays.\n.   @param mask optional operation mask, 8-bit single channel array, that\n.   specifies elements of the output array to be changed.'
    ...

def blur(src: Mat, ksize, dts: Mat = ..., anchor=..., borderType=...) -> typing.Any:
    'blur(src, ksize[, dst[, anchor[, borderType]]]) -> dst\n.   @brief Blurs an image using the normalized box filter.\n.   \n.   The function smooths an image using the kernel:\n.   \n.   \\f[\\texttt{K} =  \\frac{1}{\\texttt{ksize.width*ksize.height}} \\begin{bmatrix} 1 & 1 & 1 &  \\cdots & 1 & 1  \\\\ 1 & 1 & 1 &  \\cdots & 1 & 1  \\\\ \\hdotsfor{6} \\\\ 1 & 1 & 1 &  \\cdots & 1 & 1  \\\\ \\end{bmatrix}\\f]\n.   \n.   The call `blur(src, dst, ksize, anchor, borderType)` is equivalent to `boxFilter(src, dst, src.type(), ksize,\n.   anchor, true, borderType)`.\n.   \n.   @param src input image; it can have any number of channels, which are processed independently, but\n.   the depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.\n.   @param dst output image of the same size and type as src.\n.   @param ksize blurring kernel size.\n.   @param anchor anchor point; default value Point(-1,-1) means that the anchor is at the kernel\n.   center.\n.   @param borderType border mode used to extrapolate pixels outside of the image, see #BorderTypes. #BORDER_WRAP is not supported.\n.   @sa  boxFilter, bilateralFilter, GaussianBlur, medianBlur'
    ...

def borderInterpolate(p, len, borderType) -> typing.Any:
    'borderInterpolate(p, len, borderType) -> retval\n.   @brief Computes the source location of an extrapolated pixel.\n.   \n.   The function computes and returns the coordinate of a donor pixel corresponding to the specified\n.   extrapolated pixel when using the specified extrapolation border mode. For example, if you use\n.   cv::BORDER_WRAP mode in the horizontal direction, cv::BORDER_REFLECT_101 in the vertical direction and\n.   want to compute value of the "virtual" pixel Point(-5, 100) in a floating-point image img , it\n.   looks like:\n.   @code{.cpp}\n.       float val = img.at<float>(borderInterpolate(100, img.rows, cv::BORDER_REFLECT_101),\n.                                 borderInterpolate(-5, img.cols, cv::BORDER_WRAP));\n.   @endcode\n.   Normally, the function is not called directly. It is used inside filtering functions and also in\n.   copyMakeBorder.\n.   @param p 0-based coordinate of the extrapolated pixel along one of the axes, likely \\<0 or \\>= len\n.   @param len Length of the array along the corresponding axis.\n.   @param borderType Border type, one of the #BorderTypes, except for #BORDER_TRANSPARENT and\n.   #BORDER_ISOLATED . When borderType==#BORDER_CONSTANT , the function always returns -1, regardless\n.   of p and len.\n.   \n.   @sa copyMakeBorder'
    ...

def boundingRect(array) -> typing.Any:
    'boundingRect(array) -> retval\n.   @brief Calculates the up-right bounding rectangle of a point set or non-zero pixels of gray-scale image.\n.   \n.   The function calculates and returns the minimal up-right bounding rectangle for the specified point set or\n.   non-zero pixels of gray-scale image.\n.   \n.   @param array Input gray-scale image or 2D point set, stored in std::vector or Mat.'
    ...

def boxFilter(src: Mat, ddepth, ksize, dts: Mat = ..., anchor=..., normalize=..., borderType=...) -> typing.Any:
    'boxFilter(src, ddepth, ksize[, dst[, anchor[, normalize[, borderType]]]]) -> dst\n.   @brief Blurs an image using the box filter.\n.   \n.   The function smooths an image using the kernel:\n.   \n.   \\f[\\texttt{K} =  \\alpha \\begin{bmatrix} 1 & 1 & 1 &  \\cdots & 1 & 1  \\\\ 1 & 1 & 1 &  \\cdots & 1 & 1  \\\\ \\hdotsfor{6} \\\\ 1 & 1 & 1 &  \\cdots & 1 & 1 \\end{bmatrix}\\f]\n.   \n.   where\n.   \n.   \\f[\\alpha = \\begin{cases} \\frac{1}{\\texttt{ksize.width*ksize.height}} & \\texttt{when } \\texttt{normalize=true}  \\\\1 & \\texttt{otherwise}\\end{cases}\\f]\n.   \n.   Unnormalized box filter is useful for computing various integral characteristics over each pixel\n.   neighborhood, such as covariance matrices of image derivatives (used in dense optical flow\n.   algorithms, and so on). If you need to compute pixel sums over variable-size windows, use #integral.\n.   \n.   @param src input image.\n.   @param dst output image of the same size and type as src.\n.   @param ddepth the output image depth (-1 to use src.depth()).\n.   @param ksize blurring kernel size.\n.   @param anchor anchor point; default value Point(-1,-1) means that the anchor is at the kernel\n.   center.\n.   @param normalize flag, specifying whether the kernel is normalized by its area or not.\n.   @param borderType border mode used to extrapolate pixels outside of the image, see #BorderTypes. #BORDER_WRAP is not supported.\n.   @sa  blur, bilateralFilter, GaussianBlur, medianBlur, integral'
    ...

def boxPoints(box, points=...) -> typing.Any:
    'boxPoints(box[, points]) -> points\n.   @brief Finds the four vertices of a rotated rect. Useful to draw the rotated rectangle.\n.   \n.   The function finds the four vertices of a rotated rectangle. This function is useful to draw the\n.   rectangle. In C++, instead of using this function, you can directly use RotatedRect::points method. Please\n.   visit the @ref tutorial_bounding_rotated_ellipses "tutorial on Creating Bounding rotated boxes and ellipses for contours" for more information.\n.   \n.   @param box The input rotated rectangle. It may be the output of\n.   @param points The output array of four vertices of rectangles.'
    ...

def buildOpticalFlowPyramid(img: Mat, winSize, maxLevel, pyramid=..., withDerivatives=..., pyrBorder=..., derivBorder=..., tryReuseInputImage=...) -> typing.Any:
    'buildOpticalFlowPyramid(img, winSize, maxLevel[, pyramid[, withDerivatives[, pyrBorder[, derivBorder[, tryReuseInputImage]]]]]) -> retval, pyramid\n.   @brief Constructs the image pyramid which can be passed to calcOpticalFlowPyrLK.\n.   \n.   @param img 8-bit input image.\n.   @param pyramid output pyramid.\n.   @param winSize window size of optical flow algorithm. Must be not less than winSize argument of\n.   calcOpticalFlowPyrLK. It is needed to calculate required padding for pyramid levels.\n.   @param maxLevel 0-based maximal pyramid level number.\n.   @param withDerivatives set to precompute gradients for the every pyramid level. If pyramid is\n.   constructed without the gradients then calcOpticalFlowPyrLK will calculate them internally.\n.   @param pyrBorder the border mode for pyramid layers.\n.   @param derivBorder the border mode for gradients.\n.   @param tryReuseInputImage put ROI of input image into the pyramid if possible. You can pass false\n.   to force data copying.\n.   @return number of levels in constructed pyramid. Can be less than maxLevel.'
    ...

def calcBackProject(images: typing.List[Mat], channels: typing.List[int], hist, ranges: typing.List[int], scale, dts: Mat = ...) -> typing.Any:
    'calcBackProject(images, channels, hist, ranges, scale[, dst]) -> dst\n.   @overload'
    ...

def calcCovarMatrix(samples, mean, flags: int, covar=..., ctype=...) -> typing.Any:
    "calcCovarMatrix(samples, mean, flags[, covar[, ctype]]) -> covar, mean\n.   @overload\n.   @note use #COVAR_ROWS or #COVAR_COLS flag\n.   @param samples samples stored as rows/columns of a single matrix.\n.   @param covar output covariance matrix of the type ctype and square size.\n.   @param mean input or output (depending on the flags) array as the average value of the input vectors.\n.   @param flags operation flags as a combination of #CovarFlags\n.   @param ctype type of the matrixl; it equals 'CV_64F' by default."
    ...

def calcHist(images: typing.List[Mat], channels: typing.List[int], mask: typing.Optional[Mat], histSize: typing.List[int], ranges: typing.List[int], hist=..., accumulate=...) -> Mat:
    'calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) -> hist\n.   @overload'
    ...

def calcOpticalFlowFarneback(prev, next, flow, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags: int) -> typing.Any:
    "calcOpticalFlowFarneback(prev, next, flow, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags) -> flow\n.   @brief Computes a dense optical flow using the Gunnar Farneback's algorithm.\n.   \n.   @param prev first 8-bit single-channel input image.\n.   @param next second input image of the same size and the same type as prev.\n.   @param flow computed flow image that has the same size as prev and type CV_32FC2.\n.   @param pyr_scale parameter, specifying the image scale (\\<1) to build pyramids for each image;\n.   pyr_scale=0.5 means a classical pyramid, where each next layer is twice smaller than the previous\n.   one.\n.   @param levels number of pyramid layers including the initial image; levels=1 means that no extra\n.   layers are created and only the original images are used.\n.   @param winsize averaging window size; larger values increase the algorithm robustness to image\n.   noise and give more chances for fast motion detection, but yield more blurred motion field.\n.   @param iterations number of iterations the algorithm does at each pyramid level.\n.   @param poly_n size of the pixel neighborhood used to find polynomial expansion in each pixel;\n.   larger values mean that the image will be approximated with smoother surfaces, yielding more\n.   robust algorithm and more blurred motion field, typically poly_n =5 or 7.\n.   @param poly_sigma standard deviation of the Gaussian that is used to smooth derivatives used as a\n.   basis for the polynomial expansion; for poly_n=5, you can set poly_sigma=1.1, for poly_n=7, a\n.   good value would be poly_sigma=1.5.\n.   @param flags operation flags that can be a combination of the following:\n.    -   **OPTFLOW_USE_INITIAL_FLOW** uses the input flow as an initial flow approximation.\n.    -   **OPTFLOW_FARNEBACK_GAUSSIAN** uses the Gaussian \\f$\\texttt{winsize}\\times\\texttt{winsize}\\f$\n.        filter instead of a box filter of the same size for optical flow estimation; usually, this\n.        option gives z more accurate flow than with a box filter, at the cost of lower speed;\n.        normally, winsize for a Gaussian window should be set to a larger value to achieve the same\n.        level of robustness.\n.   \n.   The function finds an optical flow for each prev pixel using the @cite Farneback2003 algorithm so that\n.   \n.   \\f[\\texttt{prev} (y,x)  \\sim \\texttt{next} ( y + \\texttt{flow} (y,x)[1],  x + \\texttt{flow} (y,x)[0])\\f]\n.   \n.   @note\n.   \n.   -   An example using the optical flow algorithm described by Gunnar Farneback can be found at\n.       opencv_source_code/samples/cpp/fback.cpp\n.   -   (Python) An example using the optical flow algorithm described by Gunnar Farneback can be\n.       found at opencv_source_code/samples/python/opt_flow.py"
    ...

def calcOpticalFlowPyrLK(prevImg, nextImg, prevPts, nextPts, status=..., err=..., winSize=..., maxLevel=..., criteria=..., flags: int = ..., minEigThreshold=...) -> typing.Any:
    "calcOpticalFlowPyrLK(prevImg, nextImg, prevPts, nextPts[, status[, err[, winSize[, maxLevel[, criteria[, flags[, minEigThreshold]]]]]]]) -> nextPts, status, err\n.   @brief Calculates an optical flow for a sparse feature set using the iterative Lucas-Kanade method with\n.   pyramids.\n.   \n.   @param prevImg first 8-bit input image or pyramid constructed by buildOpticalFlowPyramid.\n.   @param nextImg second input image or pyramid of the same size and the same type as prevImg.\n.   @param prevPts vector of 2D points for which the flow needs to be found; point coordinates must be\n.   single-precision floating-point numbers.\n.   @param nextPts output vector of 2D points (with single-precision floating-point coordinates)\n.   containing the calculated new positions of input features in the second image; when\n.   OPTFLOW_USE_INITIAL_FLOW flag is passed, the vector must have the same size as in the input.\n.   @param status output status vector (of unsigned chars); each element of the vector is set to 1 if\n.   the flow for the corresponding features has been found, otherwise, it is set to 0.\n.   @param err output vector of errors; each element of the vector is set to an error for the\n.   corresponding feature, type of the error measure can be set in flags parameter; if the flow wasn't\n.   found then the error is not defined (use the status parameter to find such cases).\n.   @param winSize size of the search window at each pyramid level.\n.   @param maxLevel 0-based maximal pyramid level number; if set to 0, pyramids are not used (single\n.   level), if set to 1, two levels are used, and so on; if pyramids are passed to input then\n.   algorithm will use as many levels as pyramids have but no more than maxLevel.\n.   @param criteria parameter, specifying the termination criteria of the iterative search algorithm\n.   (after the specified maximum number of iterations criteria.maxCount or when the search window\n.   moves by less than criteria.epsilon.\n.   @param flags operation flags:\n.    -   **OPTFLOW_USE_INITIAL_FLOW** uses initial estimations, stored in nextPts; if the flag is\n.        not set, then prevPts is copied to nextPts and is considered the initial estimate.\n.    -   **OPTFLOW_LK_GET_MIN_EIGENVALS** use minimum eigen values as an error measure (see\n.        minEigThreshold description); if the flag is not set, then L1 distance between patches\n.        around the original and a moved point, divided by number of pixels in a window, is used as a\n.        error measure.\n.   @param minEigThreshold the algorithm calculates the minimum eigen value of a 2x2 normal matrix of\n.   optical flow equations (this matrix is called a spatial gradient matrix in @cite Bouguet00), divided\n.   by number of pixels in a window; if this value is less than minEigThreshold, then a corresponding\n.   feature is filtered out and its flow is not processed, so it allows to remove bad points and get a\n.   performance boost.\n.   \n.   The function implements a sparse iterative version of the Lucas-Kanade optical flow in pyramids. See\n.   @cite Bouguet00 . The function is parallelized with the TBB library.\n.   \n.   @note\n.   \n.   -   An example using the Lucas-Kanade optical flow algorithm can be found at\n.       opencv_source_code/samples/cpp/lkdemo.cpp\n.   -   (Python) An example using the Lucas-Kanade optical flow algorithm can be found at\n.       opencv_source_code/samples/python/lk_track.py\n.   -   (Python) An example using the Lucas-Kanade tracker for homography matching can be found at\n.       opencv_source_code/samples/python/lk_homography.py"
    ...

def calibrateCamera(objectPoints, imagePoints, imageSize, cameraMatrix, distCoeffs, rvecs=..., tvecs=..., flags: int = ..., criteria=...) -> typing.Any:
    'calibrateCamera(objectPoints, imagePoints, imageSize, cameraMatrix, distCoeffs[, rvecs[, tvecs[, flags[, criteria]]]]) -> retval, cameraMatrix, distCoeffs, rvecs, tvecs\n.   @overload'
    ...

def calibrateCameraExtended(objectPoints, imagePoints, imageSize, cameraMatrix, distCoeffs, rvecs=..., tvecs=..., stdDeviationsIntrinsics=..., stdDeviationsExtrinsics=..., perViewErrors=..., flags: int = ..., criteria=...) -> typing.Any:
    "calibrateCameraExtended(objectPoints, imagePoints, imageSize, cameraMatrix, distCoeffs[, rvecs[, tvecs[, stdDeviationsIntrinsics[, stdDeviationsExtrinsics[, perViewErrors[, flags[, criteria]]]]]]]) -> retval, cameraMatrix, distCoeffs, rvecs, tvecs, stdDeviationsIntrinsics, stdDeviationsExtrinsics, perViewErrors\n.   @brief Finds the camera intrinsic and extrinsic parameters from several views of a calibration\n.   pattern.\n.   \n.   @param objectPoints In the new interface it is a vector of vectors of calibration pattern points in\n.   the calibration pattern coordinate space (e.g. std::vector<std::vector<cv::Vec3f>>). The outer\n.   vector contains as many elements as the number of pattern views. If the same calibration pattern\n.   is shown in each view and it is fully visible, all the vectors will be the same. Although, it is\n.   possible to use partially occluded patterns or even different patterns in different views. Then,\n.   the vectors will be different. Although the points are 3D, they all lie in the calibration pattern's\n.   XY coordinate plane (thus 0 in the Z-coordinate), if the used calibration pattern is a planar rig.\n.   In the old interface all the vectors of object points from different views are concatenated\n.   together.\n.   @param imagePoints In the new interface it is a vector of vectors of the projections of calibration\n.   pattern points (e.g. std::vector<std::vector<cv::Vec2f>>). imagePoints.size() and\n.   objectPoints.size(), and imagePoints[i].size() and objectPoints[i].size() for each i, must be equal,\n.   respectively. In the old interface all the vectors of object points from different views are\n.   concatenated together.\n.   @param imageSize Size of the image used only to initialize the intrinsic camera matrix.\n.   @param cameraMatrix Input/output 3x3 floating-point camera matrix\n.   \\f$A = \\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\\f$ . If CV\\_CALIB\\_USE\\_INTRINSIC\\_GUESS\n.   and/or CALIB_FIX_ASPECT_RATIO are specified, some or all of fx, fy, cx, cy must be\n.   initialized before calling the function.\n.   @param distCoeffs Input/output vector of distortion coefficients\n.   \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6 [, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$ of\n.   4, 5, 8, 12 or 14 elements.\n.   @param rvecs Output vector of rotation vectors (@ref Rodrigues ) estimated for each pattern view\n.   (e.g. std::vector<cv::Mat>>). That is, each i-th rotation vector together with the corresponding\n.   i-th translation vector (see the next output parameter description) brings the calibration pattern\n.   from the object coordinate space (in which object points are specified) to the camera coordinate\n.   space. In more technical terms, the tuple of the i-th rotation and translation vector performs\n.   a change of basis from object coordinate space to camera coordinate space. Due to its duality, this\n.   tuple is equivalent to the position of the calibration pattern with respect to the camera coordinate\n.   space.\n.   @param tvecs Output vector of translation vectors estimated for each pattern view, see parameter\n.   describtion above.\n.   @param stdDeviationsIntrinsics Output vector of standard deviations estimated for intrinsic\n.   parameters. Order of deviations values:\n.   \\f$(f_x, f_y, c_x, c_y, k_1, k_2, p_1, p_2, k_3, k_4, k_5, k_6 , s_1, s_2, s_3,\n.    s_4, \\tau_x, \\tau_y)\\f$ If one of parameters is not estimated, it's deviation is equals to zero.\n.   @param stdDeviationsExtrinsics Output vector of standard deviations estimated for extrinsic\n.   parameters. Order of deviations values: \\f$(R_0, T_0, \\dotsc , R_{M - 1}, T_{M - 1})\\f$ where M is\n.   the number of pattern views. \\f$R_i, T_i\\f$ are concatenated 1x3 vectors.\n.    @param perViewErrors Output vector of the RMS re-projection error estimated for each pattern view.\n.   @param flags Different flags that may be zero or a combination of the following values:\n.   -   **CALIB_USE_INTRINSIC_GUESS** cameraMatrix contains valid initial values of\n.   fx, fy, cx, cy that are optimized further. Otherwise, (cx, cy) is initially set to the image\n.   center ( imageSize is used), and focal distances are computed in a least-squares fashion.\n.   Note, that if intrinsic parameters are known, there is no need to use this function just to\n.   estimate extrinsic parameters. Use solvePnP instead.\n.   -   **CALIB_FIX_PRINCIPAL_POINT** The principal point is not changed during the global\n.   optimization. It stays at the center or at a different location specified when\n.   CALIB_USE_INTRINSIC_GUESS is set too.\n.   -   **CALIB_FIX_ASPECT_RATIO** The functions consider only fy as a free parameter. The\n.   ratio fx/fy stays the same as in the input cameraMatrix . When\n.   CALIB_USE_INTRINSIC_GUESS is not set, the actual input values of fx and fy are\n.   ignored, only their ratio is computed and used further.\n.   -   **CALIB_ZERO_TANGENT_DIST** Tangential distortion coefficients \\f$(p_1, p_2)\\f$ are set\n.   to zeros and stay zero.\n.   -   **CALIB_FIX_K1,...,CALIB_FIX_K6** The corresponding radial distortion\n.   coefficient is not changed during the optimization. If CALIB_USE_INTRINSIC_GUESS is\n.   set, the coefficient from the supplied distCoeffs matrix is used. Otherwise, it is set to 0.\n.   -   **CALIB_RATIONAL_MODEL** Coefficients k4, k5, and k6 are enabled. To provide the\n.   backward compatibility, this extra flag should be explicitly specified to make the\n.   calibration function use the rational model and return 8 coefficients. If the flag is not\n.   set, the function computes and returns only 5 distortion coefficients.\n.   -   **CALIB_THIN_PRISM_MODEL** Coefficients s1, s2, s3 and s4 are enabled. To provide the\n.   backward compatibility, this extra flag should be explicitly specified to make the\n.   calibration function use the thin prism model and return 12 coefficients. If the flag is not\n.   set, the function computes and returns only 5 distortion coefficients.\n.   -   **CALIB_FIX_S1_S2_S3_S4** The thin prism distortion coefficients are not changed during\n.   the optimization. If CALIB_USE_INTRINSIC_GUESS is set, the coefficient from the\n.   supplied distCoeffs matrix is used. Otherwise, it is set to 0.\n.   -   **CALIB_TILTED_MODEL** Coefficients tauX and tauY are enabled. To provide the\n.   backward compatibility, this extra flag should be explicitly specified to make the\n.   calibration function use the tilted sensor model and return 14 coefficients. If the flag is not\n.   set, the function computes and returns only 5 distortion coefficients.\n.   -   **CALIB_FIX_TAUX_TAUY** The coefficients of the tilted sensor model are not changed during\n.   the optimization. If CALIB_USE_INTRINSIC_GUESS is set, the coefficient from the\n.   supplied distCoeffs matrix is used. Otherwise, it is set to 0.\n.   @param criteria Termination criteria for the iterative optimization algorithm.\n.   \n.   @return the overall RMS re-projection error.\n.   \n.   The function estimates the intrinsic camera parameters and extrinsic parameters for each of the\n.   views. The algorithm is based on @cite Zhang2000 and @cite BouguetMCT . The coordinates of 3D object\n.   points and their corresponding 2D projections in each view must be specified. That may be achieved\n.   by using an object with known geometry and easily detectable feature points. Such an object is\n.   called a calibration rig or calibration pattern, and OpenCV has built-in support for a chessboard as\n.   a calibration rig (see @ref findChessboardCorners). Currently, initialization of intrinsic\n.   parameters (when CALIB_USE_INTRINSIC_GUESS is not set) is only implemented for planar calibration\n.   patterns (where Z-coordinates of the object points must be all zeros). 3D calibration rigs can also\n.   be used as long as initial cameraMatrix is provided.\n.   \n.   The algorithm performs the following steps:\n.   \n.   -   Compute the initial intrinsic parameters (the option only available for planar calibration\n.       patterns) or read them from the input parameters. The distortion coefficients are all set to\n.       zeros initially unless some of CALIB_FIX_K? are specified.\n.   \n.   -   Estimate the initial camera pose as if the intrinsic parameters have been already known. This is\n.       done using solvePnP .\n.   \n.   -   Run the global Levenberg-Marquardt optimization algorithm to minimize the reprojection error,\n.       that is, the total sum of squared distances between the observed feature points imagePoints and\n.       the projected (using the current estimates for camera parameters and the poses) object points\n.       objectPoints. See projectPoints for details.\n.   \n.   @note\n.       If you use a non-square (i.e. non-N-by-N) grid and @ref findChessboardCorners for calibration,\n.       and @ref calibrateCamera returns bad values (zero distortion coefficients, \\f$c_x\\f$ and\n.       \\f$c_y\\f$ very far from the image center, and/or large differences between \\f$f_x\\f$ and\n.       \\f$f_y\\f$ (ratios of 10:1 or more)), then you are probably using patternSize=cvSize(rows,cols)\n.       instead of using patternSize=cvSize(cols,rows) in @ref findChessboardCorners.\n.   \n.   @sa\n.      calibrateCameraRO, findChessboardCorners, solvePnP, initCameraMatrix2D, stereoCalibrate,\n.      undistort"
    ...

def calibrateCameraRO(objectPoints, imagePoints, imageSize, iFixedPoint, cameraMatrix, distCoeffs, rvecs=..., tvecs=..., newObjPoints=..., flags: int = ..., criteria=...) -> typing.Any:
    'calibrateCameraRO(objectPoints, imagePoints, imageSize, iFixedPoint, cameraMatrix, distCoeffs[, rvecs[, tvecs[, newObjPoints[, flags[, criteria]]]]]) -> retval, cameraMatrix, distCoeffs, rvecs, tvecs, newObjPoints\n.   @overload'
    ...

def calibrateCameraROExtended(objectPoints, imagePoints, imageSize, iFixedPoint, cameraMatrix, distCoeffs, rvecs=..., tvecs=..., newObjPoints=..., stdDeviationsIntrinsics=..., stdDeviationsExtrinsics=..., stdDeviationsObjPoints=..., perViewErrors=..., flags: int = ..., criteria=...) -> typing.Any:
    'calibrateCameraROExtended(objectPoints, imagePoints, imageSize, iFixedPoint, cameraMatrix, distCoeffs[, rvecs[, tvecs[, newObjPoints[, stdDeviationsIntrinsics[, stdDeviationsExtrinsics[, stdDeviationsObjPoints[, perViewErrors[, flags[, criteria]]]]]]]]]) -> retval, cameraMatrix, distCoeffs, rvecs, tvecs, newObjPoints, stdDeviationsIntrinsics, stdDeviationsExtrinsics, stdDeviationsObjPoints, perViewErrors\n.   @brief Finds the camera intrinsic and extrinsic parameters from several views of a calibration pattern.\n.   \n.   This function is an extension of calibrateCamera() with the method of releasing object which was\n.   proposed in @cite strobl2011iccv. In many common cases with inaccurate, unmeasured, roughly planar\n.   targets (calibration plates), this method can dramatically improve the precision of the estimated\n.   camera parameters. Both the object-releasing method and standard method are supported by this\n.   function. Use the parameter **iFixedPoint** for method selection. In the internal implementation,\n.   calibrateCamera() is a wrapper for this function.\n.   \n.   @param objectPoints Vector of vectors of calibration pattern points in the calibration pattern\n.   coordinate space. See calibrateCamera() for details. If the method of releasing object to be used,\n.   the identical calibration board must be used in each view and it must be fully visible, and all\n.   objectPoints[i] must be the same and all points should be roughly close to a plane. **The calibration\n.   target has to be rigid, or at least static if the camera (rather than the calibration target) is\n.   shifted for grabbing images.**\n.   @param imagePoints Vector of vectors of the projections of calibration pattern points. See\n.   calibrateCamera() for details.\n.   @param imageSize Size of the image used only to initialize the intrinsic camera matrix.\n.   @param iFixedPoint The index of the 3D object point in objectPoints[0] to be fixed. It also acts as\n.   a switch for calibration method selection. If object-releasing method to be used, pass in the\n.   parameter in the range of [1, objectPoints[0].size()-2], otherwise a value out of this range will\n.   make standard calibration method selected. Usually the top-right corner point of the calibration\n.   board grid is recommended to be fixed when object-releasing method being utilized. According to\n.   \\cite strobl2011iccv, two other points are also fixed. In this implementation, objectPoints[0].front\n.   and objectPoints[0].back.z are used. With object-releasing method, accurate rvecs, tvecs and\n.   newObjPoints are only possible if coordinates of these three fixed points are accurate enough.\n.   @param cameraMatrix Output 3x3 floating-point camera matrix. See calibrateCamera() for details.\n.   @param distCoeffs Output vector of distortion coefficients. See calibrateCamera() for details.\n.   @param rvecs Output vector of rotation vectors estimated for each pattern view. See calibrateCamera()\n.   for details.\n.   @param tvecs Output vector of translation vectors estimated for each pattern view.\n.   @param newObjPoints The updated output vector of calibration pattern points. The coordinates might\n.   be scaled based on three fixed points. The returned coordinates are accurate only if the above\n.   mentioned three fixed points are accurate. If not needed, noArray() can be passed in. This parameter\n.   is ignored with standard calibration method.\n.   @param stdDeviationsIntrinsics Output vector of standard deviations estimated for intrinsic parameters.\n.   See calibrateCamera() for details.\n.   @param stdDeviationsExtrinsics Output vector of standard deviations estimated for extrinsic parameters.\n.   See calibrateCamera() for details.\n.   @param stdDeviationsObjPoints Output vector of standard deviations estimated for refined coordinates\n.   of calibration pattern points. It has the same size and order as objectPoints[0] vector. This\n.   parameter is ignored with standard calibration method.\n.    @param perViewErrors Output vector of the RMS re-projection error estimated for each pattern view.\n.   @param flags Different flags that may be zero or a combination of some predefined values. See\n.   calibrateCamera() for details. If the method of releasing object is used, the calibration time may\n.   be much longer. CALIB_USE_QR or CALIB_USE_LU could be used for faster calibration with potentially\n.   less precise and less stable in some rare cases.\n.   @param criteria Termination criteria for the iterative optimization algorithm.\n.   \n.   @return the overall RMS re-projection error.\n.   \n.   The function estimates the intrinsic camera parameters and extrinsic parameters for each of the\n.   views. The algorithm is based on @cite Zhang2000, @cite BouguetMCT and @cite strobl2011iccv. See\n.   calibrateCamera() for other detailed explanations.\n.   @sa\n.      calibrateCamera, findChessboardCorners, solvePnP, initCameraMatrix2D, stereoCalibrate, undistort'
    ...

def calibrateHandEye(R_gripper2base, t_gripper2base, R_target2cam, t_target2cam, R_cam2gripper=..., t_cam2gripper=..., method: int = ...) -> typing.Any:
    'calibrateHandEye(R_gripper2base, t_gripper2base, R_target2cam, t_target2cam[, R_cam2gripper[, t_cam2gripper[, method]]]) -> R_cam2gripper, t_cam2gripper\n.   @brief Computes Hand-Eye calibration: \\f$_{}^{g}\\textrm{T}_c\\f$\n.   \n.   @param[in] R_gripper2base Rotation part extracted from the homogeneous matrix that transforms a point\n.   expressed in the gripper frame to the robot base frame (\\f$_{}^{b}\\textrm{T}_g\\f$).\n.   This is a vector (`vector<Mat>`) that contains the rotation matrices for all the transformations\n.   from gripper frame to robot base frame.\n.   @param[in] t_gripper2base Translation part extracted from the homogeneous matrix that transforms a point\n.   expressed in the gripper frame to the robot base frame (\\f$_{}^{b}\\textrm{T}_g\\f$).\n.   This is a vector (`vector<Mat>`) that contains the translation vectors for all the transformations\n.   from gripper frame to robot base frame.\n.   @param[in] R_target2cam Rotation part extracted from the homogeneous matrix that transforms a point\n.   expressed in the target frame to the camera frame (\\f$_{}^{c}\\textrm{T}_t\\f$).\n.   This is a vector (`vector<Mat>`) that contains the rotation matrices for all the transformations\n.   from calibration target frame to camera frame.\n.   @param[in] t_target2cam Rotation part extracted from the homogeneous matrix that transforms a point\n.   expressed in the target frame to the camera frame (\\f$_{}^{c}\\textrm{T}_t\\f$).\n.   This is a vector (`vector<Mat>`) that contains the translation vectors for all the transformations\n.   from calibration target frame to camera frame.\n.   @param[out] R_cam2gripper Estimated rotation part extracted from the homogeneous matrix that transforms a point\n.   expressed in the camera frame to the gripper frame (\\f$_{}^{g}\\textrm{T}_c\\f$).\n.   @param[out] t_cam2gripper Estimated translation part extracted from the homogeneous matrix that transforms a point\n.   expressed in the camera frame to the gripper frame (\\f$_{}^{g}\\textrm{T}_c\\f$).\n.   @param[in] method One of the implemented Hand-Eye calibration method, see cv::HandEyeCalibrationMethod\n.   \n.   The function performs the Hand-Eye calibration using various methods. One approach consists in estimating the\n.   rotation then the translation (separable solutions) and the following methods are implemented:\n.     - R. Tsai, R. Lenz A New Technique for Fully Autonomous and Efficient 3D Robotics Hand/EyeCalibration \\cite Tsai89\n.     - F. Park, B. Martin Robot Sensor Calibration: Solving AX = XB on the Euclidean Group \\cite Park94\n.     - R. Horaud, F. Dornaika Hand-Eye Calibration \\cite Horaud95\n.   \n.   Another approach consists in estimating simultaneously the rotation and the translation (simultaneous solutions),\n.   with the following implemented method:\n.     - N. Andreff, R. Horaud, B. Espiau On-line Hand-Eye Calibration \\cite Andreff99\n.     - K. Daniilidis Hand-Eye Calibration Using Dual Quaternions \\cite Daniilidis98\n.   \n.   The following picture describes the Hand-Eye calibration problem where the transformation between a camera ("eye")\n.   mounted on a robot gripper ("hand") has to be estimated.\n.   \n.   ![](pics/hand-eye_figure.png)\n.   \n.   The calibration procedure is the following:\n.     - a static calibration pattern is used to estimate the transformation between the target frame\n.     and the camera frame\n.     - the robot gripper is moved in order to acquire several poses\n.     - for each pose, the homogeneous transformation between the gripper frame and the robot base frame is recorded using for\n.     instance the robot kinematics\n.   \\f[\n.       \\begin{bmatrix}\n.       X_b\\\\\n.       Y_b\\\\\n.       Z_b\\\\\n.       1\n.       \\end{bmatrix}\n.       =\n.       \\begin{bmatrix}\n.       _{}^{b}\\textrm{R}_g & _{}^{b}\\textrm{t}_g \\\\\n.       0_{1 \\times 3} & 1\n.       \\end{bmatrix}\n.       \\begin{bmatrix}\n.       X_g\\\\\n.       Y_g\\\\\n.       Z_g\\\\\n.       1\n.       \\end{bmatrix}\n.   \\f]\n.     - for each pose, the homogeneous transformation between the calibration target frame and the camera frame is recorded using\n.     for instance a pose estimation method (PnP) from 2D-3D point correspondences\n.   \\f[\n.       \\begin{bmatrix}\n.       X_c\\\\\n.       Y_c\\\\\n.       Z_c\\\\\n.       1\n.       \\end{bmatrix}\n.       =\n.       \\begin{bmatrix}\n.       _{}^{c}\\textrm{R}_t & _{}^{c}\\textrm{t}_t \\\\\n.       0_{1 \\times 3} & 1\n.       \\end{bmatrix}\n.       \\begin{bmatrix}\n.       X_t\\\\\n.       Y_t\\\\\n.       Z_t\\\\\n.       1\n.       \\end{bmatrix}\n.   \\f]\n.   \n.   The Hand-Eye calibration procedure returns the following homogeneous transformation\n.   \\f[\n.       \\begin{bmatrix}\n.       X_g\\\\\n.       Y_g\\\\\n.       Z_g\\\\\n.       1\n.       \\end{bmatrix}\n.       =\n.       \\begin{bmatrix}\n.       _{}^{g}\\textrm{R}_c & _{}^{g}\\textrm{t}_c \\\\\n.       0_{1 \\times 3} & 1\n.       \\end{bmatrix}\n.       \\begin{bmatrix}\n.       X_c\\\\\n.       Y_c\\\\\n.       Z_c\\\\\n.       1\n.       \\end{bmatrix}\n.   \\f]\n.   \n.   This problem is also known as solving the \\f$\\mathbf{A}\\mathbf{X}=\\mathbf{X}\\mathbf{B}\\f$ equation:\n.   \\f[\n.       \\begin{align*}\n.       ^{b}{\\textrm{T}_g}^{(1)} \\hspace{0.2em} ^{g}\\textrm{T}_c \\hspace{0.2em} ^{c}{\\textrm{T}_t}^{(1)} &=\n.       \\hspace{0.1em} ^{b}{\\textrm{T}_g}^{(2)} \\hspace{0.2em} ^{g}\\textrm{T}_c \\hspace{0.2em} ^{c}{\\textrm{T}_t}^{(2)} \\\\\n.   \n.       (^{b}{\\textrm{T}_g}^{(2)})^{-1} \\hspace{0.2em} ^{b}{\\textrm{T}_g}^{(1)} \\hspace{0.2em} ^{g}\\textrm{T}_c &=\n.       \\hspace{0.1em} ^{g}\\textrm{T}_c \\hspace{0.2em} ^{c}{\\textrm{T}_t}^{(2)} (^{c}{\\textrm{T}_t}^{(1)})^{-1} \\\\\n.   \n.       \\textrm{A}_i \\textrm{X} &= \\textrm{X} \\textrm{B}_i \\\\\n.       \\end{align*}\n.   \\f]\n.   \n.   \\note\n.   Additional information can be found on this [website](http://campar.in.tum.de/Chair/HandEyeCalibration).\n.   \\note\n.   A minimum of 2 motions with non parallel rotation axes are necessary to determine the hand-eye transformation.\n.   So at least 3 different poses are required, but it is strongly recommended to use many more poses.'
    ...

def calibrationMatrixValues(cameraMatrix, imageSize, apertureWidth, apertureHeight) -> typing.Any:
    "calibrationMatrixValues(cameraMatrix, imageSize, apertureWidth, apertureHeight) -> fovx, fovy, focalLength, principalPoint, aspectRatio\n.   @brief Computes useful camera characteristics from the camera matrix.\n.   \n.   @param cameraMatrix Input camera matrix that can be estimated by calibrateCamera or\n.   stereoCalibrate .\n.   @param imageSize Input image size in pixels.\n.   @param apertureWidth Physical width in mm of the sensor.\n.   @param apertureHeight Physical height in mm of the sensor.\n.   @param fovx Output field of view in degrees along the horizontal sensor axis.\n.   @param fovy Output field of view in degrees along the vertical sensor axis.\n.   @param focalLength Focal length of the lens in mm.\n.   @param principalPoint Principal point in mm.\n.   @param aspectRatio \\f$f_y/f_x\\f$\n.   \n.   The function computes various useful camera characteristics from the previously estimated camera\n.   matrix.\n.   \n.   @note\n.      Do keep in mind that the unity measure 'mm' stands for whatever unit of measure one chooses for\n.       the chessboard pitch (it can thus be any value)."
    ...

def cartToPolar(x, y, magnitude=..., angle=..., angleInDegrees=...) -> typing.Any:
    'cartToPolar(x, y[, magnitude[, angle[, angleInDegrees]]]) -> magnitude, angle\n.   @brief Calculates the magnitude and angle of 2D vectors.\n.   \n.   The function cv::cartToPolar calculates either the magnitude, angle, or both\n.   for every 2D vector (x(I),y(I)):\n.   \\f[\\begin{array}{l} \\texttt{magnitude} (I)= \\sqrt{\\texttt{x}(I)^2+\\texttt{y}(I)^2} , \\\\ \\texttt{angle} (I)= \\texttt{atan2} ( \\texttt{y} (I), \\texttt{x} (I))[ \\cdot180 / \\pi ] \\end{array}\\f]\n.   \n.   The angles are calculated with accuracy about 0.3 degrees. For the point\n.   (0,0), the angle is set to 0.\n.   @param x array of x-coordinates; this must be a single-precision or\n.   double-precision floating-point array.\n.   @param y array of y-coordinates, that must have the same size and same type as x.\n.   @param magnitude output array of magnitudes of the same size and type as x.\n.   @param angle output array of angles that has the same size and type as\n.   x; the angles are measured in radians (from 0 to 2\\*Pi) or in degrees (0 to 360 degrees).\n.   @param angleInDegrees a flag, indicating whether the angles are measured\n.   in radians (which is by default), or in degrees.\n.   @sa Sobel, Scharr'
    ...

def checkChessboard(img: Mat, size) -> typing.Any:
    'checkChessboard(img, size) -> retval\n.'
    ...

def checkHardwareSupport(feature) -> typing.Any:
    'checkHardwareSupport(feature) -> retval\n.   @brief Returns true if the specified feature is supported by the host hardware.\n.   \n.   The function returns true if the host hardware supports the specified feature. When user calls\n.   setUseOptimized(false), the subsequent calls to checkHardwareSupport() will return false until\n.   setUseOptimized(true) is called. This way user can dynamically switch on and off the optimized code\n.   in OpenCV.\n.   @param feature The feature of interest, one of cv::CpuFeatures'
    ...

def checkRange(a, quiet=..., minVal=..., maxVal=...) -> typing.Any:
    'checkRange(a[, quiet[, minVal[, maxVal]]]) -> retval, pos\n.   @brief Checks every element of an input array for invalid values.\n.   \n.   The function cv::checkRange checks that every array element is neither NaN nor infinite. When minVal \\>\n.   -DBL_MAX and maxVal \\< DBL_MAX, the function also checks that each value is between minVal and\n.   maxVal. In case of multi-channel arrays, each channel is processed independently. If some values\n.   are out of range, position of the first outlier is stored in pos (when pos != NULL). Then, the\n.   function either returns false (when quiet=true) or throws an exception.\n.   @param a input array.\n.   @param quiet a flag, indicating whether the functions quietly return false when the array elements\n.   are out of range or they throw an exception.\n.   @param pos optional output parameter, when not NULL, must be a pointer to array of src.dims\n.   elements.\n.   @param minVal inclusive lower boundary of valid values range.\n.   @param maxVal exclusive upper boundary of valid values range.'
    ...

def circle(img: Mat, center, radius, color, thickness=..., lineType=..., shift=...) -> typing.Any:
    'circle(img, center, radius, color[, thickness[, lineType[, shift]]]) -> img\n.   @brief Draws a circle.\n.   \n.   The function cv::circle draws a simple or filled circle with a given center and radius.\n.   @param img Image where the circle is drawn.\n.   @param center Center of the circle.\n.   @param radius Radius of the circle.\n.   @param color Circle color.\n.   @param thickness Thickness of the circle outline, if positive. Negative values, like #FILLED,\n.   mean that a filled circle is to be drawn.\n.   @param lineType Type of the circle boundary. See #LineTypes\n.   @param shift Number of fractional bits in the coordinates of the center and in the radius value.'
    ...

def clipLine(imgRect, pt1, pt2) -> typing.Any:
    'clipLine(imgRect, pt1, pt2) -> retval, pt1, pt2\n.   @overload\n.   @param imgRect Image rectangle.\n.   @param pt1 First line point.\n.   @param pt2 Second line point.'
    ...

def colorChange(src: Mat, mask: Mat, dts: Mat = ..., red_mul=..., green_mul=..., blue_mul=...) -> typing.Any:
    'colorChange(src, mask[, dst[, red_mul[, green_mul[, blue_mul]]]]) -> dst\n.   @brief Given an original color image, two differently colored versions of this image can be mixed\n.   seamlessly.\n.   \n.   @param src Input 8-bit 3-channel image.\n.   @param mask Input 8-bit 1 or 3-channel image.\n.   @param dst Output image with the same size and type as src .\n.   @param red_mul R-channel multiply factor.\n.   @param green_mul G-channel multiply factor.\n.   @param blue_mul B-channel multiply factor.\n.   \n.   Multiplication factor is between .5 to 2.5.'
    ...

def compare(src1: Mat, src2: Mat, cmpop, dts: Mat = ...) -> typing.Any:
    'compare(src1, src2, cmpop[, dst]) -> dst\n.   @brief Performs the per-element comparison of two arrays or an array and scalar value.\n.   \n.   The function compares:\n.   *   Elements of two arrays when src1 and src2 have the same size:\n.       \\f[\\texttt{dst} (I) =  \\texttt{src1} (I)  \\,\\texttt{cmpop}\\, \\texttt{src2} (I)\\f]\n.   *   Elements of src1 with a scalar src2 when src2 is constructed from\n.       Scalar or has a single element:\n.       \\f[\\texttt{dst} (I) =  \\texttt{src1}(I) \\,\\texttt{cmpop}\\,  \\texttt{src2}\\f]\n.   *   src1 with elements of src2 when src1 is constructed from Scalar or\n.       has a single element:\n.       \\f[\\texttt{dst} (I) =  \\texttt{src1}  \\,\\texttt{cmpop}\\, \\texttt{src2} (I)\\f]\n.   When the comparison result is true, the corresponding element of output\n.   array is set to 255. The comparison operations can be replaced with the\n.   equivalent matrix expressions:\n.   @code{.cpp}\n.       Mat dst1 = src1 >= src2;\n.       Mat dst2 = src1 < 8;\n.       ...\n.   @endcode\n.   @param src1 first input array or a scalar; when it is an array, it must have a single channel.\n.   @param src2 second input array or a scalar; when it is an array, it must have a single channel.\n.   @param dst output array of type ref CV_8U that has the same size and the same number of channels as\n.       the input arrays.\n.   @param cmpop a flag, that specifies correspondence between the arrays (cv::CmpTypes)\n.   @sa checkRange, min, max, threshold'
    ...

def compareHist(H1: Mat, H2: Mat, method: int) -> float:
    'compareHist(H1, H2, method) -> retval\n.   @brief Compares two histograms.\n.   \n.   The function cv::compareHist compares two dense or two sparse histograms using the specified method.\n.   \n.   The function returns \\f$d(H_1, H_2)\\f$ .\n.   \n.   While the function works well with 1-, 2-, 3-dimensional dense histograms, it may not be suitable\n.   for high-dimensional sparse histograms. In such histograms, because of aliasing and sampling\n.   problems, the coordinates of non-zero histogram bins can slightly shift. To compare such histograms\n.   or more general sparse configurations of weighted points, consider using the #EMD function.\n.   \n.   @param H1 First compared histogram.\n.   @param H2 Second compared histogram of the same size as H1 .\n.   @param method Comparison method, see #HistCompMethods'
    ...

def completeSymm(m, lowerToUpper=...) -> typing.Any:
    'completeSymm(m[, lowerToUpper]) -> m\n.   @brief Copies the lower or the upper half of a square matrix to its another half.\n.   \n.   The function cv::completeSymm copies the lower or the upper half of a square matrix to\n.   its another half. The matrix diagonal remains unchanged:\n.    - \\f$\\texttt{m}_{ij}=\\texttt{m}_{ji}\\f$ for \\f$i > j\\f$ if\n.       lowerToUpper=false\n.    - \\f$\\texttt{m}_{ij}=\\texttt{m}_{ji}\\f$ for \\f$i < j\\f$ if\n.       lowerToUpper=true\n.   \n.   @param m input-output floating-point square matrix.\n.   @param lowerToUpper operation flag; if true, the lower half is copied to\n.   the upper half. Otherwise, the upper half is copied to the lower half.\n.   @sa flip, transpose'
    ...

def composeRT(rvec1, tvec1, rvec2, tvec2, rvec3=..., tvec3=..., dr3dr1=..., dr3dt1=..., dr3dr2=..., dr3dt2=..., dt3dr1=..., dt3dt1=..., dt3dr2=..., dt3dt2=...) -> typing.Any:
    'composeRT(rvec1, tvec1, rvec2, tvec2[, rvec3[, tvec3[, dr3dr1[, dr3dt1[, dr3dr2[, dr3dt2[, dt3dr1[, dt3dt1[, dt3dr2[, dt3dt2]]]]]]]]]]) -> rvec3, tvec3, dr3dr1, dr3dt1, dr3dr2, dr3dt2, dt3dr1, dt3dt1, dt3dr2, dt3dt2\n.   @brief Combines two rotation-and-shift transformations.\n.   \n.   @param rvec1 First rotation vector.\n.   @param tvec1 First translation vector.\n.   @param rvec2 Second rotation vector.\n.   @param tvec2 Second translation vector.\n.   @param rvec3 Output rotation vector of the superposition.\n.   @param tvec3 Output translation vector of the superposition.\n.   @param dr3dr1 Optional output derivative of rvec3 with regard to rvec1\n.   @param dr3dt1 Optional output derivative of rvec3 with regard to tvec1\n.   @param dr3dr2 Optional output derivative of rvec3 with regard to rvec2\n.   @param dr3dt2 Optional output derivative of rvec3 with regard to tvec2\n.   @param dt3dr1 Optional output derivative of tvec3 with regard to rvec1\n.   @param dt3dt1 Optional output derivative of tvec3 with regard to tvec1\n.   @param dt3dr2 Optional output derivative of tvec3 with regard to rvec2\n.   @param dt3dt2 Optional output derivative of tvec3 with regard to tvec2\n.   \n.   The functions compute:\n.   \n.   \\f[\\begin{array}{l} \\texttt{rvec3} =  \\mathrm{rodrigues} ^{-1} \\left ( \\mathrm{rodrigues} ( \\texttt{rvec2} )  \\cdot \\mathrm{rodrigues} ( \\texttt{rvec1} ) \\right )  \\\\ \\texttt{tvec3} =  \\mathrm{rodrigues} ( \\texttt{rvec2} )  \\cdot \\texttt{tvec1} +  \\texttt{tvec2} \\end{array} ,\\f]\n.   \n.   where \\f$\\mathrm{rodrigues}\\f$ denotes a rotation vector to a rotation matrix transformation, and\n.   \\f$\\mathrm{rodrigues}^{-1}\\f$ denotes the inverse transformation. See Rodrigues for details.\n.   \n.   Also, the functions can compute the derivatives of the output vectors with regards to the input\n.   vectors (see matMulDeriv ). The functions are used inside stereoCalibrate but can also be used in\n.   your own code where Levenberg-Marquardt or another gradient-based solver is used to optimize a\n.   function that contains a matrix multiplication.'
    ...

def computeCorrespondEpilines(points, whichImage, F, lines=...) -> typing.Any:
    'computeCorrespondEpilines(points, whichImage, F[, lines]) -> lines\n.   @brief For points in an image of a stereo pair, computes the corresponding epilines in the other image.\n.   \n.   @param points Input points. \\f$N \\times 1\\f$ or \\f$1 \\times N\\f$ matrix of type CV_32FC2 or\n.   vector\\<Point2f\\> .\n.   @param whichImage Index of the image (1 or 2) that contains the points .\n.   @param F Fundamental matrix that can be estimated using findFundamentalMat or stereoRectify .\n.   @param lines Output vector of the epipolar lines corresponding to the points in the other image.\n.   Each line \\f$ax + by + c=0\\f$ is encoded by 3 numbers \\f$(a, b, c)\\f$ .\n.   \n.   For every point in one of the two images of a stereo pair, the function finds the equation of the\n.   corresponding epipolar line in the other image.\n.   \n.   From the fundamental matrix definition (see findFundamentalMat ), line \\f$l^{(2)}_i\\f$ in the second\n.   image for the point \\f$p^{(1)}_i\\f$ in the first image (when whichImage=1 ) is computed as:\n.   \n.   \\f[l^{(2)}_i = F p^{(1)}_i\\f]\n.   \n.   And vice versa, when whichImage=2, \\f$l^{(1)}_i\\f$ is computed from \\f$p^{(2)}_i\\f$ as:\n.   \n.   \\f[l^{(1)}_i = F^T p^{(2)}_i\\f]\n.   \n.   Line coefficients are defined up to a scale. They are normalized so that \\f$a_i^2+b_i^2=1\\f$ .'
    ...

def computeECC(templateImage, inputImage, inputMask=...) -> typing.Any:
    'computeECC(templateImage, inputImage[, inputMask]) -> retval\n.   @brief Computes the Enhanced Correlation Coefficient value between two images @cite EP08 .\n.   \n.   @param templateImage single-channel template image; CV_8U or CV_32F array.\n.   @param inputImage single-channel input image to be warped to provide an image similar to\n.    templateImage, same type as templateImage.\n.   @param inputMask An optional mask to indicate valid values of inputImage.\n.   \n.   @sa\n.   findTransformECC'
    ...

def connectedComponents(image: Mat, labels=..., connectivity=..., ltype=...) -> typing.Any:
    'connectedComponents(image[, labels[, connectivity[, ltype]]]) -> retval, labels\n.   @overload\n.   \n.   @param image the 8-bit single-channel image to be labeled\n.   @param labels destination labeled image\n.   @param connectivity 8 or 4 for 8-way or 4-way connectivity respectively\n.   @param ltype output image label type. Currently CV_32S and CV_16U are supported.'
    ...

def connectedComponentsWithAlgorithm(image: Mat, connectivity, ltype, ccltype, labels=...) -> typing.Any:
    "connectedComponentsWithAlgorithm(image, connectivity, ltype, ccltype[, labels]) -> retval, labels\n.   @brief computes the connected components labeled image of boolean image\n.   \n.   image with 4 or 8 way connectivity - returns N, the total number of labels [0, N-1] where 0\n.   represents the background label. ltype specifies the output label image type, an important\n.   consideration based on the total number of labels or alternatively the total number of pixels in\n.   the source image. ccltype specifies the connected components labeling algorithm to use, currently\n.   Grana (BBDT) and Wu's (SAUF) algorithms are supported, see the #ConnectedComponentsAlgorithmsTypes\n.   for details. Note that SAUF algorithm forces a row major ordering of labels while BBDT does not.\n.   This function uses parallel version of both Grana and Wu's algorithms if at least one allowed\n.   parallel framework is enabled and if the rows of the image are at least twice the number returned by #getNumberOfCPUs.\n.   \n.   @param image the 8-bit single-channel image to be labeled\n.   @param labels destination labeled image\n.   @param connectivity 8 or 4 for 8-way or 4-way connectivity respectively\n.   @param ltype output image label type. Currently CV_32S and CV_16U are supported.\n.   @param ccltype connected components algorithm type (see the #ConnectedComponentsAlgorithmsTypes)."
    ...

def connectedComponentsWithStats(image: Mat, labels=..., stats=..., centroids=..., connectivity=..., ltype=...) -> typing.Any:
    'connectedComponentsWithStats(image[, labels[, stats[, centroids[, connectivity[, ltype]]]]]) -> retval, labels, stats, centroids\n.   @overload\n.   @param image the 8-bit single-channel image to be labeled\n.   @param labels destination labeled image\n.   @param stats statistics output for each label, including the background label.\n.   Statistics are accessed via stats(label, COLUMN) where COLUMN is one of\n.   #ConnectedComponentsTypes, selecting the statistic. The data type is CV_32S.\n.   @param centroids centroid output for each label, including the background label. Centroids are\n.   accessed via centroids(label, 0) for x and centroids(label, 1) for y. The data type CV_64F.\n.   @param connectivity 8 or 4 for 8-way or 4-way connectivity respectively\n.   @param ltype output image label type. Currently CV_32S and CV_16U are supported.'
    ...

def connectedComponentsWithStatsWithAlgorithm(image: Mat, connectivity, ltype, ccltype, labels=..., stats=..., centroids=...) -> typing.Any:
    "connectedComponentsWithStatsWithAlgorithm(image, connectivity, ltype, ccltype[, labels[, stats[, centroids]]]) -> retval, labels, stats, centroids\n.   @brief computes the connected components labeled image of boolean image and also produces a statistics output for each label\n.   \n.   image with 4 or 8 way connectivity - returns N, the total number of labels [0, N-1] where 0\n.   represents the background label. ltype specifies the output label image type, an important\n.   consideration based on the total number of labels or alternatively the total number of pixels in\n.   the source image. ccltype specifies the connected components labeling algorithm to use, currently\n.   Grana's (BBDT) and Wu's (SAUF) algorithms are supported, see the #ConnectedComponentsAlgorithmsTypes\n.   for details. Note that SAUF algorithm forces a row major ordering of labels while BBDT does not.\n.   This function uses parallel version of both Grana and Wu's algorithms (statistics included) if at least one allowed\n.   parallel framework is enabled and if the rows of the image are at least twice the number returned by #getNumberOfCPUs.\n.   \n.   @param image the 8-bit single-channel image to be labeled\n.   @param labels destination labeled image\n.   @param stats statistics output for each label, including the background label.\n.   Statistics are accessed via stats(label, COLUMN) where COLUMN is one of\n.   #ConnectedComponentsTypes, selecting the statistic. The data type is CV_32S.\n.   @param centroids centroid output for each label, including the background label. Centroids are\n.   accessed via centroids(label, 0) for x and centroids(label, 1) for y. The data type CV_64F.\n.   @param connectivity 8 or 4 for 8-way or 4-way connectivity respectively\n.   @param ltype output image label type. Currently CV_32S and CV_16U are supported.\n.   @param ccltype connected components algorithm type (see #ConnectedComponentsAlgorithmsTypes)."
    ...

def contourArea(contour, oriented=...) -> typing.Any:
    'contourArea(contour[, oriented]) -> retval\n.   @brief Calculates a contour area.\n.   \n.   The function computes a contour area. Similarly to moments , the area is computed using the Green\n.   formula. Thus, the returned area and the number of non-zero pixels, if you draw the contour using\n.   #drawContours or #fillPoly , can be different. Also, the function will most certainly give a wrong\n.   results for contours with self-intersections.\n.   \n.   Example:\n.   @code\n.       vector<Point> contour;\n.       contour.push_back(Point2f(0, 0));\n.       contour.push_back(Point2f(10, 0));\n.       contour.push_back(Point2f(10, 10));\n.       contour.push_back(Point2f(5, 4));\n.   \n.       double area0 = contourArea(contour);\n.       vector<Point> approx;\n.       approxPolyDP(contour, approx, 5, true);\n.       double area1 = contourArea(approx);\n.   \n.       cout << "area0 =" << area0 << endl <<\n.               "area1 =" << area1 << endl <<\n.               "approx poly vertices" << approx.size() << endl;\n.   @endcode\n.   @param contour Input vector of 2D points (contour vertices), stored in std::vector or Mat.\n.   @param oriented Oriented area flag. If it is true, the function returns a signed area value,\n.   depending on the contour orientation (clockwise or counter-clockwise). Using this feature you can\n.   determine orientation of a contour by taking the sign of an area. By default, the parameter is\n.   false, which means that the absolute value is returned.'
    ...

def convertFp16(src: Mat, dts: Mat = ...) -> typing.Any:
    'convertFp16(src[, dst]) -> dst\n.   @brief Converts an array to half precision floating number.\n.   \n.   This function converts FP32 (single precision floating point) from/to FP16 (half precision floating point). CV_16S format is used to represent FP16 data.\n.   There are two use modes (src -> dst): CV_32F -> CV_16S and CV_16S -> CV_32F. The input array has to have type of CV_32F or\n.   CV_16S to represent the bit depth. If the input array is neither of them, the function will raise an error.\n.   The format of half precision floating point is defined in IEEE 754-2008.\n.   \n.   @param src input array.\n.   @param dst output array.'
    ...

def convertMaps(map1, map2, dstmap1type, dstmap1=..., dstmap2=..., nninterpolation=...) -> typing.Any:
    'convertMaps(map1, map2, dstmap1type[, dstmap1[, dstmap2[, nninterpolation]]]) -> dstmap1, dstmap2\n.   @brief Converts image transformation maps from one representation to another.\n.   \n.   The function converts a pair of maps for remap from one representation to another. The following\n.   options ( (map1.type(), map2.type()) \\f$\\rightarrow\\f$ (dstmap1.type(), dstmap2.type()) ) are\n.   supported:\n.   \n.   - \\f$\\texttt{(CV_32FC1, CV_32FC1)} \\rightarrow \\texttt{(CV_16SC2, CV_16UC1)}\\f$. This is the\n.   most frequently used conversion operation, in which the original floating-point maps (see remap )\n.   are converted to a more compact and much faster fixed-point representation. The first output array\n.   contains the rounded coordinates and the second array (created only when nninterpolation=false )\n.   contains indices in the interpolation tables.\n.   \n.   - \\f$\\texttt{(CV_32FC2)} \\rightarrow \\texttt{(CV_16SC2, CV_16UC1)}\\f$. The same as above but\n.   the original maps are stored in one 2-channel matrix.\n.   \n.   - Reverse conversion. Obviously, the reconstructed floating-point maps will not be exactly the same\n.   as the originals.\n.   \n.   @param map1 The first input map of type CV_16SC2, CV_32FC1, or CV_32FC2 .\n.   @param map2 The second input map of type CV_16UC1, CV_32FC1, or none (empty matrix),\n.   respectively.\n.   @param dstmap1 The first output map that has the type dstmap1type and the same size as src .\n.   @param dstmap2 The second output map.\n.   @param dstmap1type Type of the first output map that should be CV_16SC2, CV_32FC1, or\n.   CV_32FC2 .\n.   @param nninterpolation Flag indicating whether the fixed-point maps are used for the\n.   nearest-neighbor or for a more complex interpolation.\n.   \n.   @sa  remap, undistort, initUndistortRectifyMap'
    ...

def convertPointsFromHomogeneous(src: Mat, dts: Mat = ...) -> typing.Any:
    'convertPointsFromHomogeneous(src[, dst]) -> dst\n.   @brief Converts points from homogeneous to Euclidean space.\n.   \n.   @param src Input vector of N-dimensional points.\n.   @param dst Output vector of N-1-dimensional points.\n.   \n.   The function converts points homogeneous to Euclidean space using perspective projection. That is,\n.   each point (x1, x2, ... x(n-1), xn) is converted to (x1/xn, x2/xn, ..., x(n-1)/xn). When xn=0, the\n.   output point coordinates will be (0,0,0,...).'
    ...

def convertPointsToHomogeneous(src: Mat, dts: Mat = ...) -> typing.Any:
    "convertPointsToHomogeneous(src[, dst]) -> dst\n.   @brief Converts points from Euclidean to homogeneous space.\n.   \n.   @param src Input vector of N-dimensional points.\n.   @param dst Output vector of N+1-dimensional points.\n.   \n.   The function converts points from Euclidean to homogeneous space by appending 1's to the tuple of\n.   point coordinates. That is, each point (x1, x2, ..., xn) is converted to (x1, x2, ..., xn, 1)."
    ...

def convertScaleAbs(src: Mat, dts: Mat = ..., alpha=..., beta=...) -> typing.Any:
    'convertScaleAbs(src[, dst[, alpha[, beta]]]) -> dst\n.   @brief Scales, calculates absolute values, and converts the result to 8-bit.\n.   \n.   On each element of the input array, the function convertScaleAbs\n.   performs three operations sequentially: scaling, taking an absolute\n.   value, conversion to an unsigned 8-bit type:\n.   \\f[\\texttt{dst} (I)= \\texttt{saturate\\_cast<uchar>} (| \\texttt{src} (I)* \\texttt{alpha} +  \\texttt{beta} |)\\f]\n.   In case of multi-channel arrays, the function processes each channel\n.   independently. When the output is not 8-bit, the operation can be\n.   emulated by calling the Mat::convertTo method (or by using matrix\n.   expressions) and then by calculating an absolute value of the result.\n.   For example:\n.   @code{.cpp}\n.       Mat_<float> A(30,30);\n.       randu(A, Scalar(-100), Scalar(100));\n.       Mat_<float> B = A*5 + 3;\n.       B = abs(B);\n.       // Mat_<float> B = abs(A*5+3) will also do the job,\n.       // but it will allocate a temporary matrix\n.   @endcode\n.   @param src input array.\n.   @param dst output array.\n.   @param alpha optional scale factor.\n.   @param beta optional delta added to the scaled values.\n.   @sa  Mat::convertTo, cv::abs(const Mat&)'
    ...

def convexHull(points, hull=..., clockwise=..., returnPoints=...) -> typing.Any:
    'convexHull(points[, hull[, clockwise[, returnPoints]]]) -> hull\n.   @brief Finds the convex hull of a point set.\n.   \n.   The function cv::convexHull finds the convex hull of a 2D point set using the Sklansky\'s algorithm @cite Sklansky82\n.   that has *O(N logN)* complexity in the current implementation.\n.   \n.   @param points Input 2D point set, stored in std::vector or Mat.\n.   @param hull Output convex hull. It is either an integer vector of indices or vector of points. In\n.   the first case, the hull elements are 0-based indices of the convex hull points in the original\n.   array (since the set of convex hull points is a subset of the original point set). In the second\n.   case, hull elements are the convex hull points themselves.\n.   @param clockwise Orientation flag. If it is true, the output convex hull is oriented clockwise.\n.   Otherwise, it is oriented counter-clockwise. The assumed coordinate system has its X axis pointing\n.   to the right, and its Y axis pointing upwards.\n.   @param returnPoints Operation flag. In case of a matrix, when the flag is true, the function\n.   returns convex hull points. Otherwise, it returns indices of the convex hull points. When the\n.   output array is std::vector, the flag is ignored, and the output depends on the type of the\n.   vector: std::vector\\<int\\> implies returnPoints=false, std::vector\\<Point\\> implies\n.   returnPoints=true.\n.   \n.   @note `points` and `hull` should be different arrays, inplace processing isn\'t supported.\n.   \n.   Check @ref tutorial_hull "the corresponding tutorial" for more details.\n.   \n.   useful links:\n.   \n.   https://www.learnopencv.com/convex-hull-using-opencv-in-python-and-c/'
    ...

def convexityDefects(contour, convexhull, convexityDefects=...) -> typing.Any:
    'convexityDefects(contour, convexhull[, convexityDefects]) -> convexityDefects\n.   @brief Finds the convexity defects of a contour.\n.   \n.   The figure below displays convexity defects of a hand contour:\n.   \n.   ![image](pics/defects.png)\n.   \n.   @param contour Input contour.\n.   @param convexhull Convex hull obtained using convexHull that should contain indices of the contour\n.   points that make the hull.\n.   @param convexityDefects The output vector of convexity defects. In C++ and the new Python/Java\n.   interface each convexity defect is represented as 4-element integer vector (a.k.a. #Vec4i):\n.   (start_index, end_index, farthest_pt_index, fixpt_depth), where indices are 0-based indices\n.   in the original contour of the convexity defect beginning, end and the farthest point, and\n.   fixpt_depth is fixed-point approximation (with 8 fractional bits) of the distance between the\n.   farthest contour point and the hull. That is, to get the floating-point value of the depth will be\n.   fixpt_depth/256.0.'
    ...

def copyMakeBorder(src: Mat, top, bottom, left, right, borderType, dts: Mat = ..., value=...) -> typing.Any:
    'copyMakeBorder(src, top, bottom, left, right, borderType[, dst[, value]]) -> dst\n.   @brief Forms a border around an image.\n.   \n.   The function copies the source image into the middle of the destination image. The areas to the\n.   left, to the right, above and below the copied source image will be filled with extrapolated\n.   pixels. This is not what filtering functions based on it do (they extrapolate pixels on-fly), but\n.   what other more complex functions, including your own, may do to simplify image boundary handling.\n.   \n.   The function supports the mode when src is already in the middle of dst . In this case, the\n.   function does not copy src itself but simply constructs the border, for example:\n.   \n.   @code{.cpp}\n.       // let border be the same in all directions\n.       int border=2;\n.       // constructs a larger image to fit both the image and the border\n.       Mat gray_buf(rgb.rows + border*2, rgb.cols + border*2, rgb.depth());\n.       // select the middle part of it w/o copying data\n.       Mat gray(gray_canvas, Rect(border, border, rgb.cols, rgb.rows));\n.       // convert image from RGB to grayscale\n.       cvtColor(rgb, gray, COLOR_RGB2GRAY);\n.       // form a border in-place\n.       copyMakeBorder(gray, gray_buf, border, border,\n.                      border, border, BORDER_REPLICATE);\n.       // now do some custom filtering ...\n.       ...\n.   @endcode\n.   @note When the source image is a part (ROI) of a bigger image, the function will try to use the\n.   pixels outside of the ROI to form a border. To disable this feature and always do extrapolation, as\n.   if src was not a ROI, use borderType | #BORDER_ISOLATED.\n.   \n.   @param src Source image.\n.   @param dst Destination image of the same type as src and the size Size(src.cols+left+right,\n.   src.rows+top+bottom) .\n.   @param top the top pixels\n.   @param bottom the bottom pixels\n.   @param left the left pixels\n.   @param right Parameter specifying how many pixels in each direction from the source image rectangle\n.   to extrapolate. For example, top=1, bottom=1, left=1, right=1 mean that 1 pixel-wide border needs\n.   to be built.\n.   @param borderType Border type. See borderInterpolate for details.\n.   @param value Border value if borderType==BORDER_CONSTANT .\n.   \n.   @sa  borderInterpolate'
    ...

def copyTo(src: Mat, mask: Mat, dts: Mat = ...) -> typing.Any:
    'copyTo(src, mask[, dst]) -> dst\n.   @brief  This is an overloaded member function, provided for convenience (python)\n.   Copies the matrix to another one.\n.   When the operation mask is specified, if the Mat::create call shown above reallocates the matrix, the newly allocated matrix is initialized with all zeros before copying the data.\n.   @param src source matrix.\n.   @param dst Destination matrix. If it does not have a proper size or type before the operation, it is\n.   reallocated.\n.   @param mask Operation mask of the same size as \\*this. Its non-zero elements indicate which matrix\n.   elements need to be copied. The mask has to be of type CV_8U and can have 1 or multiple channels.'
    ...

def cornerEigenValsAndVecs(src: Mat, blockSize, ksize, dts: Mat = ..., borderType=...) -> typing.Any:
    'cornerEigenValsAndVecs(src, blockSize, ksize[, dst[, borderType]]) -> dst\n.   @brief Calculates eigenvalues and eigenvectors of image blocks for corner detection.\n.   \n.   For every pixel \\f$p\\f$ , the function cornerEigenValsAndVecs considers a blockSize \\f$\\times\\f$ blockSize\n.   neighborhood \\f$S(p)\\f$ . It calculates the covariation matrix of derivatives over the neighborhood as:\n.   \n.   \\f[M =  \\begin{bmatrix} \\sum _{S(p)}(dI/dx)^2 &  \\sum _{S(p)}dI/dx dI/dy  \\\\ \\sum _{S(p)}dI/dx dI/dy &  \\sum _{S(p)}(dI/dy)^2 \\end{bmatrix}\\f]\n.   \n.   where the derivatives are computed using the Sobel operator.\n.   \n.   After that, it finds eigenvectors and eigenvalues of \\f$M\\f$ and stores them in the destination image as\n.   \\f$(\\lambda_1, \\lambda_2, x_1, y_1, x_2, y_2)\\f$ where\n.   \n.   -   \\f$\\lambda_1, \\lambda_2\\f$ are the non-sorted eigenvalues of \\f$M\\f$\n.   -   \\f$x_1, y_1\\f$ are the eigenvectors corresponding to \\f$\\lambda_1\\f$\n.   -   \\f$x_2, y_2\\f$ are the eigenvectors corresponding to \\f$\\lambda_2\\f$\n.   \n.   The output of the function can be used for robust edge or corner detection.\n.   \n.   @param src Input single-channel 8-bit or floating-point image.\n.   @param dst Image to store the results. It has the same size as src and the type CV_32FC(6) .\n.   @param blockSize Neighborhood size (see details below).\n.   @param ksize Aperture parameter for the Sobel operator.\n.   @param borderType Pixel extrapolation method. See #BorderTypes. #BORDER_WRAP is not supported.\n.   \n.   @sa  cornerMinEigenVal, cornerHarris, preCornerDetect'
    ...

def cornerHarris(src: Mat, blockSize, ksize, k, dts: Mat = ..., borderType=...) -> typing.Any:
    'cornerHarris(src, blockSize, ksize, k[, dst[, borderType]]) -> dst\n.   @brief Harris corner detector.\n.   \n.   The function runs the Harris corner detector on the image. Similarly to cornerMinEigenVal and\n.   cornerEigenValsAndVecs , for each pixel \\f$(x, y)\\f$ it calculates a \\f$2\\times2\\f$ gradient covariance\n.   matrix \\f$M^{(x,y)}\\f$ over a \\f$\\texttt{blockSize} \\times \\texttt{blockSize}\\f$ neighborhood. Then, it\n.   computes the following characteristic:\n.   \n.   \\f[\\texttt{dst} (x,y) =  \\mathrm{det} M^{(x,y)} - k  \\cdot \\left ( \\mathrm{tr} M^{(x,y)} \\right )^2\\f]\n.   \n.   Corners in the image can be found as the local maxima of this response map.\n.   \n.   @param src Input single-channel 8-bit or floating-point image.\n.   @param dst Image to store the Harris detector responses. It has the type CV_32FC1 and the same\n.   size as src .\n.   @param blockSize Neighborhood size (see the details on #cornerEigenValsAndVecs ).\n.   @param ksize Aperture parameter for the Sobel operator.\n.   @param k Harris detector free parameter. See the formula above.\n.   @param borderType Pixel extrapolation method. See #BorderTypes. #BORDER_WRAP is not supported.'
    ...

def cornerMinEigenVal(src: Mat, blockSize, dts: Mat = ..., ksize=..., borderType=...) -> typing.Any:
    'cornerMinEigenVal(src, blockSize[, dst[, ksize[, borderType]]]) -> dst\n.   @brief Calculates the minimal eigenvalue of gradient matrices for corner detection.\n.   \n.   The function is similar to cornerEigenValsAndVecs but it calculates and stores only the minimal\n.   eigenvalue of the covariance matrix of derivatives, that is, \\f$\\min(\\lambda_1, \\lambda_2)\\f$ in terms\n.   of the formulae in the cornerEigenValsAndVecs description.\n.   \n.   @param src Input single-channel 8-bit or floating-point image.\n.   @param dst Image to store the minimal eigenvalues. It has the type CV_32FC1 and the same size as\n.   src .\n.   @param blockSize Neighborhood size (see the details on #cornerEigenValsAndVecs ).\n.   @param ksize Aperture parameter for the Sobel operator.\n.   @param borderType Pixel extrapolation method. See #BorderTypes. #BORDER_WRAP is not supported.'
    ...

def cornerSubPix(image: Mat, corners, winSize, zeroZone, criteria) -> typing.Any:
    'cornerSubPix(image, corners, winSize, zeroZone, criteria) -> corners\n.   @brief Refines the corner locations.\n.   \n.   The function iterates to find the sub-pixel accurate location of corners or radial saddle points, as\n.   shown on the figure below.\n.   \n.   ![image](pics/cornersubpix.png)\n.   \n.   Sub-pixel accurate corner locator is based on the observation that every vector from the center \\f$q\\f$\n.   to a point \\f$p\\f$ located within a neighborhood of \\f$q\\f$ is orthogonal to the image gradient at \\f$p\\f$\n.   subject to image and measurement noise. Consider the expression:\n.   \n.   \\f[\\epsilon _i = {DI_{p_i}}^T  \\cdot (q - p_i)\\f]\n.   \n.   where \\f${DI_{p_i}}\\f$ is an image gradient at one of the points \\f$p_i\\f$ in a neighborhood of \\f$q\\f$ . The\n.   value of \\f$q\\f$ is to be found so that \\f$\\epsilon_i\\f$ is minimized. A system of equations may be set up\n.   with \\f$\\epsilon_i\\f$ set to zero:\n.   \n.   \\f[\\sum _i(DI_{p_i}  \\cdot {DI_{p_i}}^T) \\cdot q -  \\sum _i(DI_{p_i}  \\cdot {DI_{p_i}}^T  \\cdot p_i)\\f]\n.   \n.   where the gradients are summed within a neighborhood ("search window") of \\f$q\\f$ . Calling the first\n.   gradient term \\f$G\\f$ and the second gradient term \\f$b\\f$ gives:\n.   \n.   \\f[q = G^{-1}  \\cdot b\\f]\n.   \n.   The algorithm sets the center of the neighborhood window at this new center \\f$q\\f$ and then iterates\n.   until the center stays within a set threshold.\n.   \n.   @param image Input single-channel, 8-bit or float image.\n.   @param corners Initial coordinates of the input corners and refined coordinates provided for\n.   output.\n.   @param winSize Half of the side length of the search window. For example, if winSize=Size(5,5) ,\n.   then a \\f$(5*2+1) \\times (5*2+1) = 11 \\times 11\\f$ search window is used.\n.   @param zeroZone Half of the size of the dead region in the middle of the search zone over which\n.   the summation in the formula below is not done. It is used sometimes to avoid possible\n.   singularities of the autocorrelation matrix. The value of (-1,-1) indicates that there is no such\n.   a size.\n.   @param criteria Criteria for termination of the iterative process of corner refinement. That is,\n.   the process of corner position refinement stops either after criteria.maxCount iterations or when\n.   the corner position moves by less than criteria.epsilon on some iteration.'
    ...

def correctMatches(F, points1, points2, newPoints1=..., newPoints2=...) -> typing.Any:
    'correctMatches(F, points1, points2[, newPoints1[, newPoints2]]) -> newPoints1, newPoints2\n.   @brief Refines coordinates of corresponding points.\n.   \n.   @param F 3x3 fundamental matrix.\n.   @param points1 1xN array containing the first set of points.\n.   @param points2 1xN array containing the second set of points.\n.   @param newPoints1 The optimized points1.\n.   @param newPoints2 The optimized points2.\n.   \n.   The function implements the Optimal Triangulation Method (see Multiple View Geometry for details).\n.   For each given point correspondence points1[i] \\<-\\> points2[i], and a fundamental matrix F, it\n.   computes the corrected correspondences newPoints1[i] \\<-\\> newPoints2[i] that minimize the geometric\n.   error \\f$d(points1[i], newPoints1[i])^2 + d(points2[i],newPoints2[i])^2\\f$ (where \\f$d(a,b)\\f$ is the\n.   geometric distance between points \\f$a\\f$ and \\f$b\\f$ ) subject to the epipolar constraint\n.   \\f$newPoints2^T * F * newPoints1 = 0\\f$ .'
    ...

def countNonZero(src) -> typing.Any:
    'countNonZero(src) -> retval\n.   @brief Counts non-zero array elements.\n.   \n.   The function returns the number of non-zero elements in src :\n.   \\f[\\sum _{I: \\; \\texttt{src} (I) \\ne0 } 1\\f]\n.   @param src single-channel array.\n.   @sa  mean, meanStdDev, norm, minMaxLoc, calcCovarMatrix'
    ...

def createAlignMTB(max_bits=..., exclude_range=..., cut=...) -> typing.Any:
    'createAlignMTB([, max_bits[, exclude_range[, cut]]]) -> retval\n.   @brief Creates AlignMTB object\n.   \n.   @param max_bits logarithm to the base 2 of maximal shift in each dimension. Values of 5 and 6 are\n.   usually good enough (31 and 63 pixels shift respectively).\n.   @param exclude_range range for exclusion bitmap that is constructed to suppress noise around the\n.   median value.\n.   @param cut if true cuts images, otherwise fills the new regions with zeros.'
    ...

def createBackgroundSubtractorKNN(history=..., dist2Threshold=..., detectShadows=...) -> typing.Any:
    'createBackgroundSubtractorKNN([, history[, dist2Threshold[, detectShadows]]]) -> retval\n.   @brief Creates KNN Background Subtractor\n.   \n.   @param history Length of the history.\n.   @param dist2Threshold Threshold on the squared distance between the pixel and the sample to decide\n.   whether a pixel is close to that sample. This parameter does not affect the background update.\n.   @param detectShadows If true, the algorithm will detect shadows and mark them. It decreases the\n.   speed a bit, so if you do not need this feature, set the parameter to false.'
    ...

def createBackgroundSubtractorMOG2(history=..., varThreshold=..., detectShadows=...) -> typing.Any:
    'createBackgroundSubtractorMOG2([, history[, varThreshold[, detectShadows]]]) -> retval\n.   @brief Creates MOG2 Background Subtractor\n.   \n.   @param history Length of the history.\n.   @param varThreshold Threshold on the squared Mahalanobis distance between the pixel and the model\n.   to decide whether a pixel is well described by the background model. This parameter does not\n.   affect the background update.\n.   @param detectShadows If true, the algorithm will detect shadows and mark them. It decreases the\n.   speed a bit, so if you do not need this feature, set the parameter to false.'
    ...

def createButton(buttonName, onChange, userData=..., buttonType=..., initialButtonState=...) -> typing.Any:
    'createButton(buttonName, onChange [, userData, buttonType, initialButtonState]) -> None'
    ...

def createCLAHE(clipLimit=..., tileGridSize=...) -> typing.Any:
    'createCLAHE([, clipLimit[, tileGridSize]]) -> retval\n.   @brief Creates a smart pointer to a cv::CLAHE class and initializes it.\n.   \n.   @param clipLimit Threshold for contrast limiting.\n.   @param tileGridSize Size of grid for histogram equalization. Input image will be divided into\n.   equally sized rectangular tiles. tileGridSize defines the number of tiles in row and column.'
    ...

def createCalibrateDebevec(samples=..., lambda_=..., random=...) -> typing.Any:
    'createCalibrateDebevec([, samples[, lambda[, random]]]) -> retval\n.   @brief Creates CalibrateDebevec object\n.   \n.   @param samples number of pixel locations to use\n.   @param lambda smoothness term weight. Greater values produce smoother results, but can alter the\n.   response.\n.   @param random if true sample pixel locations are chosen at random, otherwise they form a\n.   rectangular grid.'
    ...

def createCalibrateRobertson(max_iter=..., threshold=...) -> typing.Any:
    'createCalibrateRobertson([, max_iter[, threshold]]) -> retval\n.   @brief Creates CalibrateRobertson object\n.   \n.   @param max_iter maximal number of Gauss-Seidel solver iterations.\n.   @param threshold target difference between results of two successive steps of the minimization.'
    ...

def createGeneralizedHoughBallard() -> typing.Any:
    'createGeneralizedHoughBallard() -> retval\n.   @brief Creates a smart pointer to a cv::GeneralizedHoughBallard class and initializes it.'
    ...

def createGeneralizedHoughGuil() -> typing.Any:
    'createGeneralizedHoughGuil() -> retval\n.   @brief Creates a smart pointer to a cv::GeneralizedHoughGuil class and initializes it.'
    ...

def createHanningWindow(winSize, type, dts: Mat = ...) -> typing.Any:
    'createHanningWindow(winSize, type[, dst]) -> dst\n.   @brief This function computes a Hanning window coefficients in two dimensions.\n.   \n.   See (http://en.wikipedia.org/wiki/Hann_function) and (http://en.wikipedia.org/wiki/Window_function)\n.   for more information.\n.   \n.   An example is shown below:\n.   @code\n.       // create hanning window of size 100x100 and type CV_32F\n.       Mat hann;\n.       createHanningWindow(hann, Size(100, 100), CV_32F);\n.   @endcode\n.   @param dst Destination array to place Hann coefficients in\n.   @param winSize The window size specifications (both width and height must be > 1)\n.   @param type Created array type'
    ...

def createLineSegmentDetector(_refine=..., _scale=..., _sigma_scale=..., _quant=..., _ang_th=..., _log_eps=..., _density_th=..., _n_bins=...) -> typing.Any:
    'createLineSegmentDetector([, _refine[, _scale[, _sigma_scale[, _quant[, _ang_th[, _log_eps[, _density_th[, _n_bins]]]]]]]]) -> retval\n.   @brief Creates a smart pointer to a LineSegmentDetector object and initializes it.\n.   \n.   The LineSegmentDetector algorithm is defined using the standard values. Only advanced users may want\n.   to edit those, as to tailor it for their own application.\n.   \n.   @param _refine The way found lines will be refined, see #LineSegmentDetectorModes\n.   @param _scale The scale of the image that will be used to find the lines. Range (0..1].\n.   @param _sigma_scale Sigma for Gaussian filter. It is computed as sigma = _sigma_scale/_scale.\n.   @param _quant Bound to the quantization error on the gradient norm.\n.   @param _ang_th Gradient angle tolerance in degrees.\n.   @param _log_eps Detection threshold: -log10(NFA) \\> log_eps. Used only when advance refinement\n.   is chosen.\n.   @param _density_th Minimal density of aligned region points in the enclosing rectangle.\n.   @param _n_bins Number of bins in pseudo-ordering of gradient modulus.\n.   \n.   @note Implementation has been removed due original code license conflict'
    ...

def createMergeDebevec() -> typing.Any:
    'createMergeDebevec() -> retval\n.   @brief Creates MergeDebevec object'
    ...

def createMergeMertens(contrast_weight=..., saturation_weight=..., exposure_weight=...) -> typing.Any:
    'createMergeMertens([, contrast_weight[, saturation_weight[, exposure_weight]]]) -> retval\n.   @brief Creates MergeMertens object\n.   \n.   @param contrast_weight contrast measure weight. See MergeMertens.\n.   @param saturation_weight saturation measure weight\n.   @param exposure_weight well-exposedness measure weight'
    ...

def createMergeRobertson() -> typing.Any:
    'createMergeRobertson() -> retval\n.   @brief Creates MergeRobertson object'
    ...

def createTonemap(gamma=...) -> typing.Any:
    'createTonemap([, gamma]) -> retval\n.   @brief Creates simple linear mapper with gamma correction\n.   \n.   @param gamma positive value for gamma correction. Gamma value of 1.0 implies no correction, gamma\n.   equal to 2.2f is suitable for most displays.\n.   Generally gamma \\> 1 brightens the image and gamma \\< 1 darkens it.'
    ...

def createTonemapDrago(gamma=..., saturation=..., bias=...) -> typing.Any:
    'createTonemapDrago([, gamma[, saturation[, bias]]]) -> retval\n.   @brief Creates TonemapDrago object\n.   \n.   @param gamma gamma value for gamma correction. See createTonemap\n.   @param saturation positive saturation enhancement value. 1.0 preserves saturation, values greater\n.   than 1 increase saturation and values less than 1 decrease it.\n.   @param bias value for bias function in [0, 1] range. Values from 0.7 to 0.9 usually give best\n.   results, default value is 0.85.'
    ...

def createTonemapMantiuk(gamma=..., scale=..., saturation=...) -> typing.Any:
    'createTonemapMantiuk([, gamma[, scale[, saturation]]]) -> retval\n.   @brief Creates TonemapMantiuk object\n.   \n.   @param gamma gamma value for gamma correction. See createTonemap\n.   @param scale contrast scale factor. HVS response is multiplied by this parameter, thus compressing\n.   dynamic range. Values from 0.6 to 0.9 produce best results.\n.   @param saturation saturation enhancement value. See createTonemapDrago'
    ...

def createTonemapReinhard(gamma=..., intensity=..., light_adapt=..., color_adapt=...) -> typing.Any:
    "createTonemapReinhard([, gamma[, intensity[, light_adapt[, color_adapt]]]]) -> retval\n.   @brief Creates TonemapReinhard object\n.   \n.   @param gamma gamma value for gamma correction. See createTonemap\n.   @param intensity result intensity in [-8, 8] range. Greater intensity produces brighter results.\n.   @param light_adapt light adaptation in [0, 1] range. If 1 adaptation is based only on pixel\n.   value, if 0 it's global, otherwise it's a weighted mean of this two cases.\n.   @param color_adapt chromatic adaptation in [0, 1] range. If 1 channels are treated independently,\n.   if 0 adaptation level is the same for each channel."
    ...

def createTrackbar(trackbarName, windowName, value, count, onChange) -> typing.Any:
    'createTrackbar(trackbarName, windowName, value, count, onChange) -> None'
    ...

def cubeRoot(val) -> typing.Any:
    'cubeRoot(val) -> retval\n.   @brief Computes the cube root of an argument.\n.   \n.    The function cubeRoot computes \\f$\\sqrt[3]{\\texttt{val}}\\f$. Negative arguments are handled correctly.\n.    NaN and Inf are not handled. The accuracy approaches the maximum possible accuracy for\n.    single-precision data.\n.    @param val A function argument.'
    ...

cuda_BufferPool = _mod_cv2.cuda_BufferPool
cuda_DeviceInfo = _mod_cv2.cuda_DeviceInfo
cuda_Event = _mod_cv2.cuda_Event
cuda_GpuMat = _mod_cv2.cuda_GpuMat
cuda_GpuMat_Allocator = _mod_cv2.cuda_GpuMat_Allocator
cuda_HostMem = _mod_cv2.cuda_HostMem
cuda_Stream = _mod_cv2.cuda_Stream
cuda_TargetArchs = _mod_cv2.cuda_TargetArchs
def cvtColor(src: Mat, code: int, dts: Mat = ..., dstCn: int = ...) -> Mat:
    'cvtColor(src, code[, dst[, dstCn]]) -> dst\n.   @brief Converts an image from one color space to another.\n.   \n.   The function converts an input image from one color space to another. In case of a transformation\n.   to-from RGB color space, the order of the channels should be specified explicitly (RGB or BGR). Note\n.   that the default color format in OpenCV is often referred to as RGB but it is actually BGR (the\n.   bytes are reversed). So the first byte in a standard (24-bit) color image will be an 8-bit Blue\n.   component, the second byte will be Green, and the third byte will be Red. The fourth, fifth, and\n.   sixth bytes would then be the second pixel (Blue, then Green, then Red), and so on.\n.   \n.   The conventional ranges for R, G, and B channel values are:\n.   -   0 to 255 for CV_8U images\n.   -   0 to 65535 for CV_16U images\n.   -   0 to 1 for CV_32F images\n.   \n.   In case of linear transformations, the range does not matter. But in case of a non-linear\n.   transformation, an input RGB image should be normalized to the proper value range to get the correct\n.   results, for example, for RGB \\f$\\rightarrow\\f$ L\\*u\\*v\\* transformation. For example, if you have a\n.   32-bit floating-point image directly converted from an 8-bit image without any scaling, then it will\n.   have the 0..255 value range instead of 0..1 assumed by the function. So, before calling #cvtColor ,\n.   you need first to scale the image down:\n.   @code\n.       img *= 1./255;\n.       cvtColor(img, img, COLOR_BGR2Luv);\n.   @endcode\n.   If you use #cvtColor with 8-bit images, the conversion will have some information lost. For many\n.   applications, this will not be noticeable but it is recommended to use 32-bit images in applications\n.   that need the full range of colors or that convert an image before an operation and then convert\n.   back.\n.   \n.   If conversion adds the alpha channel, its value will set to the maximum of corresponding channel\n.   range: 255 for CV_8U, 65535 for CV_16U, 1 for CV_32F.\n.   \n.   @param src input image: 8-bit unsigned, 16-bit unsigned ( CV_16UC... ), or single-precision\n.   floating-point.\n.   @param dst output image of the same size and depth as src.\n.   @param code color space conversion code (see #ColorConversionCodes).\n.   @param dstCn number of channels in the destination image; if the parameter is 0, the number of the\n.   channels is derived automatically from src and code.\n.   \n.   @see @ref imgproc_color_conversions'
    ...

def cvtColorTwoPlane(src1: Mat, src2: Mat, code: int, dts: Mat = ...) -> typing.Any:
    'cvtColorTwoPlane(src1, src2, code[, dst]) -> dst\n.   @brief Converts an image from one color space to another where the source image is\n.   stored in two planes.\n.   \n.   This function only supports YUV420 to RGB conversion as of now.\n.   \n.   @param src1: 8-bit image (#CV_8U) of the Y plane.\n.   @param src2: image containing interleaved U/V plane.\n.   @param dst: output image.\n.   @param code: Specifies the type of conversion. It can take any of the following values:\n.   - #COLOR_YUV2BGR_NV12\n.   - #COLOR_YUV2RGB_NV12\n.   - #COLOR_YUV2BGRA_NV12\n.   - #COLOR_YUV2RGBA_NV12\n.   - #COLOR_YUV2BGR_NV21\n.   - #COLOR_YUV2RGB_NV21\n.   - #COLOR_YUV2BGRA_NV21\n.   - #COLOR_YUV2RGBA_NV21'
    ...

def dct(src: Mat, dts: Mat = ..., flags: int = ...) -> typing.Any:
    'dct(src[, dst[, flags]]) -> dst\n.   @brief Performs a forward or inverse discrete Cosine transform of 1D or 2D array.\n.   \n.   The function cv::dct performs a forward or inverse discrete Cosine transform (DCT) of a 1D or 2D\n.   floating-point array:\n.   -   Forward Cosine transform of a 1D vector of N elements:\n.       \\f[Y = C^{(N)}  \\cdot X\\f]\n.       where\n.       \\f[C^{(N)}_{jk}= \\sqrt{\\alpha_j/N} \\cos \\left ( \\frac{\\pi(2k+1)j}{2N} \\right )\\f]\n.       and\n.       \\f$\\alpha_0=1\\f$, \\f$\\alpha_j=2\\f$ for *j \\> 0*.\n.   -   Inverse Cosine transform of a 1D vector of N elements:\n.       \\f[X =  \\left (C^{(N)} \\right )^{-1}  \\cdot Y =  \\left (C^{(N)} \\right )^T  \\cdot Y\\f]\n.       (since \\f$C^{(N)}\\f$ is an orthogonal matrix, \\f$C^{(N)} \\cdot \\left(C^{(N)}\\right)^T = I\\f$ )\n.   -   Forward 2D Cosine transform of M x N matrix:\n.       \\f[Y = C^{(N)}  \\cdot X  \\cdot \\left (C^{(N)} \\right )^T\\f]\n.   -   Inverse 2D Cosine transform of M x N matrix:\n.       \\f[X =  \\left (C^{(N)} \\right )^T  \\cdot X  \\cdot C^{(N)}\\f]\n.   \n.   The function chooses the mode of operation by looking at the flags and size of the input array:\n.   -   If (flags & #DCT_INVERSE) == 0 , the function does a forward 1D or 2D transform. Otherwise, it\n.       is an inverse 1D or 2D transform.\n.   -   If (flags & #DCT_ROWS) != 0 , the function performs a 1D transform of each row.\n.   -   If the array is a single column or a single row, the function performs a 1D transform.\n.   -   If none of the above is true, the function performs a 2D transform.\n.   \n.   @note Currently dct supports even-size arrays (2, 4, 6 ...). For data analysis and approximation, you\n.   can pad the array when necessary.\n.   Also, the function performance depends very much, and not monotonically, on the array size (see\n.   getOptimalDFTSize ). In the current implementation DCT of a vector of size N is calculated via DFT\n.   of a vector of size N/2 . Thus, the optimal DCT size N1 \\>= N can be calculated as:\n.   @code\n.       size_t getOptimalDCTSize(size_t N) { return 2*getOptimalDFTSize((N+1)/2); }\n.       N1 = getOptimalDCTSize(N);\n.   @endcode\n.   @param src input floating-point array.\n.   @param dst output array of the same size and type as src .\n.   @param flags transformation flags as a combination of cv::DftFlags (DCT_*)\n.   @sa dft , getOptimalDFTSize , idct'
    ...

def decolor(src: Mat, grayscale=..., color_boost=...) -> typing.Any:
    'decolor(src[, grayscale[, color_boost]]) -> grayscale, color_boost\n.   @brief Transforms a color image to a grayscale image. It is a basic tool in digital printing, stylized\n.   black-and-white photograph rendering, and in many single channel image processing applications\n.   @cite CL12 .\n.   \n.   @param src Input 8-bit 3-channel image.\n.   @param grayscale Output 8-bit 1-channel image.\n.   @param color_boost Output 8-bit 3-channel image.\n.   \n.   This function is to be applied on color images.'
    ...

def decomposeEssentialMat(E, R1=..., R2=..., t=...) -> typing.Any:
    "decomposeEssentialMat(E[, R1[, R2[, t]]]) -> R1, R2, t\n.   @brief Decompose an essential matrix to possible rotations and translation.\n.   \n.   @param E The input essential matrix.\n.   @param R1 One possible rotation matrix.\n.   @param R2 Another possible rotation matrix.\n.   @param t One possible translation.\n.   \n.   This function decomposes the essential matrix E using svd decomposition @cite HartleyZ00. In\n.   general, four possible poses exist for the decomposition of E. They are \\f$[R_1, t]\\f$,\n.   \\f$[R_1, -t]\\f$, \\f$[R_2, t]\\f$, \\f$[R_2, -t]\\f$.\n.   \n.   If E gives the epipolar constraint \\f$[p_2; 1]^T A^{-T} E A^{-1} [p_1; 1] = 0\\f$ between the image\n.   points \\f$p_1\\f$ in the first image and \\f$p_2\\f$ in second image, then any of the tuples\n.   \\f$[R_1, t]\\f$, \\f$[R_1, -t]\\f$, \\f$[R_2, t]\\f$, \\f$[R_2, -t]\\f$ is a change of basis from the first\n.   camera's coordinate system to the second camera's coordinate system. However, by decomposing E, one\n.   can only get the direction of the translation. For this reason, the translation t is returned with\n.   unit length."
    ...

def decomposeHomographyMat(H, K, rotations=..., translations=..., normals=...) -> typing.Any:
    "decomposeHomographyMat(H, K[, rotations[, translations[, normals]]]) -> retval, rotations, translations, normals\n.   @brief Decompose a homography matrix to rotation(s), translation(s) and plane normal(s).\n.   \n.   @param H The input homography matrix between two images.\n.   @param K The input intrinsic camera calibration matrix.\n.   @param rotations Array of rotation matrices.\n.   @param translations Array of translation matrices.\n.   @param normals Array of plane normal matrices.\n.   \n.   This function extracts relative camera motion between two views of a planar object and returns up to\n.   four mathematical solution tuples of rotation, translation, and plane normal. The decomposition of\n.   the homography matrix H is described in detail in @cite Malis.\n.   \n.   If the homography H, induced by the plane, gives the constraint\n.   \\f[s_i \\vecthree{x'_i}{y'_i}{1} \\sim H \\vecthree{x_i}{y_i}{1}\\f] on the source image points\n.   \\f$p_i\\f$ and the destination image points \\f$p'_i\\f$, then the tuple of rotations[k] and\n.   translations[k] is a change of basis from the source camera's coordinate system to the destination\n.   camera's coordinate system. However, by decomposing H, one can only get the translation normalized\n.   by the (typically unknown) depth of the scene, i.e. its direction but with normalized length.\n.   \n.   If point correspondences are available, at least two solutions may further be invalidated, by\n.   applying positive depth constraint, i.e. all points must be in front of the camera."
    ...

def decomposeProjectionMatrix(projMatrix, cameraMatrix=..., rotMatrix=..., transVect=..., rotMatrixX=..., rotMatrixY=..., rotMatrixZ=..., eulerAngles=...) -> typing.Any:
    'decomposeProjectionMatrix(projMatrix[, cameraMatrix[, rotMatrix[, transVect[, rotMatrixX[, rotMatrixY[, rotMatrixZ[, eulerAngles]]]]]]]) -> cameraMatrix, rotMatrix, transVect, rotMatrixX, rotMatrixY, rotMatrixZ, eulerAngles\n.   @brief Decomposes a projection matrix into a rotation matrix and a camera matrix.\n.   \n.   @param projMatrix 3x4 input projection matrix P.\n.   @param cameraMatrix Output 3x3 camera matrix K.\n.   @param rotMatrix Output 3x3 external rotation matrix R.\n.   @param transVect Output 4x1 translation vector T.\n.   @param rotMatrixX Optional 3x3 rotation matrix around x-axis.\n.   @param rotMatrixY Optional 3x3 rotation matrix around y-axis.\n.   @param rotMatrixZ Optional 3x3 rotation matrix around z-axis.\n.   @param eulerAngles Optional three-element vector containing three Euler angles of rotation in\n.   degrees.\n.   \n.   The function computes a decomposition of a projection matrix into a calibration and a rotation\n.   matrix and the position of a camera.\n.   \n.   It optionally returns three rotation matrices, one for each axis, and three Euler angles that could\n.   be used in OpenGL. Note, there is always more than one sequence of rotations about the three\n.   principal axes that results in the same orientation of an object, e.g. see @cite Slabaugh . Returned\n.   tree rotation matrices and corresponding three Euler angles are only one of the possible solutions.\n.   \n.   The function is based on RQDecomp3x3 .'
    ...

def demosaicing(src: Mat, code: int, dts: Mat = ..., dstCn: int = ...) -> typing.Any:
    'demosaicing(src, code[, dst[, dstCn]]) -> dst\n.   @brief main function for all demosaicing processes\n.   \n.   @param src input image: 8-bit unsigned or 16-bit unsigned.\n.   @param dst output image of the same size and depth as src.\n.   @param code Color space conversion code (see the description below).\n.   @param dstCn number of channels in the destination image; if the parameter is 0, the number of the\n.   channels is derived automatically from src and code.\n.   \n.   The function can do the following transformations:\n.   \n.   -   Demosaicing using bilinear interpolation\n.   \n.       #COLOR_BayerBG2BGR , #COLOR_BayerGB2BGR , #COLOR_BayerRG2BGR , #COLOR_BayerGR2BGR\n.   \n.       #COLOR_BayerBG2GRAY , #COLOR_BayerGB2GRAY , #COLOR_BayerRG2GRAY , #COLOR_BayerGR2GRAY\n.   \n.   -   Demosaicing using Variable Number of Gradients.\n.   \n.       #COLOR_BayerBG2BGR_VNG , #COLOR_BayerGB2BGR_VNG , #COLOR_BayerRG2BGR_VNG , #COLOR_BayerGR2BGR_VNG\n.   \n.   -   Edge-Aware Demosaicing.\n.   \n.       #COLOR_BayerBG2BGR_EA , #COLOR_BayerGB2BGR_EA , #COLOR_BayerRG2BGR_EA , #COLOR_BayerGR2BGR_EA\n.   \n.   -   Demosaicing with alpha channel\n.   \n.       #COLOR_BayerBG2BGRA , #COLOR_BayerGB2BGRA , #COLOR_BayerRG2BGRA , #COLOR_BayerGR2BGRA\n.   \n.   @sa cvtColor'
    ...

def denoise_TVL1(observations, result, lambda_=..., niters=...) -> typing.Any:
    "denoise_TVL1(observations, result[, lambda[, niters]]) -> None\n.   @brief Primal-dual algorithm is an algorithm for solving special types of variational problems (that is,\n.   finding a function to minimize some functional). As the image denoising, in particular, may be seen\n.   as the variational problem, primal-dual algorithm then can be used to perform denoising and this is\n.   exactly what is implemented.\n.   \n.   It should be noted, that this implementation was taken from the July 2013 blog entry\n.   @cite MA13 , which also contained (slightly more general) ready-to-use source code on Python.\n.   Subsequently, that code was rewritten on C++ with the usage of openCV by Vadim Pisarevsky at the end\n.   of July 2013 and finally it was slightly adapted by later authors.\n.   \n.   Although the thorough discussion and justification of the algorithm involved may be found in\n.   @cite ChambolleEtAl, it might make sense to skim over it here, following @cite MA13 . To begin\n.   with, we consider the 1-byte gray-level images as the functions from the rectangular domain of\n.   pixels (it may be seen as set\n.   \\f$\\left\\{(x,y)\\in\\mathbb{N}\\times\\mathbb{N}\\mid 1\\leq x\\leq n,\\;1\\leq y\\leq m\\right\\}\\f$ for some\n.   \\f$m,\\;n\\in\\mathbb{N}\\f$) into \\f$\\{0,1,\\dots,255\\}\\f$. We shall denote the noised images as \\f$f_i\\f$ and with\n.   this view, given some image \\f$x\\f$ of the same size, we may measure how bad it is by the formula\n.   \n.   \\f[\\left\\|\\left\\|\\nabla x\\right\\|\\right\\| + \\lambda\\sum_i\\left\\|\\left\\|x-f_i\\right\\|\\right\\|\\f]\n.   \n.   \\f$\\|\\|\\cdot\\|\\|\\f$ here denotes \\f$L_2\\f$-norm and as you see, the first addend states that we want our\n.   image to be smooth (ideally, having zero gradient, thus being constant) and the second states that\n.   we want our result to be close to the observations we've got. If we treat \\f$x\\f$ as a function, this is\n.   exactly the functional what we seek to minimize and here the Primal-Dual algorithm comes into play.\n.   \n.   @param observations This array should contain one or more noised versions of the image that is to\n.   be restored.\n.   @param result Here the denoised image will be stored. There is no need to do pre-allocation of\n.   storage space, as it will be automatically allocated, if necessary.\n.   @param lambda Corresponds to \\f$\\lambda\\f$ in the formulas above. As it is enlarged, the smooth\n.   (blurred) images are treated more favorably than detailed (but maybe more noised) ones. Roughly\n.   speaking, as it becomes smaller, the result will be more blur but more sever outliers will be\n.   removed.\n.   @param niters Number of iterations that the algorithm will run. Of course, as more iterations as\n.   better, but it is hard to quantitatively refine this statement, so just use the default and\n.   increase it if the results are poor."
    ...

def destroyAllWindows() -> typing.Any:
    'destroyAllWindows() -> None\n.   @brief Destroys all of the HighGUI windows.\n.   \n.   The function destroyAllWindows destroys all of the opened HighGUI windows.'
    ...

def destroyWindow(winname) -> typing.Any:
    'destroyWindow(winname) -> None\n.   @brief Destroys the specified window.\n.   \n.   The function destroyWindow destroys the window with the given name.\n.   \n.   @param winname Name of the window to be destroyed.'
    ...

def detailEnhance(src: Mat, dts: Mat = ..., sigma_s=..., sigma_r=...) -> typing.Any:
    'detailEnhance(src[, dst[, sigma_s[, sigma_r]]]) -> dst\n.   @brief This filter enhances the details of a particular image.\n.   \n.   @param src Input 8-bit 3-channel image.\n.   @param dst Output image with the same size and type as src.\n.   @param sigma_s %Range between 0 to 200.\n.   @param sigma_r %Range between 0 to 1.'
    ...

detail_AffineBasedEstimator = _mod_cv2.detail_AffineBasedEstimator
detail_AffineBestOf2NearestMatcher = _mod_cv2.detail_AffineBestOf2NearestMatcher
detail_BestOf2NearestMatcher = _mod_cv2.detail_BestOf2NearestMatcher
detail_BestOf2NearestRangeMatcher = _mod_cv2.detail_BestOf2NearestRangeMatcher
detail_Blender = _mod_cv2.detail_Blender
detail_BlocksChannelsCompensator = _mod_cv2.detail_BlocksChannelsCompensator
detail_BlocksCompensator = _mod_cv2.detail_BlocksCompensator
detail_BlocksGainCompensator = _mod_cv2.detail_BlocksGainCompensator
detail_BundleAdjusterAffine = _mod_cv2.detail_BundleAdjusterAffine
detail_BundleAdjusterAffinePartial = _mod_cv2.detail_BundleAdjusterAffinePartial
detail_BundleAdjusterBase = _mod_cv2.detail_BundleAdjusterBase
detail_BundleAdjusterRay = _mod_cv2.detail_BundleAdjusterRay
detail_BundleAdjusterReproj = _mod_cv2.detail_BundleAdjusterReproj
detail_CameraParams = _mod_cv2.detail_CameraParams
detail_ChannelsCompensator = _mod_cv2.detail_ChannelsCompensator
detail_DpSeamFinder = _mod_cv2.detail_DpSeamFinder
detail_Estimator = _mod_cv2.detail_Estimator
detail_ExposureCompensator = _mod_cv2.detail_ExposureCompensator
detail_FeatherBlender = _mod_cv2.detail_FeatherBlender
detail_FeaturesMatcher = _mod_cv2.detail_FeaturesMatcher
detail_GainCompensator = _mod_cv2.detail_GainCompensator
detail_GraphCutSeamFinder = _mod_cv2.detail_GraphCutSeamFinder
detail_HomographyBasedEstimator = _mod_cv2.detail_HomographyBasedEstimator
detail_ImageFeatures = _mod_cv2.detail_ImageFeatures
detail_MatchesInfo = _mod_cv2.detail_MatchesInfo
detail_MultiBandBlender = _mod_cv2.detail_MultiBandBlender
detail_NoBundleAdjuster = _mod_cv2.detail_NoBundleAdjuster
detail_NoExposureCompensator = _mod_cv2.detail_NoExposureCompensator
detail_NoSeamFinder = _mod_cv2.detail_NoSeamFinder
detail_PairwiseSeamFinder = _mod_cv2.detail_PairwiseSeamFinder
detail_ProjectorBase = _mod_cv2.detail_ProjectorBase
detail_SeamFinder = _mod_cv2.detail_SeamFinder
detail_SphericalProjector = _mod_cv2.detail_SphericalProjector
detail_Timelapser = _mod_cv2.detail_Timelapser
detail_TimelapserCrop = _mod_cv2.detail_TimelapserCrop
detail_VoronoiSeamFinder = _mod_cv2.detail_VoronoiSeamFinder
def determinant(mtx) -> typing.Any:
    'determinant(mtx) -> retval\n.   @brief Returns the determinant of a square floating-point matrix.\n.   \n.   The function cv::determinant calculates and returns the determinant of the\n.   specified matrix. For small matrices ( mtx.cols=mtx.rows\\<=3 ), the\n.   direct method is used. For larger matrices, the function uses LU\n.   factorization with partial pivoting.\n.   \n.   For symmetric positively-determined matrices, it is also possible to use\n.   eigen decomposition to calculate the determinant.\n.   @param mtx input matrix that must have CV_32FC1 or CV_64FC1 type and\n.   square size.\n.   @sa trace, invert, solve, eigen, @ref MatrixExpressions'
    ...

def dft(src: Mat, dts: Mat = ..., flags: int = ..., nonzeroRows=...) -> typing.Any:
    'dft(src[, dst[, flags[, nonzeroRows]]]) -> dst\n.   @brief Performs a forward or inverse Discrete Fourier transform of a 1D or 2D floating-point array.\n.   \n.   The function cv::dft performs one of the following:\n.   -   Forward the Fourier transform of a 1D vector of N elements:\n.       \\f[Y = F^{(N)}  \\cdot X,\\f]\n.       where \\f$F^{(N)}_{jk}=\\exp(-2\\pi i j k/N)\\f$ and \\f$i=\\sqrt{-1}\\f$\n.   -   Inverse the Fourier transform of a 1D vector of N elements:\n.       \\f[\\begin{array}{l} X\'=  \\left (F^{(N)} \\right )^{-1}  \\cdot Y =  \\left (F^{(N)} \\right )^*  \\cdot y  \\\\ X = (1/N)  \\cdot X, \\end{array}\\f]\n.       where \\f$F^*=\\left(\\textrm{Re}(F^{(N)})-\\textrm{Im}(F^{(N)})\\right)^T\\f$\n.   -   Forward the 2D Fourier transform of a M x N matrix:\n.       \\f[Y = F^{(M)}  \\cdot X  \\cdot F^{(N)}\\f]\n.   -   Inverse the 2D Fourier transform of a M x N matrix:\n.       \\f[\\begin{array}{l} X\'=  \\left (F^{(M)} \\right )^*  \\cdot Y  \\cdot \\left (F^{(N)} \\right )^* \\\\ X =  \\frac{1}{M \\cdot N} \\cdot X\' \\end{array}\\f]\n.   \n.   In case of real (single-channel) data, the output spectrum of the forward Fourier transform or input\n.   spectrum of the inverse Fourier transform can be represented in a packed format called *CCS*\n.   (complex-conjugate-symmetrical). It was borrowed from IPL (Intel\\* Image Processing Library). Here\n.   is how 2D *CCS* spectrum looks:\n.   \\f[\\begin{bmatrix} Re Y_{0,0} & Re Y_{0,1} & Im Y_{0,1} & Re Y_{0,2} & Im Y_{0,2} &  \\cdots & Re Y_{0,N/2-1} & Im Y_{0,N/2-1} & Re Y_{0,N/2}  \\\\ Re Y_{1,0} & Re Y_{1,1} & Im Y_{1,1} & Re Y_{1,2} & Im Y_{1,2} &  \\cdots & Re Y_{1,N/2-1} & Im Y_{1,N/2-1} & Re Y_{1,N/2}  \\\\ Im Y_{1,0} & Re Y_{2,1} & Im Y_{2,1} & Re Y_{2,2} & Im Y_{2,2} &  \\cdots & Re Y_{2,N/2-1} & Im Y_{2,N/2-1} & Im Y_{1,N/2}  \\\\ \\hdotsfor{9} \\\\ Re Y_{M/2-1,0} &  Re Y_{M-3,1}  & Im Y_{M-3,1} &  \\hdotsfor{3} & Re Y_{M-3,N/2-1} & Im Y_{M-3,N/2-1}& Re Y_{M/2-1,N/2}  \\\\ Im Y_{M/2-1,0} &  Re Y_{M-2,1}  & Im Y_{M-2,1} &  \\hdotsfor{3} & Re Y_{M-2,N/2-1} & Im Y_{M-2,N/2-1}& Im Y_{M/2-1,N/2}  \\\\ Re Y_{M/2,0}  &  Re Y_{M-1,1} &  Im Y_{M-1,1} &  \\hdotsfor{3} & Re Y_{M-1,N/2-1} & Im Y_{M-1,N/2-1}& Re Y_{M/2,N/2} \\end{bmatrix}\\f]\n.   \n.   In case of 1D transform of a real vector, the output looks like the first row of the matrix above.\n.   \n.   So, the function chooses an operation mode depending on the flags and size of the input array:\n.   -   If #DFT_ROWS is set or the input array has a single row or single column, the function\n.       performs a 1D forward or inverse transform of each row of a matrix when #DFT_ROWS is set.\n.       Otherwise, it performs a 2D transform.\n.   -   If the input array is real and #DFT_INVERSE is not set, the function performs a forward 1D or\n.       2D transform:\n.       -   When #DFT_COMPLEX_OUTPUT is set, the output is a complex matrix of the same size as\n.           input.\n.       -   When #DFT_COMPLEX_OUTPUT is not set, the output is a real matrix of the same size as\n.           input. In case of 2D transform, it uses the packed format as shown above. In case of a\n.           single 1D transform, it looks like the first row of the matrix above. In case of\n.           multiple 1D transforms (when using the #DFT_ROWS flag), each row of the output matrix\n.           looks like the first row of the matrix above.\n.   -   If the input array is complex and either #DFT_INVERSE or #DFT_REAL_OUTPUT are not set, the\n.       output is a complex array of the same size as input. The function performs a forward or\n.       inverse 1D or 2D transform of the whole input array or each row of the input array\n.       independently, depending on the flags DFT_INVERSE and DFT_ROWS.\n.   -   When #DFT_INVERSE is set and the input array is real, or it is complex but #DFT_REAL_OUTPUT\n.       is set, the output is a real array of the same size as input. The function performs a 1D or 2D\n.       inverse transformation of the whole input array or each individual row, depending on the flags\n.       #DFT_INVERSE and #DFT_ROWS.\n.   \n.   If #DFT_SCALE is set, the scaling is done after the transformation.\n.   \n.   Unlike dct , the function supports arrays of arbitrary size. But only those arrays are processed\n.   efficiently, whose sizes can be factorized in a product of small prime numbers (2, 3, and 5 in the\n.   current implementation). Such an efficient DFT size can be calculated using the getOptimalDFTSize\n.   method.\n.   \n.   The sample below illustrates how to calculate a DFT-based convolution of two 2D real arrays:\n.   @code\n.       void convolveDFT(InputArray A, InputArray B, OutputArray C)\n.       {\n.           // reallocate the output array if needed\n.           C.create(abs(A.rows - B.rows)+1, abs(A.cols - B.cols)+1, A.type());\n.           Size dftSize;\n.           // calculate the size of DFT transform\n.           dftSize.width = getOptimalDFTSize(A.cols + B.cols - 1);\n.           dftSize.height = getOptimalDFTSize(A.rows + B.rows - 1);\n.   \n.           // allocate temporary buffers and initialize them with 0\'s\n.           Mat tempA(dftSize, A.type(), Scalar::all(0));\n.           Mat tempB(dftSize, B.type(), Scalar::all(0));\n.   \n.           // copy A and B to the top-left corners of tempA and tempB, respectively\n.           Mat roiA(tempA, Rect(0,0,A.cols,A.rows));\n.           A.copyTo(roiA);\n.           Mat roiB(tempB, Rect(0,0,B.cols,B.rows));\n.           B.copyTo(roiB);\n.   \n.           // now transform the padded A & B in-place;\n.           // use "nonzeroRows" hint for faster processing\n.           dft(tempA, tempA, 0, A.rows);\n.           dft(tempB, tempB, 0, B.rows);\n.   \n.           // multiply the spectrums;\n.           // the function handles packed spectrum representations well\n.           mulSpectrums(tempA, tempB, tempA);\n.   \n.           // transform the product back from the frequency domain.\n.           // Even though all the result rows will be non-zero,\n.           // you need only the first C.rows of them, and thus you\n.           // pass nonzeroRows == C.rows\n.           dft(tempA, tempA, DFT_INVERSE + DFT_SCALE, C.rows);\n.   \n.           // now copy the result back to C.\n.           tempA(Rect(0, 0, C.cols, C.rows)).copyTo(C);\n.   \n.           // all the temporary buffers will be deallocated automatically\n.       }\n.   @endcode\n.   To optimize this sample, consider the following approaches:\n.   -   Since nonzeroRows != 0 is passed to the forward transform calls and since A and B are copied to\n.       the top-left corners of tempA and tempB, respectively, it is not necessary to clear the whole\n.       tempA and tempB. It is only necessary to clear the tempA.cols - A.cols ( tempB.cols - B.cols)\n.       rightmost columns of the matrices.\n.   -   This DFT-based convolution does not have to be applied to the whole big arrays, especially if B\n.       is significantly smaller than A or vice versa. Instead, you can calculate convolution by parts.\n.       To do this, you need to split the output array C into multiple tiles. For each tile, estimate\n.       which parts of A and B are required to calculate convolution in this tile. If the tiles in C are\n.       too small, the speed will decrease a lot because of repeated work. In the ultimate case, when\n.       each tile in C is a single pixel, the algorithm becomes equivalent to the naive convolution\n.       algorithm. If the tiles are too big, the temporary arrays tempA and tempB become too big and\n.       there is also a slowdown because of bad cache locality. So, there is an optimal tile size\n.       somewhere in the middle.\n.   -   If different tiles in C can be calculated in parallel and, thus, the convolution is done by\n.       parts, the loop can be threaded.\n.   \n.   All of the above improvements have been implemented in #matchTemplate and #filter2D . Therefore, by\n.   using them, you can get the performance even better than with the above theoretically optimal\n.   implementation. Though, those two functions actually calculate cross-correlation, not convolution,\n.   so you need to "flip" the second convolution operand B vertically and horizontally using flip .\n.   @note\n.   -   An example using the discrete fourier transform can be found at\n.       opencv_source_code/samples/cpp/dft.cpp\n.   -   (Python) An example using the dft functionality to perform Wiener deconvolution can be found\n.       at opencv_source/samples/python/deconvolution.py\n.   -   (Python) An example rearranging the quadrants of a Fourier image can be found at\n.       opencv_source/samples/python/dft.py\n.   @param src input array that could be real or complex.\n.   @param dst output array whose size and type depends on the flags .\n.   @param flags transformation flags, representing a combination of the #DftFlags\n.   @param nonzeroRows when the parameter is not zero, the function assumes that only the first\n.   nonzeroRows rows of the input array (#DFT_INVERSE is not set) or only the first nonzeroRows of the\n.   output array (#DFT_INVERSE is set) contain non-zeros, thus, the function can handle the rest of the\n.   rows more efficiently and save some time; this technique is very useful for calculating array\n.   cross-correlation or convolution using DFT.\n.   @sa dct , getOptimalDFTSize , mulSpectrums, filter2D , matchTemplate , flip , cartToPolar ,\n.   magnitude , phase'
    ...

def dilate(src: Mat, kernel, dts: Mat = ..., anchor=..., iterations=..., borderType=..., borderValue=...) -> typing.Any:
    "dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) -> dst\n.   @brief Dilates an image by using a specific structuring element.\n.   \n.   The function dilates the source image using the specified structuring element that determines the\n.   shape of a pixel neighborhood over which the maximum is taken:\n.   \\f[\\texttt{dst} (x,y) =  \\max _{(x',y'):  \\, \\texttt{element} (x',y') \\ne0 } \\texttt{src} (x+x',y+y')\\f]\n.   \n.   The function supports the in-place mode. Dilation can be applied several ( iterations ) times. In\n.   case of multi-channel images, each channel is processed independently.\n.   \n.   @param src input image; the number of channels can be arbitrary, but the depth should be one of\n.   CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.\n.   @param dst output image of the same size and type as src.\n.   @param kernel structuring element used for dilation; if elemenat=Mat(), a 3 x 3 rectangular\n.   structuring element is used. Kernel can be created using #getStructuringElement\n.   @param anchor position of the anchor within the element; default value (-1, -1) means that the\n.   anchor is at the element center.\n.   @param iterations number of times dilation is applied.\n.   @param borderType pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not suported.\n.   @param borderValue border value in case of a constant border\n.   @sa  erode, morphologyEx, getStructuringElement"
    ...

def displayOverlay(winname, text, delayms=...) -> typing.Any:
    'displayOverlay(winname, text[, delayms]) -> None\n.   @brief Displays a text on a window image as an overlay for a specified duration.\n.   \n.   The function displayOverlay displays useful information/tips on top of the window for a certain\n.   amount of time *delayms*. The function does not modify the image, displayed in the window, that is,\n.   after the specified delay the original content of the window is restored.\n.   \n.   @param winname Name of the window.\n.   @param text Overlay text to write on a window image.\n.   @param delayms The period (in milliseconds), during which the overlay text is displayed. If this\n.   function is called before the previous overlay text timed out, the timer is restarted and the text\n.   is updated. If this value is zero, the text never disappears.'
    ...

def displayStatusBar(winname, text, delayms=...) -> typing.Any:
    'displayStatusBar(winname, text[, delayms]) -> None\n.   @brief Displays a text on the window statusbar during the specified period of time.\n.   \n.   The function displayStatusBar displays useful information/tips on top of the window for a certain\n.   amount of time *delayms* . This information is displayed on the window statusbar (the window must be\n.   created with the CV_GUI_EXPANDED flags).\n.   \n.   @param winname Name of the window.\n.   @param text Text to write on the window statusbar.\n.   @param delayms Duration (in milliseconds) to display the text. If this function is called before\n.   the previous text timed out, the timer is restarted and the text is updated. If this value is\n.   zero, the text never disappears.'
    ...

def distanceTransform(src: Mat, distanceType, maskSize, dts: Mat = ..., dstType=...) -> typing.Any:
    'distanceTransform(src, distanceType, maskSize[, dst[, dstType]]) -> dst\n.   @overload\n.   @param src 8-bit, single-channel (binary) source image.\n.   @param dst Output image with calculated distances. It is a 8-bit or 32-bit floating-point,\n.   single-channel image of the same size as src .\n.   @param distanceType Type of distance, see #DistanceTypes\n.   @param maskSize Size of the distance transform mask, see #DistanceTransformMasks. In case of the\n.   #DIST_L1 or #DIST_C distance type, the parameter is forced to 3 because a \\f$3\\times 3\\f$ mask gives\n.   the same result as \\f$5\\times 5\\f$ or any larger aperture.\n.   @param dstType Type of output image. It can be CV_8U or CV_32F. Type CV_8U can be used only for\n.   the first variant of the function and distanceType == #DIST_L1.'
    ...

def distanceTransformWithLabels(src: Mat, distanceType, maskSize, dts: Mat = ..., labels=..., labelType=...) -> typing.Any:
    "distanceTransformWithLabels(src, distanceType, maskSize[, dst[, labels[, labelType]]]) -> dst, labels\n.   @brief Calculates the distance to the closest zero pixel for each pixel of the source image.\n.   \n.   The function cv::distanceTransform calculates the approximate or precise distance from every binary\n.   image pixel to the nearest zero pixel. For zero image pixels, the distance will obviously be zero.\n.   \n.   When maskSize == #DIST_MASK_PRECISE and distanceType == #DIST_L2 , the function runs the\n.   algorithm described in @cite Felzenszwalb04 . This algorithm is parallelized with the TBB library.\n.   \n.   In other cases, the algorithm @cite Borgefors86 is used. This means that for a pixel the function\n.   finds the shortest path to the nearest zero pixel consisting of basic shifts: horizontal, vertical,\n.   diagonal, or knight's move (the latest is available for a \\f$5\\times 5\\f$ mask). The overall\n.   distance is calculated as a sum of these basic distances. Since the distance function should be\n.   symmetric, all of the horizontal and vertical shifts must have the same cost (denoted as a ), all\n.   the diagonal shifts must have the same cost (denoted as `b`), and all knight's moves must have the\n.   same cost (denoted as `c`). For the #DIST_C and #DIST_L1 types, the distance is calculated\n.   precisely, whereas for #DIST_L2 (Euclidean distance) the distance can be calculated only with a\n.   relative error (a \\f$5\\times 5\\f$ mask gives more accurate results). For `a`,`b`, and `c`, OpenCV\n.   uses the values suggested in the original paper:\n.   - DIST_L1: `a = 1, b = 2`\n.   - DIST_L2:\n.       - `3 x 3`: `a=0.955, b=1.3693`\n.       - `5 x 5`: `a=1, b=1.4, c=2.1969`\n.   - DIST_C: `a = 1, b = 1`\n.   \n.   Typically, for a fast, coarse distance estimation #DIST_L2, a \\f$3\\times 3\\f$ mask is used. For a\n.   more accurate distance estimation #DIST_L2, a \\f$5\\times 5\\f$ mask or the precise algorithm is used.\n.   Note that both the precise and the approximate algorithms are linear on the number of pixels.\n.   \n.   This variant of the function does not only compute the minimum distance for each pixel \\f$(x, y)\\f$\n.   but also identifies the nearest connected component consisting of zero pixels\n.   (labelType==#DIST_LABEL_CCOMP) or the nearest zero pixel (labelType==#DIST_LABEL_PIXEL). Index of the\n.   component/pixel is stored in `labels(x, y)`. When labelType==#DIST_LABEL_CCOMP, the function\n.   automatically finds connected components of zero pixels in the input image and marks them with\n.   distinct labels. When labelType==#DIST_LABEL_CCOMP, the function scans through the input image and\n.   marks all the zero pixels with distinct labels.\n.   \n.   In this mode, the complexity is still linear. That is, the function provides a very fast way to\n.   compute the Voronoi diagram for a binary image. Currently, the second variant can use only the\n.   approximate distance transform algorithm, i.e. maskSize=#DIST_MASK_PRECISE is not supported\n.   yet.\n.   \n.   @param src 8-bit, single-channel (binary) source image.\n.   @param dst Output image with calculated distances. It is a 8-bit or 32-bit floating-point,\n.   single-channel image of the same size as src.\n.   @param labels Output 2D array of labels (the discrete Voronoi diagram). It has the type\n.   CV_32SC1 and the same size as src.\n.   @param distanceType Type of distance, see #DistanceTypes\n.   @param maskSize Size of the distance transform mask, see #DistanceTransformMasks.\n.   #DIST_MASK_PRECISE is not supported by this variant. In case of the #DIST_L1 or #DIST_C distance type,\n.   the parameter is forced to 3 because a \\f$3\\times 3\\f$ mask gives the same result as \\f$5\\times\n.   5\\f$ or any larger aperture.\n.   @param labelType Type of the label array to build, see #DistanceTransformLabelTypes."
    ...

def divide(src1: Mat, src2: Mat, dts: Mat = ..., scale=..., dtype=...) -> typing.Any:
    'divide(src1, src2[, dst[, scale[, dtype]]]) -> dst\n.   @brief Performs per-element division of two arrays or a scalar by an array.\n.   \n.   The function cv::divide divides one array by another:\n.   \\f[\\texttt{dst(I) = saturate(src1(I)*scale/src2(I))}\\f]\n.   or a scalar by an array when there is no src1 :\n.   \\f[\\texttt{dst(I) = saturate(scale/src2(I))}\\f]\n.   \n.   Different channels of multi-channel arrays are processed independently.\n.   \n.   For integer types when src2(I) is zero, dst(I) will also be zero.\n.   \n.   @note In case of floating point data there is no special defined behavior for zero src2(I) values.\n.   Regular floating-point division is used.\n.   Expect correct IEEE-754 behaviour for floating-point data (with NaN, Inf result values).\n.   \n.   @note Saturation is not applied when the output array has the depth CV_32S. You may even get\n.   result of an incorrect sign in the case of overflow.\n.   @param src1 first input array.\n.   @param src2 second input array of the same size and type as src1.\n.   @param scale scalar factor.\n.   @param dst output array of the same size and type as src2.\n.   @param dtype optional depth of the output array; if -1, dst will have depth src2.depth(), but in\n.   case of an array-by-array division, you can only pass -1 when src1.depth()==src2.depth().\n.   @sa  multiply, add, subtract\n\n\n\ndivide(scale, src2[, dst[, dtype]]) -> dst\n.   @overload'
    ...

dnn_ClassificationModel = _mod_cv2.dnn_ClassificationModel
dnn_DetectionModel = _mod_cv2.dnn_DetectionModel
dnn_DictValue = _mod_cv2.dnn_DictValue
dnn_KeypointsModel = _mod_cv2.dnn_KeypointsModel
dnn_Layer = _mod_cv2.dnn_Layer
dnn_Model = _mod_cv2.dnn_Model
dnn_Net = _mod_cv2.dnn_Net
dnn_SegmentationModel = _mod_cv2.dnn_SegmentationModel
def dnn_registerLayer() -> typing.Any:
    'registerLayer(type, class) -> None'
    ...

def dnn_unregisterLayer() -> typing.Any:
    'unregisterLayer(type) -> None'
    ...

def drawChessboardCorners(image: Mat, patternSize, corners, patternWasFound) -> typing.Any:
    'drawChessboardCorners(image, patternSize, corners, patternWasFound) -> image\n.   @brief Renders the detected chessboard corners.\n.   \n.   @param image Destination image. It must be an 8-bit color image.\n.   @param patternSize Number of inner corners per a chessboard row and column\n.   (patternSize = cv::Size(points_per_row,points_per_column)).\n.   @param corners Array of detected corners, the output of findChessboardCorners.\n.   @param patternWasFound Parameter indicating whether the complete board was found or not. The\n.   return value of findChessboardCorners should be passed here.\n.   \n.   The function draws individual chessboard corners detected either as red circles if the board was not\n.   found, or as colored corners connected with lines if the board was found.'
    ...

def drawContours(image: Mat, contours, contourIdx, color, thickness=..., lineType=..., hierarchy=..., maxLevel=..., offset=...) -> typing.Any:
    'drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) -> image\n.   @brief Draws contours outlines or filled contours.\n.   \n.   The function draws contour outlines in the image if \\f$\\texttt{thickness} \\ge 0\\f$ or fills the area\n.   bounded by the contours if \\f$\\texttt{thickness}<0\\f$ . The example below shows how to retrieve\n.   connected components from the binary image and label them: :\n.   @include snippets/imgproc_drawContours.cpp\n.   \n.   @param image Destination image.\n.   @param contours All the input contours. Each contour is stored as a point vector.\n.   @param contourIdx Parameter indicating a contour to draw. If it is negative, all the contours are drawn.\n.   @param color Color of the contours.\n.   @param thickness Thickness of lines the contours are drawn with. If it is negative (for example,\n.   thickness=#FILLED ), the contour interiors are drawn.\n.   @param lineType Line connectivity. See #LineTypes\n.   @param hierarchy Optional information about hierarchy. It is only needed if you want to draw only\n.   some of the contours (see maxLevel ).\n.   @param maxLevel Maximal level for drawn contours. If it is 0, only the specified contour is drawn.\n.   If it is 1, the function draws the contour(s) and all the nested contours. If it is 2, the function\n.   draws the contours, all the nested contours, all the nested-to-nested contours, and so on. This\n.   parameter is only taken into account when there is hierarchy available.\n.   @param offset Optional contour shift parameter. Shift all the drawn contours by the specified\n.   \\f$\\texttt{offset}=(dx,dy)\\f$ .\n.   @note When thickness=#FILLED, the function is designed to handle connected components with holes correctly\n.   even when no hierarchy date is provided. This is done by analyzing all the outlines together\n.   using even-odd rule. This may give incorrect results if you have a joint collection of separately retrieved\n.   contours. In order to solve this problem, you need to call #drawContours separately for each sub-group\n.   of contours, or iterate over the collection using contourIdx parameter.'
    ...

def drawFrameAxes(image: Mat, cameraMatrix, distCoeffs, rvec, tvec, length, thickness=...) -> typing.Any:
    'drawFrameAxes(image, cameraMatrix, distCoeffs, rvec, tvec, length[, thickness]) -> image\n.   @brief Draw axes of the world/object coordinate system from pose estimation. @sa solvePnP\n.   \n.   @param image Input/output image. It must have 1 or 3 channels. The number of channels is not altered.\n.   @param cameraMatrix Input 3x3 floating-point matrix of camera intrinsic parameters.\n.   \\f$A = \\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\\f$\n.   @param distCoeffs Input vector of distortion coefficients\n.   \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6 [, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$ of\n.   4, 5, 8, 12 or 14 elements. If the vector is empty, the zero distortion coefficients are assumed.\n.   @param rvec Rotation vector (see @ref Rodrigues ) that, together with tvec, brings points from\n.   the model coordinate system to the camera coordinate system.\n.   @param tvec Translation vector.\n.   @param length Length of the painted axes in the same unit than tvec (usually in meters).\n.   @param thickness Line thickness of the painted axes.\n.   \n.   This function draws the axes of the world/object coordinate system w.r.t. to the camera frame.\n.   OX is drawn in red, OY in green and OZ in blue.'
    ...

def drawKeypoints(image: Mat, keypoints, outImage, color=..., flags: int = ...) -> typing.Any:
    'drawKeypoints(image, keypoints, outImage[, color[, flags]]) -> outImage\n.   @brief Draws keypoints.\n.   \n.   @param image Source image.\n.   @param keypoints Keypoints from the source image.\n.   @param outImage Output image. Its content depends on the flags value defining what is drawn in the\n.   output image. See possible flags bit values below.\n.   @param color Color of keypoints.\n.   @param flags Flags setting drawing features. Possible flags bit values are defined by\n.   DrawMatchesFlags. See details above in drawMatches .\n.   \n.   @note\n.   For Python API, flags are modified as cv.DRAW_MATCHES_FLAGS_DEFAULT,\n.   cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, cv.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG,\n.   cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS'
    ...

def drawMarker(img: Mat, position, color, markerType=..., markerSize=..., thickness=..., line_type=...) -> typing.Any:
    'drawMarker(img, position, color[, markerType[, markerSize[, thickness[, line_type]]]]) -> img\n.   @brief Draws a marker on a predefined position in an image.\n.   \n.   The function cv::drawMarker draws a marker on a given position in the image. For the moment several\n.   marker types are supported, see #MarkerTypes for more information.\n.   \n.   @param img Image.\n.   @param position The point where the crosshair is positioned.\n.   @param color Line color.\n.   @param markerType The specific type of marker you want to use, see #MarkerTypes\n.   @param thickness Line thickness.\n.   @param line_type Type of the line, See #LineTypes\n.   @param markerSize The length of the marker axis [default = 20 pixels]'
    ...

def drawMatches(img1, keypoints1, img2, keypoints2, matches1to2, outImg, matchColor=..., singlePointColor=..., matchesMask=..., flags: int = ...) -> typing.Any:
    'drawMatches(img1, keypoints1, img2, keypoints2, matches1to2, outImg[, matchColor[, singlePointColor[, matchesMask[, flags]]]]) -> outImg\n.   @brief Draws the found matches of keypoints from two images.\n.   \n.   @param img1 First source image.\n.   @param keypoints1 Keypoints from the first source image.\n.   @param img2 Second source image.\n.   @param keypoints2 Keypoints from the second source image.\n.   @param matches1to2 Matches from the first image to the second one, which means that keypoints1[i]\n.   has a corresponding point in keypoints2[matches[i]] .\n.   @param outImg Output image. Its content depends on the flags value defining what is drawn in the\n.   output image. See possible flags bit values below.\n.   @param matchColor Color of matches (lines and connected keypoints). If matchColor==Scalar::all(-1)\n.   , the color is generated randomly.\n.   @param singlePointColor Color of single keypoints (circles), which means that keypoints do not\n.   have the matches. If singlePointColor==Scalar::all(-1) , the color is generated randomly.\n.   @param matchesMask Mask determining which matches are drawn. If the mask is empty, all matches are\n.   drawn.\n.   @param flags Flags setting drawing features. Possible flags bit values are defined by\n.   DrawMatchesFlags.\n.   \n.   This function draws matches of keypoints from two images in the output image. Match is a line\n.   connecting two keypoints (circles). See cv::DrawMatchesFlags.'
    ...

def drawMatchesKnn(img1, keypoints1, img2, keypoints2, matches1to2, outImg, matchColor=..., singlePointColor=..., matchesMask=..., flags: int = ...) -> typing.Any:
    'drawMatchesKnn(img1, keypoints1, img2, keypoints2, matches1to2, outImg[, matchColor[, singlePointColor[, matchesMask[, flags]]]]) -> outImg\n.   @overload'
    ...

def edgePreservingFilter(src: Mat, dts: Mat = ..., flags: int = ..., sigma_s=..., sigma_r=...) -> typing.Any:
    'edgePreservingFilter(src[, dst[, flags[, sigma_s[, sigma_r]]]]) -> dst\n.   @brief Filtering is the fundamental operation in image and video processing. Edge-preserving smoothing\n.   filters are used in many different applications @cite EM11 .\n.   \n.   @param src Input 8-bit 3-channel image.\n.   @param dst Output 8-bit 3-channel image.\n.   @param flags Edge preserving filters: cv::RECURS_FILTER or cv::NORMCONV_FILTER\n.   @param sigma_s %Range between 0 to 200.\n.   @param sigma_r %Range between 0 to 1.'
    ...

def eigen(src: Mat, eigenvalues=..., eigenvectors=...) -> typing.Any:
    'eigen(src[, eigenvalues[, eigenvectors]]) -> retval, eigenvalues, eigenvectors\n.   @brief Calculates eigenvalues and eigenvectors of a symmetric matrix.\n.   \n.   The function cv::eigen calculates just eigenvalues, or eigenvalues and eigenvectors of the symmetric\n.   matrix src:\n.   @code\n.       src*eigenvectors.row(i).t() = eigenvalues.at<srcType>(i)*eigenvectors.row(i).t()\n.   @endcode\n.   \n.   @note Use cv::eigenNonSymmetric for calculation of real eigenvalues and eigenvectors of non-symmetric matrix.\n.   \n.   @param src input matrix that must have CV_32FC1 or CV_64FC1 type, square size and be symmetrical\n.   (src ^T^ == src).\n.   @param eigenvalues output vector of eigenvalues of the same type as src; the eigenvalues are stored\n.   in the descending order.\n.   @param eigenvectors output matrix of eigenvectors; it has the same size and type as src; the\n.   eigenvectors are stored as subsequent matrix rows, in the same order as the corresponding\n.   eigenvalues.\n.   @sa eigenNonSymmetric, completeSymm , PCA'
    ...

def eigenNonSymmetric(src: Mat, eigenvalues=..., eigenvectors=...) -> typing.Any:
    'eigenNonSymmetric(src[, eigenvalues[, eigenvectors]]) -> eigenvalues, eigenvectors\n.   @brief Calculates eigenvalues and eigenvectors of a non-symmetric matrix (real eigenvalues only).\n.   \n.   @note Assumes real eigenvalues.\n.   \n.   The function calculates eigenvalues and eigenvectors (optional) of the square matrix src:\n.   @code\n.       src*eigenvectors.row(i).t() = eigenvalues.at<srcType>(i)*eigenvectors.row(i).t()\n.   @endcode\n.   \n.   @param src input matrix (CV_32FC1 or CV_64FC1 type).\n.   @param eigenvalues output vector of eigenvalues (type is the same type as src).\n.   @param eigenvectors output matrix of eigenvectors (type is the same type as src). The eigenvectors are stored as subsequent matrix rows, in the same order as the corresponding eigenvalues.\n.   @sa eigen'
    ...

def ellipse(img: Mat, center, axes, angle, startAngle, endAngle, color, thickness=..., lineType=..., shift=...) -> typing.Any:
    'ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]) -> img\n.   @brief Draws a simple or thick elliptic arc or fills an ellipse sector.\n.   \n.   The function cv::ellipse with more parameters draws an ellipse outline, a filled ellipse, an elliptic\n.   arc, or a filled ellipse sector. The drawing code uses general parametric form.\n.   A piecewise-linear curve is used to approximate the elliptic arc\n.   boundary. If you need more control of the ellipse rendering, you can retrieve the curve using\n.   #ellipse2Poly and then render it with #polylines or fill it with #fillPoly. If you use the first\n.   variant of the function and want to draw the whole ellipse, not an arc, pass `startAngle=0` and\n.   `endAngle=360`. If `startAngle` is greater than `endAngle`, they are swapped. The figure below explains\n.   the meaning of the parameters to draw the blue arc.\n.   \n.   ![Parameters of Elliptic Arc](pics/ellipse.svg)\n.   \n.   @param img Image.\n.   @param center Center of the ellipse.\n.   @param axes Half of the size of the ellipse main axes.\n.   @param angle Ellipse rotation angle in degrees.\n.   @param startAngle Starting angle of the elliptic arc in degrees.\n.   @param endAngle Ending angle of the elliptic arc in degrees.\n.   @param color Ellipse color.\n.   @param thickness Thickness of the ellipse arc outline, if positive. Otherwise, this indicates that\n.   a filled ellipse sector is to be drawn.\n.   @param lineType Type of the ellipse boundary. See #LineTypes\n.   @param shift Number of fractional bits in the coordinates of the center and values of axes.\n\n\n\nellipse(img, box, color[, thickness[, lineType]]) -> img\n.   @overload\n.   @param img Image.\n.   @param box Alternative ellipse representation via RotatedRect. This means that the function draws\n.   an ellipse inscribed in the rotated rectangle.\n.   @param color Ellipse color.\n.   @param thickness Thickness of the ellipse arc outline, if positive. Otherwise, this indicates that\n.   a filled ellipse sector is to be drawn.\n.   @param lineType Type of the ellipse boundary. See #LineTypes'
    ...

def ellipse2Poly(center, axes, angle, arcStart, arcEnd, delta) -> typing.Any:
    'ellipse2Poly(center, axes, angle, arcStart, arcEnd, delta) -> pts\n.   @brief Approximates an elliptic arc with a polyline.\n.   \n.   The function ellipse2Poly computes the vertices of a polyline that approximates the specified\n.   elliptic arc. It is used by #ellipse. If `arcStart` is greater than `arcEnd`, they are swapped.\n.   \n.   @param center Center of the arc.\n.   @param axes Half of the size of the ellipse main axes. See #ellipse for details.\n.   @param angle Rotation angle of the ellipse in degrees. See #ellipse for details.\n.   @param arcStart Starting angle of the elliptic arc in degrees.\n.   @param arcEnd Ending angle of the elliptic arc in degrees.\n.   @param delta Angle between the subsequent polyline vertices. It defines the approximation\n.   accuracy.\n.   @param pts Output vector of polyline vertices.'
    ...

def equalizeHist(src: Mat, dts: Mat = ...) -> typing.Any:
    "equalizeHist(src[, dst]) -> dst\n.   @brief Equalizes the histogram of a grayscale image.\n.   \n.   The function equalizes the histogram of the input image using the following algorithm:\n.   \n.   - Calculate the histogram \\f$H\\f$ for src .\n.   - Normalize the histogram so that the sum of histogram bins is 255.\n.   - Compute the integral of the histogram:\n.   \\f[H'_i =  \\sum _{0  \\le j < i} H(j)\\f]\n.   - Transform the image using \\f$H'\\f$ as a look-up table: \\f$\\texttt{dst}(x,y) = H'(\\texttt{src}(x,y))\\f$\n.   \n.   The algorithm normalizes the brightness and increases the contrast of the image.\n.   \n.   @param src Source 8-bit single channel image.\n.   @param dst Destination image of the same size and type as src ."
    ...

def erode(src: Mat, kernel, dts: Mat = ..., anchor=..., iterations=..., borderType=..., borderValue=...) -> typing.Any:
    "erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) -> dst\n.   @brief Erodes an image by using a specific structuring element.\n.   \n.   The function erodes the source image using the specified structuring element that determines the\n.   shape of a pixel neighborhood over which the minimum is taken:\n.   \n.   \\f[\\texttt{dst} (x,y) =  \\min _{(x',y'):  \\, \\texttt{element} (x',y') \\ne0 } \\texttt{src} (x+x',y+y')\\f]\n.   \n.   The function supports the in-place mode. Erosion can be applied several ( iterations ) times. In\n.   case of multi-channel images, each channel is processed independently.\n.   \n.   @param src input image; the number of channels can be arbitrary, but the depth should be one of\n.   CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.\n.   @param dst output image of the same size and type as src.\n.   @param kernel structuring element used for erosion; if `element=Mat()`, a `3 x 3` rectangular\n.   structuring element is used. Kernel can be created using #getStructuringElement.\n.   @param anchor position of the anchor within the element; default value (-1, -1) means that the\n.   anchor is at the element center.\n.   @param iterations number of times erosion is applied.\n.   @param borderType pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not supported.\n.   @param borderValue border value in case of a constant border\n.   @sa  dilate, morphologyEx, getStructuringElement"
    ...

error = _mod_cv2.error
def estimateAffine2D(from_, to, inliers=..., method: int = ..., ransacReprojThreshold=..., maxIters=..., confidence=..., refineIters=...) -> typing.Any:
    'estimateAffine2D(from, to[, inliers[, method[, ransacReprojThreshold[, maxIters[, confidence[, refineIters]]]]]]) -> retval, inliers\n.   @brief Computes an optimal affine transformation between two 2D point sets.\n.   \n.   It computes\n.   \\f[\n.   \\begin{bmatrix}\n.   x\\\\\n.   y\\\\\n.   \\end{bmatrix}\n.   =\n.   \\begin{bmatrix}\n.   a_{11} & a_{12}\\\\\n.   a_{21} & a_{22}\\\\\n.   \\end{bmatrix}\n.   \\begin{bmatrix}\n.   X\\\\\n.   Y\\\\\n.   \\end{bmatrix}\n.   +\n.   \\begin{bmatrix}\n.   b_1\\\\\n.   b_2\\\\\n.   \\end{bmatrix}\n.   \\f]\n.   \n.   @param from First input 2D point set containing \\f$(X,Y)\\f$.\n.   @param to Second input 2D point set containing \\f$(x,y)\\f$.\n.   @param inliers Output vector indicating which points are inliers (1-inlier, 0-outlier).\n.   @param method Robust method used to compute transformation. The following methods are possible:\n.   -   cv::RANSAC - RANSAC-based robust method\n.   -   cv::LMEDS - Least-Median robust method\n.   RANSAC is the default method.\n.   @param ransacReprojThreshold Maximum reprojection error in the RANSAC algorithm to consider\n.   a point as an inlier. Applies only to RANSAC.\n.   @param maxIters The maximum number of robust method iterations.\n.   @param confidence Confidence level, between 0 and 1, for the estimated transformation. Anything\n.   between 0.95 and 0.99 is usually good enough. Values too close to 1 can slow down the estimation\n.   significantly. Values lower than 0.8-0.9 can result in an incorrectly estimated transformation.\n.   @param refineIters Maximum number of iterations of refining algorithm (Levenberg-Marquardt).\n.   Passing 0 will disable refining, so the output matrix will be output of robust method.\n.   \n.   @return Output 2D affine transformation matrix \\f$2 \\times 3\\f$ or empty matrix if transformation\n.   could not be estimated. The returned matrix has the following form:\n.   \\f[\n.   \\begin{bmatrix}\n.   a_{11} & a_{12} & b_1\\\\\n.   a_{21} & a_{22} & b_2\\\\\n.   \\end{bmatrix}\n.   \\f]\n.   \n.   The function estimates an optimal 2D affine transformation between two 2D point sets using the\n.   selected robust algorithm.\n.   \n.   The computed transformation is then refined further (using only inliers) with the\n.   Levenberg-Marquardt method to reduce the re-projection error even more.\n.   \n.   @note\n.   The RANSAC method can handle practically any ratio of outliers but needs a threshold to\n.   distinguish inliers from outliers. The method LMeDS does not need any threshold but it works\n.   correctly only when there are more than 50% of inliers.\n.   \n.   @sa estimateAffinePartial2D, getAffineTransform'
    ...

def estimateAffine3D(src: Mat, dts: Mat, out=..., inliers=..., ransacThreshold=..., confidence=...) -> typing.Any:
    'estimateAffine3D(src, dst[, out[, inliers[, ransacThreshold[, confidence]]]]) -> retval, out, inliers\n.   @brief Computes an optimal affine transformation between two 3D point sets.\n.   \n.   It computes\n.   \\f[\n.   \\begin{bmatrix}\n.   x\\\\\n.   y\\\\\n.   z\\\\\n.   \\end{bmatrix}\n.   =\n.   \\begin{bmatrix}\n.   a_{11} & a_{12} & a_{13}\\\\\n.   a_{21} & a_{22} & a_{23}\\\\\n.   a_{31} & a_{32} & a_{33}\\\\\n.   \\end{bmatrix}\n.   \\begin{bmatrix}\n.   X\\\\\n.   Y\\\\\n.   Z\\\\\n.   \\end{bmatrix}\n.   +\n.   \\begin{bmatrix}\n.   b_1\\\\\n.   b_2\\\\\n.   b_3\\\\\n.   \\end{bmatrix}\n.   \\f]\n.   \n.   @param src First input 3D point set containing \\f$(X,Y,Z)\\f$.\n.   @param dst Second input 3D point set containing \\f$(x,y,z)\\f$.\n.   @param out Output 3D affine transformation matrix \\f$3 \\times 4\\f$ of the form\n.   \\f[\n.   \\begin{bmatrix}\n.   a_{11} & a_{12} & a_{13} & b_1\\\\\n.   a_{21} & a_{22} & a_{23} & b_2\\\\\n.   a_{31} & a_{32} & a_{33} & b_3\\\\\n.   \\end{bmatrix}\n.   \\f]\n.   @param inliers Output vector indicating which points are inliers (1-inlier, 0-outlier).\n.   @param ransacThreshold Maximum reprojection error in the RANSAC algorithm to consider a point as\n.   an inlier.\n.   @param confidence Confidence level, between 0 and 1, for the estimated transformation. Anything\n.   between 0.95 and 0.99 is usually good enough. Values too close to 1 can slow down the estimation\n.   significantly. Values lower than 0.8-0.9 can result in an incorrectly estimated transformation.\n.   \n.   The function estimates an optimal 3D affine transformation between two 3D point sets using the\n.   RANSAC algorithm.'
    ...

def estimateAffinePartial2D(from_, to, inliers=..., method: int = ..., ransacReprojThreshold=..., maxIters=..., confidence=..., refineIters=...) -> typing.Any:
    'estimateAffinePartial2D(from, to[, inliers[, method[, ransacReprojThreshold[, maxIters[, confidence[, refineIters]]]]]]) -> retval, inliers\n.   @brief Computes an optimal limited affine transformation with 4 degrees of freedom between\n.   two 2D point sets.\n.   \n.   @param from First input 2D point set.\n.   @param to Second input 2D point set.\n.   @param inliers Output vector indicating which points are inliers.\n.   @param method Robust method used to compute transformation. The following methods are possible:\n.   -   cv::RANSAC - RANSAC-based robust method\n.   -   cv::LMEDS - Least-Median robust method\n.   RANSAC is the default method.\n.   @param ransacReprojThreshold Maximum reprojection error in the RANSAC algorithm to consider\n.   a point as an inlier. Applies only to RANSAC.\n.   @param maxIters The maximum number of robust method iterations.\n.   @param confidence Confidence level, between 0 and 1, for the estimated transformation. Anything\n.   between 0.95 and 0.99 is usually good enough. Values too close to 1 can slow down the estimation\n.   significantly. Values lower than 0.8-0.9 can result in an incorrectly estimated transformation.\n.   @param refineIters Maximum number of iterations of refining algorithm (Levenberg-Marquardt).\n.   Passing 0 will disable refining, so the output matrix will be output of robust method.\n.   \n.   @return Output 2D affine transformation (4 degrees of freedom) matrix \\f$2 \\times 3\\f$ or\n.   empty matrix if transformation could not be estimated.\n.   \n.   The function estimates an optimal 2D affine transformation with 4 degrees of freedom limited to\n.   combinations of translation, rotation, and uniform scaling. Uses the selected algorithm for robust\n.   estimation.\n.   \n.   The computed transformation is then refined further (using only inliers) with the\n.   Levenberg-Marquardt method to reduce the re-projection error even more.\n.   \n.   Estimated transformation matrix is:\n.   \\f[ \\begin{bmatrix} \\cos(\\theta) \\cdot s & -\\sin(\\theta) \\cdot s & t_x \\\\\n.                   \\sin(\\theta) \\cdot s & \\cos(\\theta) \\cdot s & t_y\n.   \\end{bmatrix} \\f]\n.   Where \\f$ \\theta \\f$ is the rotation angle, \\f$ s \\f$ the scaling factor and \\f$ t_x, t_y \\f$ are\n.   translations in \\f$ x, y \\f$ axes respectively.\n.   \n.   @note\n.   The RANSAC method can handle practically any ratio of outliers but need a threshold to\n.   distinguish inliers from outliers. The method LMeDS does not need any threshold but it works\n.   correctly only when there are more than 50% of inliers.\n.   \n.   @sa estimateAffine2D, getAffineTransform'
    ...

def estimateChessboardSharpness(image: Mat, patternSize, corners, rise_distance=..., vertical=..., sharpness=...) -> typing.Any:
    'estimateChessboardSharpness(image, patternSize, corners[, rise_distance[, vertical[, sharpness]]]) -> retval, sharpness\n.   @brief Estimates the sharpness of a detected chessboard.\n.   \n.   Image sharpness, as well as brightness, are a critical parameter for accuracte\n.   camera calibration. For accessing these parameters for filtering out\n.   problematic calibraiton images, this method calculates edge profiles by traveling from\n.   black to white chessboard cell centers. Based on this, the number of pixels is\n.   calculated required to transit from black to white. This width of the\n.   transition area is a good indication of how sharp the chessboard is imaged\n.   and should be below ~3.0 pixels.\n.   \n.   @param image Gray image used to find chessboard corners\n.   @param patternSize Size of a found chessboard pattern\n.   @param corners Corners found by findChessboardCorners(SB)\n.   @param rise_distance Rise distance 0.8 means 10% ... 90% of the final signal strength\n.   @param vertical By default edge responses for horizontal lines are calculated\n.   @param sharpness Optional output array with a sharpness value for calculated edge responses (see description)\n.   \n.   The optional sharpness array is of type CV_32FC1 and has for each calculated\n.   profile one row with the following five entries:\n.   * 0 = x coordinate of the underlying edge in the image\n.   * 1 = y coordinate of the underlying edge in the image\n.   * 2 = width of the transition area (sharpness)\n.   * 3 = signal strength in the black cell (min brightness)\n.   * 4 = signal strength in the white cell (max brightness)\n.   \n.   @return Scalar(average sharpness, average min brightness, average max brightness,0)'
    ...

def estimateTranslation3D(src: Mat, dts: Mat, out=..., inliers=..., ransacThreshold=..., confidence=...) -> typing.Any:
    'estimateTranslation3D(src, dst[, out[, inliers[, ransacThreshold[, confidence]]]]) -> retval, out, inliers\n.   @brief Computes an optimal translation between two 3D point sets.\n.    *\n.    * It computes\n.    * \\f[\n.    * \\begin{bmatrix}\n.    * x\\\\\n.    * y\\\\\n.    * z\\\\\n.    * \\end{bmatrix}\n.    * =\n.    * \\begin{bmatrix}\n.    * X\\\\\n.    * Y\\\\\n.    * Z\\\\\n.    * \\end{bmatrix}\n.    * +\n.    * \\begin{bmatrix}\n.    * b_1\\\\\n.    * b_2\\\\\n.    * b_3\\\\\n.    * \\end{bmatrix}\n.    * \\f]\n.    *\n.    * @param src First input 3D point set containing \\f$(X,Y,Z)\\f$.\n.    * @param dst Second input 3D point set containing \\f$(x,y,z)\\f$.\n.    * @param out Output 3D translation vector \\f$3 \\times 1\\f$ of the form\n.    * \\f[\n.    * \\begin{bmatrix}\n.    * b_1 \\\\\n.    * b_2 \\\\\n.    * b_3 \\\\\n.    * \\end{bmatrix}\n.    * \\f]\n.    * @param inliers Output vector indicating which points are inliers (1-inlier, 0-outlier).\n.    * @param ransacThreshold Maximum reprojection error in the RANSAC algorithm to consider a point as\n.    * an inlier.\n.    * @param confidence Confidence level, between 0 and 1, for the estimated transformation. Anything\n.    * between 0.95 and 0.99 is usually good enough. Values too close to 1 can slow down the estimation\n.    * significantly. Values lower than 0.8-0.9 can result in an incorrectly estimated transformation.\n.    *\n.    * The function estimates an optimal 3D translation between two 3D point sets using the\n.    * RANSAC algorithm.\n.   *'
    ...

def exp(src: Mat, dts: Mat = ...) -> typing.Any:
    'exp(src[, dst]) -> dst\n.   @brief Calculates the exponent of every array element.\n.   \n.   The function cv::exp calculates the exponent of every element of the input\n.   array:\n.   \\f[\\texttt{dst} [I] = e^{ src(I) }\\f]\n.   \n.   The maximum relative error is about 7e-6 for single-precision input and\n.   less than 1e-10 for double-precision input. Currently, the function\n.   converts denormalized values to zeros on output. Special values (NaN,\n.   Inf) are not handled.\n.   @param src input array.\n.   @param dst output array of the same size and type as src.\n.   @sa log , cartToPolar , polarToCart , phase , pow , sqrt , magnitude'
    ...

def extractChannel(src: Mat, coi, dts: Mat = ...) -> typing.Any:
    'extractChannel(src, coi[, dst]) -> dst\n.   @brief Extracts a single channel from src (coi is 0-based index)\n.   @param src input array\n.   @param dst output array\n.   @param coi index of channel to extract\n.   @sa mixChannels, split'
    ...

def fastAtan2(y, x) -> typing.Any:
    'fastAtan2(y, x) -> retval\n.   @brief Calculates the angle of a 2D vector in degrees.\n.   \n.    The function fastAtan2 calculates the full-range angle of an input 2D vector. The angle is measured\n.    in degrees and varies from 0 to 360 degrees. The accuracy is about 0.3 degrees.\n.    @param x x-coordinate of the vector.\n.    @param y y-coordinate of the vector.'
    ...

def fastNlMeansDenoising(src: Mat, dts: Mat = ..., h=..., templateWindowSize=..., searchWindowSize=...) -> typing.Any:
    'fastNlMeansDenoising(src[, dst[, h[, templateWindowSize[, searchWindowSize]]]]) -> dst\n.   @brief Perform image denoising using Non-local Means Denoising algorithm\n.   <http://www.ipol.im/pub/algo/bcm_non_local_means_denoising/> with several computational\n.   optimizations. Noise expected to be a gaussian white noise\n.   \n.   @param src Input 8-bit 1-channel, 2-channel, 3-channel or 4-channel image.\n.   @param dst Output image with the same size and type as src .\n.   @param templateWindowSize Size in pixels of the template patch that is used to compute weights.\n.   Should be odd. Recommended value 7 pixels\n.   @param searchWindowSize Size in pixels of the window that is used to compute weighted average for\n.   given pixel. Should be odd. Affect performance linearly: greater searchWindowsSize - greater\n.   denoising time. Recommended value 21 pixels\n.   @param h Parameter regulating filter strength. Big h value perfectly removes noise but also\n.   removes image details, smaller h value preserves details but also preserves some noise\n.   \n.   This function expected to be applied to grayscale images. For colored images look at\n.   fastNlMeansDenoisingColored. Advanced usage of this functions can be manual denoising of colored\n.   image in different colorspaces. Such approach is used in fastNlMeansDenoisingColored by converting\n.   image to CIELAB colorspace and then separately denoise L and AB components with different h\n.   parameter.\n\n\n\nfastNlMeansDenoising(src, h[, dst[, templateWindowSize[, searchWindowSize[, normType]]]]) -> dst\n.   @brief Perform image denoising using Non-local Means Denoising algorithm\n.   <http://www.ipol.im/pub/algo/bcm_non_local_means_denoising/> with several computational\n.   optimizations. Noise expected to be a gaussian white noise\n.   \n.   @param src Input 8-bit or 16-bit (only with NORM_L1) 1-channel,\n.   2-channel, 3-channel or 4-channel image.\n.   @param dst Output image with the same size and type as src .\n.   @param templateWindowSize Size in pixels of the template patch that is used to compute weights.\n.   Should be odd. Recommended value 7 pixels\n.   @param searchWindowSize Size in pixels of the window that is used to compute weighted average for\n.   given pixel. Should be odd. Affect performance linearly: greater searchWindowsSize - greater\n.   denoising time. Recommended value 21 pixels\n.   @param h Array of parameters regulating filter strength, either one\n.   parameter applied to all channels or one per channel in dst. Big h value\n.   perfectly removes noise but also removes image details, smaller h\n.   value preserves details but also preserves some noise\n.   @param normType Type of norm used for weight calculation. Can be either NORM_L2 or NORM_L1\n.   \n.   This function expected to be applied to grayscale images. For colored images look at\n.   fastNlMeansDenoisingColored. Advanced usage of this functions can be manual denoising of colored\n.   image in different colorspaces. Such approach is used in fastNlMeansDenoisingColored by converting\n.   image to CIELAB colorspace and then separately denoise L and AB components with different h\n.   parameter.'
    ...

def fastNlMeansDenoisingColored(src: Mat, dts: Mat = ..., h=..., hColor=..., templateWindowSize=..., searchWindowSize=...) -> typing.Any:
    'fastNlMeansDenoisingColored(src[, dst[, h[, hColor[, templateWindowSize[, searchWindowSize]]]]]) -> dst\n.   @brief Modification of fastNlMeansDenoising function for colored images\n.   \n.   @param src Input 8-bit 3-channel image.\n.   @param dst Output image with the same size and type as src .\n.   @param templateWindowSize Size in pixels of the template patch that is used to compute weights.\n.   Should be odd. Recommended value 7 pixels\n.   @param searchWindowSize Size in pixels of the window that is used to compute weighted average for\n.   given pixel. Should be odd. Affect performance linearly: greater searchWindowsSize - greater\n.   denoising time. Recommended value 21 pixels\n.   @param h Parameter regulating filter strength for luminance component. Bigger h value perfectly\n.   removes noise but also removes image details, smaller h value preserves details but also preserves\n.   some noise\n.   @param hColor The same as h but for color components. For most images value equals 10\n.   will be enough to remove colored noise and do not distort colors\n.   \n.   The function converts image to CIELAB colorspace and then separately denoise L and AB components\n.   with given h parameters using fastNlMeansDenoising function.'
    ...

def fastNlMeansDenoisingColoredMulti(srcImgs, imgToDenoiseIndex, temporalWindowSize, dts: Mat = ..., h=..., hColor=..., templateWindowSize=..., searchWindowSize=...) -> typing.Any:
    'fastNlMeansDenoisingColoredMulti(srcImgs, imgToDenoiseIndex, temporalWindowSize[, dst[, h[, hColor[, templateWindowSize[, searchWindowSize]]]]]) -> dst\n.   @brief Modification of fastNlMeansDenoisingMulti function for colored images sequences\n.   \n.   @param srcImgs Input 8-bit 3-channel images sequence. All images should have the same type and\n.   size.\n.   @param imgToDenoiseIndex Target image to denoise index in srcImgs sequence\n.   @param temporalWindowSize Number of surrounding images to use for target image denoising. Should\n.   be odd. Images from imgToDenoiseIndex - temporalWindowSize / 2 to\n.   imgToDenoiseIndex - temporalWindowSize / 2 from srcImgs will be used to denoise\n.   srcImgs[imgToDenoiseIndex] image.\n.   @param dst Output image with the same size and type as srcImgs images.\n.   @param templateWindowSize Size in pixels of the template patch that is used to compute weights.\n.   Should be odd. Recommended value 7 pixels\n.   @param searchWindowSize Size in pixels of the window that is used to compute weighted average for\n.   given pixel. Should be odd. Affect performance linearly: greater searchWindowsSize - greater\n.   denoising time. Recommended value 21 pixels\n.   @param h Parameter regulating filter strength for luminance component. Bigger h value perfectly\n.   removes noise but also removes image details, smaller h value preserves details but also preserves\n.   some noise.\n.   @param hColor The same as h but for color components.\n.   \n.   The function converts images to CIELAB colorspace and then separately denoise L and AB components\n.   with given h parameters using fastNlMeansDenoisingMulti function.'
    ...

def fastNlMeansDenoisingMulti(srcImgs, imgToDenoiseIndex, temporalWindowSize, dts: Mat = ..., h=..., templateWindowSize=..., searchWindowSize=...) -> typing.Any:
    'fastNlMeansDenoisingMulti(srcImgs, imgToDenoiseIndex, temporalWindowSize[, dst[, h[, templateWindowSize[, searchWindowSize]]]]) -> dst\n.   @brief Modification of fastNlMeansDenoising function for images sequence where consecutive images have been\n.   captured in small period of time. For example video. This version of the function is for grayscale\n.   images or for manual manipulation with colorspaces. For more details see\n.   <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.131.6394>\n.   \n.   @param srcImgs Input 8-bit 1-channel, 2-channel, 3-channel or\n.   4-channel images sequence. All images should have the same type and\n.   size.\n.   @param imgToDenoiseIndex Target image to denoise index in srcImgs sequence\n.   @param temporalWindowSize Number of surrounding images to use for target image denoising. Should\n.   be odd. Images from imgToDenoiseIndex - temporalWindowSize / 2 to\n.   imgToDenoiseIndex - temporalWindowSize / 2 from srcImgs will be used to denoise\n.   srcImgs[imgToDenoiseIndex] image.\n.   @param dst Output image with the same size and type as srcImgs images.\n.   @param templateWindowSize Size in pixels of the template patch that is used to compute weights.\n.   Should be odd. Recommended value 7 pixels\n.   @param searchWindowSize Size in pixels of the window that is used to compute weighted average for\n.   given pixel. Should be odd. Affect performance linearly: greater searchWindowsSize - greater\n.   denoising time. Recommended value 21 pixels\n.   @param h Parameter regulating filter strength. Bigger h value\n.   perfectly removes noise but also removes image details, smaller h\n.   value preserves details but also preserves some noise\n\n\n\nfastNlMeansDenoisingMulti(srcImgs, imgToDenoiseIndex, temporalWindowSize, h[, dst[, templateWindowSize[, searchWindowSize[, normType]]]]) -> dst\n.   @brief Modification of fastNlMeansDenoising function for images sequence where consecutive images have been\n.   captured in small period of time. For example video. This version of the function is for grayscale\n.   images or for manual manipulation with colorspaces. For more details see\n.   <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.131.6394>\n.   \n.   @param srcImgs Input 8-bit or 16-bit (only with NORM_L1) 1-channel,\n.   2-channel, 3-channel or 4-channel images sequence. All images should\n.   have the same type and size.\n.   @param imgToDenoiseIndex Target image to denoise index in srcImgs sequence\n.   @param temporalWindowSize Number of surrounding images to use for target image denoising. Should\n.   be odd. Images from imgToDenoiseIndex - temporalWindowSize / 2 to\n.   imgToDenoiseIndex - temporalWindowSize / 2 from srcImgs will be used to denoise\n.   srcImgs[imgToDenoiseIndex] image.\n.   @param dst Output image with the same size and type as srcImgs images.\n.   @param templateWindowSize Size in pixels of the template patch that is used to compute weights.\n.   Should be odd. Recommended value 7 pixels\n.   @param searchWindowSize Size in pixels of the window that is used to compute weighted average for\n.   given pixel. Should be odd. Affect performance linearly: greater searchWindowsSize - greater\n.   denoising time. Recommended value 21 pixels\n.   @param h Array of parameters regulating filter strength, either one\n.   parameter applied to all channels or one per channel in dst. Big h value\n.   perfectly removes noise but also removes image details, smaller h\n.   value preserves details but also preserves some noise\n.   @param normType Type of norm used for weight calculation. Can be either NORM_L2 or NORM_L1'
    ...

def fillConvexPoly(img: Mat, points, color, lineType=..., shift=...) -> typing.Any:
    'fillConvexPoly(img, points, color[, lineType[, shift]]) -> img\n.   @brief Fills a convex polygon.\n.   \n.   The function cv::fillConvexPoly draws a filled convex polygon. This function is much faster than the\n.   function #fillPoly . It can fill not only convex polygons but any monotonic polygon without\n.   self-intersections, that is, a polygon whose contour intersects every horizontal line (scan line)\n.   twice at the most (though, its top-most and/or the bottom edge could be horizontal).\n.   \n.   @param img Image.\n.   @param points Polygon vertices.\n.   @param color Polygon color.\n.   @param lineType Type of the polygon boundaries. See #LineTypes\n.   @param shift Number of fractional bits in the vertex coordinates.'
    ...

def fillPoly(img: Mat, pts, color, lineType=..., shift=..., offset=...) -> typing.Any:
    'fillPoly(img, pts, color[, lineType[, shift[, offset]]]) -> img\n.   @brief Fills the area bounded by one or more polygons.\n.   \n.   The function cv::fillPoly fills an area bounded by several polygonal contours. The function can fill\n.   complex areas, for example, areas with holes, contours with self-intersections (some of their\n.   parts), and so forth.\n.   \n.   @param img Image.\n.   @param pts Array of polygons where each polygon is represented as an array of points.\n.   @param color Polygon color.\n.   @param lineType Type of the polygon boundaries. See #LineTypes\n.   @param shift Number of fractional bits in the vertex coordinates.\n.   @param offset Optional offset of all points of the contours.'
    ...

def filter2D(src: Mat, ddepth, kernel, dts: Mat = ..., anchor=..., delta=..., borderType=...) -> typing.Any:
    'filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]) -> dst\n.   @brief Convolves an image with the kernel.\n.   \n.   The function applies an arbitrary linear filter to an image. In-place operation is supported. When\n.   the aperture is partially outside the image, the function interpolates outlier pixel values\n.   according to the specified border mode.\n.   \n.   The function does actually compute correlation, not the convolution:\n.   \n.   \\f[\\texttt{dst} (x,y) =  \\sum _{ \\substack{0\\leq x\' < \\texttt{kernel.cols}\\\\{0\\leq y\' < \\texttt{kernel.rows}}}}  \\texttt{kernel} (x\',y\')* \\texttt{src} (x+x\'- \\texttt{anchor.x} ,y+y\'- \\texttt{anchor.y} )\\f]\n.   \n.   That is, the kernel is not mirrored around the anchor point. If you need a real convolution, flip\n.   the kernel using #flip and set the new anchor to `(kernel.cols - anchor.x - 1, kernel.rows -\n.   anchor.y - 1)`.\n.   \n.   The function uses the DFT-based algorithm in case of sufficiently large kernels (~`11 x 11` or\n.   larger) and the direct algorithm for small kernels.\n.   \n.   @param src input image.\n.   @param dst output image of the same size and the same number of channels as src.\n.   @param ddepth desired depth of the destination image, see @ref filter_depths "combinations"\n.   @param kernel convolution kernel (or rather a correlation kernel), a single-channel floating point\n.   matrix; if you want to apply different kernels to different channels, split the image into\n.   separate color planes using split and process them individually.\n.   @param anchor anchor of the kernel that indicates the relative position of a filtered point within\n.   the kernel; the anchor should lie within the kernel; default value (-1,-1) means that the anchor\n.   is at the kernel center.\n.   @param delta optional value added to the filtered pixels before storing them in dst.\n.   @param borderType pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not supported.\n.   @sa  sepFilter2D, dft, matchTemplate'
    ...

def filterHomographyDecompByVisibleRefpoints(rotations, normals, beforePoints, afterPoints, possibleSolutions=..., pointsMask=...) -> typing.Any:
    'filterHomographyDecompByVisibleRefpoints(rotations, normals, beforePoints, afterPoints[, possibleSolutions[, pointsMask]]) -> possibleSolutions\n.   @brief Filters homography decompositions based on additional information.\n.   \n.   @param rotations Vector of rotation matrices.\n.   @param normals Vector of plane normal matrices.\n.   @param beforePoints Vector of (rectified) visible reference points before the homography is applied\n.   @param afterPoints Vector of (rectified) visible reference points after the homography is applied\n.   @param possibleSolutions Vector of int indices representing the viable solution set after filtering\n.   @param pointsMask optional Mat/Vector of 8u type representing the mask for the inliers as given by the findHomography function\n.   \n.   This function is intended to filter the output of the decomposeHomographyMat based on additional\n.   information as described in @cite Malis . The summary of the method: the decomposeHomographyMat function\n.   returns 2 unique solutions and their "opposites" for a total of 4 solutions. If we have access to the\n.   sets of points visible in the camera frame before and after the homography transformation is applied,\n.   we can determine which are the true potential solutions and which are the opposites by verifying which\n.   homographies are consistent with all visible reference points being in front of the camera. The inputs\n.   are left unchanged; the filtered solution set is returned as indices into the existing one.'
    ...

def filterSpeckles(img: Mat, newVal, maxSpeckleSize, maxDiff, buf=...) -> typing.Any:
    'filterSpeckles(img, newVal, maxSpeckleSize, maxDiff[, buf]) -> img, buf\n.   @brief Filters off small noise blobs (speckles) in the disparity map\n.   \n.   @param img The input 16-bit signed disparity image\n.   @param newVal The disparity value used to paint-off the speckles\n.   @param maxSpeckleSize The maximum speckle size to consider it a speckle. Larger blobs are not\n.   affected by the algorithm\n.   @param maxDiff Maximum difference between neighbor disparity pixels to put them into the same\n.   blob. Note that since StereoBM, StereoSGBM and may be other algorithms return a fixed-point\n.   disparity map, where disparity values are multiplied by 16, this scale factor should be taken into\n.   account when specifying this parameter value.\n.   @param buf The optional temporary buffer to avoid memory allocation within the function.'
    ...

def find4QuadCornerSubpix(img: Mat, corners, region_size) -> typing.Any:
    'find4QuadCornerSubpix(img, corners, region_size) -> retval, corners\n.'
    ...

def findChessboardCorners(image: Mat, patternSize, corners=..., flags: int = ...) -> typing.Any:
    'findChessboardCorners(image, patternSize[, corners[, flags]]) -> retval, corners\n.   @brief Finds the positions of internal corners of the chessboard.\n.   \n.   @param image Source chessboard view. It must be an 8-bit grayscale or color image.\n.   @param patternSize Number of inner corners per a chessboard row and column\n.   ( patternSize = cv::Size(points_per_row,points_per_colum) = cv::Size(columns,rows) ).\n.   @param corners Output array of detected corners.\n.   @param flags Various operation flags that can be zero or a combination of the following values:\n.   -   **CALIB_CB_ADAPTIVE_THRESH** Use adaptive thresholding to convert the image to black\n.   and white, rather than a fixed threshold level (computed from the average image brightness).\n.   -   **CALIB_CB_NORMALIZE_IMAGE** Normalize the image gamma with equalizeHist before\n.   applying fixed or adaptive thresholding.\n.   -   **CALIB_CB_FILTER_QUADS** Use additional criteria (like contour area, perimeter,\n.   square-like shape) to filter out false quads extracted at the contour retrieval stage.\n.   -   **CALIB_CB_FAST_CHECK** Run a fast check on the image that looks for chessboard corners,\n.   and shortcut the call if none is found. This can drastically speed up the call in the\n.   degenerate condition when no chessboard is observed.\n.   \n.   The function attempts to determine whether the input image is a view of the chessboard pattern and\n.   locate the internal chessboard corners. The function returns a non-zero value if all of the corners\n.   are found and they are placed in a certain order (row by row, left to right in every row).\n.   Otherwise, if the function fails to find all the corners or reorder them, it returns 0. For example,\n.   a regular chessboard has 8 x 8 squares and 7 x 7 internal corners, that is, points where the black\n.   squares touch each other. The detected coordinates are approximate, and to determine their positions\n.   more accurately, the function calls cornerSubPix. You also may use the function cornerSubPix with\n.   different parameters if returned coordinates are not accurate enough.\n.   \n.   Sample usage of detecting and drawing chessboard corners: :\n.   @code\n.       Size patternsize(8,6); //interior number of corners\n.       Mat gray = ....; //source image\n.       vector<Point2f> corners; //this will be filled by the detected corners\n.   \n.       //CALIB_CB_FAST_CHECK saves a lot of time on images\n.       //that do not contain any chessboard corners\n.       bool patternfound = findChessboardCorners(gray, patternsize, corners,\n.               CALIB_CB_ADAPTIVE_THRESH + CALIB_CB_NORMALIZE_IMAGE\n.               + CALIB_CB_FAST_CHECK);\n.   \n.       if(patternfound)\n.         cornerSubPix(gray, corners, Size(11, 11), Size(-1, -1),\n.           TermCriteria(CV_TERMCRIT_EPS + CV_TERMCRIT_ITER, 30, 0.1));\n.   \n.       drawChessboardCorners(img, patternsize, Mat(corners), patternfound);\n.   @endcode\n.   @note The function requires white space (like a square-thick border, the wider the better) around\n.   the board to make the detection more robust in various environments. Otherwise, if there is no\n.   border and the background is dark, the outer black squares cannot be segmented properly and so the\n.   square grouping and ordering algorithm fails.'
    ...

def findChessboardCornersSB(image: Mat, patternSize, corners=..., flags: int = ...) -> typing.Any:
    'findChessboardCornersSB(image, patternSize[, corners[, flags]]) -> retval, corners\n.   @overload'
    ...

def findChessboardCornersSBWithMeta(image: Mat, patternSize, flags: int, corners=..., meta=...) -> typing.Any:
    'findChessboardCornersSBWithMeta(image, patternSize, flags[, corners[, meta]]) -> retval, corners, meta\n.   @brief Finds the positions of internal corners of the chessboard using a sector based approach.\n.   \n.   @param image Source chessboard view. It must be an 8-bit grayscale or color image.\n.   @param patternSize Number of inner corners per a chessboard row and column\n.   ( patternSize = cv::Size(points_per_row,points_per_colum) = cv::Size(columns,rows) ).\n.   @param corners Output array of detected corners.\n.   @param flags Various operation flags that can be zero or a combination of the following values:\n.   -   **CALIB_CB_NORMALIZE_IMAGE** Normalize the image gamma with equalizeHist before detection.\n.   -   **CALIB_CB_EXHAUSTIVE** Run an exhaustive search to improve detection rate.\n.   -   **CALIB_CB_ACCURACY** Up sample input image to improve sub-pixel accuracy due to aliasing effects.\n.   -   **CALIB_CB_LARGER** The detected pattern is allowed to be larger than patternSize (see description).\n.   -   **CALIB_CB_MARKER** The detected pattern must have a marker (see description).\n.   This should be used if an accurate camera calibration is required.\n.   @param meta Optional output arrray of detected corners (CV_8UC1 and size = cv::Size(columns,rows)).\n.   Each entry stands for one corner of the pattern and can have one of the following values:\n.   -   0 = no meta data attached\n.   -   1 = left-top corner of a black cell\n.   -   2 = left-top corner of a white cell\n.   -   3 = left-top corner of a black cell with a white marker dot\n.   -   4 = left-top corner of a white cell with a black marker dot (pattern origin in case of markers otherwise first corner)\n.   \n.   The function is analog to findchessboardCorners but uses a localized radon\n.   transformation approximated by box filters being more robust to all sort of\n.   noise, faster on larger images and is able to directly return the sub-pixel\n.   position of the internal chessboard corners. The Method is based on the paper\n.   @cite duda2018 "Accurate Detection and Localization of Checkerboard Corners for\n.   Calibration" demonstrating that the returned sub-pixel positions are more\n.   accurate than the one returned by cornerSubPix allowing a precise camera\n.   calibration for demanding applications.\n.   \n.   In the case, the flags **CALIB_CB_LARGER** or **CALIB_CB_MARKER** are given,\n.   the result can be recovered from the optional meta array. Both flags are\n.   helpful to use calibration patterns exceeding the field of view of the camera.\n.   These oversized patterns allow more accurate calibrations as corners can be\n.   utilized, which are as close as possible to the image borders.  For a\n.   consistent coordinate system across all images, the optional marker (see image\n.   below) can be used to move the origin of the board to the location where the\n.   black circle is located.\n.   \n.   @note The function requires a white boarder with roughly the same width as one\n.   of the checkerboard fields around the whole board to improve the detection in\n.   various environments. In addition, because of the localized radon\n.   transformation it is beneficial to use round corners for the field corners\n.   which are located on the outside of the board. The following figure illustrates\n.   a sample checkerboard optimized for the detection. However, any other checkerboard\n.   can be used as well.\n.   ![Checkerboard](pics/checkerboard_radon.png)'
    ...

def findCirclesGrid(image: Mat, patternSize, flags: int, blobDetector, parameters, centers=...) -> typing.Any:
    'findCirclesGrid(image, patternSize, flags, blobDetector, parameters[, centers]) -> retval, centers\n.   @brief Finds centers in the grid of circles.\n.   \n.   @param image grid view of input circles; it must be an 8-bit grayscale or color image.\n.   @param patternSize number of circles per row and column\n.   ( patternSize = Size(points_per_row, points_per_colum) ).\n.   @param centers output array of detected centers.\n.   @param flags various operation flags that can be one of the following values:\n.   -   **CALIB_CB_SYMMETRIC_GRID** uses symmetric pattern of circles.\n.   -   **CALIB_CB_ASYMMETRIC_GRID** uses asymmetric pattern of circles.\n.   -   **CALIB_CB_CLUSTERING** uses a special algorithm for grid detection. It is more robust to\n.   perspective distortions but much more sensitive to background clutter.\n.   @param blobDetector feature detector that finds blobs like dark circles on light background.\n.   @param parameters struct for finding circles in a grid pattern.\n.   \n.   The function attempts to determine whether the input image contains a grid of circles. If it is, the\n.   function locates centers of the circles. The function returns a non-zero value if all of the centers\n.   have been found and they have been placed in a certain order (row by row, left to right in every\n.   row). Otherwise, if the function fails to find all the corners or reorder them, it returns 0.\n.   \n.   Sample usage of detecting and drawing the centers of circles: :\n.   @code\n.       Size patternsize(7,7); //number of centers\n.       Mat gray = ....; //source image\n.       vector<Point2f> centers; //this will be filled by the detected centers\n.   \n.       bool patternfound = findCirclesGrid(gray, patternsize, centers);\n.   \n.       drawChessboardCorners(img, patternsize, Mat(centers), patternfound);\n.   @endcode\n.   @note The function requires white space (like a square-thick border, the wider the better) around\n.   the board to make the detection more robust in various environments.\n\n\n\nfindCirclesGrid(image, patternSize[, centers[, flags[, blobDetector]]]) -> retval, centers\n.   @overload'
    ...

def findContours(image: Mat, mode, method: int, contours=..., hierarchy=..., offset=...) -> typing.Any:
    "findContours(image, mode, method[, contours[, hierarchy[, offset]]]) -> contours, hierarchy\n.   @brief Finds contours in a binary image.\n.   \n.   The function retrieves contours from the binary image using the algorithm @cite Suzuki85 . The contours\n.   are a useful tool for shape analysis and object detection and recognition. See squares.cpp in the\n.   OpenCV sample directory.\n.   @note Since opencv 3.2 source image is not modified by this function.\n.   \n.   @param image Source, an 8-bit single-channel image. Non-zero pixels are treated as 1's. Zero\n.   pixels remain 0's, so the image is treated as binary . You can use #compare, #inRange, #threshold ,\n.   #adaptiveThreshold, #Canny, and others to create a binary image out of a grayscale or color one.\n.   If mode equals to #RETR_CCOMP or #RETR_FLOODFILL, the input can also be a 32-bit integer image of labels (CV_32SC1).\n.   @param contours Detected contours. Each contour is stored as a vector of points (e.g.\n.   std::vector<std::vector<cv::Point> >).\n.   @param hierarchy Optional output vector (e.g. std::vector<cv::Vec4i>), containing information about the image topology. It has\n.   as many elements as the number of contours. For each i-th contour contours[i], the elements\n.   hierarchy[i][0] , hierarchy[i][1] , hierarchy[i][2] , and hierarchy[i][3] are set to 0-based indices\n.   in contours of the next and previous contours at the same hierarchical level, the first child\n.   contour and the parent contour, respectively. If for the contour i there are no next, previous,\n.   parent, or nested contours, the corresponding elements of hierarchy[i] will be negative.\n.   @param mode Contour retrieval mode, see #RetrievalModes\n.   @param method Contour approximation method, see #ContourApproximationModes\n.   @param offset Optional offset by which every contour point is shifted. This is useful if the\n.   contours are extracted from the image ROI and then they should be analyzed in the whole image\n.   context."
    ...

def findEssentialMat(points1, points2, cameraMatrix, method: int = ..., prob=..., threshold=..., mask: Mat = ...) -> typing.Any:
    'findEssentialMat(points1, points2, cameraMatrix[, method[, prob[, threshold[, mask]]]]) -> retval, mask\n.   @brief Calculates an essential matrix from the corresponding points in two images.\n.   \n.   @param points1 Array of N (N \\>= 5) 2D points from the first image. The point coordinates should\n.   be floating-point (single or double precision).\n.   @param points2 Array of the second image points of the same size and format as points1 .\n.   @param cameraMatrix Camera matrix \\f$K = \\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\\f$ .\n.   Note that this function assumes that points1 and points2 are feature points from cameras with the\n.   same camera matrix. If this assumption does not hold for your use case, use\n.   `undistortPoints()` with `P = cv::NoArray()` for both cameras to transform image points\n.   to normalized image coordinates, which are valid for the identity camera matrix. When\n.   passing these coordinates, pass the identity matrix for this parameter.\n.   @param method Method for computing an essential matrix.\n.   -   **RANSAC** for the RANSAC algorithm.\n.   -   **LMEDS** for the LMedS algorithm.\n.   @param prob Parameter used for the RANSAC or LMedS methods only. It specifies a desirable level of\n.   confidence (probability) that the estimated matrix is correct.\n.   @param threshold Parameter used for RANSAC. It is the maximum distance from a point to an epipolar\n.   line in pixels, beyond which the point is considered an outlier and is not used for computing the\n.   final fundamental matrix. It can be set to something like 1-3, depending on the accuracy of the\n.   point localization, image resolution, and the image noise.\n.   @param mask Output array of N elements, every element of which is set to 0 for outliers and to 1\n.   for the other points. The array is computed only in the RANSAC and LMedS methods.\n.   \n.   This function estimates essential matrix based on the five-point algorithm solver in @cite Nister03 .\n.   @cite SteweniusCFS is also a related. The epipolar geometry is described by the following equation:\n.   \n.   \\f[[p_2; 1]^T K^{-T} E K^{-1} [p_1; 1] = 0\\f]\n.   \n.   where \\f$E\\f$ is an essential matrix, \\f$p_1\\f$ and \\f$p_2\\f$ are corresponding points in the first and the\n.   second images, respectively. The result of this function may be passed further to\n.   decomposeEssentialMat or recoverPose to recover the relative pose between cameras.\n\n\n\nfindEssentialMat(points1, points2[, focal[, pp[, method[, prob[, threshold[, mask]]]]]]) -> retval, mask\n.   @overload\n.   @param points1 Array of N (N \\>= 5) 2D points from the first image. The point coordinates should\n.   be floating-point (single or double precision).\n.   @param points2 Array of the second image points of the same size and format as points1 .\n.   @param focal focal length of the camera. Note that this function assumes that points1 and points2\n.   are feature points from cameras with same focal length and principal point.\n.   @param pp principal point of the camera.\n.   @param method Method for computing a fundamental matrix.\n.   -   **RANSAC** for the RANSAC algorithm.\n.   -   **LMEDS** for the LMedS algorithm.\n.   @param threshold Parameter used for RANSAC. It is the maximum distance from a point to an epipolar\n.   line in pixels, beyond which the point is considered an outlier and is not used for computing the\n.   final fundamental matrix. It can be set to something like 1-3, depending on the accuracy of the\n.   point localization, image resolution, and the image noise.\n.   @param prob Parameter used for the RANSAC or LMedS methods only. It specifies a desirable level of\n.   confidence (probability) that the estimated matrix is correct.\n.   @param mask Output array of N elements, every element of which is set to 0 for outliers and to 1\n.   for the other points. The array is computed only in the RANSAC and LMedS methods.\n.   \n.   This function differs from the one above that it computes camera matrix from focal length and\n.   principal point:\n.   \n.   \\f[K =\n.   \\begin{bmatrix}\n.   f & 0 & x_{pp}  \\\\\n.   0 & f & y_{pp}  \\\\\n.   0 & 0 & 1\n.   \\end{bmatrix}\\f]'
    ...

def findFundamentalMat(points1, points2, method: int, ransacReprojThreshold, confidence, maxIters, mask: Mat = ...) -> typing.Any:
    'findFundamentalMat(points1, points2, method, ransacReprojThreshold, confidence, maxIters[, mask]) -> retval, mask\n.   @brief Calculates a fundamental matrix from the corresponding points in two images.\n.   \n.   @param points1 Array of N points from the first image. The point coordinates should be\n.   floating-point (single or double precision).\n.   @param points2 Array of the second image points of the same size and format as points1 .\n.   @param method Method for computing a fundamental matrix.\n.   -   **CV_FM_7POINT** for a 7-point algorithm. \\f$N = 7\\f$\n.   -   **CV_FM_8POINT** for an 8-point algorithm. \\f$N \\ge 8\\f$\n.   -   **CV_FM_RANSAC** for the RANSAC algorithm. \\f$N \\ge 8\\f$\n.   -   **CV_FM_LMEDS** for the LMedS algorithm. \\f$N \\ge 8\\f$\n.   @param ransacReprojThreshold Parameter used only for RANSAC. It is the maximum distance from a point to an epipolar\n.   line in pixels, beyond which the point is considered an outlier and is not used for computing the\n.   final fundamental matrix. It can be set to something like 1-3, depending on the accuracy of the\n.   point localization, image resolution, and the image noise.\n.   @param confidence Parameter used for the RANSAC and LMedS methods only. It specifies a desirable level\n.   of confidence (probability) that the estimated matrix is correct.\n.   @param mask\n.   @param maxIters The maximum number of robust method iterations.\n.   \n.   The epipolar geometry is described by the following equation:\n.   \n.   \\f[[p_2; 1]^T F [p_1; 1] = 0\\f]\n.   \n.   where \\f$F\\f$ is a fundamental matrix, \\f$p_1\\f$ and \\f$p_2\\f$ are corresponding points in the first and the\n.   second images, respectively.\n.   \n.   The function calculates the fundamental matrix using one of four methods listed above and returns\n.   the found fundamental matrix. Normally just one matrix is found. But in case of the 7-point\n.   algorithm, the function may return up to 3 solutions ( \\f$9 \\times 3\\f$ matrix that stores all 3\n.   matrices sequentially).\n.   \n.   The calculated fundamental matrix may be passed further to computeCorrespondEpilines that finds the\n.   epipolar lines corresponding to the specified points. It can also be passed to\n.   stereoRectifyUncalibrated to compute the rectification transformation. :\n.   @code\n.       // Example. Estimation of fundamental matrix using the RANSAC algorithm\n.       int point_count = 100;\n.       vector<Point2f> points1(point_count);\n.       vector<Point2f> points2(point_count);\n.   \n.       // initialize the points here ...\n.       for( int i = 0; i < point_count; i++ )\n.       {\n.           points1[i] = ...;\n.           points2[i] = ...;\n.       }\n.   \n.       Mat fundamental_matrix =\n.        findFundamentalMat(points1, points2, FM_RANSAC, 3, 0.99);\n.   @endcode\n\n\n\nfindFundamentalMat(points1, points2[, method[, ransacReprojThreshold[, confidence[, mask]]]]) -> retval, mask\n.   @overload'
    ...

def findHomography(srcPoints, dstPoints, method: int = ..., ransacReprojThreshold=..., mask: Mat = ..., maxIters=..., confidence=...) -> typing.Any:
    "findHomography(srcPoints, dstPoints[, method[, ransacReprojThreshold[, mask[, maxIters[, confidence]]]]]) -> retval, mask\n.   @brief Finds a perspective transformation between two planes.\n.   \n.   @param srcPoints Coordinates of the points in the original plane, a matrix of the type CV_32FC2\n.   or vector\\<Point2f\\> .\n.   @param dstPoints Coordinates of the points in the target plane, a matrix of the type CV_32FC2 or\n.   a vector\\<Point2f\\> .\n.   @param method Method used to compute a homography matrix. The following methods are possible:\n.   -   **0** - a regular method using all the points, i.e., the least squares method\n.   -   **RANSAC** - RANSAC-based robust method\n.   -   **LMEDS** - Least-Median robust method\n.   -   **RHO** - PROSAC-based robust method\n.   @param ransacReprojThreshold Maximum allowed reprojection error to treat a point pair as an inlier\n.   (used in the RANSAC and RHO methods only). That is, if\n.   \\f[\\| \\texttt{dstPoints} _i -  \\texttt{convertPointsHomogeneous} ( \\texttt{H} * \\texttt{srcPoints} _i) \\|_2  >  \\texttt{ransacReprojThreshold}\\f]\n.   then the point \\f$i\\f$ is considered as an outlier. If srcPoints and dstPoints are measured in pixels,\n.   it usually makes sense to set this parameter somewhere in the range of 1 to 10.\n.   @param mask Optional output mask set by a robust method ( RANSAC or LMEDS ). Note that the input\n.   mask values are ignored.\n.   @param maxIters The maximum number of RANSAC iterations.\n.   @param confidence Confidence level, between 0 and 1.\n.   \n.   The function finds and returns the perspective transformation \\f$H\\f$ between the source and the\n.   destination planes:\n.   \n.   \\f[s_i  \\vecthree{x'_i}{y'_i}{1} \\sim H  \\vecthree{x_i}{y_i}{1}\\f]\n.   \n.   so that the back-projection error\n.   \n.   \\f[\\sum _i \\left ( x'_i- \\frac{h_{11} x_i + h_{12} y_i + h_{13}}{h_{31} x_i + h_{32} y_i + h_{33}} \\right )^2+ \\left ( y'_i- \\frac{h_{21} x_i + h_{22} y_i + h_{23}}{h_{31} x_i + h_{32} y_i + h_{33}} \\right )^2\\f]\n.   \n.   is minimized. If the parameter method is set to the default value 0, the function uses all the point\n.   pairs to compute an initial homography estimate with a simple least-squares scheme.\n.   \n.   However, if not all of the point pairs ( \\f$srcPoints_i\\f$, \\f$dstPoints_i\\f$ ) fit the rigid perspective\n.   transformation (that is, there are some outliers), this initial estimate will be poor. In this case,\n.   you can use one of the three robust methods. The methods RANSAC, LMeDS and RHO try many different\n.   random subsets of the corresponding point pairs (of four pairs each, collinear pairs are discarded), estimate the homography matrix\n.   using this subset and a simple least-squares algorithm, and then compute the quality/goodness of the\n.   computed homography (which is the number of inliers for RANSAC or the least median re-projection error for\n.   LMeDS). The best subset is then used to produce the initial estimate of the homography matrix and\n.   the mask of inliers/outliers.\n.   \n.   Regardless of the method, robust or not, the computed homography matrix is refined further (using\n.   inliers only in case of a robust method) with the Levenberg-Marquardt method to reduce the\n.   re-projection error even more.\n.   \n.   The methods RANSAC and RHO can handle practically any ratio of outliers but need a threshold to\n.   distinguish inliers from outliers. The method LMeDS does not need any threshold but it works\n.   correctly only when there are more than 50% of inliers. Finally, if there are no outliers and the\n.   noise is rather small, use the default method (method=0).\n.   \n.   The function is used to find initial intrinsic and extrinsic matrices. Homography matrix is\n.   determined up to a scale. Thus, it is normalized so that \\f$h_{33}=1\\f$. Note that whenever an \\f$H\\f$ matrix\n.   cannot be estimated, an empty one will be returned.\n.   \n.   @sa\n.   getAffineTransform, estimateAffine2D, estimateAffinePartial2D, getPerspectiveTransform, warpPerspective,\n.   perspectiveTransform"
    ...

def findNonZero(src: Mat, idx=...) -> typing.Any:
    'findNonZero(src[, idx]) -> idx\n.   @brief Returns the list of locations of non-zero pixels\n.   \n.   Given a binary matrix (likely returned from an operation such\n.   as threshold(), compare(), >, ==, etc, return all of\n.   the non-zero indices as a cv::Mat or std::vector<cv::Point> (x,y)\n.   For example:\n.   @code{.cpp}\n.       cv::Mat binaryImage; // input, binary image\n.       cv::Mat locations;   // output, locations of non-zero pixels\n.       cv::findNonZero(binaryImage, locations);\n.   \n.       // access pixel coordinates\n.       Point pnt = locations.at<Point>(i);\n.   @endcode\n.   or\n.   @code{.cpp}\n.       cv::Mat binaryImage; // input, binary image\n.       vector<Point> locations;   // output, locations of non-zero pixels\n.       cv::findNonZero(binaryImage, locations);\n.   \n.       // access pixel coordinates\n.       Point pnt = locations[i];\n.   @endcode\n.   @param src single-channel array\n.   @param idx the output array, type of cv::Mat or std::vector<Point>, corresponding to non-zero indices in the input'
    ...

def findTransformECC(templateImage, inputImage, warpMatrix, motionType, criteria, inputMask, gaussFiltSize) -> typing.Any:
    "findTransformECC(templateImage, inputImage, warpMatrix, motionType, criteria, inputMask, gaussFiltSize) -> retval, warpMatrix\n.   @brief Finds the geometric transform (warp) between two images in terms of the ECC criterion @cite EP08 .\n.   \n.   @param templateImage single-channel template image; CV_8U or CV_32F array.\n.   @param inputImage single-channel input image which should be warped with the final warpMatrix in\n.   order to provide an image similar to templateImage, same type as templateImage.\n.   @param warpMatrix floating-point \\f$2\\times 3\\f$ or \\f$3\\times 3\\f$ mapping matrix (warp).\n.   @param motionType parameter, specifying the type of motion:\n.    -   **MOTION_TRANSLATION** sets a translational motion model; warpMatrix is \\f$2\\times 3\\f$ with\n.        the first \\f$2\\times 2\\f$ part being the unity matrix and the rest two parameters being\n.        estimated.\n.    -   **MOTION_EUCLIDEAN** sets a Euclidean (rigid) transformation as motion model; three\n.        parameters are estimated; warpMatrix is \\f$2\\times 3\\f$.\n.    -   **MOTION_AFFINE** sets an affine motion model (DEFAULT); six parameters are estimated;\n.        warpMatrix is \\f$2\\times 3\\f$.\n.    -   **MOTION_HOMOGRAPHY** sets a homography as a motion model; eight parameters are\n.        estimated;\\`warpMatrix\\` is \\f$3\\times 3\\f$.\n.   @param criteria parameter, specifying the termination criteria of the ECC algorithm;\n.   criteria.epsilon defines the threshold of the increment in the correlation coefficient between two\n.   iterations (a negative criteria.epsilon makes criteria.maxcount the only termination criterion).\n.   Default values are shown in the declaration above.\n.   @param inputMask An optional mask to indicate valid values of inputImage.\n.   @param gaussFiltSize An optional value indicating size of gaussian blur filter; (DEFAULT: 5)\n.   \n.   The function estimates the optimum transformation (warpMatrix) with respect to ECC criterion\n.   (@cite EP08), that is\n.   \n.   \\f[\\texttt{warpMatrix} = \\arg\\max_{W} \\texttt{ECC}(\\texttt{templateImage}(x,y),\\texttt{inputImage}(x',y'))\\f]\n.   \n.   where\n.   \n.   \\f[\\begin{bmatrix} x' \\\\ y' \\end{bmatrix} = W \\cdot \\begin{bmatrix} x \\\\ y \\\\ 1 \\end{bmatrix}\\f]\n.   \n.   (the equation holds with homogeneous coordinates for homography). It returns the final enhanced\n.   correlation coefficient, that is the correlation coefficient between the template image and the\n.   final warped input image. When a \\f$3\\times 3\\f$ matrix is given with motionType =0, 1 or 2, the third\n.   row is ignored.\n.   \n.   Unlike findHomography and estimateRigidTransform, the function findTransformECC implements an\n.   area-based alignment that builds on intensity similarities. In essence, the function updates the\n.   initial transformation that roughly aligns the images. If this information is missing, the identity\n.   warp (unity matrix) is used as an initialization. Note that if images undergo strong\n.   displacements/rotations, an initial transformation that roughly aligns the images is necessary\n.   (e.g., a simple euclidean/similarity transform that allows for the images showing the same image\n.   content approximately). Use inverse warping in the second image to take an image close to the first\n.   one, i.e. use the flag WARP_INVERSE_MAP with warpAffine or warpPerspective. See also the OpenCV\n.   sample image_alignment.cpp that demonstrates the use of the function. Note that the function throws\n.   an exception if algorithm does not converges.\n.   \n.   @sa\n.   computeECC, estimateAffine2D, estimateAffinePartial2D, findHomography"
    ...

def fitEllipse(points) -> typing.Any:
    'fitEllipse(points) -> retval\n.   @brief Fits an ellipse around a set of 2D points.\n.   \n.   The function calculates the ellipse that fits (in a least-squares sense) a set of 2D points best of\n.   all. It returns the rotated rectangle in which the ellipse is inscribed. The first algorithm described by @cite Fitzgibbon95\n.   is used. Developer should keep in mind that it is possible that the returned\n.   ellipse/rotatedRect data contains negative indices, due to the data points being close to the\n.   border of the containing Mat element.\n.   \n.   @param points Input 2D point set, stored in std::vector\\<\\> or Mat'
    ...

def fitEllipseAMS(points) -> typing.Any:
    'fitEllipseAMS(points) -> retval\n.   @brief Fits an ellipse around a set of 2D points.\n.   \n.    The function calculates the ellipse that fits a set of 2D points.\n.    It returns the rotated rectangle in which the ellipse is inscribed.\n.    The Approximate Mean Square (AMS) proposed by @cite Taubin1991 is used.\n.   \n.    For an ellipse, this basis set is \\f$ \\chi= \\left(x^2, x y, y^2, x, y, 1\\right) \\f$,\n.    which is a set of six free coefficients \\f$ A^T=\\left\\{A_{\\text{xx}},A_{\\text{xy}},A_{\\text{yy}},A_x,A_y,A_0\\right\\} \\f$.\n.    However, to specify an ellipse, all that is needed is five numbers; the major and minor axes lengths \\f$ (a,b) \\f$,\n.    the position \\f$ (x_0,y_0) \\f$, and the orientation \\f$ \\theta \\f$. This is because the basis set includes lines,\n.    quadratics, parabolic and hyperbolic functions as well as elliptical functions as possible fits.\n.    If the fit is found to be a parabolic or hyperbolic function then the standard #fitEllipse method is used.\n.    The AMS method restricts the fit to parabolic, hyperbolic and elliptical curves\n.    by imposing the condition that \\f$ A^T ( D_x^T D_x  +   D_y^T D_y) A = 1 \\f$ where\n.    the matrices \\f$ Dx \\f$ and \\f$ Dy \\f$ are the partial derivatives of the design matrix \\f$ D \\f$ with\n.    respect to x and y. The matrices are formed row by row applying the following to\n.    each of the points in the set:\n.    \\f{align*}{\n.    D(i,:)&=\\left\\{x_i^2, x_i y_i, y_i^2, x_i, y_i, 1\\right\\} &\n.    D_x(i,:)&=\\left\\{2 x_i,y_i,0,1,0,0\\right\\} &\n.    D_y(i,:)&=\\left\\{0,x_i,2 y_i,0,1,0\\right\\}\n.    \\f}\n.    The AMS method minimizes the cost function\n.    \\f{equation*}{\n.    \\epsilon ^2=\\frac{ A^T D^T D A }{ A^T (D_x^T D_x +  D_y^T D_y) A^T }\n.    \\f}\n.   \n.    The minimum cost is found by solving the generalized eigenvalue problem.\n.   \n.    \\f{equation*}{\n.    D^T D A = \\lambda  \\left( D_x^T D_x +  D_y^T D_y\\right) A\n.    \\f}\n.   \n.    @param points Input 2D point set, stored in std::vector\\<\\> or Mat'
    ...

def fitEllipseDirect(points) -> typing.Any:
    'fitEllipseDirect(points) -> retval\n.   @brief Fits an ellipse around a set of 2D points.\n.   \n.    The function calculates the ellipse that fits a set of 2D points.\n.    It returns the rotated rectangle in which the ellipse is inscribed.\n.    The Direct least square (Direct) method by @cite Fitzgibbon1999 is used.\n.   \n.    For an ellipse, this basis set is \\f$ \\chi= \\left(x^2, x y, y^2, x, y, 1\\right) \\f$,\n.    which is a set of six free coefficients \\f$ A^T=\\left\\{A_{\\text{xx}},A_{\\text{xy}},A_{\\text{yy}},A_x,A_y,A_0\\right\\} \\f$.\n.    However, to specify an ellipse, all that is needed is five numbers; the major and minor axes lengths \\f$ (a,b) \\f$,\n.    the position \\f$ (x_0,y_0) \\f$, and the orientation \\f$ \\theta \\f$. This is because the basis set includes lines,\n.    quadratics, parabolic and hyperbolic functions as well as elliptical functions as possible fits.\n.    The Direct method confines the fit to ellipses by ensuring that \\f$ 4 A_{xx} A_{yy}- A_{xy}^2 > 0 \\f$.\n.    The condition imposed is that \\f$ 4 A_{xx} A_{yy}- A_{xy}^2=1 \\f$ which satisfies the inequality\n.    and as the coefficients can be arbitrarily scaled is not overly restrictive.\n.   \n.    \\f{equation*}{\n.    \\epsilon ^2= A^T D^T D A \\quad \\text{with} \\quad A^T C A =1 \\quad \\text{and} \\quad C=\\left(\\begin{matrix}\n.    0 & 0  & 2  & 0  & 0  &  0  \\\\\n.    0 & -1  & 0  & 0  & 0  &  0 \\\\\n.    2 & 0  & 0  & 0  & 0  &  0 \\\\\n.    0 & 0  & 0  & 0  & 0  &  0 \\\\\n.    0 & 0  & 0  & 0  & 0  &  0 \\\\\n.    0 & 0  & 0  & 0  & 0  &  0\n.    \\end{matrix} \\right)\n.    \\f}\n.   \n.    The minimum cost is found by solving the generalized eigenvalue problem.\n.   \n.    \\f{equation*}{\n.    D^T D A = \\lambda  \\left( C\\right) A\n.    \\f}\n.   \n.    The system produces only one positive eigenvalue \\f$ \\lambda\\f$ which is chosen as the solution\n.    with its eigenvector \\f$\\mathbf{u}\\f$. These are used to find the coefficients\n.   \n.    \\f{equation*}{\n.    A = \\sqrt{\\frac{1}{\\mathbf{u}^T C \\mathbf{u}}}  \\mathbf{u}\n.    \\f}\n.    The scaling factor guarantees that  \\f$A^T C A =1\\f$.\n.   \n.    @param points Input 2D point set, stored in std::vector\\<\\> or Mat'
    ...

def fitLine(points, distType, param, reps, aeps, line=...) -> typing.Any:
    'fitLine(points, distType, param, reps, aeps[, line]) -> line\n.   @brief Fits a line to a 2D or 3D point set.\n.   \n.   The function fitLine fits a line to a 2D or 3D point set by minimizing \\f$\\sum_i \\rho(r_i)\\f$ where\n.   \\f$r_i\\f$ is a distance between the \\f$i^{th}\\f$ point, the line and \\f$\\rho(r)\\f$ is a distance function, one\n.   of the following:\n.   -  DIST_L2\n.   \\f[\\rho (r) = r^2/2  \\quad \\text{(the simplest and the fastest least-squares method)}\\f]\n.   - DIST_L1\n.   \\f[\\rho (r) = r\\f]\n.   - DIST_L12\n.   \\f[\\rho (r) = 2  \\cdot ( \\sqrt{1 + \\frac{r^2}{2}} - 1)\\f]\n.   - DIST_FAIR\n.   \\f[\\rho \\left (r \\right ) = C^2  \\cdot \\left (  \\frac{r}{C} -  \\log{\\left(1 + \\frac{r}{C}\\right)} \\right )  \\quad \\text{where} \\quad C=1.3998\\f]\n.   - DIST_WELSCH\n.   \\f[\\rho \\left (r \\right ) =  \\frac{C^2}{2} \\cdot \\left ( 1 -  \\exp{\\left(-\\left(\\frac{r}{C}\\right)^2\\right)} \\right )  \\quad \\text{where} \\quad C=2.9846\\f]\n.   - DIST_HUBER\n.   \\f[\\rho (r) =  \\fork{r^2/2}{if \\(r < C\\)}{C \\cdot (r-C/2)}{otherwise} \\quad \\text{where} \\quad C=1.345\\f]\n.   \n.   The algorithm is based on the M-estimator ( <http://en.wikipedia.org/wiki/M-estimator> ) technique\n.   that iteratively fits the line using the weighted least-squares algorithm. After each iteration the\n.   weights \\f$w_i\\f$ are adjusted to be inversely proportional to \\f$\\rho(r_i)\\f$ .\n.   \n.   @param points Input vector of 2D or 3D points, stored in std::vector\\<\\> or Mat.\n.   @param line Output line parameters. In case of 2D fitting, it should be a vector of 4 elements\n.   (like Vec4f) - (vx, vy, x0, y0), where (vx, vy) is a normalized vector collinear to the line and\n.   (x0, y0) is a point on the line. In case of 3D fitting, it should be a vector of 6 elements (like\n.   Vec6f) - (vx, vy, vz, x0, y0, z0), where (vx, vy, vz) is a normalized vector collinear to the line\n.   and (x0, y0, z0) is a point on the line.\n.   @param distType Distance used by the M-estimator, see #DistanceTypes\n.   @param param Numerical parameter ( C ) for some types of distances. If it is 0, an optimal value\n.   is chosen.\n.   @param reps Sufficient accuracy for the radius (distance between the coordinate origin and the line).\n.   @param aeps Sufficient accuracy for the angle. 0.01 would be a good default value for reps and aeps.'
    ...

flann_Index = _mod_cv2.flann_Index
def flip(src: Mat, flipCode, dts: Mat = ...) -> typing.Any:
    'flip(src, flipCode[, dst]) -> dst\n.   @brief Flips a 2D array around vertical, horizontal, or both axes.\n.   \n.   The function cv::flip flips the array in one of three different ways (row\n.   and column indices are 0-based):\n.   \\f[\\texttt{dst} _{ij} =\n.   \\left\\{\n.   \\begin{array}{l l}\n.   \\texttt{src} _{\\texttt{src.rows}-i-1,j} & if\\;  \\texttt{flipCode} = 0 \\\\\n.   \\texttt{src} _{i, \\texttt{src.cols} -j-1} & if\\;  \\texttt{flipCode} > 0 \\\\\n.   \\texttt{src} _{ \\texttt{src.rows} -i-1, \\texttt{src.cols} -j-1} & if\\; \\texttt{flipCode} < 0 \\\\\n.   \\end{array}\n.   \\right.\\f]\n.   The example scenarios of using the function are the following:\n.   *   Vertical flipping of the image (flipCode == 0) to switch between\n.       top-left and bottom-left image origin. This is a typical operation\n.       in video processing on Microsoft Windows\\* OS.\n.   *   Horizontal flipping of the image with the subsequent horizontal\n.       shift and absolute difference calculation to check for a\n.       vertical-axis symmetry (flipCode \\> 0).\n.   *   Simultaneous horizontal and vertical flipping of the image with\n.       the subsequent shift and absolute difference calculation to check\n.       for a central symmetry (flipCode \\< 0).\n.   *   Reversing the order of point arrays (flipCode \\> 0 or\n.       flipCode == 0).\n.   @param src input array.\n.   @param dst output array of the same size and type as src.\n.   @param flipCode a flag to specify how to flip the array; 0 means\n.   flipping around the x-axis and positive value (for example, 1) means\n.   flipping around y-axis. Negative value (for example, -1) means flipping\n.   around both axes.\n.   @sa transpose , repeat , completeSymm'
    ...

def floodFill(image: Mat, mask: typing.Optional[Mat], seedPoint, newVal, loDiff=..., upDiff=..., flags: int = ...) -> typing.Any:
    "floodFill(image, mask, seedPoint, newVal[, loDiff[, upDiff[, flags]]]) -> retval, image, mask, rect\n.   @brief Fills a connected component with the given color.\n.   \n.   The function cv::floodFill fills a connected component starting from the seed point with the specified\n.   color. The connectivity is determined by the color/brightness closeness of the neighbor pixels. The\n.   pixel at \\f$(x,y)\\f$ is considered to belong to the repainted domain if:\n.   \n.   - in case of a grayscale image and floating range\n.   \\f[\\texttt{src} (x',y')- \\texttt{loDiff} \\leq \\texttt{src} (x,y)  \\leq \\texttt{src} (x',y')+ \\texttt{upDiff}\\f]\n.   \n.   \n.   - in case of a grayscale image and fixed range\n.   \\f[\\texttt{src} ( \\texttt{seedPoint} .x, \\texttt{seedPoint} .y)- \\texttt{loDiff} \\leq \\texttt{src} (x,y)  \\leq \\texttt{src} ( \\texttt{seedPoint} .x, \\texttt{seedPoint} .y)+ \\texttt{upDiff}\\f]\n.   \n.   \n.   - in case of a color image and floating range\n.   \\f[\\texttt{src} (x',y')_r- \\texttt{loDiff} _r \\leq \\texttt{src} (x,y)_r \\leq \\texttt{src} (x',y')_r+ \\texttt{upDiff} _r,\\f]\n.   \\f[\\texttt{src} (x',y')_g- \\texttt{loDiff} _g \\leq \\texttt{src} (x,y)_g \\leq \\texttt{src} (x',y')_g+ \\texttt{upDiff} _g\\f]\n.   and\n.   \\f[\\texttt{src} (x',y')_b- \\texttt{loDiff} _b \\leq \\texttt{src} (x,y)_b \\leq \\texttt{src} (x',y')_b+ \\texttt{upDiff} _b\\f]\n.   \n.   \n.   - in case of a color image and fixed range\n.   \\f[\\texttt{src} ( \\texttt{seedPoint} .x, \\texttt{seedPoint} .y)_r- \\texttt{loDiff} _r \\leq \\texttt{src} (x,y)_r \\leq \\texttt{src} ( \\texttt{seedPoint} .x, \\texttt{seedPoint} .y)_r+ \\texttt{upDiff} _r,\\f]\n.   \\f[\\texttt{src} ( \\texttt{seedPoint} .x, \\texttt{seedPoint} .y)_g- \\texttt{loDiff} _g \\leq \\texttt{src} (x,y)_g \\leq \\texttt{src} ( \\texttt{seedPoint} .x, \\texttt{seedPoint} .y)_g+ \\texttt{upDiff} _g\\f]\n.   and\n.   \\f[\\texttt{src} ( \\texttt{seedPoint} .x, \\texttt{seedPoint} .y)_b- \\texttt{loDiff} _b \\leq \\texttt{src} (x,y)_b \\leq \\texttt{src} ( \\texttt{seedPoint} .x, \\texttt{seedPoint} .y)_b+ \\texttt{upDiff} _b\\f]\n.   \n.   \n.   where \\f$src(x',y')\\f$ is the value of one of pixel neighbors that is already known to belong to the\n.   component. That is, to be added to the connected component, a color/brightness of the pixel should\n.   be close enough to:\n.   - Color/brightness of one of its neighbors that already belong to the connected component in case\n.   of a floating range.\n.   - Color/brightness of the seed point in case of a fixed range.\n.   \n.   Use these functions to either mark a connected component with the specified color in-place, or build\n.   a mask and then extract the contour, or copy the region to another image, and so on.\n.   \n.   @param image Input/output 1- or 3-channel, 8-bit, or floating-point image. It is modified by the\n.   function unless the #FLOODFILL_MASK_ONLY flag is set in the second variant of the function. See\n.   the details below.\n.   @param mask Operation mask that should be a single-channel 8-bit image, 2 pixels wider and 2 pixels\n.   taller than image. Since this is both an input and output parameter, you must take responsibility\n.   of initializing it. Flood-filling cannot go across non-zero pixels in the input mask. For example,\n.   an edge detector output can be used as a mask to stop filling at edges. On output, pixels in the\n.   mask corresponding to filled pixels in the image are set to 1 or to the a value specified in flags\n.   as described below. Additionally, the function fills the border of the mask with ones to simplify\n.   internal processing. It is therefore possible to use the same mask in multiple calls to the function\n.   to make sure the filled areas do not overlap.\n.   @param seedPoint Starting point.\n.   @param newVal New value of the repainted domain pixels.\n.   @param loDiff Maximal lower brightness/color difference between the currently observed pixel and\n.   one of its neighbors belonging to the component, or a seed pixel being added to the component.\n.   @param upDiff Maximal upper brightness/color difference between the currently observed pixel and\n.   one of its neighbors belonging to the component, or a seed pixel being added to the component.\n.   @param rect Optional output parameter set by the function to the minimum bounding rectangle of the\n.   repainted domain.\n.   @param flags Operation flags. The first 8 bits contain a connectivity value. The default value of\n.   4 means that only the four nearest neighbor pixels (those that share an edge) are considered. A\n.   connectivity value of 8 means that the eight nearest neighbor pixels (those that share a corner)\n.   will be considered. The next 8 bits (8-16) contain a value between 1 and 255 with which to fill\n.   the mask (the default value is 1). For example, 4 | ( 255 \\<\\< 8 ) will consider 4 nearest\n.   neighbours and fill the mask with a value of 255. The following additional options occupy higher\n.   bits and therefore may be further combined with the connectivity and mask fill values using\n.   bit-wise or (|), see #FloodFillFlags.\n.   \n.   @note Since the mask is larger than the filled image, a pixel \\f$(x, y)\\f$ in image corresponds to the\n.   pixel \\f$(x+1, y+1)\\f$ in the mask .\n.   \n.   @sa findContours"
    ...

def gemm(src1: Mat, src2: Mat, alpha, src3, beta, dts: Mat = ..., flags: int = ...) -> typing.Any:
    'gemm(src1, src2, alpha, src3, beta[, dst[, flags]]) -> dst\n.   @brief Performs generalized matrix multiplication.\n.   \n.   The function cv::gemm performs generalized matrix multiplication similar to the\n.   gemm functions in BLAS level 3. For example,\n.   `gemm(src1, src2, alpha, src3, beta, dst, GEMM_1_T + GEMM_3_T)`\n.   corresponds to\n.   \\f[\\texttt{dst} =  \\texttt{alpha} \\cdot \\texttt{src1} ^T  \\cdot \\texttt{src2} +  \\texttt{beta} \\cdot \\texttt{src3} ^T\\f]\n.   \n.   In case of complex (two-channel) data, performed a complex matrix\n.   multiplication.\n.   \n.   The function can be replaced with a matrix expression. For example, the\n.   above call can be replaced with:\n.   @code{.cpp}\n.       dst = alpha*src1.t()*src2 + beta*src3.t();\n.   @endcode\n.   @param src1 first multiplied input matrix that could be real(CV_32FC1,\n.   CV_64FC1) or complex(CV_32FC2, CV_64FC2).\n.   @param src2 second multiplied input matrix of the same type as src1.\n.   @param alpha weight of the matrix product.\n.   @param src3 third optional delta matrix added to the matrix product; it\n.   should have the same type as src1 and src2.\n.   @param beta weight of src3.\n.   @param dst output matrix; it has the proper size and the same type as\n.   input matrices.\n.   @param flags operation flags (cv::GemmFlags)\n.   @sa mulTransposed , transform'
    ...

def getAffineTransform(src: Mat, dts: Mat) -> typing.Any:
    'getAffineTransform(src, dst) -> retval\n.   @overload'
    ...

def getBuildInformation() -> typing.Any:
    'getBuildInformation() -> retval\n.   @brief Returns full configuration time cmake output.\n.   \n.   Returned value is raw cmake output including version control system revision, compiler version,\n.   compiler flags, enabled modules and third party libraries, etc. Output format depends on target\n.   architecture.'
    ...

def getCPUFeaturesLine() -> typing.Any:
    'getCPUFeaturesLine() -> retval\n.   @brief Returns list of CPU features enabled during compilation.\n.   \n.   Returned value is a string containing space separated list of CPU features with following markers:\n.   \n.   - no markers - baseline features\n.   - prefix `*` - features enabled in dispatcher\n.   - suffix `?` - features enabled but not available in HW\n.   \n.   Example: `SSE SSE2 SSE3 *SSE4.1 *SSE4.2 *FP16 *AVX *AVX2 *AVX512-SKX?`'
    ...

def getCPUTickCount() -> typing.Any:
    'getCPUTickCount() -> retval\n.   @brief Returns the number of CPU ticks.\n.   \n.   The function returns the current number of CPU ticks on some architectures (such as x86, x64,\n.   PowerPC). On other platforms the function is equivalent to getTickCount. It can also be used for\n.   very accurate time measurements, as well as for RNG initialization. Note that in case of multi-CPU\n.   systems a thread, from which getCPUTickCount is called, can be suspended and resumed at another CPU\n.   with its own counter. So, theoretically (and practically) the subsequent calls to the function do\n.   not necessary return the monotonously increasing values. Also, since a modern CPU varies the CPU\n.   frequency depending on the load, the number of CPU clocks spent in some code cannot be directly\n.   converted to time units. Therefore, getTickCount is generally a preferable solution for measuring\n.   execution time.'
    ...

def getDefaultNewCameraMatrix(cameraMatrix, imgsize=..., centerPrincipalPoint=...) -> typing.Any:
    'getDefaultNewCameraMatrix(cameraMatrix[, imgsize[, centerPrincipalPoint]]) -> retval\n.   @brief Returns the default new camera matrix.\n.   \n.   The function returns the camera matrix that is either an exact copy of the input cameraMatrix (when\n.   centerPrinicipalPoint=false ), or the modified one (when centerPrincipalPoint=true).\n.   \n.   In the latter case, the new camera matrix will be:\n.   \n.   \\f[\\begin{bmatrix} f_x && 0 && ( \\texttt{imgSize.width} -1)*0.5  \\\\ 0 && f_y && ( \\texttt{imgSize.height} -1)*0.5  \\\\ 0 && 0 && 1 \\end{bmatrix} ,\\f]\n.   \n.   where \\f$f_x\\f$ and \\f$f_y\\f$ are \\f$(0,0)\\f$ and \\f$(1,1)\\f$ elements of cameraMatrix, respectively.\n.   \n.   By default, the undistortion functions in OpenCV (see #initUndistortRectifyMap, #undistort) do not\n.   move the principal point. However, when you work with stereo, it is important to move the principal\n.   points in both views to the same y-coordinate (which is required by most of stereo correspondence\n.   algorithms), and may be to the same x-coordinate too. So, you can form the new camera matrix for\n.   each view where the principal points are located at the center.\n.   \n.   @param cameraMatrix Input camera matrix.\n.   @param imgsize Camera view image size in pixels.\n.   @param centerPrincipalPoint Location of the principal point in the new camera matrix. The\n.   parameter indicates whether this location should be at the image center or not.'
    ...

def getDerivKernels(dx, dy, ksize, kx=..., ky=..., normalize=..., ktype=...) -> typing.Any:
    'getDerivKernels(dx, dy, ksize[, kx[, ky[, normalize[, ktype]]]]) -> kx, ky\n.   @brief Returns filter coefficients for computing spatial image derivatives.\n.   \n.   The function computes and returns the filter coefficients for spatial image derivatives. When\n.   `ksize=FILTER_SCHARR`, the Scharr \\f$3 \\times 3\\f$ kernels are generated (see #Scharr). Otherwise, Sobel\n.   kernels are generated (see #Sobel). The filters are normally passed to #sepFilter2D or to\n.   \n.   @param kx Output matrix of row filter coefficients. It has the type ktype .\n.   @param ky Output matrix of column filter coefficients. It has the type ktype .\n.   @param dx Derivative order in respect of x.\n.   @param dy Derivative order in respect of y.\n.   @param ksize Aperture size. It can be FILTER_SCHARR, 1, 3, 5, or 7.\n.   @param normalize Flag indicating whether to normalize (scale down) the filter coefficients or not.\n.   Theoretically, the coefficients should have the denominator \\f$=2^{ksize*2-dx-dy-2}\\f$. If you are\n.   going to filter floating-point images, you are likely to use the normalized kernels. But if you\n.   compute derivatives of an 8-bit image, store the results in a 16-bit image, and wish to preserve\n.   all the fractional bits, you may want to set normalize=false .\n.   @param ktype Type of filter coefficients. It can be CV_32f or CV_64F .'
    ...

def getFontScaleFromHeight(fontFace, pixelHeight, thickness=...) -> typing.Any:
    'getFontScaleFromHeight(fontFace, pixelHeight[, thickness]) -> retval\n.   @brief Calculates the font-specific size to use to achieve a given height in pixels.\n.   \n.   @param fontFace Font to use, see cv::HersheyFonts.\n.   @param pixelHeight Pixel height to compute the fontScale for\n.   @param thickness Thickness of lines used to render the text.See putText for details.\n.   @return The fontSize to use for cv::putText\n.   \n.   @see cv::putText'
    ...

def getGaborKernel(ksize, sigma, theta, lambd, gamma, psi=..., ktype=...) -> typing.Any:
    'getGaborKernel(ksize, sigma, theta, lambd, gamma[, psi[, ktype]]) -> retval\n.   @brief Returns Gabor filter coefficients.\n.   \n.   For more details about gabor filter equations and parameters, see: [Gabor\n.   Filter](http://en.wikipedia.org/wiki/Gabor_filter).\n.   \n.   @param ksize Size of the filter returned.\n.   @param sigma Standard deviation of the gaussian envelope.\n.   @param theta Orientation of the normal to the parallel stripes of a Gabor function.\n.   @param lambd Wavelength of the sinusoidal factor.\n.   @param gamma Spatial aspect ratio.\n.   @param psi Phase offset.\n.   @param ktype Type of filter coefficients. It can be CV_32F or CV_64F .'
    ...

def getGaussianKernel(ksize, sigma, ktype=...) -> typing.Any:
    'getGaussianKernel(ksize, sigma[, ktype]) -> retval\n.   @brief Returns Gaussian filter coefficients.\n.   \n.   The function computes and returns the \\f$\\texttt{ksize} \\times 1\\f$ matrix of Gaussian filter\n.   coefficients:\n.   \n.   \\f[G_i= \\alpha *e^{-(i-( \\texttt{ksize} -1)/2)^2/(2* \\texttt{sigma}^2)},\\f]\n.   \n.   where \\f$i=0..\\texttt{ksize}-1\\f$ and \\f$\\alpha\\f$ is the scale factor chosen so that \\f$\\sum_i G_i=1\\f$.\n.   \n.   Two of such generated kernels can be passed to sepFilter2D. Those functions automatically recognize\n.   smoothing kernels (a symmetrical kernel with sum of weights equal to 1) and handle them accordingly.\n.   You may also use the higher-level GaussianBlur.\n.   @param ksize Aperture size. It should be odd ( \\f$\\texttt{ksize} \\mod 2 = 1\\f$ ) and positive.\n.   @param sigma Gaussian standard deviation. If it is non-positive, it is computed from ksize as\n.   `sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8`.\n.   @param ktype Type of filter coefficients. It can be CV_32F or CV_64F .\n.   @sa  sepFilter2D, getDerivKernels, getStructuringElement, GaussianBlur'
    ...

def getHardwareFeatureName(feature) -> typing.Any:
    'getHardwareFeatureName(feature) -> retval\n.   @brief Returns feature name by ID\n.   \n.   Returns empty string if feature is not defined'
    ...

def getNumThreads() -> typing.Any:
    'getNumThreads() -> retval\n.   @brief Returns the number of threads used by OpenCV for parallel regions.\n.   \n.   Always returns 1 if OpenCV is built without threading support.\n.   \n.   The exact meaning of return value depends on the threading framework used by OpenCV library:\n.   - `TBB` - The number of threads, that OpenCV will try to use for parallel regions. If there is\n.     any tbb::thread_scheduler_init in user code conflicting with OpenCV, then function returns\n.     default number of threads used by TBB library.\n.   - `OpenMP` - An upper bound on the number of threads that could be used to form a new team.\n.   - `Concurrency` - The number of threads, that OpenCV will try to use for parallel regions.\n.   - `GCD` - Unsupported; returns the GCD thread pool limit (512) for compatibility.\n.   - `C=` - The number of threads, that OpenCV will try to use for parallel regions, if before\n.     called setNumThreads with threads \\> 0, otherwise returns the number of logical CPUs,\n.     available for the process.\n.   @sa setNumThreads, getThreadNum'
    ...

def getNumberOfCPUs() -> typing.Any:
    'getNumberOfCPUs() -> retval\n.   @brief Returns the number of logical CPUs available for the process.'
    ...

def getOptimalDFTSize(vecsize) -> typing.Any:
    "getOptimalDFTSize(vecsize) -> retval\n.   @brief Returns the optimal DFT size for a given vector size.\n.   \n.   DFT performance is not a monotonic function of a vector size. Therefore, when you calculate\n.   convolution of two arrays or perform the spectral analysis of an array, it usually makes sense to\n.   pad the input data with zeros to get a bit larger array that can be transformed much faster than the\n.   original one. Arrays whose size is a power-of-two (2, 4, 8, 16, 32, ...) are the fastest to process.\n.   Though, the arrays whose size is a product of 2's, 3's, and 5's (for example, 300 = 5\\*5\\*3\\*2\\*2)\n.   are also processed quite efficiently.\n.   \n.   The function cv::getOptimalDFTSize returns the minimum number N that is greater than or equal to vecsize\n.   so that the DFT of a vector of size N can be processed efficiently. In the current implementation N\n.   = 2 ^p^ \\* 3 ^q^ \\* 5 ^r^ for some integer p, q, r.\n.   \n.   The function returns a negative number if vecsize is too large (very close to INT_MAX ).\n.   \n.   While the function cannot be used directly to estimate the optimal vector size for DCT transform\n.   (since the current DCT implementation supports only even-size vectors), it can be easily processed\n.   as getOptimalDFTSize((vecsize+1)/2)\\*2.\n.   @param vecsize vector size.\n.   @sa dft , dct , idft , idct , mulSpectrums"
    ...

def getOptimalNewCameraMatrix(cameraMatrix, distCoeffs, imageSize, alpha, newImgSize=..., centerPrincipalPoint=...) -> typing.Any:
    'getOptimalNewCameraMatrix(cameraMatrix, distCoeffs, imageSize, alpha[, newImgSize[, centerPrincipalPoint]]) -> retval, validPixROI\n.   @brief Returns the new camera matrix based on the free scaling parameter.\n.   \n.   @param cameraMatrix Input camera matrix.\n.   @param distCoeffs Input vector of distortion coefficients\n.   \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6 [, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$ of\n.   4, 5, 8, 12 or 14 elements. If the vector is NULL/empty, the zero distortion coefficients are\n.   assumed.\n.   @param imageSize Original image size.\n.   @param alpha Free scaling parameter between 0 (when all the pixels in the undistorted image are\n.   valid) and 1 (when all the source image pixels are retained in the undistorted image). See\n.   stereoRectify for details.\n.   @param newImgSize Image size after rectification. By default, it is set to imageSize .\n.   @param validPixROI Optional output rectangle that outlines all-good-pixels region in the\n.   undistorted image. See roi1, roi2 description in stereoRectify .\n.   @param centerPrincipalPoint Optional flag that indicates whether in the new camera matrix the\n.   principal point should be at the image center or not. By default, the principal point is chosen to\n.   best fit a subset of the source image (determined by alpha) to the corrected image.\n.   @return new_camera_matrix Output new camera matrix.\n.   \n.   The function computes and returns the optimal new camera matrix based on the free scaling parameter.\n.   By varying this parameter, you may retrieve only sensible pixels alpha=0 , keep all the original\n.   image pixels if there is valuable information in the corners alpha=1 , or get something in between.\n.   When alpha\\>0 , the undistorted result is likely to have some black pixels corresponding to\n.   "virtual" pixels outside of the captured distorted image. The original camera matrix, distortion\n.   coefficients, the computed new camera matrix, and newImageSize should be passed to\n.   initUndistortRectifyMap to produce the maps for remap .'
    ...

def getPerspectiveTransform(src: Mat, dts: Mat, solveMethod=...) -> typing.Any:
    "getPerspectiveTransform(src, dst[, solveMethod]) -> retval\n.   @brief Calculates a perspective transform from four pairs of the corresponding points.\n.   \n.   The function calculates the \\f$3 \\times 3\\f$ matrix of a perspective transform so that:\n.   \n.   \\f[\\begin{bmatrix} t_i x'_i \\\\ t_i y'_i \\\\ t_i \\end{bmatrix} = \\texttt{map_matrix} \\cdot \\begin{bmatrix} x_i \\\\ y_i \\\\ 1 \\end{bmatrix}\\f]\n.   \n.   where\n.   \n.   \\f[dst(i)=(x'_i,y'_i), src(i)=(x_i, y_i), i=0,1,2,3\\f]\n.   \n.   @param src Coordinates of quadrangle vertices in the source image.\n.   @param dst Coordinates of the corresponding quadrangle vertices in the destination image.\n.   @param solveMethod method passed to cv::solve (#DecompTypes)\n.   \n.   @sa  findHomography, warpPerspective, perspectiveTransform"
    ...

def getRectSubPix(image: Mat, patchSize, center, patch=..., patchType=...) -> typing.Any:
    'getRectSubPix(image, patchSize, center[, patch[, patchType]]) -> patch\n.   @brief Retrieves a pixel rectangle from an image with sub-pixel accuracy.\n.   \n.   The function getRectSubPix extracts pixels from src:\n.   \n.   \\f[patch(x, y) = src(x +  \\texttt{center.x} - ( \\texttt{dst.cols} -1)*0.5, y +  \\texttt{center.y} - ( \\texttt{dst.rows} -1)*0.5)\\f]\n.   \n.   where the values of the pixels at non-integer coordinates are retrieved using bilinear\n.   interpolation. Every channel of multi-channel images is processed independently. Also\n.   the image should be a single channel or three channel image. While the center of the\n.   rectangle must be inside the image, parts of the rectangle may be outside.\n.   \n.   @param image Source image.\n.   @param patchSize Size of the extracted patch.\n.   @param center Floating point coordinates of the center of the extracted rectangle within the\n.   source image. The center must be inside the image.\n.   @param patch Extracted patch that has the size patchSize and the same number of channels as src .\n.   @param patchType Depth of the extracted pixels. By default, they have the same depth as src .\n.   \n.   @sa  warpAffine, warpPerspective'
    ...

def getRotationMatrix2D(center, angle, scale) -> typing.Any:
    'getRotationMatrix2D(center, angle, scale) -> retval\n.   @brief Calculates an affine matrix of 2D rotation.\n.   \n.   The function calculates the following matrix:\n.   \n.   \\f[\\begin{bmatrix} \\alpha &  \\beta & (1- \\alpha )  \\cdot \\texttt{center.x} -  \\beta \\cdot \\texttt{center.y} \\\\ - \\beta &  \\alpha &  \\beta \\cdot \\texttt{center.x} + (1- \\alpha )  \\cdot \\texttt{center.y} \\end{bmatrix}\\f]\n.   \n.   where\n.   \n.   \\f[\\begin{array}{l} \\alpha =  \\texttt{scale} \\cdot \\cos \\texttt{angle} , \\\\ \\beta =  \\texttt{scale} \\cdot \\sin \\texttt{angle} \\end{array}\\f]\n.   \n.   The transformation maps the rotation center to itself. If this is not the target, adjust the shift.\n.   \n.   @param center Center of the rotation in the source image.\n.   @param angle Rotation angle in degrees. Positive values mean counter-clockwise rotation (the\n.   coordinate origin is assumed to be the top-left corner).\n.   @param scale Isotropic scale factor.\n.   \n.   @sa  getAffineTransform, warpAffine, transform'
    ...

def getStructuringElement(shape, ksize, anchor=...) -> typing.Any:
    'getStructuringElement(shape, ksize[, anchor]) -> retval\n.   @brief Returns a structuring element of the specified size and shape for morphological operations.\n.   \n.   The function constructs and returns the structuring element that can be further passed to #erode,\n.   #dilate or #morphologyEx. But you can also construct an arbitrary binary mask yourself and use it as\n.   the structuring element.\n.   \n.   @param shape Element shape that could be one of #MorphShapes\n.   @param ksize Size of the structuring element.\n.   @param anchor Anchor position within the element. The default value \\f$(-1, -1)\\f$ means that the\n.   anchor is at the center. Note that only the shape of a cross-shaped element depends on the anchor\n.   position. In other cases the anchor just regulates how much the result of the morphological\n.   operation is shifted.'
    ...

def getTextSize(text, fontFace, fontScale, thickness) -> typing.Any:
    'getTextSize(text, fontFace, fontScale, thickness) -> retval, baseLine\n.   @brief Calculates the width and height of a text string.\n.   \n.   The function cv::getTextSize calculates and returns the size of a box that contains the specified text.\n.   That is, the following code renders some text, the tight box surrounding it, and the baseline: :\n.   @code\n.       String text = "Funny text inside the box";\n.       int fontFace = FONT_HERSHEY_SCRIPT_SIMPLEX;\n.       double fontScale = 2;\n.       int thickness = 3;\n.   \n.       Mat img(600, 800, CV_8UC3, Scalar::all(0));\n.   \n.       int baseline=0;\n.       Size textSize = getTextSize(text, fontFace,\n.                                   fontScale, thickness, &baseline);\n.       baseline += thickness;\n.   \n.       // center the text\n.       Point textOrg((img.cols - textSize.width)/2,\n.                     (img.rows + textSize.height)/2);\n.   \n.       // draw the box\n.       rectangle(img, textOrg + Point(0, baseline),\n.                 textOrg + Point(textSize.width, -textSize.height),\n.                 Scalar(0,0,255));\n.       // ... and the baseline first\n.       line(img, textOrg + Point(0, thickness),\n.            textOrg + Point(textSize.width, thickness),\n.            Scalar(0, 0, 255));\n.   \n.       // then put the text itself\n.       putText(img, text, textOrg, fontFace, fontScale,\n.               Scalar::all(255), thickness, 8);\n.   @endcode\n.   \n.   @param text Input text string.\n.   @param fontFace Font to use, see #HersheyFonts.\n.   @param fontScale Font scale factor that is multiplied by the font-specific base size.\n.   @param thickness Thickness of lines used to render the text. See #putText for details.\n.   @param[out] baseLine y-coordinate of the baseline relative to the bottom-most text\n.   point.\n.   @return The size of a box that contains the specified text.\n.   \n.   @see putText'
    ...

def getThreadNum() -> typing.Any:
    "getThreadNum() -> retval\n.   @brief Returns the index of the currently executed thread within the current parallel region. Always\n.   returns 0 if called outside of parallel region.\n.   \n.   @deprecated Current implementation doesn't corresponding to this documentation.\n.   \n.   The exact meaning of the return value depends on the threading framework used by OpenCV library:\n.   - `TBB` - Unsupported with current 4.1 TBB release. Maybe will be supported in future.\n.   - `OpenMP` - The thread number, within the current team, of the calling thread.\n.   - `Concurrency` - An ID for the virtual processor that the current context is executing on (0\n.     for master thread and unique number for others, but not necessary 1,2,3,...).\n.   - `GCD` - System calling thread's ID. Never returns 0 inside parallel region.\n.   - `C=` - The index of the current parallel task.\n.   @sa setNumThreads, getNumThreads"
    ...

def getTickCount() -> typing.Any:
    'getTickCount() -> retval\n.   @brief Returns the number of ticks.\n.   \n.   The function returns the number of ticks after the certain event (for example, when the machine was\n.   turned on). It can be used to initialize RNG or to measure a function execution time by reading the\n.   tick count before and after the function call.\n.   @sa getTickFrequency, TickMeter'
    ...

def getTickFrequency() -> typing.Any:
    'getTickFrequency() -> retval\n.   @brief Returns the number of ticks per second.\n.   \n.   The function returns the number of ticks per second. That is, the following code computes the\n.   execution time in seconds:\n.   @code\n.       double t = (double)getTickCount();\n.       // do something ...\n.       t = ((double)getTickCount() - t)/getTickFrequency();\n.   @endcode\n.   @sa getTickCount, TickMeter'
    ...

def getTrackbarPos(trackbarname, winname) -> typing.Any:
    'getTrackbarPos(trackbarname, winname) -> retval\n.   @brief Returns the trackbar position.\n.   \n.   The function returns the current position of the specified trackbar.\n.   \n.   @note\n.   \n.   [__Qt Backend Only__] winname can be empty if the trackbar is attached to the control\n.   panel.\n.   \n.   @param trackbarname Name of the trackbar.\n.   @param winname Name of the window that is the parent of the trackbar.'
    ...

def getValidDisparityROI(roi1, roi2, minDisparity, numberOfDisparities, blockSize) -> typing.Any:
    'getValidDisparityROI(roi1, roi2, minDisparity, numberOfDisparities, blockSize) -> retval\n.'
    ...

def getVersionMajor() -> typing.Any:
    'getVersionMajor() -> retval\n.   @brief Returns major library version'
    ...

def getVersionMinor() -> typing.Any:
    'getVersionMinor() -> retval\n.   @brief Returns minor library version'
    ...

def getVersionRevision() -> typing.Any:
    'getVersionRevision() -> retval\n.   @brief Returns revision field of the library version'
    ...

def getVersionString() -> typing.Any:
    'getVersionString() -> retval\n.   @brief Returns library version string\n.   \n.   For example "3.4.1-dev".\n.   \n.   @sa getMajorVersion, getMinorVersion, getRevisionVersion'
    ...

def getWindowImageRect(winname) -> typing.Any:
    'getWindowImageRect(winname) -> retval\n.   @brief Provides rectangle of image in the window.\n.   \n.   The function getWindowImageRect returns the client screen coordinates, width and height of the image rendering area.\n.   \n.   @param winname Name of the window.\n.   \n.   @sa resizeWindow moveWindow'
    ...

def getWindowProperty(winname, prop_id) -> typing.Any:
    'getWindowProperty(winname, prop_id) -> retval\n.   @brief Provides parameters of a window.\n.   \n.   The function getWindowProperty returns properties of a window.\n.   \n.   @param winname Name of the window.\n.   @param prop_id Window property to retrieve. The following operation flags are available: (cv::WindowPropertyFlags)\n.   \n.   @sa setWindowProperty'
    ...

def goodFeaturesToTrack(image: Mat, maxCorners, qualityLevel, minDistance, corners=..., mask: Mat = ..., blockSize=..., useHarrisDetector=..., k=...) -> typing.Any:
    'goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]]) -> corners\n.   @brief Determines strong corners on an image.\n.   \n.   The function finds the most prominent corners in the image or in the specified image region, as\n.   described in @cite Shi94\n.   \n.   -   Function calculates the corner quality measure at every source image pixel using the\n.       #cornerMinEigenVal or #cornerHarris .\n.   -   Function performs a non-maximum suppression (the local maximums in *3 x 3* neighborhood are\n.       retained).\n.   -   The corners with the minimal eigenvalue less than\n.       \\f$\\texttt{qualityLevel} \\cdot \\max_{x,y} qualityMeasureMap(x,y)\\f$ are rejected.\n.   -   The remaining corners are sorted by the quality measure in the descending order.\n.   -   Function throws away each corner for which there is a stronger corner at a distance less than\n.       maxDistance.\n.   \n.   The function can be used to initialize a point-based tracker of an object.\n.   \n.   @note If the function is called with different values A and B of the parameter qualityLevel , and\n.   A \\> B, the vector of returned corners with qualityLevel=A will be the prefix of the output vector\n.   with qualityLevel=B .\n.   \n.   @param image Input 8-bit or floating-point 32-bit, single-channel image.\n.   @param corners Output vector of detected corners.\n.   @param maxCorners Maximum number of corners to return. If there are more corners than are found,\n.   the strongest of them is returned. `maxCorners <= 0` implies that no limit on the maximum is set\n.   and all detected corners are returned.\n.   @param qualityLevel Parameter characterizing the minimal accepted quality of image corners. The\n.   parameter value is multiplied by the best corner quality measure, which is the minimal eigenvalue\n.   (see #cornerMinEigenVal ) or the Harris function response (see #cornerHarris ). The corners with the\n.   quality measure less than the product are rejected. For example, if the best corner has the\n.   quality measure = 1500, and the qualityLevel=0.01 , then all the corners with the quality measure\n.   less than 15 are rejected.\n.   @param minDistance Minimum possible Euclidean distance between the returned corners.\n.   @param mask Optional region of interest. If the image is not empty (it needs to have the type\n.   CV_8UC1 and the same size as image ), it specifies the region in which the corners are detected.\n.   @param blockSize Size of an average block for computing a derivative covariation matrix over each\n.   pixel neighborhood. See cornerEigenValsAndVecs .\n.   @param useHarrisDetector Parameter indicating whether to use a Harris detector (see #cornerHarris)\n.   or #cornerMinEigenVal.\n.   @param k Free parameter of the Harris detector.\n.   \n.   @sa  cornerMinEigenVal, cornerHarris, calcOpticalFlowPyrLK, estimateRigidTransform,\n\n\n\ngoodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, mask, blockSize, gradientSize[, corners[, useHarrisDetector[, k]]]) -> corners\n.'
    ...

def grabCut(img: Mat, mask: typing.Optional[Mat], rect, bgdModel, fgdModel, iterCount, mode=...) -> typing.Any:
    'grabCut(img, mask, rect, bgdModel, fgdModel, iterCount[, mode]) -> mask, bgdModel, fgdModel\n.   @brief Runs the GrabCut algorithm.\n.   \n.   The function implements the [GrabCut image segmentation algorithm](http://en.wikipedia.org/wiki/GrabCut).\n.   \n.   @param img Input 8-bit 3-channel image.\n.   @param mask Input/output 8-bit single-channel mask. The mask is initialized by the function when\n.   mode is set to #GC_INIT_WITH_RECT. Its elements may have one of the #GrabCutClasses.\n.   @param rect ROI containing a segmented object. The pixels outside of the ROI are marked as\n.   "obvious background". The parameter is only used when mode==#GC_INIT_WITH_RECT .\n.   @param bgdModel Temporary array for the background model. Do not modify it while you are\n.   processing the same image.\n.   @param fgdModel Temporary arrays for the foreground model. Do not modify it while you are\n.   processing the same image.\n.   @param iterCount Number of iterations the algorithm should make before returning the result. Note\n.   that the result can be refined with further calls with mode==#GC_INIT_WITH_MASK or\n.   mode==GC_EVAL .\n.   @param mode Operation mode that could be one of the #GrabCutModes'
    ...

def groupRectangles(rectList, groupThreshold, eps=...) -> typing.Any:
    'groupRectangles(rectList, groupThreshold[, eps]) -> rectList, weights\n.   @overload'
    ...

def haveImageReader(filename: str) -> typing.Any:
    'haveImageReader(filename) -> retval\n.   @brief Returns true if the specified image can be decoded by OpenCV\n.   \n.   @param filename File name of the image'
    ...

def haveImageWriter(filename: str) -> typing.Any:
    'haveImageWriter(filename) -> retval\n.   @brief Returns true if an image with the specified filename can be encoded by OpenCV\n.   \n.    @param filename File name of the image'
    ...

def haveOpenVX() -> typing.Any:
    'haveOpenVX() -> retval\n.'
    ...

def hconcat(src: Mat, dts: Mat = ...) -> typing.Any:
    'hconcat(src[, dst]) -> dst\n.   @overload\n.    @code{.cpp}\n.       std::vector<cv::Mat> matrices = { cv::Mat(4, 1, CV_8UC1, cv::Scalar(1)),\n.                                         cv::Mat(4, 1, CV_8UC1, cv::Scalar(2)),\n.                                         cv::Mat(4, 1, CV_8UC1, cv::Scalar(3)),};\n.   \n.       cv::Mat out;\n.       cv::hconcat( matrices, out );\n.       //out:\n.       //[1, 2, 3;\n.       // 1, 2, 3;\n.       // 1, 2, 3;\n.       // 1, 2, 3]\n.    @endcode\n.    @param src input array or vector of matrices. all of the matrices must have the same number of rows and the same depth.\n.    @param dst output array. It has the same number of rows and depth as the src, and the sum of cols of the src.\n.   same depth.'
    ...

def idct(src: Mat, dts: Mat = ..., flags: int = ...) -> typing.Any:
    'idct(src[, dst[, flags]]) -> dst\n.   @brief Calculates the inverse Discrete Cosine Transform of a 1D or 2D array.\n.   \n.   idct(src, dst, flags) is equivalent to dct(src, dst, flags | DCT_INVERSE).\n.   @param src input floating-point single-channel array.\n.   @param dst output array of the same size and type as src.\n.   @param flags operation flags.\n.   @sa  dct, dft, idft, getOptimalDFTSize'
    ...

def idft(src: Mat, dts: Mat = ..., flags: int = ..., nonzeroRows=...) -> typing.Any:
    'idft(src[, dst[, flags[, nonzeroRows]]]) -> dst\n.   @brief Calculates the inverse Discrete Fourier Transform of a 1D or 2D array.\n.   \n.   idft(src, dst, flags) is equivalent to dft(src, dst, flags | #DFT_INVERSE) .\n.   @note None of dft and idft scales the result by default. So, you should pass #DFT_SCALE to one of\n.   dft or idft explicitly to make these transforms mutually inverse.\n.   @sa dft, dct, idct, mulSpectrums, getOptimalDFTSize\n.   @param src input floating-point real or complex array.\n.   @param dst output array whose size and type depend on the flags.\n.   @param flags operation flags (see dft and #DftFlags).\n.   @param nonzeroRows number of dst rows to process; the rest of the rows have undefined content (see\n.   the convolution sample in dft description.'
    ...

def illuminationChange(src: Mat, mask: Mat, dts: Mat = ..., alpha=..., beta=...) -> typing.Any:
    'illuminationChange(src, mask[, dst[, alpha[, beta]]]) -> dst\n.   @brief Applying an appropriate non-linear transformation to the gradient field inside the selection and\n.   then integrating back with a Poisson solver, modifies locally the apparent illumination of an image.\n.   \n.   @param src Input 8-bit 3-channel image.\n.   @param mask Input 8-bit 1 or 3-channel image.\n.   @param dst Output image with the same size and type as src.\n.   @param alpha Value ranges between 0-2.\n.   @param beta Value ranges between 0-2.\n.   \n.   This is useful to highlight under-exposed foreground objects or to reduce specular reflections.'
    ...

def imdecode(buf, flags: int) -> typing.Any:
    'imdecode(buf, flags) -> retval\n.   @brief Reads an image from a buffer in memory.\n.   \n.   The function imdecode reads an image from the specified buffer in the memory. If the buffer is too short or\n.   contains invalid data, the function returns an empty matrix ( Mat::data==NULL ).\n.   \n.   See cv::imread for the list of supported formats and flags description.\n.   \n.   @note In the case of color images, the decoded images will have the channels stored in **B G R** order.\n.   @param buf Input array or vector of bytes.\n.   @param flags The same flags as in cv::imread, see cv::ImreadModes.'
    ...

def imencode(ext, img: Mat, params=...) -> typing.Any:
    'imencode(ext, img[, params]) -> retval, buf\n.   @brief Encodes an image into a memory buffer.\n.   \n.   The function imencode compresses the image and stores it in the memory buffer that is resized to fit the\n.   result. See cv::imwrite for the list of supported formats and flags description.\n.   \n.   @param ext File extension that defines the output format.\n.   @param img Image to be written.\n.   @param buf Output buffer resized to fit the compressed image.\n.   @param params Format-specific parameters. See cv::imwrite and cv::ImwriteFlags.'
    ...

def imread(filename: str, flags: int = ...) -> Mat:
    'imread(filename[, flags]) -> retval\n.   @brief Loads an image from a file.\n.   \n.   @anchor imread\n.   \n.   The function imread loads an image from the specified file and returns it. If the image cannot be\n.   read (because of missing file, improper permissions, unsupported or invalid format), the function\n.   returns an empty matrix ( Mat::data==NULL ).\n.   \n.   Currently, the following file formats are supported:\n.   \n.   -   Windows bitmaps - \\*.bmp, \\*.dib (always supported)\n.   -   JPEG files - \\*.jpeg, \\*.jpg, \\*.jpe (see the *Note* section)\n.   -   JPEG 2000 files - \\*.jp2 (see the *Note* section)\n.   -   Portable Network Graphics - \\*.png (see the *Note* section)\n.   -   WebP - \\*.webp (see the *Note* section)\n.   -   Portable image format - \\*.pbm, \\*.pgm, \\*.ppm \\*.pxm, \\*.pnm (always supported)\n.   -   PFM files - \\*.pfm (see the *Note* section)\n.   -   Sun rasters - \\*.sr, \\*.ras (always supported)\n.   -   TIFF files - \\*.tiff, \\*.tif (see the *Note* section)\n.   -   OpenEXR Image files - \\*.exr (see the *Note* section)\n.   -   Radiance HDR - \\*.hdr, \\*.pic (always supported)\n.   -   Raster and Vector geospatial data supported by GDAL (see the *Note* section)\n.   \n.   @note\n.   -   The function determines the type of an image by the content, not by the file extension.\n.   -   In the case of color images, the decoded images will have the channels stored in **B G R** order.\n.   -   When using IMREAD_GRAYSCALE, the codec\'s internal grayscale conversion will be used, if available.\n.       Results may differ to the output of cvtColor()\n.   -   On Microsoft Windows\\* OS and MacOSX\\*, the codecs shipped with an OpenCV image (libjpeg,\n.       libpng, libtiff, and libjasper) are used by default. So, OpenCV can always read JPEGs, PNGs,\n.       and TIFFs. On MacOSX, there is also an option to use native MacOSX image readers. But beware\n.       that currently these native image loaders give images with different pixel values because of\n.       the color management embedded into MacOSX.\n.   -   On Linux\\*, BSD flavors and other Unix-like open-source operating systems, OpenCV looks for\n.       codecs supplied with an OS image. Install the relevant packages (do not forget the development\n.       files, for example, "libjpeg-dev", in Debian\\* and Ubuntu\\*) to get the codec support or turn\n.       on the OPENCV_BUILD_3RDPARTY_LIBS flag in CMake.\n.   -   In the case you set *WITH_GDAL* flag to true in CMake and @ref IMREAD_LOAD_GDAL to load the image,\n.       then the [GDAL](http://www.gdal.org) driver will be used in order to decode the image, supporting\n.       the following formats: [Raster](http://www.gdal.org/formats_list.html),\n.       [Vector](http://www.gdal.org/ogr_formats.html).\n.   -   If EXIF information is embedded in the image file, the EXIF orientation will be taken into account\n.       and thus the image will be rotated accordingly except if the flags @ref IMREAD_IGNORE_ORIENTATION\n.       or @ref IMREAD_UNCHANGED are passed.\n.   -   Use the IMREAD_UNCHANGED flag to keep the floating point values from PFM image.\n.   -   By default number of pixels must be less than 2^30. Limit can be set using system\n.       variable OPENCV_IO_MAX_IMAGE_PIXELS\n.   \n.   @param filename Name of file to be loaded.\n.   @param flags Flag that can take values of cv::ImreadModes'
    ...

def imreadmulti(filename: str, mats=..., flags: int = ...) -> typing.Any:
    'imreadmulti(filename[, mats[, flags]]) -> retval, mats\n.   @brief Loads a multi-page image from a file.\n.   \n.   The function imreadmulti loads a multi-page image from the specified file into a vector of Mat objects.\n.   @param filename Name of file to be loaded.\n.   @param flags Flag that can take values of cv::ImreadModes, default with cv::IMREAD_ANYCOLOR.\n.   @param mats A vector of Mat objects holding each page, if more than one.\n.   @sa cv::imread'
    ...

def imshow(winname, mat) -> typing.Any:
    'imshow(winname, mat) -> None\n.   @brief Displays an image in the specified window.\n.   \n.   The function imshow displays an image in the specified window. If the window was created with the\n.   cv::WINDOW_AUTOSIZE flag, the image is shown with its original size, however it is still limited by the screen resolution.\n.   Otherwise, the image is scaled to fit the window. The function may scale the image, depending on its depth:\n.   \n.   -   If the image is 8-bit unsigned, it is displayed as is.\n.   -   If the image is 16-bit unsigned or 32-bit integer, the pixels are divided by 256. That is, the\n.       value range [0,255\\*256] is mapped to [0,255].\n.   -   If the image is 32-bit or 64-bit floating-point, the pixel values are multiplied by 255. That is, the\n.       value range [0,1] is mapped to [0,255].\n.   \n.   If window was created with OpenGL support, cv::imshow also support ogl::Buffer , ogl::Texture2D and\n.   cuda::GpuMat as input.\n.   \n.   If the window was not created before this function, it is assumed creating a window with cv::WINDOW_AUTOSIZE.\n.   \n.   If you need to show an image that is bigger than the screen resolution, you will need to call namedWindow("", WINDOW_NORMAL) before the imshow.\n.   \n.   @note This function should be followed by cv::waitKey function which displays the image for specified\n.   milliseconds. Otherwise, it won\'t display the image. For example, **waitKey(0)** will display the window\n.   infinitely until any keypress (it is suitable for image display). **waitKey(25)** will display a frame\n.   for 25 ms, after which display will be automatically closed. (If you put it in a loop to read\n.   videos, it will display the video frame-by-frame)\n.   \n.   @note\n.   \n.   [__Windows Backend Only__] Pressing Ctrl+C will copy the image to the clipboard.\n.   \n.   [__Windows Backend Only__] Pressing Ctrl+S will show a dialog to save the image.\n.   \n.   @param winname Name of the window.\n.   @param mat Image to be shown.'
    ...

def imwrite(filename: str, img: Mat, params: typing.List[int] = ...) -> bool:
    "imwrite(filename, img[, params]) -> retval\n.   @brief Saves an image to a specified file.\n.   \n.   The function imwrite saves the image to the specified file. The image format is chosen based on the\n.   filename extension (see cv::imread for the list of extensions). In general, only 8-bit\n.   single-channel or 3-channel (with 'BGR' channel order) images\n.   can be saved using this function, with these exceptions:\n.   \n.   - 16-bit unsigned (CV_16U) images can be saved in the case of PNG, JPEG 2000, and TIFF formats\n.   - 32-bit float (CV_32F) images can be saved in PFM, TIFF, OpenEXR, and Radiance HDR formats;\n.     3-channel (CV_32FC3) TIFF images will be saved using the LogLuv high dynamic range encoding\n.     (4 bytes per pixel)\n.   - PNG images with an alpha channel can be saved using this function. To do this, create\n.   8-bit (or 16-bit) 4-channel image BGRA, where the alpha channel goes last. Fully transparent pixels\n.   should have alpha set to 0, fully opaque pixels should have alpha set to 255/65535 (see the code sample below).\n.   - Multiple images (vector of Mat) can be saved in TIFF format (see the code sample below).\n.   \n.   If the format, depth or channel order is different, use\n.   Mat::convertTo and cv::cvtColor to convert it before saving. Or, use the universal FileStorage I/O\n.   functions to save the image to XML or YAML format.\n.   \n.   The sample below shows how to create a BGRA image, how to set custom compression parameters and save it to a PNG file.\n.   It also demonstrates how to save multiple images in a TIFF file:\n.   @include snippets/imgcodecs_imwrite.cpp\n.   @param filename Name of the file.\n.   @param img (Mat or vector of Mat) Image or Images to be saved.\n.   @param params Format-specific parameters encoded as pairs (paramId_1, paramValue_1, paramId_2, paramValue_2, ... .) see cv::ImwriteFlags"
    ...

def inRange(src: Mat, lowerBound: Mat, upperbBound: Mat, dts: Mat = ...) -> Mat:
    'inRange(src, lowerBound, upperbBound[, dst]) -> dst\n.   @brief  Checks if array elements lie between the elements of two other arrays.\n.   \n.   The function checks the range as follows:\n.   -   For every element of a single-channel input array:\n.       \\f[\\texttt{dst} (I)= \\texttt{lowerBound} (I)_0  \\leq \\texttt{src} (I)_0 \\leq  \\texttt{upperbBound} (I)_0\\f]\n.   -   For two-channel arrays:\n.       \\f[\\texttt{dst} (I)= \\texttt{lowerBound} (I)_0  \\leq \\texttt{src} (I)_0 \\leq  \\texttt{upperbBound} (I)_0  \\land \\texttt{lowerBound} (I)_1  \\leq \\texttt{src} (I)_1 \\leq  \\texttt{upperbBound} (I)_1\\f]\n.   -   and so forth.\n.   \n.   That is, dst (I) is set to 255 (all 1 -bits) if src (I) is within the\n.   specified 1D, 2D, 3D, ... box and 0 otherwise.\n.   \n.   When the lower and/or upper boundary parameters are scalars, the indexes\n.   (I) at lowerBound and upperbBound in the above formulas should be omitted.\n.   @param src first input array.\n.   @param lowerBound inclusive lower boundary array or a scalar.\n.   @param upperbBound inclusive upper boundary array or a scalar.\n.   @param dst output array of the same size as src and CV_8U type.'
    ...

def initCameraMatrix2D(objectPoints, imagePoints, imageSize, aspectRatio=...) -> typing.Any:
    'initCameraMatrix2D(objectPoints, imagePoints, imageSize[, aspectRatio]) -> retval\n.   @brief Finds an initial camera matrix from 3D-2D point correspondences.\n.   \n.   @param objectPoints Vector of vectors of the calibration pattern points in the calibration pattern\n.   coordinate space. In the old interface all the per-view vectors are concatenated. See\n.   calibrateCamera for details.\n.   @param imagePoints Vector of vectors of the projections of the calibration pattern points. In the\n.   old interface all the per-view vectors are concatenated.\n.   @param imageSize Image size in pixels used to initialize the principal point.\n.   @param aspectRatio If it is zero or negative, both \\f$f_x\\f$ and \\f$f_y\\f$ are estimated independently.\n.   Otherwise, \\f$f_x = f_y * \\texttt{aspectRatio}\\f$ .\n.   \n.   The function estimates and returns an initial camera matrix for the camera calibration process.\n.   Currently, the function only supports planar calibration patterns, which are patterns where each\n.   object point has z-coordinate =0.'
    ...

def initUndistortRectifyMap(cameraMatrix, distCoeffs, R, newCameraMatrix, size, m1type, map1=..., map2=...) -> typing.Any:
    "initUndistortRectifyMap(cameraMatrix, distCoeffs, R, newCameraMatrix, size, m1type[, map1[, map2]]) -> map1, map2\n.   @brief Computes the undistortion and rectification transformation map.\n.   \n.   The function computes the joint undistortion and rectification transformation and represents the\n.   result in the form of maps for remap. The undistorted image looks like original, as if it is\n.   captured with a camera using the camera matrix =newCameraMatrix and zero distortion. In case of a\n.   monocular camera, newCameraMatrix is usually equal to cameraMatrix, or it can be computed by\n.   #getOptimalNewCameraMatrix for a better control over scaling. In case of a stereo camera,\n.   newCameraMatrix is normally set to P1 or P2 computed by #stereoRectify .\n.   \n.   Also, this new camera is oriented differently in the coordinate space, according to R. That, for\n.   example, helps to align two heads of a stereo camera so that the epipolar lines on both images\n.   become horizontal and have the same y- coordinate (in case of a horizontally aligned stereo camera).\n.   \n.   The function actually builds the maps for the inverse mapping algorithm that is used by remap. That\n.   is, for each pixel \\f$(u, v)\\f$ in the destination (corrected and rectified) image, the function\n.   computes the corresponding coordinates in the source image (that is, in the original image from\n.   camera). The following process is applied:\n.   \\f[\n.   \\begin{array}{l}\n.   x  \\leftarrow (u - {c'}_x)/{f'}_x  \\\\\n.   y  \\leftarrow (v - {c'}_y)/{f'}_y  \\\\\n.   {[X\\,Y\\,W]} ^T  \\leftarrow R^{-1}*[x \\, y \\, 1]^T  \\\\\n.   x'  \\leftarrow X/W  \\\\\n.   y'  \\leftarrow Y/W  \\\\\n.   r^2  \\leftarrow x'^2 + y'^2 \\\\\n.   x''  \\leftarrow x' \\frac{1 + k_1 r^2 + k_2 r^4 + k_3 r^6}{1 + k_4 r^2 + k_5 r^4 + k_6 r^6}\n.   + 2p_1 x' y' + p_2(r^2 + 2 x'^2)  + s_1 r^2 + s_2 r^4\\\\\n.   y''  \\leftarrow y' \\frac{1 + k_1 r^2 + k_2 r^4 + k_3 r^6}{1 + k_4 r^2 + k_5 r^4 + k_6 r^6}\n.   + p_1 (r^2 + 2 y'^2) + 2 p_2 x' y' + s_3 r^2 + s_4 r^4 \\\\\n.   s\\vecthree{x'''}{y'''}{1} =\n.   \\vecthreethree{R_{33}(\\tau_x, \\tau_y)}{0}{-R_{13}((\\tau_x, \\tau_y)}\n.   {0}{R_{33}(\\tau_x, \\tau_y)}{-R_{23}(\\tau_x, \\tau_y)}\n.   {0}{0}{1} R(\\tau_x, \\tau_y) \\vecthree{x''}{y''}{1}\\\\\n.   map_x(u,v)  \\leftarrow x''' f_x + c_x  \\\\\n.   map_y(u,v)  \\leftarrow y''' f_y + c_y\n.   \\end{array}\n.   \\f]\n.   where \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6[, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$\n.   are the distortion coefficients.\n.   \n.   In case of a stereo camera, this function is called twice: once for each camera head, after\n.   stereoRectify, which in its turn is called after #stereoCalibrate. But if the stereo camera\n.   was not calibrated, it is still possible to compute the rectification transformations directly from\n.   the fundamental matrix using #stereoRectifyUncalibrated. For each camera, the function computes\n.   homography H as the rectification transformation in a pixel domain, not a rotation matrix R in 3D\n.   space. R can be computed from H as\n.   \\f[\\texttt{R} = \\texttt{cameraMatrix} ^{-1} \\cdot \\texttt{H} \\cdot \\texttt{cameraMatrix}\\f]\n.   where cameraMatrix can be chosen arbitrarily.\n.   \n.   @param cameraMatrix Input camera matrix \\f$A=\\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\\f$ .\n.   @param distCoeffs Input vector of distortion coefficients\n.   \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6[, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$\n.   of 4, 5, 8, 12 or 14 elements. If the vector is NULL/empty, the zero distortion coefficients are assumed.\n.   @param R Optional rectification transformation in the object space (3x3 matrix). R1 or R2 ,\n.   computed by #stereoRectify can be passed here. If the matrix is empty, the identity transformation\n.   is assumed. In cvInitUndistortMap R assumed to be an identity matrix.\n.   @param newCameraMatrix New camera matrix \\f$A'=\\vecthreethree{f_x'}{0}{c_x'}{0}{f_y'}{c_y'}{0}{0}{1}\\f$.\n.   @param size Undistorted image size.\n.   @param m1type Type of the first output map that can be CV_32FC1, CV_32FC2 or CV_16SC2, see #convertMaps\n.   @param map1 The first output map.\n.   @param map2 The second output map."
    ...

def inpaint(src: Mat, inpaintMask, inpaintRadius, flags: int, dts: Mat = ...) -> typing.Any:
    'inpaint(src, inpaintMask, inpaintRadius, flags[, dst]) -> dst\n.   @brief Restores the selected region in an image using the region neighborhood.\n.   \n.   @param src Input 8-bit, 16-bit unsigned or 32-bit float 1-channel or 8-bit 3-channel image.\n.   @param inpaintMask Inpainting mask, 8-bit 1-channel image. Non-zero pixels indicate the area that\n.   needs to be inpainted.\n.   @param dst Output image with the same size and type as src .\n.   @param inpaintRadius Radius of a circular neighborhood of each point inpainted that is considered\n.   by the algorithm.\n.   @param flags Inpainting method that could be cv::INPAINT_NS or cv::INPAINT_TELEA\n.   \n.   The function reconstructs the selected image area from the pixel near the area boundary. The\n.   function may be used to remove dust and scratches from a scanned photo, or to remove undesirable\n.   objects from still images or video. See <http://en.wikipedia.org/wiki/Inpainting> for more details.\n.   \n.   @note\n.      -   An example using the inpainting technique can be found at\n.           opencv_source_code/samples/cpp/inpaint.cpp\n.      -   (Python) An example using the inpainting technique can be found at\n.           opencv_source_code/samples/python/inpaint.py'
    ...

def insertChannel(src: Mat, dts: Mat, coi) -> typing.Any:
    'insertChannel(src, dst, coi) -> dst\n.   @brief Inserts a single channel to dst (coi is 0-based index)\n.   @param src input array\n.   @param dst output array\n.   @param coi index of channel for insertion\n.   @sa mixChannels, merge'
    ...

def integral(src: Mat, sum=..., sdepth=...) -> typing.Any:
    'integral(src[, sum[, sdepth]]) -> sum\n.   @overload'
    ...

def integral2(src: Mat, sum=..., sqsum=..., sdepth=..., sqdepth=...) -> typing.Any:
    'integral2(src[, sum[, sqsum[, sdepth[, sqdepth]]]]) -> sum, sqsum\n.   @overload'
    ...

def integral3(src: Mat, sum=..., sqsum=..., tilted=..., sdepth=..., sqdepth=...) -> typing.Any:
    'integral3(src[, sum[, sqsum[, tilted[, sdepth[, sqdepth]]]]]) -> sum, sqsum, tilted\n.   @brief Calculates the integral of an image.\n.   \n.   The function calculates one or more integral images for the source image as follows:\n.   \n.   \\f[\\texttt{sum} (X,Y) =  \\sum _{x<X,y<Y}  \\texttt{image} (x,y)\\f]\n.   \n.   \\f[\\texttt{sqsum} (X,Y) =  \\sum _{x<X,y<Y}  \\texttt{image} (x,y)^2\\f]\n.   \n.   \\f[\\texttt{tilted} (X,Y) =  \\sum _{y<Y,abs(x-X+1) \\leq Y-y-1}  \\texttt{image} (x,y)\\f]\n.   \n.   Using these integral images, you can calculate sum, mean, and standard deviation over a specific\n.   up-right or rotated rectangular region of the image in a constant time, for example:\n.   \n.   \\f[\\sum _{x_1 \\leq x < x_2,  \\, y_1  \\leq y < y_2}  \\texttt{image} (x,y) =  \\texttt{sum} (x_2,y_2)- \\texttt{sum} (x_1,y_2)- \\texttt{sum} (x_2,y_1)+ \\texttt{sum} (x_1,y_1)\\f]\n.   \n.   It makes possible to do a fast blurring or fast block correlation with a variable window size, for\n.   example. In case of multi-channel images, sums for each channel are accumulated independently.\n.   \n.   As a practical example, the next figure shows the calculation of the integral of a straight\n.   rectangle Rect(3,3,3,2) and of a tilted rectangle Rect(5,1,2,3) . The selected pixels in the\n.   original image are shown, as well as the relative pixels in the integral images sum and tilted .\n.   \n.   ![integral calculation example](pics/integral.png)\n.   \n.   @param src input image as \\f$W \\times H\\f$, 8-bit or floating-point (32f or 64f).\n.   @param sum integral image as \\f$(W+1)\\times (H+1)\\f$ , 32-bit integer or floating-point (32f or 64f).\n.   @param sqsum integral image for squared pixel values; it is \\f$(W+1)\\times (H+1)\\f$, double-precision\n.   floating-point (64f) array.\n.   @param tilted integral for the image rotated by 45 degrees; it is \\f$(W+1)\\times (H+1)\\f$ array with\n.   the same data type as sum.\n.   @param sdepth desired depth of the integral and the tilted integral images, CV_32S, CV_32F, or\n.   CV_64F.\n.   @param sqdepth desired depth of the integral image of squared pixel values, CV_32F or CV_64F.'
    ...

def intersectConvexConvex(_p1, _p2, _p12=..., handleNested=...) -> typing.Any:
    "intersectConvexConvex(_p1, _p2[, _p12[, handleNested]]) -> retval, _p12\n.   @brief Finds intersection of two convex polygons\n.   \n.   @param _p1 First polygon\n.   @param _p2 Second polygon\n.   @param _p12 Output polygon describing the intersecting area\n.   @param handleNested When true, an intersection is found if one of the polygons is fully enclosed in the other.\n.   When false, no intersection is found. If the polygons share a side or the vertex of one polygon lies on an edge\n.   of the other, they are not considered nested and an intersection will be found regardless of the value of handleNested.\n.   \n.   @returns Absolute value of area of intersecting polygon\n.   \n.   @note intersectConvexConvex doesn't confirm that both polygons are convex and will return invalid results if they aren't."
    ...

def invert(src: Mat, dts: Mat = ..., flags: int = ...) -> typing.Any:
    'invert(src[, dst[, flags]]) -> retval, dst\n.   @brief Finds the inverse or pseudo-inverse of a matrix.\n.   \n.   The function cv::invert inverts the matrix src and stores the result in dst\n.   . When the matrix src is singular or non-square, the function calculates\n.   the pseudo-inverse matrix (the dst matrix) so that norm(src\\*dst - I) is\n.   minimal, where I is an identity matrix.\n.   \n.   In case of the #DECOMP_LU method, the function returns non-zero value if\n.   the inverse has been successfully calculated and 0 if src is singular.\n.   \n.   In case of the #DECOMP_SVD method, the function returns the inverse\n.   condition number of src (the ratio of the smallest singular value to the\n.   largest singular value) and 0 if src is singular. The SVD method\n.   calculates a pseudo-inverse matrix if src is singular.\n.   \n.   Similarly to #DECOMP_LU, the method #DECOMP_CHOLESKY works only with\n.   non-singular square matrices that should also be symmetrical and\n.   positively defined. In this case, the function stores the inverted\n.   matrix in dst and returns non-zero. Otherwise, it returns 0.\n.   \n.   @param src input floating-point M x N matrix.\n.   @param dst output matrix of N x M size and the same type as src.\n.   @param flags inversion method (cv::DecompTypes)\n.   @sa solve, SVD'
    ...

def invertAffineTransform(M, iM=...) -> typing.Any:
    'invertAffineTransform(M[, iM]) -> iM\n.   @brief Inverts an affine transformation.\n.   \n.   The function computes an inverse affine transformation represented by \\f$2 \\times 3\\f$ matrix M:\n.   \n.   \\f[\\begin{bmatrix} a_{11} & a_{12} & b_1  \\\\ a_{21} & a_{22} & b_2 \\end{bmatrix}\\f]\n.   \n.   The result is also a \\f$2 \\times 3\\f$ matrix of the same type as M.\n.   \n.   @param M Original affine transformation.\n.   @param iM Output reverse affine transformation.'
    ...

def isContourConvex(contour) -> typing.Any:
    'isContourConvex(contour) -> retval\n.   @brief Tests a contour convexity.\n.   \n.   The function tests whether the input contour is convex or not. The contour must be simple, that is,\n.   without self-intersections. Otherwise, the function output is undefined.\n.   \n.   @param contour Input vector of 2D points, stored in std::vector\\<\\> or Mat'
    ...

def kmeans(data, K, bestLabels, criteria, attempts, flags: int, centers=...) -> typing.Any:
    'kmeans(data, K, bestLabels, criteria, attempts, flags[, centers]) -> retval, bestLabels, centers\n.   @brief Finds centers of clusters and groups input samples around the clusters.\n.   \n.   The function kmeans implements a k-means algorithm that finds the centers of cluster_count clusters\n.   and groups the input samples around the clusters. As an output, \\f$\\texttt{bestLabels}_i\\f$ contains a\n.   0-based cluster index for the sample stored in the \\f$i^{th}\\f$ row of the samples matrix.\n.   \n.   @note\n.   -   (Python) An example on K-means clustering can be found at\n.       opencv_source_code/samples/python/kmeans.py\n.   @param data Data for clustering. An array of N-Dimensional points with float coordinates is needed.\n.   Examples of this array can be:\n.   -   Mat points(count, 2, CV_32F);\n.   -   Mat points(count, 1, CV_32FC2);\n.   -   Mat points(1, count, CV_32FC2);\n.   -   std::vector\\<cv::Point2f\\> points(sampleCount);\n.   @param K Number of clusters to split the set by.\n.   @param bestLabels Input/output integer array that stores the cluster indices for every sample.\n.   @param criteria The algorithm termination criteria, that is, the maximum number of iterations and/or\n.   the desired accuracy. The accuracy is specified as criteria.epsilon. As soon as each of the cluster\n.   centers moves by less than criteria.epsilon on some iteration, the algorithm stops.\n.   @param attempts Flag to specify the number of times the algorithm is executed using different\n.   initial labellings. The algorithm returns the labels that yield the best compactness (see the last\n.   function parameter).\n.   @param flags Flag that can take values of cv::KmeansFlags\n.   @param centers Output matrix of the cluster centers, one row per each cluster center.\n.   @return The function returns the compactness measure that is computed as\n.   \\f[\\sum _i  \\| \\texttt{samples} _i -  \\texttt{centers} _{ \\texttt{labels} _i} \\| ^2\\f]\n.   after every attempt. The best (minimum) value is chosen and the corresponding labels and the\n.   compactness value are returned by the function. Basically, you can use only the core of the\n.   function, set the number of attempts to 1, initialize labels each time using a custom algorithm,\n.   pass them with the ( flags = #KMEANS_USE_INITIAL_LABELS ) flag, and then choose the best\n.   (most-compact) clustering.'
    ...

def line(img: Mat, pt1, pt2, color, thickness=..., lineType=..., shift=...) -> typing.Any:
    'line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img\n.   @brief Draws a line segment connecting two points.\n.   \n.   The function line draws the line segment between pt1 and pt2 points in the image. The line is\n.   clipped by the image boundaries. For non-antialiased lines with integer coordinates, the 8-connected\n.   or 4-connected Bresenham algorithm is used. Thick lines are drawn with rounding endings. Antialiased\n.   lines are drawn using Gaussian filtering.\n.   \n.   @param img Image.\n.   @param pt1 First point of the line segment.\n.   @param pt2 Second point of the line segment.\n.   @param color Line color.\n.   @param thickness Line thickness.\n.   @param lineType Type of the line. See #LineTypes.\n.   @param shift Number of fractional bits in the point coordinates.'
    ...

def linearPolar(src: Mat, center, maxRadius, flags: int, dts: Mat = ...) -> typing.Any:
    'linearPolar(src, center, maxRadius, flags[, dst]) -> dst\n.   @brief Remaps an image to polar coordinates space.\n.   \n.   @deprecated This function produces same result as cv::warpPolar(src, dst, src.size(), center, maxRadius, flags)\n.   \n.   @internal\n.   Transform the source image using the following transformation (See @ref polar_remaps_reference_image "Polar remaps reference image c)"):\n.   \\f[\\begin{array}{l}\n.     dst( \\rho , \\phi ) = src(x,y) \\\\\n.     dst.size() \\leftarrow src.size()\n.   \\end{array}\\f]\n.   \n.   where\n.   \\f[\\begin{array}{l}\n.     I = (dx,dy) = (x - center.x,y - center.y) \\\\\n.     \\rho = Kmag \\cdot \\texttt{magnitude} (I) ,\\\\\n.     \\phi = angle \\cdot \\texttt{angle} (I)\n.   \\end{array}\\f]\n.   \n.   and\n.   \\f[\\begin{array}{l}\n.     Kx = src.cols / maxRadius \\\\\n.     Ky = src.rows / 2\\Pi\n.   \\end{array}\\f]\n.   \n.   \n.   @param src Source image\n.   @param dst Destination image. It will have same size and type as src.\n.   @param center The transformation center;\n.   @param maxRadius The radius of the bounding circle to transform. It determines the inverse magnitude scale parameter too.\n.   @param flags A combination of interpolation methods, see #InterpolationFlags\n.   \n.   @note\n.   -   The function can not operate in-place.\n.   -   To calculate magnitude and angle in degrees #cartToPolar is used internally thus angles are measured from 0 to 360 with accuracy about 0.3 degrees.\n.   \n.   @sa cv::logPolar\n.   @endinternal'
    ...

def log(src: Mat, dts: Mat = ...) -> typing.Any:
    'log(src[, dst]) -> dst\n.   @brief Calculates the natural logarithm of every array element.\n.   \n.   The function cv::log calculates the natural logarithm of every element of the input array:\n.   \\f[\\texttt{dst} (I) =  \\log (\\texttt{src}(I)) \\f]\n.   \n.   Output on zero, negative and special (NaN, Inf) values is undefined.\n.   \n.   @param src input array.\n.   @param dst output array of the same size and type as src .\n.   @sa exp, cartToPolar, polarToCart, phase, pow, sqrt, magnitude'
    ...

def logPolar(src: Mat, center, M, flags: int, dts: Mat = ...) -> typing.Any:
    'logPolar(src, center, M, flags[, dst]) -> dst\n.   @brief Remaps an image to semilog-polar coordinates space.\n.   \n.   @deprecated This function produces same result as cv::warpPolar(src, dst, src.size(), center, maxRadius, flags+WARP_POLAR_LOG);\n.   \n.   @internal\n.   Transform the source image using the following transformation (See @ref polar_remaps_reference_image "Polar remaps reference image d)"):\n.   \\f[\\begin{array}{l}\n.     dst( \\rho , \\phi ) = src(x,y) \\\\\n.     dst.size() \\leftarrow src.size()\n.   \\end{array}\\f]\n.   \n.   where\n.   \\f[\\begin{array}{l}\n.     I = (dx,dy) = (x - center.x,y - center.y) \\\\\n.     \\rho = M \\cdot log_e(\\texttt{magnitude} (I)) ,\\\\\n.     \\phi = Kangle \\cdot \\texttt{angle} (I) \\\\\n.   \\end{array}\\f]\n.   \n.   and\n.   \\f[\\begin{array}{l}\n.     M = src.cols / log_e(maxRadius) \\\\\n.     Kangle = src.rows / 2\\Pi \\\\\n.   \\end{array}\\f]\n.   \n.   The function emulates the human "foveal" vision and can be used for fast scale and\n.   rotation-invariant template matching, for object tracking and so forth.\n.   @param src Source image\n.   @param dst Destination image. It will have same size and type as src.\n.   @param center The transformation center; where the output precision is maximal\n.   @param M Magnitude scale parameter. It determines the radius of the bounding circle to transform too.\n.   @param flags A combination of interpolation methods, see #InterpolationFlags\n.   \n.   @note\n.   -   The function can not operate in-place.\n.   -   To calculate magnitude and angle in degrees #cartToPolar is used internally thus angles are measured from 0 to 360 with accuracy about 0.3 degrees.\n.   \n.   @sa cv::linearPolar\n.   @endinternal'
    ...

def magnitude(x, y, magnitude=...) -> typing.Any:
    'magnitude(x, y[, magnitude]) -> magnitude\n.   @brief Calculates the magnitude of 2D vectors.\n.   \n.   The function cv::magnitude calculates the magnitude of 2D vectors formed\n.   from the corresponding elements of x and y arrays:\n.   \\f[\\texttt{dst} (I) =  \\sqrt{\\texttt{x}(I)^2 + \\texttt{y}(I)^2}\\f]\n.   @param x floating-point array of x-coordinates of the vectors.\n.   @param y floating-point array of y-coordinates of the vectors; it must\n.   have the same size as x.\n.   @param magnitude output array of the same size and type as x.\n.   @sa cartToPolar, polarToCart, phase, sqrt'
    ...

def matMulDeriv(A, B, dABdA=..., dABdB=...) -> typing.Any:
    'matMulDeriv(A, B[, dABdA[, dABdB]]) -> dABdA, dABdB\n.   @brief Computes partial derivatives of the matrix product for each multiplied matrix.\n.   \n.   @param A First multiplied matrix.\n.   @param B Second multiplied matrix.\n.   @param dABdA First output derivative matrix d(A\\*B)/dA of size\n.   \\f$\\texttt{A.rows*B.cols} \\times {A.rows*A.cols}\\f$ .\n.   @param dABdB Second output derivative matrix d(A\\*B)/dB of size\n.   \\f$\\texttt{A.rows*B.cols} \\times {B.rows*B.cols}\\f$ .\n.   \n.   The function computes partial derivatives of the elements of the matrix product \\f$A*B\\f$ with regard to\n.   the elements of each of the two input matrices. The function is used to compute the Jacobian\n.   matrices in stereoCalibrate but can also be used in any other similar optimization function.'
    ...

def matchShapes(contour1, contour2, method: int, parameter) -> typing.Any:
    'matchShapes(contour1, contour2, method, parameter) -> retval\n.   @brief Compares two shapes.\n.   \n.   The function compares two shapes. All three implemented methods use the Hu invariants (see #HuMoments)\n.   \n.   @param contour1 First contour or grayscale image.\n.   @param contour2 Second contour or grayscale image.\n.   @param method Comparison method, see #ShapeMatchModes\n.   @param parameter Method-specific parameter (not supported now).'
    ...

def matchTemplate(image: Mat, templ: Mat, method: int, result: Mat = ..., mask: typing.Optional[Mat] = ...) -> Mat:
    "matchTemplate(image, templ, method[, result[, mask]]) -> result\n.   @brief Compares a template against overlapped image regions.\n.   \n.   The function slides through image , compares the overlapped patches of size \\f$w \\times h\\f$ against\n.   templ using the specified method and stores the comparison results in result . #TemplateMatchModes\n.   describes the formulae for the available comparison methods ( \\f$I\\f$ denotes image, \\f$T\\f$\n.   template, \\f$R\\f$ result, \\f$M\\f$ the optional mask ). The summation is done over template and/or\n.   the image patch: \\f$x' = 0...w-1, y' = 0...h-1\\f$\n.   \n.   After the function finishes the comparison, the best matches can be found as global minimums (when\n.   #TM_SQDIFF was used) or maximums (when #TM_CCORR or #TM_CCOEFF was used) using the\n.   #minMaxLoc function. In case of a color image, template summation in the numerator and each sum in\n.   the denominator is done over all of the channels and separate mean values are used for each channel.\n.   That is, the function can take a color template and a color image. The result will still be a\n.   single-channel image, which is easier to analyze.\n.   \n.   @param image Image where the search is running. It must be 8-bit or 32-bit floating-point.\n.   @param templ Searched template. It must be not greater than the source image and have the same\n.   data type.\n.   @param result Map of comparison results. It must be single-channel 32-bit floating-point. If image\n.   is \\f$W \\times H\\f$ and templ is \\f$w \\times h\\f$ , then result is \\f$(W-w+1) \\times (H-h+1)\\f$ .\n.   @param method Parameter specifying the comparison method, see #TemplateMatchModes\n.   @param mask Optional mask. It must have the same size as templ. It must either have the same number\n.               of channels as template or only one channel, which is then used for all template and\n.               image channels. If the data type is #CV_8U, the mask is interpreted as a binary mask,\n.               meaning only elements where mask is nonzero are used and are kept unchanged independent\n.               of the actual mask value (weight equals 1). For data tpye #CV_32F, the mask values are\n.               used as weights. The exact formulas are documented in #TemplateMatchModes."
    ...

def max(src1: Mat, src2: Mat, dts: Mat = ...) -> typing.Any:
    'max(src1, src2[, dst]) -> dst\n.   @brief Calculates per-element maximum of two arrays or an array and a scalar.\n.   \n.   The function cv::max calculates the per-element maximum of two arrays:\n.   \\f[\\texttt{dst} (I)= \\max ( \\texttt{src1} (I), \\texttt{src2} (I))\\f]\n.   or array and a scalar:\n.   \\f[\\texttt{dst} (I)= \\max ( \\texttt{src1} (I), \\texttt{value} )\\f]\n.   @param src1 first input array.\n.   @param src2 second input array of the same size and type as src1 .\n.   @param dst output array of the same size and type as src1.\n.   @sa  min, compare, inRange, minMaxLoc, @ref MatrixExpressions'
    ...

def mean(src: Mat, mask: Mat = ...) -> typing.Any:
    "mean(src[, mask]) -> retval\n.   @brief Calculates an average (mean) of array elements.\n.   \n.   The function cv::mean calculates the mean value M of array elements,\n.   independently for each channel, and return it:\n.   \\f[\\begin{array}{l} N =  \\sum _{I: \\; \\texttt{mask} (I) \\ne 0} 1 \\\\ M_c =  \\left ( \\sum _{I: \\; \\texttt{mask} (I) \\ne 0}{ \\texttt{mtx} (I)_c} \\right )/N \\end{array}\\f]\n.   When all the mask elements are 0's, the function returns Scalar::all(0)\n.   @param src input array that should have from 1 to 4 channels so that the result can be stored in\n.   Scalar_ .\n.   @param mask optional operation mask.\n.   @sa  countNonZero, meanStdDev, norm, minMaxLoc"
    ...

def meanShift(probImage, window, criteria) -> typing.Any:
    'meanShift(probImage, window, criteria) -> retval, window\n.   @brief Finds an object on a back projection image.\n.   \n.   @param probImage Back projection of the object histogram. See calcBackProject for details.\n.   @param window Initial search window.\n.   @param criteria Stop criteria for the iterative search algorithm.\n.   returns\n.   :   Number of iterations CAMSHIFT took to converge.\n.   The function implements the iterative object search algorithm. It takes the input back projection of\n.   an object and the initial position. The mass center in window of the back projection image is\n.   computed and the search window center shifts to the mass center. The procedure is repeated until the\n.   specified number of iterations criteria.maxCount is done or until the window center shifts by less\n.   than criteria.epsilon. The algorithm is used inside CamShift and, unlike CamShift , the search\n.   window size or orientation do not change during the search. You can simply pass the output of\n.   calcBackProject to this function. But better results can be obtained if you pre-filter the back\n.   projection and remove the noise. For example, you can do this by retrieving connected components\n.   with findContours , throwing away contours with small area ( contourArea ), and rendering the\n.   remaining contours with drawContours.'
    ...

def meanStdDev(src: Mat, mean=..., stddev=..., mask: Mat = ...) -> typing.Any:
    "meanStdDev(src[, mean[, stddev[, mask]]]) -> mean, stddev\n.   Calculates a mean and standard deviation of array elements.\n.   \n.   The function cv::meanStdDev calculates the mean and the standard deviation M\n.   of array elements independently for each channel and returns it via the\n.   output parameters:\n.   \\f[\\begin{array}{l} N =  \\sum _{I, \\texttt{mask} (I)  \\ne 0} 1 \\\\ \\texttt{mean} _c =  \\frac{\\sum_{ I: \\; \\texttt{mask}(I) \\ne 0} \\texttt{src} (I)_c}{N} \\\\ \\texttt{stddev} _c =  \\sqrt{\\frac{\\sum_{ I: \\; \\texttt{mask}(I) \\ne 0} \\left ( \\texttt{src} (I)_c -  \\texttt{mean} _c \\right )^2}{N}} \\end{array}\\f]\n.   When all the mask elements are 0's, the function returns\n.   mean=stddev=Scalar::all(0).\n.   @note The calculated standard deviation is only the diagonal of the\n.   complete normalized covariance matrix. If the full matrix is needed, you\n.   can reshape the multi-channel array M x N to the single-channel array\n.   M\\*N x mtx.channels() (only possible when the matrix is continuous) and\n.   then pass the matrix to calcCovarMatrix .\n.   @param src input array that should have from 1 to 4 channels so that the results can be stored in\n.   Scalar_ 's.\n.   @param mean output parameter: calculated mean value.\n.   @param stddev output parameter: calculated standard deviation.\n.   @param mask optional operation mask.\n.   @sa  countNonZero, mean, norm, minMaxLoc, calcCovarMatrix"
    ...

def medianBlur(src: Mat, ksize, dts: Mat = ...) -> typing.Any:
    'medianBlur(src, ksize[, dst]) -> dst\n.   @brief Blurs an image using the median filter.\n.   \n.   The function smoothes an image using the median filter with the \\f$\\texttt{ksize} \\times\n.   \\texttt{ksize}\\f$ aperture. Each channel of a multi-channel image is processed independently.\n.   In-place operation is supported.\n.   \n.   @note The median filter uses #BORDER_REPLICATE internally to cope with border pixels, see #BorderTypes\n.   \n.   @param src input 1-, 3-, or 4-channel image; when ksize is 3 or 5, the image depth should be\n.   CV_8U, CV_16U, or CV_32F, for larger aperture sizes, it can only be CV_8U.\n.   @param dst destination array of the same size and type as src.\n.   @param ksize aperture linear size; it must be odd and greater than 1, for example: 3, 5, 7 ...\n.   @sa  bilateralFilter, blur, boxFilter, GaussianBlur'
    ...

def merge(mv, dts: Mat = ...) -> typing.Any:
    'merge(mv[, dst]) -> dst\n.   @overload\n.   @param mv input vector of matrices to be merged; all the matrices in mv must have the same\n.   size and the same depth.\n.   @param dst output array of the same size and the same depth as mv[0]; The number of channels will\n.   be the total number of channels in the matrix array.'
    ...

def min(src1: Mat, src2: Mat, dts: Mat = ...) -> typing.Any:
    'min(src1, src2[, dst]) -> dst\n.   @brief Calculates per-element minimum of two arrays or an array and a scalar.\n.   \n.   The function cv::min calculates the per-element minimum of two arrays:\n.   \\f[\\texttt{dst} (I)= \\min ( \\texttt{src1} (I), \\texttt{src2} (I))\\f]\n.   or array and a scalar:\n.   \\f[\\texttt{dst} (I)= \\min ( \\texttt{src1} (I), \\texttt{value} )\\f]\n.   @param src1 first input array.\n.   @param src2 second input array of the same size and type as src1.\n.   @param dst output array of the same size and type as src1.\n.   @sa max, compare, inRange, minMaxLoc'
    ...

def minAreaRect(points) -> typing.Any:
    'minAreaRect(points) -> retval\n.   @brief Finds a rotated rectangle of the minimum area enclosing the input 2D point set.\n.   \n.   The function calculates and returns the minimum-area bounding rectangle (possibly rotated) for a\n.   specified point set. Developer should keep in mind that the returned RotatedRect can contain negative\n.   indices when data is close to the containing Mat element boundary.\n.   \n.   @param points Input vector of 2D points, stored in std::vector\\<\\> or Mat'
    ...

def minEnclosingCircle(points) -> typing.Any:
    'minEnclosingCircle(points) -> center, radius\n.   @brief Finds a circle of the minimum area enclosing a 2D point set.\n.   \n.   The function finds the minimal enclosing circle of a 2D point set using an iterative algorithm.\n.   \n.   @param points Input vector of 2D points, stored in std::vector\\<\\> or Mat\n.   @param center Output center of the circle.\n.   @param radius Output radius of the circle.'
    ...

def minEnclosingTriangle(points, triangle=...) -> typing.Any:
    "minEnclosingTriangle(points[, triangle]) -> retval, triangle\n.   @brief Finds a triangle of minimum area enclosing a 2D point set and returns its area.\n.   \n.   The function finds a triangle of minimum area enclosing the given set of 2D points and returns its\n.   area. The output for a given 2D point set is shown in the image below. 2D points are depicted in\n.   *red* and the enclosing triangle in *yellow*.\n.   \n.   ![Sample output of the minimum enclosing triangle function](pics/minenclosingtriangle.png)\n.   \n.   The implementation of the algorithm is based on O'Rourke's @cite ORourke86 and Klee and Laskowski's\n.   @cite KleeLaskowski85 papers. O'Rourke provides a \\f$\\theta(n)\\f$ algorithm for finding the minimal\n.   enclosing triangle of a 2D convex polygon with n vertices. Since the #minEnclosingTriangle function\n.   takes a 2D point set as input an additional preprocessing step of computing the convex hull of the\n.   2D point set is required. The complexity of the #convexHull function is \\f$O(n log(n))\\f$ which is higher\n.   than \\f$\\theta(n)\\f$. Thus the overall complexity of the function is \\f$O(n log(n))\\f$.\n.   \n.   @param points Input vector of 2D points with depth CV_32S or CV_32F, stored in std::vector\\<\\> or Mat\n.   @param triangle Output vector of three 2D points defining the vertices of the triangle. The depth\n.   of the OutputArray must be CV_32F."
    ...

def minMaxLoc(src: Mat, mask: Mat = ...) -> typing.Tuple[float, float, typing.Tuple[int, int], typing.Tuple[int, int]]:
    'minMaxLoc(src[, mask]) -> minVal, maxVal, minLoc, maxLoc\n.   @brief Finds the global minimum and maximum in an array.\n.   \n.   The function cv::minMaxLoc finds the minimum and maximum element values and their positions. The\n.   extremums are searched across the whole array or, if mask is not an empty array, in the specified\n.   array region.\n.   \n.   The function do not work with multi-channel arrays. If you need to find minimum or maximum\n.   elements across all the channels, use Mat::reshape first to reinterpret the array as\n.   single-channel. Or you may extract the particular channel using either extractImageCOI , or\n.   mixChannels , or split .\n.   @param src input single-channel array.\n.   @param minVal pointer to the returned minimum value; NULL is used if not required.\n.   @param maxVal pointer to the returned maximum value; NULL is used if not required.\n.   @param minLoc pointer to the returned minimum location (in 2D case); NULL is used if not required.\n.   @param maxLoc pointer to the returned maximum location (in 2D case); NULL is used if not required.\n.   @param mask optional mask used to select a sub-array.\n.   @sa max, min, compare, inRange, extractImageCOI, mixChannels, split, Mat::reshape'
    ...

def mixChannels(src: Mat, dts: Mat, fromTo) -> typing.Any:
    'mixChannels(src, dst, fromTo) -> dst\n.   @overload\n.   @param src input array or vector of matrices; all of the matrices must have the same size and the\n.   same depth.\n.   @param dst output array or vector of matrices; all the matrices **must be allocated**; their size and\n.   depth must be the same as in src[0].\n.   @param fromTo array of index pairs specifying which channels are copied and where; fromTo[k\\*2] is\n.   a 0-based index of the input channel in src, fromTo[k\\*2+1] is an index of the output channel in\n.   dst; the continuous channel numbering is used: the first input image channels are indexed from 0 to\n.   src[0].channels()-1, the second input image channels are indexed from src[0].channels() to\n.   src[0].channels() + src[1].channels()-1, and so on, the same scheme is used for the output image\n.   channels; as a special case, when fromTo[k\\*2] is negative, the corresponding output channel is\n.   filled with zero .'
    ...

ml_ANN_MLP = _mod_cv2.ml_ANN_MLP
ml_Boost = _mod_cv2.ml_Boost
ml_DTrees = _mod_cv2.ml_DTrees
ml_EM = _mod_cv2.ml_EM
ml_KNearest = _mod_cv2.ml_KNearest
ml_LogisticRegression = _mod_cv2.ml_LogisticRegression
ml_NormalBayesClassifier = _mod_cv2.ml_NormalBayesClassifier
ml_ParamGrid = _mod_cv2.ml_ParamGrid
ml_RTrees = _mod_cv2.ml_RTrees
ml_SVM = _mod_cv2.ml_SVM
ml_SVMSGD = _mod_cv2.ml_SVMSGD
ml_StatModel = _mod_cv2.ml_StatModel
ml_TrainData = _mod_cv2.ml_TrainData
def moments(array, binaryImage=...) -> typing.Any:
    "moments(array[, binaryImage]) -> retval\n.   @brief Calculates all of the moments up to the third order of a polygon or rasterized shape.\n.   \n.   The function computes moments, up to the 3rd order, of a vector shape or a rasterized shape. The\n.   results are returned in the structure cv::Moments.\n.   \n.   @param array Raster image (single-channel, 8-bit or floating-point 2D array) or an array (\n.   \\f$1 \\times N\\f$ or \\f$N \\times 1\\f$ ) of 2D points (Point or Point2f ).\n.   @param binaryImage If it is true, all non-zero image pixels are treated as 1's. The parameter is\n.   used for images only.\n.   @returns moments.\n.   \n.   @note Only applicable to contour moments calculations from Python bindings: Note that the numpy\n.   type for the input array should be either np.int32 or np.float32.\n.   \n.   @sa  contourArea, arcLength"
    ...

def morphologyEx(src: Mat, op, kernel, dts: Mat = ..., anchor=..., iterations=..., borderType=..., borderValue=...) -> typing.Any:
    'morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) -> dst\n.   @brief Performs advanced morphological transformations.\n.   \n.   The function cv::morphologyEx can perform advanced morphological transformations using an erosion and dilation as\n.   basic operations.\n.   \n.   Any of the operations can be done in-place. In case of multi-channel images, each channel is\n.   processed independently.\n.   \n.   @param src Source image. The number of channels can be arbitrary. The depth should be one of\n.   CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.\n.   @param dst Destination image of the same size and type as source image.\n.   @param op Type of a morphological operation, see #MorphTypes\n.   @param kernel Structuring element. It can be created using #getStructuringElement.\n.   @param anchor Anchor position with the kernel. Negative values mean that the anchor is at the\n.   kernel center.\n.   @param iterations Number of times erosion and dilation are applied.\n.   @param borderType Pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not supported.\n.   @param borderValue Border value in case of a constant border. The default value has a special\n.   meaning.\n.   @sa  dilate, erode, getStructuringElement\n.   @note The number of iterations is the number of times erosion or dilatation operation will be applied.\n.   For instance, an opening operation (#MORPH_OPEN) with two iterations is equivalent to apply\n.   successively: erode -> erode -> dilate -> dilate (and not erode -> dilate -> erode -> dilate).'
    ...

def moveWindow(winname, x, y) -> typing.Any:
    'moveWindow(winname, x, y) -> None\n.   @brief Moves window to the specified position\n.   \n.   @param winname Name of the window.\n.   @param x The new x-coordinate of the window.\n.   @param y The new y-coordinate of the window.'
    ...

def mulSpectrums(a, b, flags: int, c=..., conjB=...) -> typing.Any:
    'mulSpectrums(a, b, flags[, c[, conjB]]) -> c\n.   @brief Performs the per-element multiplication of two Fourier spectrums.\n.   \n.   The function cv::mulSpectrums performs the per-element multiplication of the two CCS-packed or complex\n.   matrices that are results of a real or complex Fourier transform.\n.   \n.   The function, together with dft and idft , may be used to calculate convolution (pass conjB=false )\n.   or correlation (pass conjB=true ) of two arrays rapidly. When the arrays are complex, they are\n.   simply multiplied (per element) with an optional conjugation of the second-array elements. When the\n.   arrays are real, they are assumed to be CCS-packed (see dft for details).\n.   @param a first input array.\n.   @param b second input array of the same size and type as src1 .\n.   @param c output array of the same size and type as src1 .\n.   @param flags operation flags; currently, the only supported flag is cv::DFT_ROWS, which indicates that\n.   each row of src1 and src2 is an independent 1D Fourier spectrum. If you do not want to use this flag, then simply add a `0` as value.\n.   @param conjB optional flag that conjugates the second input array before the multiplication (true)\n.   or not (false).'
    ...

def mulTransposed(src: Mat, aTa, dts: Mat = ..., delta=..., scale=..., dtype=...) -> typing.Any:
    'mulTransposed(src, aTa[, dst[, delta[, scale[, dtype]]]]) -> dst\n.   @brief Calculates the product of a matrix and its transposition.\n.   \n.   The function cv::mulTransposed calculates the product of src and its\n.   transposition:\n.   \\f[\\texttt{dst} = \\texttt{scale} ( \\texttt{src} - \\texttt{delta} )^T ( \\texttt{src} - \\texttt{delta} )\\f]\n.   if aTa=true , and\n.   \\f[\\texttt{dst} = \\texttt{scale} ( \\texttt{src} - \\texttt{delta} ) ( \\texttt{src} - \\texttt{delta} )^T\\f]\n.   otherwise. The function is used to calculate the covariance matrix. With\n.   zero delta, it can be used as a faster substitute for general matrix\n.   product A\\*B when B=A\'\n.   @param src input single-channel matrix. Note that unlike gemm, the\n.   function can multiply not only floating-point matrices.\n.   @param dst output square matrix.\n.   @param aTa Flag specifying the multiplication ordering. See the\n.   description below.\n.   @param delta Optional delta matrix subtracted from src before the\n.   multiplication. When the matrix is empty ( delta=noArray() ), it is\n.   assumed to be zero, that is, nothing is subtracted. If it has the same\n.   size as src , it is simply subtracted. Otherwise, it is "repeated" (see\n.   repeat ) to cover the full src and then subtracted. Type of the delta\n.   matrix, when it is not empty, must be the same as the type of created\n.   output matrix. See the dtype parameter description below.\n.   @param scale Optional scale factor for the matrix product.\n.   @param dtype Optional type of the output matrix. When it is negative,\n.   the output matrix will have the same type as src . Otherwise, it will be\n.   type=CV_MAT_DEPTH(dtype) that should be either CV_32F or CV_64F .\n.   @sa calcCovarMatrix, gemm, repeat, reduce'
    ...

def multiply(src1: Mat, src2: Mat, dts: Mat = ..., scale=..., dtype=...) -> typing.Any:
    'multiply(src1, src2[, dst[, scale[, dtype]]]) -> dst\n.   @brief Calculates the per-element scaled product of two arrays.\n.   \n.   The function multiply calculates the per-element product of two arrays:\n.   \n.   \\f[\\texttt{dst} (I)= \\texttt{saturate} ( \\texttt{scale} \\cdot \\texttt{src1} (I)  \\cdot \\texttt{src2} (I))\\f]\n.   \n.   There is also a @ref MatrixExpressions -friendly variant of the first function. See Mat::mul .\n.   \n.   For a not-per-element matrix product, see gemm .\n.   \n.   @note Saturation is not applied when the output array has the depth\n.   CV_32S. You may even get result of an incorrect sign in the case of\n.   overflow.\n.   @param src1 first input array.\n.   @param src2 second input array of the same size and the same type as src1.\n.   @param dst output array of the same size and type as src1.\n.   @param scale optional scale factor.\n.   @param dtype optional depth of the output array\n.   @sa add, subtract, divide, scaleAdd, addWeighted, accumulate, accumulateProduct, accumulateSquare,\n.   Mat::convertTo'
    ...

def namedWindow(winname, flags: int = ...) -> typing.Any:
    'namedWindow(winname[, flags]) -> None\n.   @brief Creates a window.\n.   \n.   The function namedWindow creates a window that can be used as a placeholder for images and\n.   trackbars. Created windows are referred to by their names.\n.   \n.   If a window with the same name already exists, the function does nothing.\n.   \n.   You can call cv::destroyWindow or cv::destroyAllWindows to close the window and de-allocate any associated\n.   memory usage. For a simple program, you do not really have to call these functions because all the\n.   resources and windows of the application are closed automatically by the operating system upon exit.\n.   \n.   @note\n.   \n.   Qt backend supports additional flags:\n.    -   **WINDOW_NORMAL or WINDOW_AUTOSIZE:** WINDOW_NORMAL enables you to resize the\n.        window, whereas WINDOW_AUTOSIZE adjusts automatically the window size to fit the\n.        displayed image (see imshow ), and you cannot change the window size manually.\n.    -   **WINDOW_FREERATIO or WINDOW_KEEPRATIO:** WINDOW_FREERATIO adjusts the image\n.        with no respect to its ratio, whereas WINDOW_KEEPRATIO keeps the image ratio.\n.    -   **WINDOW_GUI_NORMAL or WINDOW_GUI_EXPANDED:** WINDOW_GUI_NORMAL is the old way to draw the window\n.        without statusbar and toolbar, whereas WINDOW_GUI_EXPANDED is a new enhanced GUI.\n.   By default, flags == WINDOW_AUTOSIZE | WINDOW_KEEPRATIO | WINDOW_GUI_EXPANDED\n.   \n.   @param winname Name of the window in the window caption that may be used as a window identifier.\n.   @param flags Flags of the window. The supported flags are: (cv::WindowFlags)'
    ...

def norm(src1: Mat, src2: Mat, normType: int = ..., mask: Mat = ...) -> float:
    'norm(src1, src2[, normType[, mask]]) -> retval\n.   @brief Calculates the  absolute norm of an array.\n.   \n.   This version of #norm calculates the absolute norm of src1. The type of norm to calculate is specified using #NormTypes.\n.   \n.   As example for one array consider the function \\f$r(x)= \\begin{pmatrix} x \\\\ 1-x \\end{pmatrix}, x \\in [-1;1]\\f$.\n.   The \\f$ L_{1}, L_{2} \\f$ and \\f$ L_{\\infty} \\f$ norm for the sample value \\f$r(-1) = \\begin{pmatrix} -1 \\\\ 2 \\end{pmatrix}\\f$\n.   is calculated as follows\n.   \\f{align*}\n.       \\| r(-1) \\|_{L_1} &= |-1| + |2| = 3 \\\\\n.       \\| r(-1) \\|_{L_2} &= \\sqrt{(-1)^{2} + (2)^{2}} = \\sqrt{5} \\\\\n.       \\| r(-1) \\|_{L_\\infty} &= \\max(|-1|,|2|) = 2\n.   \\f}\n.   and for \\f$r(0.5) = \\begin{pmatrix} 0.5 \\\\ 0.5 \\end{pmatrix}\\f$ the calculation is\n.   \\f{align*}\n.       \\| r(0.5) \\|_{L_1} &= |0.5| + |0.5| = 1 \\\\\n.       \\| r(0.5) \\|_{L_2} &= \\sqrt{(0.5)^{2} + (0.5)^{2}} = \\sqrt{0.5} \\\\\n.       \\| r(0.5) \\|_{L_\\infty} &= \\max(|0.5|,|0.5|) = 0.5.\n.   \\f}\n.   The following graphic shows all values for the three norm functions \\f$\\| r(x) \\|_{L_1}, \\| r(x) \\|_{L_2}\\f$ and \\f$\\| r(x) \\|_{L_\\infty}\\f$.\n.   It is notable that the \\f$ L_{1} \\f$ norm forms the upper and the \\f$ L_{\\infty} \\f$ norm forms the lower border for the example function \\f$ r(x) \\f$.\n.   ![Graphs for the different norm functions from the above example](pics/NormTypes_OneArray_1-2-INF.png)\n.   \n.   When the mask parameter is specified and it is not empty, the norm is\n.   \n.   If normType is not specified, #NORM_L2 is used.\n.   calculated only over the region specified by the mask.\n.   \n.   Multi-channel input arrays are treated as single-channel arrays, that is,\n.   the results for all channels are combined.\n.   \n.   Hamming norms can only be calculated with CV_8U depth arrays.\n.   \n.   @param src1 first input array.\n.   @param normType type of the norm (see #NormTypes).\n.   @param mask optional operation mask; it must have the same size as src1 and CV_8UC1 type.\n\n\n\nnorm(src1, src2[, normType[, mask]]) -> retval\n.   @brief Calculates an absolute difference norm or a relative difference norm.\n.   \n.   This version of cv::norm calculates the absolute difference norm\n.   or the relative difference norm of arrays src1 and src2.\n.   The type of norm to calculate is specified using #NormTypes.\n.   \n.   @param src1 first input array.\n.   @param src2 second input array of the same size and the same type as src1.\n.   @param normType type of the norm (see #NormTypes).\n.   @param mask optional operation mask; it must have the same size as src1 and CV_8UC1 type.'
    ...

def normalize(src: Mat, dts: Mat, alpha=..., beta=..., normType: int = ..., dtype=..., mask: Mat = ...) -> Mat:
    'normalize(src, dst[, alpha[, beta[, normType[, dtype[, mask]]]]]) -> dst\n.   @brief Normalizes the norm or value range of an array.\n.   \n.   The function cv::normalize normalizes scale and shift the input array elements so that\n.   \\f[\\| \\texttt{dst} \\| _{L_p}= \\texttt{alpha}\\f]\n.   (where p=Inf, 1 or 2) when normType=NORM_INF, NORM_L1, or NORM_L2, respectively; or so that\n.   \\f[\\min _I  \\texttt{dst} (I)= \\texttt{alpha} , \\, \\, \\max _I  \\texttt{dst} (I)= \\texttt{beta}\\f]\n.   \n.   when normType=NORM_MINMAX (for dense arrays only). The optional mask specifies a sub-array to be\n.   normalized. This means that the norm or min-n-max are calculated over the sub-array, and then this\n.   sub-array is modified to be normalized. If you want to only use the mask to calculate the norm or\n.   min-max but modify the whole array, you can use norm and Mat::convertTo.\n.   \n.   In case of sparse matrices, only the non-zero values are analyzed and transformed. Because of this,\n.   the range transformation for sparse matrices is not allowed since it can shift the zero level.\n.   \n.   Possible usage with some positive example data:\n.   @code{.cpp}\n.       vector<double> positiveData = { 2.0, 8.0, 10.0 };\n.       vector<double> normalizedData_l1, normalizedData_l2, normalizedData_inf, normalizedData_minmax;\n.   \n.       // Norm to probability (total count)\n.       // sum(numbers) = 20.0\n.       // 2.0      0.1     (2.0/20.0)\n.       // 8.0      0.4     (8.0/20.0)\n.       // 10.0     0.5     (10.0/20.0)\n.       normalize(positiveData, normalizedData_l1, 1.0, 0.0, NORM_L1);\n.   \n.       // Norm to unit vector: ||positiveData|| = 1.0\n.       // 2.0      0.15\n.       // 8.0      0.62\n.       // 10.0     0.77\n.       normalize(positiveData, normalizedData_l2, 1.0, 0.0, NORM_L2);\n.   \n.       // Norm to max element\n.       // 2.0      0.2     (2.0/10.0)\n.       // 8.0      0.8     (8.0/10.0)\n.       // 10.0     1.0     (10.0/10.0)\n.       normalize(positiveData, normalizedData_inf, 1.0, 0.0, NORM_INF);\n.   \n.       // Norm to range [0.0;1.0]\n.       // 2.0      0.0     (shift to left border)\n.       // 8.0      0.75    (6.0/8.0)\n.       // 10.0     1.0     (shift to right border)\n.       normalize(positiveData, normalizedData_minmax, 1.0, 0.0, NORM_MINMAX);\n.   @endcode\n.   \n.   @param src input array.\n.   @param dst output array of the same size as src .\n.   @param alpha norm value to normalize to or the lower range boundary in case of the range\n.   normalization.\n.   @param beta upper range boundary in case of the range normalization; it is not used for the norm\n.   normalization.\n.   @param normType normalization type (see cv::NormTypes).\n.   @param dtype when negative, the output array has the same type as src; otherwise, it has the same\n.   number of channels as src and the depth =CV_MAT_DEPTH(dtype).\n.   @param mask optional operation mask.\n.   @sa norm, Mat::convertTo, SparseMat::convertTo'
    ...

ocl_Device = _mod_cv2.ocl_Device
def patchNaNs(a, val=...) -> typing.Any:
    "patchNaNs(a[, val]) -> a\n.   @brief converts NaN's to the given number"
    ...

def pencilSketch(src: Mat, dts1: Mat = ..., dts2: Mat = ..., sigma_s=..., sigma_r=..., shade_factor=...) -> typing.Any:
    'pencilSketch(src[, dst1[, dst2[, sigma_s[, sigma_r[, shade_factor]]]]]) -> dst1, dst2\n.   @brief Pencil-like non-photorealistic line drawing\n.   \n.   @param src Input 8-bit 3-channel image.\n.   @param dst1 Output 8-bit 1-channel image.\n.   @param dst2 Output image with the same size and type as src.\n.   @param sigma_s %Range between 0 to 200.\n.   @param sigma_r %Range between 0 to 1.\n.   @param shade_factor %Range between 0 to 0.1.'
    ...

def perspectiveTransform(src: Mat, m, dts: Mat = ...) -> typing.Any:
    "perspectiveTransform(src, m[, dst]) -> dst\n.   @brief Performs the perspective matrix transformation of vectors.\n.   \n.   The function cv::perspectiveTransform transforms every element of src by\n.   treating it as a 2D or 3D vector, in the following way:\n.   \\f[(x, y, z)  \\rightarrow (x'/w, y'/w, z'/w)\\f]\n.   where\n.   \\f[(x', y', z', w') =  \\texttt{mat} \\cdot \\begin{bmatrix} x & y & z & 1  \\end{bmatrix}\\f]\n.   and\n.   \\f[w =  \\fork{w'}{if \\(w' \\ne 0\\)}{\\infty}{otherwise}\\f]\n.   \n.   Here a 3D vector transformation is shown. In case of a 2D vector\n.   transformation, the z component is omitted.\n.   \n.   @note The function transforms a sparse set of 2D or 3D vectors. If you\n.   want to transform an image using perspective transformation, use\n.   warpPerspective . If you have an inverse problem, that is, you want to\n.   compute the most probable perspective transformation out of several\n.   pairs of corresponding points, you can use getPerspectiveTransform or\n.   findHomography .\n.   @param src input two-channel or three-channel floating-point array; each\n.   element is a 2D/3D vector to be transformed.\n.   @param dst output array of the same size and type as src.\n.   @param m 3x3 or 4x4 floating-point transformation matrix.\n.   @sa  transform, warpPerspective, getPerspectiveTransform, findHomography"
    ...

def phase(x, y, angle=..., angleInDegrees=...) -> typing.Any:
    'phase(x, y[, angle[, angleInDegrees]]) -> angle\n.   @brief Calculates the rotation angle of 2D vectors.\n.   \n.   The function cv::phase calculates the rotation angle of each 2D vector that\n.   is formed from the corresponding elements of x and y :\n.   \\f[\\texttt{angle} (I) =  \\texttt{atan2} ( \\texttt{y} (I), \\texttt{x} (I))\\f]\n.   \n.   The angle estimation accuracy is about 0.3 degrees. When x(I)=y(I)=0 ,\n.   the corresponding angle(I) is set to 0.\n.   @param x input floating-point array of x-coordinates of 2D vectors.\n.   @param y input array of y-coordinates of 2D vectors; it must have the\n.   same size and the same type as x.\n.   @param angle output array of vector angles; it has the same size and\n.   same type as x .\n.   @param angleInDegrees when true, the function calculates the angle in\n.   degrees, otherwise, they are measured in radians.'
    ...

def phaseCorrelate(src1: Mat, src2: Mat, window=...) -> typing.Any:
    'phaseCorrelate(src1, src2[, window]) -> retval, response\n.   @brief The function is used to detect translational shifts that occur between two images.\n.   \n.   The operation takes advantage of the Fourier shift theorem for detecting the translational shift in\n.   the frequency domain. It can be used for fast image registration as well as motion estimation. For\n.   more information please see <http://en.wikipedia.org/wiki/Phase_correlation>\n.   \n.   Calculates the cross-power spectrum of two supplied source arrays. The arrays are padded if needed\n.   with getOptimalDFTSize.\n.   \n.   The function performs the following equations:\n.   - First it applies a Hanning window (see <http://en.wikipedia.org/wiki/Hann_function>) to each\n.   image to remove possible edge effects. This window is cached until the array size changes to speed\n.   up processing time.\n.   - Next it computes the forward DFTs of each source array:\n.   \\f[\\mathbf{G}_a = \\mathcal{F}\\{src_1\\}, \\; \\mathbf{G}_b = \\mathcal{F}\\{src_2\\}\\f]\n.   where \\f$\\mathcal{F}\\f$ is the forward DFT.\n.   - It then computes the cross-power spectrum of each frequency domain array:\n.   \\f[R = \\frac{ \\mathbf{G}_a \\mathbf{G}_b^*}{|\\mathbf{G}_a \\mathbf{G}_b^*|}\\f]\n.   - Next the cross-correlation is converted back into the time domain via the inverse DFT:\n.   \\f[r = \\mathcal{F}^{-1}\\{R\\}\\f]\n.   - Finally, it computes the peak location and computes a 5x5 weighted centroid around the peak to\n.   achieve sub-pixel accuracy.\n.   \\f[(\\Delta x, \\Delta y) = \\texttt{weightedCentroid} \\{\\arg \\max_{(x, y)}\\{r\\}\\}\\f]\n.   - If non-zero, the response parameter is computed as the sum of the elements of r within the 5x5\n.   centroid around the peak location. It is normalized to a maximum of 1 (meaning there is a single\n.   peak) and will be smaller when there are multiple peaks.\n.   \n.   @param src1 Source floating point array (CV_32FC1 or CV_64FC1)\n.   @param src2 Source floating point array (CV_32FC1 or CV_64FC1)\n.   @param window Floating point array with windowing coefficients to reduce edge effects (optional).\n.   @param response Signal power within the 5x5 centroid around the peak, between 0 and 1 (optional).\n.   @returns detected phase shift (sub-pixel) between the two arrays.\n.   \n.   @sa dft, getOptimalDFTSize, idft, mulSpectrums createHanningWindow'
    ...

def pointPolygonTest(contour, pt, measureDist) -> typing.Any:
    'pointPolygonTest(contour, pt, measureDist) -> retval\n.   @brief Performs a point-in-contour test.\n.   \n.   The function determines whether the point is inside a contour, outside, or lies on an edge (or\n.   coincides with a vertex). It returns positive (inside), negative (outside), or zero (on an edge)\n.   value, correspondingly. When measureDist=false , the return value is +1, -1, and 0, respectively.\n.   Otherwise, the return value is a signed distance between the point and the nearest contour edge.\n.   \n.   See below a sample output of the function where each image pixel is tested against the contour:\n.   \n.   ![sample output](pics/pointpolygon.png)\n.   \n.   @param contour Input contour.\n.   @param pt Point tested against the contour.\n.   @param measureDist If true, the function estimates the signed distance from the point to the\n.   nearest contour edge. Otherwise, the function only checks if the point is inside a contour or not.'
    ...

def polarToCart(magnitude, angle, x=..., y=..., angleInDegrees=...) -> typing.Any:
    'polarToCart(magnitude, angle[, x[, y[, angleInDegrees]]]) -> x, y\n.   @brief Calculates x and y coordinates of 2D vectors from their magnitude and angle.\n.   \n.   The function cv::polarToCart calculates the Cartesian coordinates of each 2D\n.   vector represented by the corresponding elements of magnitude and angle:\n.   \\f[\\begin{array}{l} \\texttt{x} (I) =  \\texttt{magnitude} (I) \\cos ( \\texttt{angle} (I)) \\\\ \\texttt{y} (I) =  \\texttt{magnitude} (I) \\sin ( \\texttt{angle} (I)) \\\\ \\end{array}\\f]\n.   \n.   The relative accuracy of the estimated coordinates is about 1e-6.\n.   @param magnitude input floating-point array of magnitudes of 2D vectors;\n.   it can be an empty matrix (=Mat()), in this case, the function assumes\n.   that all the magnitudes are =1; if it is not empty, it must have the\n.   same size and type as angle.\n.   @param angle input floating-point array of angles of 2D vectors.\n.   @param x output array of x-coordinates of 2D vectors; it has the same\n.   size and type as angle.\n.   @param y output array of y-coordinates of 2D vectors; it has the same\n.   size and type as angle.\n.   @param angleInDegrees when true, the input angles are measured in\n.   degrees, otherwise, they are measured in radians.\n.   @sa cartToPolar, magnitude, phase, exp, log, pow, sqrt'
    ...

def polylines(img: Mat, pts, isClosed, color, thickness=..., lineType=..., shift=...) -> typing.Any:
    'polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]]) -> img\n.   @brief Draws several polygonal curves.\n.   \n.   @param img Image.\n.   @param pts Array of polygonal curves.\n.   @param isClosed Flag indicating whether the drawn polylines are closed or not. If they are closed,\n.   the function draws a line from the last vertex of each curve to its first vertex.\n.   @param color Polyline color.\n.   @param thickness Thickness of the polyline edges.\n.   @param lineType Type of the line segments. See #LineTypes\n.   @param shift Number of fractional bits in the vertex coordinates.\n.   \n.   The function cv::polylines draws one or more polygonal curves.'
    ...

def pow(src: Mat, power, dts: Mat = ...) -> typing.Any:
    'pow(src, power[, dst]) -> dst\n.   @brief Raises every array element to a power.\n.   \n.   The function cv::pow raises every element of the input array to power :\n.   \\f[\\texttt{dst} (I) =  \\fork{\\texttt{src}(I)^{power}}{if \\(\\texttt{power}\\) is integer}{|\\texttt{src}(I)|^{power}}{otherwise}\\f]\n.   \n.   So, for a non-integer power exponent, the absolute values of input array\n.   elements are used. However, it is possible to get true values for\n.   negative values using some extra operations. In the example below,\n.   computing the 5th root of array src shows:\n.   @code{.cpp}\n.       Mat mask = src < 0;\n.       pow(src, 1./5, dst);\n.       subtract(Scalar::all(0), dst, dst, mask);\n.   @endcode\n.   For some values of power, such as integer values, 0.5 and -0.5,\n.   specialized faster algorithms are used.\n.   \n.   Special values (NaN, Inf) are not handled.\n.   @param src input array.\n.   @param power exponent of power.\n.   @param dst output array of the same size and type as src.\n.   @sa sqrt, exp, log, cartToPolar, polarToCart'
    ...

def preCornerDetect(src: Mat, ksize, dts: Mat = ..., borderType=...) -> typing.Any:
    'preCornerDetect(src, ksize[, dst[, borderType]]) -> dst\n.   @brief Calculates a feature map for corner detection.\n.   \n.   The function calculates the complex spatial derivative-based function of the source image\n.   \n.   \\f[\\texttt{dst} = (D_x  \\texttt{src} )^2  \\cdot D_{yy}  \\texttt{src} + (D_y  \\texttt{src} )^2  \\cdot D_{xx}  \\texttt{src} - 2 D_x  \\texttt{src} \\cdot D_y  \\texttt{src} \\cdot D_{xy}  \\texttt{src}\\f]\n.   \n.   where \\f$D_x\\f$,\\f$D_y\\f$ are the first image derivatives, \\f$D_{xx}\\f$,\\f$D_{yy}\\f$ are the second image\n.   derivatives, and \\f$D_{xy}\\f$ is the mixed derivative.\n.   \n.   The corners can be found as local maximums of the functions, as shown below:\n.   @code\n.       Mat corners, dilated_corners;\n.       preCornerDetect(image, corners, 3);\n.       // dilation with 3x3 rectangular structuring element\n.       dilate(corners, dilated_corners, Mat(), 1);\n.       Mat corner_mask = corners == dilated_corners;\n.   @endcode\n.   \n.   @param src Source single-channel 8-bit of floating-point image.\n.   @param dst Output image that has the type CV_32F and the same size as src .\n.   @param ksize %Aperture size of the Sobel .\n.   @param borderType Pixel extrapolation method. See #BorderTypes. #BORDER_WRAP is not supported.'
    ...

def projectPoints(objectPoints, rvec, tvec, cameraMatrix, distCoeffs, imagePoints=..., jacobian=..., aspectRatio=...) -> typing.Any:
    'projectPoints(objectPoints, rvec, tvec, cameraMatrix, distCoeffs[, imagePoints[, jacobian[, aspectRatio]]]) -> imagePoints, jacobian\n.   @brief Projects 3D points to an image plane.\n.   \n.   @param objectPoints Array of object points expressed wrt. the world coordinate frame. A 3xN/Nx3\n.   1-channel or 1xN/Nx1 3-channel (or vector\\<Point3f\\> ), where N is the number of points in the view.\n.   @param rvec The rotation vector (@ref Rodrigues) that, together with tvec, performs a change of\n.   basis from world to camera coordinate system, see @ref calibrateCamera for details.\n.   @param tvec The translation vector, see parameter description above.\n.   @param cameraMatrix Camera matrix \\f$A = \\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{_1}\\f$ .\n.   @param distCoeffs Input vector of distortion coefficients\n.   \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6 [, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$ of\n.   4, 5, 8, 12 or 14 elements. If the vector is empty, the zero distortion coefficients are assumed.\n.   @param imagePoints Output array of image points, 1xN/Nx1 2-channel, or\n.   vector\\<Point2f\\> .\n.   @param jacobian Optional output 2Nx(10+\\<numDistCoeffs\\>) jacobian matrix of derivatives of image\n.   points with respect to components of the rotation vector, translation vector, focal lengths,\n.   coordinates of the principal point and the distortion coefficients. In the old interface different\n.   components of the jacobian are returned via different output parameters.\n.   @param aspectRatio Optional "fixed aspect ratio" parameter. If the parameter is not 0, the\n.   function assumes that the aspect ratio (\\f$f_x / f_y\\f$) is fixed and correspondingly adjusts the\n.   jacobian matrix.\n.   \n.   The function computes the 2D projections of 3D points to the image plane, given intrinsic and\n.   extrinsic camera parameters. Optionally, the function computes Jacobians -matrices of partial\n.   derivatives of image points coordinates (as functions of all the input parameters) with respect to\n.   the particular parameters, intrinsic and/or extrinsic. The Jacobians are used during the global\n.   optimization in @ref calibrateCamera, @ref solvePnP, and @ref stereoCalibrate. The function itself\n.   can also be used to compute a re-projection error, given the current intrinsic and extrinsic\n.   parameters.\n.   \n.   @note By setting rvec = tvec = \\f$[0, 0, 0]\\f$, or by setting cameraMatrix to a 3x3 identity matrix,\n.   or by passing zero distortion coefficients, one can get various useful partial cases of the\n.   function. This means, one can compute the distorted coordinates for a sparse set of points or apply\n.   a perspective transformation (and also compute the derivatives) in the ideal zero-distortion setup.'
    ...

def putText(img: Mat, text, org, fontFace, fontScale, color, thickness=..., lineType=..., bottomLeftOrigin=...) -> typing.Any:
    'putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) -> img\n.   @brief Draws a text string.\n.   \n.   The function cv::putText renders the specified text string in the image. Symbols that cannot be rendered\n.   using the specified font are replaced by question marks. See #getTextSize for a text rendering code\n.   example.\n.   \n.   @param img Image.\n.   @param text Text string to be drawn.\n.   @param org Bottom-left corner of the text string in the image.\n.   @param fontFace Font type, see #HersheyFonts.\n.   @param fontScale Font scale factor that is multiplied by the font-specific base size.\n.   @param color Text color.\n.   @param thickness Thickness of the lines used to draw a text.\n.   @param lineType Line type. See #LineTypes\n.   @param bottomLeftOrigin When true, the image data origin is at the bottom-left corner. Otherwise,\n.   it is at the top-left corner.'
    ...

def pyrDown(src: Mat, dts: Mat = ..., dstsize=..., borderType=...) -> typing.Any:
    "pyrDown(src[, dst[, dstsize[, borderType]]]) -> dst\n.   @brief Blurs an image and downsamples it.\n.   \n.   By default, size of the output image is computed as `Size((src.cols+1)/2, (src.rows+1)/2)`, but in\n.   any case, the following conditions should be satisfied:\n.   \n.   \\f[\\begin{array}{l} | \\texttt{dstsize.width} *2-src.cols| \\leq 2 \\\\ | \\texttt{dstsize.height} *2-src.rows| \\leq 2 \\end{array}\\f]\n.   \n.   The function performs the downsampling step of the Gaussian pyramid construction. First, it\n.   convolves the source image with the kernel:\n.   \n.   \\f[\\frac{1}{256} \\begin{bmatrix} 1 & 4 & 6 & 4 & 1  \\\\ 4 & 16 & 24 & 16 & 4  \\\\ 6 & 24 & 36 & 24 & 6  \\\\ 4 & 16 & 24 & 16 & 4  \\\\ 1 & 4 & 6 & 4 & 1 \\end{bmatrix}\\f]\n.   \n.   Then, it downsamples the image by rejecting even rows and columns.\n.   \n.   @param src input image.\n.   @param dst output image; it has the specified size and the same type as src.\n.   @param dstsize size of the output image.\n.   @param borderType Pixel extrapolation method, see #BorderTypes (#BORDER_CONSTANT isn't supported)"
    ...

def pyrMeanShiftFiltering(src: Mat, sp, sr, dts: Mat = ..., maxLevel=..., termcrit=...) -> typing.Any:
    'pyrMeanShiftFiltering(src, sp, sr[, dst[, maxLevel[, termcrit]]]) -> dst\n.   @brief Performs initial step of meanshift segmentation of an image.\n.   \n.   The function implements the filtering stage of meanshift segmentation, that is, the output of the\n.   function is the filtered "posterized" image with color gradients and fine-grain texture flattened.\n.   At every pixel (X,Y) of the input image (or down-sized input image, see below) the function executes\n.   meanshift iterations, that is, the pixel (X,Y) neighborhood in the joint space-color hyperspace is\n.   considered:\n.   \n.   \\f[(x,y): X- \\texttt{sp} \\le x  \\le X+ \\texttt{sp} , Y- \\texttt{sp} \\le y  \\le Y+ \\texttt{sp} , ||(R,G,B)-(r,g,b)||   \\le \\texttt{sr}\\f]\n.   \n.   where (R,G,B) and (r,g,b) are the vectors of color components at (X,Y) and (x,y), respectively\n.   (though, the algorithm does not depend on the color space used, so any 3-component color space can\n.   be used instead). Over the neighborhood the average spatial value (X\',Y\') and average color vector\n.   (R\',G\',B\') are found and they act as the neighborhood center on the next iteration:\n.   \n.   \\f[(X,Y)~(X\',Y\'), (R,G,B)~(R\',G\',B\').\\f]\n.   \n.   After the iterations over, the color components of the initial pixel (that is, the pixel from where\n.   the iterations started) are set to the final value (average color at the last iteration):\n.   \n.   \\f[I(X,Y) <- (R*,G*,B*)\\f]\n.   \n.   When maxLevel \\> 0, the gaussian pyramid of maxLevel+1 levels is built, and the above procedure is\n.   run on the smallest layer first. After that, the results are propagated to the larger layer and the\n.   iterations are run again only on those pixels where the layer colors differ by more than sr from the\n.   lower-resolution layer of the pyramid. That makes boundaries of color regions sharper. Note that the\n.   results will be actually different from the ones obtained by running the meanshift procedure on the\n.   whole original image (i.e. when maxLevel==0).\n.   \n.   @param src The source 8-bit, 3-channel image.\n.   @param dst The destination image of the same format and the same size as the source.\n.   @param sp The spatial window radius.\n.   @param sr The color window radius.\n.   @param maxLevel Maximum level of the pyramid for the segmentation.\n.   @param termcrit Termination criteria: when to stop meanshift iterations.'
    ...

def pyrUp(src: Mat, dts: Mat = ..., dstsize=..., borderType=...) -> typing.Any:
    'pyrUp(src[, dst[, dstsize[, borderType]]]) -> dst\n.   @brief Upsamples an image and then blurs it.\n.   \n.   By default, size of the output image is computed as `Size(src.cols\\*2, (src.rows\\*2)`, but in any\n.   case, the following conditions should be satisfied:\n.   \n.   \\f[\\begin{array}{l} | \\texttt{dstsize.width} -src.cols*2| \\leq  ( \\texttt{dstsize.width}   \\mod  2)  \\\\ | \\texttt{dstsize.height} -src.rows*2| \\leq  ( \\texttt{dstsize.height}   \\mod  2) \\end{array}\\f]\n.   \n.   The function performs the upsampling step of the Gaussian pyramid construction, though it can\n.   actually be used to construct the Laplacian pyramid. First, it upsamples the source image by\n.   injecting even zero rows and columns and then convolves the result with the same kernel as in\n.   pyrDown multiplied by 4.\n.   \n.   @param src input image.\n.   @param dst output image. It has the specified size and the same type as src .\n.   @param dstsize size of the output image.\n.   @param borderType Pixel extrapolation method, see #BorderTypes (only #BORDER_DEFAULT is supported)'
    ...

def randShuffle(dts: Mat, iterFactor=...) -> typing.Any:
    'randShuffle(dst[, iterFactor]) -> dst\n.   @brief Shuffles the array elements randomly.\n.   \n.   The function cv::randShuffle shuffles the specified 1D array by randomly choosing pairs of elements and\n.   swapping them. The number of such swap operations will be dst.rows\\*dst.cols\\*iterFactor .\n.   @param dst input/output numerical 1D array.\n.   @param iterFactor scale factor that determines the number of random swap operations (see the details\n.   below).\n.   @param rng optional random number generator used for shuffling; if it is zero, theRNG () is used\n.   instead.\n.   @sa RNG, sort'
    ...

def randn(dts: Mat, mean, stddev) -> typing.Any:
    'randn(dst, mean, stddev) -> dst\n.   @brief Fills the array with normally distributed random numbers.\n.   \n.   The function cv::randn fills the matrix dst with normally distributed random numbers with the specified\n.   mean vector and the standard deviation matrix. The generated random numbers are clipped to fit the\n.   value range of the output array data type.\n.   @param dst output array of random numbers; the array must be pre-allocated and have 1 to 4 channels.\n.   @param mean mean value (expectation) of the generated random numbers.\n.   @param stddev standard deviation of the generated random numbers; it can be either a vector (in\n.   which case a diagonal standard deviation matrix is assumed) or a square matrix.\n.   @sa RNG, randu'
    ...

def randu(dts: Mat, low, high) -> typing.Any:
    'randu(dst, low, high) -> dst\n.   @brief Generates a single uniformly-distributed random number or an array of random numbers.\n.   \n.   Non-template variant of the function fills the matrix dst with uniformly-distributed\n.   random numbers from the specified range:\n.   \\f[\\texttt{low} _c  \\leq \\texttt{dst} (I)_c <  \\texttt{high} _c\\f]\n.   @param dst output array of random numbers; the array must be pre-allocated.\n.   @param low inclusive lower boundary of the generated random numbers.\n.   @param high exclusive upper boundary of the generated random numbers.\n.   @sa RNG, randn, theRNG'
    ...

def readOpticalFlow(path) -> typing.Any:
    'readOpticalFlow(path) -> retval\n.   @brief Read a .flo file\n.   \n.    @param path Path to the file to be loaded\n.   \n.    The function readOpticalFlow loads a flow field from a file and returns it as a single matrix.\n.    Resulting Mat has a type CV_32FC2 - floating-point, 2-channel. First channel corresponds to the\n.    flow in the horizontal direction (u), second - vertical (v).'
    ...

def recoverPose(E, points1, points2, cameraMatrix, R=..., t=..., mask: Mat = ...) -> typing.Any:
    "recoverPose(E, points1, points2, cameraMatrix[, R[, t[, mask]]]) -> retval, R, t, mask\n.   @brief Recovers the relative camera rotation and the translation from an estimated essential\n.   matrix and the corresponding points in two images, using cheirality check. Returns the number of\n.   inliers that pass the check.\n.   \n.   @param E The input essential matrix.\n.   @param points1 Array of N 2D points from the first image. The point coordinates should be\n.   floating-point (single or double precision).\n.   @param points2 Array of the second image points of the same size and format as points1 .\n.   @param cameraMatrix Camera matrix \\f$A = \\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\\f$ .\n.   Note that this function assumes that points1 and points2 are feature points from cameras with the\n.   same camera matrix.\n.   @param R Output rotation matrix. Together with the translation vector, this matrix makes up a tuple\n.   that performs a change of basis from the first camera's coordinate system to the second camera's\n.   coordinate system. Note that, in general, t can not be used for this tuple, see the parameter\n.   described below.\n.   @param t Output translation vector. This vector is obtained by @ref decomposeEssentialMat and\n.   therefore is only known up to scale, i.e. t is the direction of the translation vector and has unit\n.   length.\n.   @param mask Input/output mask for inliers in points1 and points2. If it is not empty, then it marks\n.   inliers in points1 and points2 for then given essential matrix E. Only these inliers will be used to\n.   recover pose. In the output mask only inliers which pass the cheirality check.\n.   \n.   This function decomposes an essential matrix using @ref decomposeEssentialMat and then verifies\n.   possible pose hypotheses by doing cheirality check. The cheirality check means that the\n.   triangulated 3D points should have positive depth. Some details can be found in @cite Nister03.\n.   \n.   This function can be used to process the output E and mask from @ref findEssentialMat. In this\n.   scenario, points1 and points2 are the same input for findEssentialMat.:\n.   @code\n.       // Example. Estimation of fundamental matrix using the RANSAC algorithm\n.       int point_count = 100;\n.       vector<Point2f> points1(point_count);\n.       vector<Point2f> points2(point_count);\n.   \n.       // initialize the points here ...\n.       for( int i = 0; i < point_count; i++ )\n.       {\n.           points1[i] = ...;\n.           points2[i] = ...;\n.       }\n.   \n.       // cametra matrix with both focal lengths = 1, and principal point = (0, 0)\n.       Mat cameraMatrix = Mat::eye(3, 3, CV_64F);\n.   \n.       Mat E, R, t, mask;\n.   \n.       E = findEssentialMat(points1, points2, cameraMatrix, RANSAC, 0.999, 1.0, mask);\n.       recoverPose(E, points1, points2, cameraMatrix, R, t, mask);\n.   @endcode\n\n\n\nrecoverPose(E, points1, points2[, R[, t[, focal[, pp[, mask]]]]]) -> retval, R, t, mask\n.   @overload\n.   @param E The input essential matrix.\n.   @param points1 Array of N 2D points from the first image. The point coordinates should be\n.   floating-point (single or double precision).\n.   @param points2 Array of the second image points of the same size and format as points1 .\n.   @param R Output rotation matrix. Together with the translation vector, this matrix makes up a tuple\n.   that performs a change of basis from the first camera's coordinate system to the second camera's\n.   coordinate system. Note that, in general, t can not be used for this tuple, see the parameter\n.   description below.\n.   @param t Output translation vector. This vector is obtained by @ref decomposeEssentialMat and\n.   therefore is only known up to scale, i.e. t is the direction of the translation vector and has unit\n.   length.\n.   @param focal Focal length of the camera. Note that this function assumes that points1 and points2\n.   are feature points from cameras with same focal length and principal point.\n.   @param pp principal point of the camera.\n.   @param mask Input/output mask for inliers in points1 and points2. If it is not empty, then it marks\n.   inliers in points1 and points2 for then given essential matrix E. Only these inliers will be used to\n.   recover pose. In the output mask only inliers which pass the cheirality check.\n.   \n.   This function differs from the one above that it computes camera matrix from focal length and\n.   principal point:\n.   \n.   \\f[A =\n.   \\begin{bmatrix}\n.   f & 0 & x_{pp}  \\\\\n.   0 & f & y_{pp}  \\\\\n.   0 & 0 & 1\n.   \\end{bmatrix}\\f]\n\n\n\nrecoverPose(E, points1, points2, cameraMatrix, distanceThresh[, R[, t[, mask[, triangulatedPoints]]]]) -> retval, R, t, mask, triangulatedPoints\n.   @overload\n.   @param E The input essential matrix.\n.   @param points1 Array of N 2D points from the first image. The point coordinates should be\n.   floating-point (single or double precision).\n.   @param points2 Array of the second image points of the same size and format as points1.\n.   @param cameraMatrix Camera matrix \\f$A = \\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\\f$ .\n.   Note that this function assumes that points1 and points2 are feature points from cameras with the\n.   same camera matrix.\n.   @param R Output rotation matrix. Together with the translation vector, this matrix makes up a tuple\n.   that performs a change of basis from the first camera's coordinate system to the second camera's\n.   coordinate system. Note that, in general, t can not be used for this tuple, see the parameter\n.   description below.\n.   @param t Output translation vector. This vector is obtained by @ref decomposeEssentialMat and\n.   therefore is only known up to scale, i.e. t is the direction of the translation vector and has unit\n.   length.\n.   @param distanceThresh threshold distance which is used to filter out far away points (i.e. infinite\n.   points).\n.   @param mask Input/output mask for inliers in points1 and points2. If it is not empty, then it marks\n.   inliers in points1 and points2 for then given essential matrix E. Only these inliers will be used to\n.   recover pose. In the output mask only inliers which pass the cheirality check.\n.   @param triangulatedPoints 3D points which were reconstructed by triangulation.\n.   \n.   This function differs from the one above that it outputs the triangulated 3D point that are used for\n.   the cheirality check."
    ...

def rectangle(img: Mat, pt1, pt2, color, thickness=..., lineType=..., shift=...) -> typing.Any:
    'rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img\n.   @brief Draws a simple, thick, or filled up-right rectangle.\n.   \n.   The function cv::rectangle draws a rectangle outline or a filled rectangle whose two opposite corners\n.   are pt1 and pt2.\n.   \n.   @param img Image.\n.   @param pt1 Vertex of the rectangle.\n.   @param pt2 Vertex of the rectangle opposite to pt1 .\n.   @param color Rectangle color or brightness (grayscale image).\n.   @param thickness Thickness of lines that make up the rectangle. Negative values, like #FILLED,\n.   mean that the function has to draw a filled rectangle.\n.   @param lineType Type of the line. See #LineTypes\n.   @param shift Number of fractional bits in the point coordinates.\n\n\n\nrectangle(img, rec, color[, thickness[, lineType[, shift]]]) -> img\n.   @overload\n.   \n.   use `rec` parameter as alternative specification of the drawn rectangle: `r.tl() and\n.   r.br()-Point(1,1)` are opposite corners'
    ...

def rectify3Collinear(cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, cameraMatrix3, distCoeffs3, imgpt1, imgpt3, imageSize, R12, T12, R13, T13, alpha, newImgSize, flags: int, R1=..., R2=..., R3=..., P1=..., P2=..., P3=..., Q=...) -> typing.Any:
    'rectify3Collinear(cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, cameraMatrix3, distCoeffs3, imgpt1, imgpt3, imageSize, R12, T12, R13, T13, alpha, newImgSize, flags[, R1[, R2[, R3[, P1[, P2[, P3[, Q]]]]]]]) -> retval, R1, R2, R3, P1, P2, P3, Q, roi1, roi2\n.'
    ...

def redirectError(onError) -> typing.Any:
    'redirectError(onError) -> None'
    ...

def reduce(src: Mat, dim, rtype, dts: Mat = ..., dtype=...) -> typing.Any:
    'reduce(src, dim, rtype[, dst[, dtype]]) -> dst\n.   @brief Reduces a matrix to a vector.\n.   \n.   The function #reduce reduces the matrix to a vector by treating the matrix rows/columns as a set of\n.   1D vectors and performing the specified operation on the vectors until a single row/column is\n.   obtained. For example, the function can be used to compute horizontal and vertical projections of a\n.   raster image. In case of #REDUCE_MAX and #REDUCE_MIN , the output image should have the same type as the source one.\n.   In case of #REDUCE_SUM and #REDUCE_AVG , the output may have a larger element bit-depth to preserve accuracy.\n.   And multi-channel arrays are also supported in these two reduction modes.\n.   \n.   The following code demonstrates its usage for a single channel matrix.\n.   @snippet snippets/core_reduce.cpp example\n.   \n.   And the following code demonstrates its usage for a two-channel matrix.\n.   @snippet snippets/core_reduce.cpp example2\n.   \n.   @param src input 2D matrix.\n.   @param dst output vector. Its size and type is defined by dim and dtype parameters.\n.   @param dim dimension index along which the matrix is reduced. 0 means that the matrix is reduced to\n.   a single row. 1 means that the matrix is reduced to a single column.\n.   @param rtype reduction operation that could be one of #ReduceTypes\n.   @param dtype when negative, the output vector will have the same type as the input matrix,\n.   otherwise, its type will be CV_MAKE_TYPE(CV_MAT_DEPTH(dtype), src.channels()).\n.   @sa repeat'
    ...

def remap(src: Mat, map1, map2, interpolation: int, dts: Mat = ..., borderMode=..., borderValue=...) -> typing.Any:
    'remap(src, map1, map2, interpolation[, dst[, borderMode[, borderValue]]]) -> dst\n.   @brief Applies a generic geometrical transformation to an image.\n.   \n.   The function remap transforms the source image using the specified map:\n.   \n.   \\f[\\texttt{dst} (x,y) =  \\texttt{src} (map_x(x,y),map_y(x,y))\\f]\n.   \n.   where values of pixels with non-integer coordinates are computed using one of available\n.   interpolation methods. \\f$map_x\\f$ and \\f$map_y\\f$ can be encoded as separate floating-point maps\n.   in \\f$map_1\\f$ and \\f$map_2\\f$ respectively, or interleaved floating-point maps of \\f$(x,y)\\f$ in\n.   \\f$map_1\\f$, or fixed-point maps created by using convertMaps. The reason you might want to\n.   convert from floating to fixed-point representations of a map is that they can yield much faster\n.   (\\~2x) remapping operations. In the converted case, \\f$map_1\\f$ contains pairs (cvFloor(x),\n.   cvFloor(y)) and \\f$map_2\\f$ contains indices in a table of interpolation coefficients.\n.   \n.   This function cannot operate in-place.\n.   \n.   @param src Source image.\n.   @param dst Destination image. It has the same size as map1 and the same type as src .\n.   @param map1 The first map of either (x,y) points or just x values having the type CV_16SC2 ,\n.   CV_32FC1, or CV_32FC2. See convertMaps for details on converting a floating point\n.   representation to fixed-point for speed.\n.   @param map2 The second map of y values having the type CV_16UC1, CV_32FC1, or none (empty map\n.   if map1 is (x,y) points), respectively.\n.   @param interpolation Interpolation method (see #InterpolationFlags). The method #INTER_AREA is\n.   not supported by this function.\n.   @param borderMode Pixel extrapolation method (see #BorderTypes). When\n.   borderMode=#BORDER_TRANSPARENT, it means that the pixels in the destination image that\n.   corresponds to the "outliers" in the source image are not modified by the function.\n.   @param borderValue Value used in case of a constant border. By default, it is 0.\n.   @note\n.   Due to current implementation limitations the size of an input and output images should be less than 32767x32767.'
    ...

def repeat(src: Mat, ny, nx, dts: Mat = ...) -> typing.Any:
    'repeat(src, ny, nx[, dst]) -> dst\n.   @brief Fills the output array with repeated copies of the input array.\n.   \n.   The function cv::repeat duplicates the input array one or more times along each of the two axes:\n.   \\f[\\texttt{dst} _{ij}= \\texttt{src} _{i\\mod src.rows, \\; j\\mod src.cols }\\f]\n.   The second variant of the function is more convenient to use with @ref MatrixExpressions.\n.   @param src input array to replicate.\n.   @param ny Flag to specify how many times the `src` is repeated along the\n.   vertical axis.\n.   @param nx Flag to specify how many times the `src` is repeated along the\n.   horizontal axis.\n.   @param dst output array of the same type as `src`.\n.   @sa cv::reduce'
    ...

def reprojectImageTo3D(disparity, Q, _3dImage=..., handleMissingValues=..., ddepth=...) -> typing.Any:
    "reprojectImageTo3D(disparity, Q[, _3dImage[, handleMissingValues[, ddepth]]]) -> _3dImage\n.   @brief Reprojects a disparity image to 3D space.\n.   \n.   @param disparity Input single-channel 8-bit unsigned, 16-bit signed, 32-bit signed or 32-bit\n.   floating-point disparity image. The values of 8-bit / 16-bit signed formats are assumed to have no\n.   fractional bits. If the disparity is 16-bit signed format, as computed by @ref StereoBM or\n.   @ref StereoSGBM and maybe other algorithms, it should be divided by 16 (and scaled to float) before\n.   being used here.\n.   @param _3dImage Output 3-channel floating-point image of the same size as disparity. Each element of\n.   _3dImage(x,y) contains 3D coordinates of the point (x,y) computed from the disparity map. If one\n.   uses Q obtained by @ref stereoRectify, then the returned points are represented in the first\n.   camera's rectified coordinate system.\n.   @param Q \\f$4 \\times 4\\f$ perspective transformation matrix that can be obtained with\n.   @ref stereoRectify.\n.   @param handleMissingValues Indicates, whether the function should handle missing values (i.e.\n.   points where the disparity was not computed). If handleMissingValues=true, then pixels with the\n.   minimal disparity that corresponds to the outliers (see StereoMatcher::compute ) are transformed\n.   to 3D points with a very large Z value (currently set to 10000).\n.   @param ddepth The optional output array depth. If it is -1, the output image will have CV_32F\n.   depth. ddepth can also be set to CV_16S, CV_32S or CV_32F.\n.   \n.   The function transforms a single-channel disparity map to a 3-channel image representing a 3D\n.   surface. That is, for each pixel (x,y) and the corresponding disparity d=disparity(x,y) , it\n.   computes:\n.   \n.   \\f[\\begin{bmatrix}\n.   X \\\\\n.   Y \\\\\n.   Z \\\\\n.   W\n.   \\end{bmatrix} = Q \\begin{bmatrix}\n.   x \\\\\n.   y \\\\\n.   \\texttt{disparity} (x,y) \\\\\n.   z\n.   \\end{bmatrix}.\\f]\n.   \n.   @sa\n.      To reproject a sparse set of points {(x,y,d),...} to 3D space, use perspectiveTransform."
    ...

def resize(src: Mat, dsize: typing.Tuple[int, int], dts: Mat = ..., fx: int = ..., fy: int = ..., interpolation: int = ...) -> Mat:
    'resize(src, dsize[, dst[, fx[, fy[, interpolation]]]]) -> dst\n.   @brief Resizes an image.\n.   \n.   The function resize resizes the image src down to or up to the specified size. Note that the\n.   initial dst type or size are not taken into account. Instead, the size and type are derived from\n.   the `src`,`dsize`,`fx`, and `fy`. If you want to resize src so that it fits the pre-created dst,\n.   you may call the function as follows:\n.   @code\n.       // explicitly specify dsize=dst.size(); fx and fy will be computed from that.\n.       resize(src, dst, dst.size(), 0, 0, interpolation);\n.   @endcode\n.   If you want to decimate the image by factor of 2 in each direction, you can call the function this\n.   way:\n.   @code\n.       // specify fx and fy and let the function compute the destination image size.\n.       resize(src, dst, Size(), 0.5, 0.5, interpolation);\n.   @endcode\n.   To shrink an image, it will generally look best with #INTER_AREA interpolation, whereas to\n.   enlarge an image, it will generally look best with c#INTER_CUBIC (slow) or #INTER_LINEAR\n.   (faster but still looks OK).\n.   \n.   @param src input image.\n.   @param dst output image; it has the size dsize (when it is non-zero) or the size computed from\n.   src.size(), fx, and fy; the type of dst is the same as of src.\n.   @param dsize output image size; if it equals zero, it is computed as:\n.    \\f[\\texttt{dsize = Size(round(fx*src.cols), round(fy*src.rows))}\\f]\n.    Either dsize or both fx and fy must be non-zero.\n.   @param fx scale factor along the horizontal axis; when it equals 0, it is computed as\n.   \\f[\\texttt{(double)dsize.width/src.cols}\\f]\n.   @param fy scale factor along the vertical axis; when it equals 0, it is computed as\n.   \\f[\\texttt{(double)dsize.height/src.rows}\\f]\n.   @param interpolation interpolation method, see #InterpolationFlags\n.   \n.   @sa  warpAffine, warpPerspective, remap'
    ...

def resizeWindow(winname, width, height) -> typing.Any:
    'resizeWindow(winname, width, height) -> None\n.   @brief Resizes window to the specified size\n.   \n.   @note\n.   \n.   -   The specified window size is for the image area. Toolbars are not counted.\n.   -   Only windows created without cv::WINDOW_AUTOSIZE flag can be resized.\n.   \n.   @param winname Window name.\n.   @param width The new window width.\n.   @param height The new window height.\n\n\n\nresizeWindow(winname, size) -> None\n.   @overload\n.   @param winname Window name.\n.   @param size The new window size.'
    ...

def rotate(src: Mat, rotateCode, dts: Mat = ...) -> typing.Any:
    'rotate(src, rotateCode[, dst]) -> dst\n.   @brief Rotates a 2D array in multiples of 90 degrees.\n.   The function cv::rotate rotates the array in one of three different ways:\n.   *   Rotate by 90 degrees clockwise (rotateCode = ROTATE_90_CLOCKWISE).\n.   *   Rotate by 180 degrees clockwise (rotateCode = ROTATE_180).\n.   *   Rotate by 270 degrees clockwise (rotateCode = ROTATE_90_COUNTERCLOCKWISE).\n.   @param src input array.\n.   @param dst output array of the same type as src.  The size is the same with ROTATE_180,\n.   and the rows and cols are switched for ROTATE_90_CLOCKWISE and ROTATE_90_COUNTERCLOCKWISE.\n.   @param rotateCode an enum to specify how to rotate the array; see the enum #RotateFlags\n.   @sa transpose , repeat , completeSymm, flip, RotateFlags'
    ...

def rotatedRectangleIntersection(rect1, rect2, intersectingRegion=...) -> typing.Any:
    'rotatedRectangleIntersection(rect1, rect2[, intersectingRegion]) -> retval, intersectingRegion\n.   @brief Finds out if there is any intersection between two rotated rectangles.\n.   \n.   If there is then the vertices of the intersecting region are returned as well.\n.   \n.   Below are some examples of intersection configurations. The hatched pattern indicates the\n.   intersecting region and the red vertices are returned by the function.\n.   \n.   ![intersection examples](pics/intersection.png)\n.   \n.   @param rect1 First rectangle\n.   @param rect2 Second rectangle\n.   @param intersectingRegion The output array of the vertices of the intersecting region. It returns\n.   at most 8 vertices. Stored as std::vector\\<cv::Point2f\\> or cv::Mat as Mx1 of type CV_32FC2.\n.   @returns One of #RectanglesIntersectTypes'
    ...

def sampsonDistance(pt1, pt2, F) -> typing.Any:
    'sampsonDistance(pt1, pt2, F) -> retval\n.   @brief Calculates the Sampson Distance between two points.\n.   \n.   The function cv::sampsonDistance calculates and returns the first order approximation of the geometric error as:\n.   \\f[\n.   sd( \\texttt{pt1} , \\texttt{pt2} )=\n.   \\frac{(\\texttt{pt2}^t \\cdot \\texttt{F} \\cdot \\texttt{pt1})^2}\n.   {((\\texttt{F} \\cdot \\texttt{pt1})(0))^2 +\n.   ((\\texttt{F} \\cdot \\texttt{pt1})(1))^2 +\n.   ((\\texttt{F}^t \\cdot \\texttt{pt2})(0))^2 +\n.   ((\\texttt{F}^t \\cdot \\texttt{pt2})(1))^2}\n.   \\f]\n.   The fundamental matrix may be calculated using the cv::findFundamentalMat function. See @cite HartleyZ00 11.4.3 for details.\n.   @param pt1 first homogeneous 2d point\n.   @param pt2 second homogeneous 2d point\n.   @param F fundamental matrix\n.   @return The computed Sampson distance.'
    ...

def scaleAdd(src1: Mat, alpha, src2: Mat, dts: Mat = ...) -> typing.Any:
    'scaleAdd(src1, alpha, src2[, dst]) -> dst\n.   @brief Calculates the sum of a scaled array and another array.\n.   \n.   The function scaleAdd is one of the classical primitive linear algebra operations, known as DAXPY\n.   or SAXPY in [BLAS](http://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms). It calculates\n.   the sum of a scaled array and another array:\n.   \\f[\\texttt{dst} (I)= \\texttt{scale} \\cdot \\texttt{src1} (I) +  \\texttt{src2} (I)\\f]\n.   The function can also be emulated with a matrix expression, for example:\n.   @code{.cpp}\n.       Mat A(3, 3, CV_64F);\n.       ...\n.       A.row(0) = A.row(1)*2 + A.row(2);\n.   @endcode\n.   @param src1 first input array.\n.   @param alpha scale factor for the first array.\n.   @param src2 second input array of the same size and type as src1.\n.   @param dst output array of the same size and type as src1.\n.   @sa add, addWeighted, subtract, Mat::dot, Mat::convertTo'
    ...

def seamlessClone(src: Mat, dts: Mat, mask: typing.Optional[Mat], p, flags: int, blend=...) -> typing.Any:
    'seamlessClone(src, dst, mask, p, flags[, blend]) -> blend\n.   @brief Image editing tasks concern either global changes (color/intensity corrections, filters,\n.   deformations) or local changes concerned to a selection. Here we are interested in achieving local\n.   changes, ones that are restricted to a region manually selected (ROI), in a seamless and effortless\n.   manner. The extent of the changes ranges from slight distortions to complete replacement by novel\n.   content @cite PM03 .\n.   \n.   @param src Input 8-bit 3-channel image.\n.   @param dst Input 8-bit 3-channel image.\n.   @param mask Input 8-bit 1 or 3-channel image.\n.   @param p Point in dst image where object is placed.\n.   @param blend Output image with the same size and type as dst.\n.   @param flags Cloning method that could be cv::NORMAL_CLONE, cv::MIXED_CLONE or cv::MONOCHROME_TRANSFER'
    ...

def selectROI(windowName, img: Mat, showCrosshair=..., fromCenter=...) -> typing.Any:
    "selectROI(windowName, img[, showCrosshair[, fromCenter]]) -> retval\n.   @brief Selects ROI on the given image.\n.   Function creates a window and allows user to select a ROI using mouse.\n.   Controls: use `space` or `enter` to finish selection, use key `c` to cancel selection (function will return the zero cv::Rect).\n.   \n.   @param windowName name of the window where selection process will be shown.\n.   @param img image to select a ROI.\n.   @param showCrosshair if true crosshair of selection rectangle will be shown.\n.   @param fromCenter if true center of selection will match initial mouse position. In opposite case a corner of\n.   selection rectangle will correspont to the initial mouse position.\n.   @return selected ROI or empty rect if selection canceled.\n.   \n.   @note The function sets it's own mouse callback for specified window using cv::setMouseCallback(windowName, ...).\n.   After finish of work an empty callback will be set for the used window.\n\n\n\nselectROI(img[, showCrosshair[, fromCenter]]) -> retval\n.   @overload"
    ...

def selectROIs(windowName, img: Mat, showCrosshair=..., fromCenter=...) -> typing.Any:
    "selectROIs(windowName, img[, showCrosshair[, fromCenter]]) -> boundingBoxes\n.   @brief Selects ROIs on the given image.\n.   Function creates a window and allows user to select a ROIs using mouse.\n.   Controls: use `space` or `enter` to finish current selection and start a new one,\n.   use `esc` to terminate multiple ROI selection process.\n.   \n.   @param windowName name of the window where selection process will be shown.\n.   @param img image to select a ROI.\n.   @param boundingBoxes selected ROIs.\n.   @param showCrosshair if true crosshair of selection rectangle will be shown.\n.   @param fromCenter if true center of selection will match initial mouse position. In opposite case a corner of\n.   selection rectangle will correspont to the initial mouse position.\n.   \n.   @note The function sets it's own mouse callback for specified window using cv::setMouseCallback(windowName, ...).\n.   After finish of work an empty callback will be set for the used window."
    ...

def sepFilter2D(src: Mat, ddepth, kernelX, kernelY, dts: Mat = ..., anchor=..., delta=..., borderType=...) -> typing.Any:
    'sepFilter2D(src, ddepth, kernelX, kernelY[, dst[, anchor[, delta[, borderType]]]]) -> dst\n.   @brief Applies a separable linear filter to an image.\n.   \n.   The function applies a separable linear filter to the image. That is, first, every row of src is\n.   filtered with the 1D kernel kernelX. Then, every column of the result is filtered with the 1D\n.   kernel kernelY. The final result shifted by delta is stored in dst .\n.   \n.   @param src Source image.\n.   @param dst Destination image of the same size and the same number of channels as src .\n.   @param ddepth Destination image depth, see @ref filter_depths "combinations"\n.   @param kernelX Coefficients for filtering each row.\n.   @param kernelY Coefficients for filtering each column.\n.   @param anchor Anchor position within the kernel. The default value \\f$(-1,-1)\\f$ means that the anchor\n.   is at the kernel center.\n.   @param delta Value added to the filtered results before storing them.\n.   @param borderType Pixel extrapolation method, see #BorderTypes. #BORDER_WRAP is not supported.\n.   @sa  filter2D, Sobel, GaussianBlur, boxFilter, blur'
    ...

def setIdentity(mtx, s=...) -> typing.Any:
    'setIdentity(mtx[, s]) -> mtx\n.   @brief Initializes a scaled identity matrix.\n.   \n.   The function cv::setIdentity initializes a scaled identity matrix:\n.   \\f[\\texttt{mtx} (i,j)= \\fork{\\texttt{value}}{ if \\(i=j\\)}{0}{otherwise}\\f]\n.   \n.   The function can also be emulated using the matrix initializers and the\n.   matrix expressions:\n.   @code\n.       Mat A = Mat::eye(4, 3, CV_32F)*5;\n.       // A will be set to [[5, 0, 0], [0, 5, 0], [0, 0, 5], [0, 0, 0]]\n.   @endcode\n.   @param mtx matrix to initialize (not necessarily square).\n.   @param s value to assign to diagonal elements.\n.   @sa Mat::zeros, Mat::ones, Mat::setTo, Mat::operator='
    ...

def setMouseCallback(windowName, onMouse, param=...) -> typing.Any:
    'setMouseCallback(windowName, onMouse [, param]) -> None'
    ...

def setNumThreads(nthreads) -> typing.Any:
    "setNumThreads(nthreads) -> None\n.   @brief OpenCV will try to set the number of threads for the next parallel region.\n.   \n.   If threads == 0, OpenCV will disable threading optimizations and run all it's functions\n.   sequentially. Passing threads \\< 0 will reset threads number to system default. This function must\n.   be called outside of parallel region.\n.   \n.   OpenCV will try to run its functions with specified threads number, but some behaviour differs from\n.   framework:\n.   -   `TBB` - User-defined parallel constructions will run with the same threads number, if\n.       another is not specified. If later on user creates his own scheduler, OpenCV will use it.\n.   -   `OpenMP` - No special defined behaviour.\n.   -   `Concurrency` - If threads == 1, OpenCV will disable threading optimizations and run its\n.       functions sequentially.\n.   -   `GCD` - Supports only values \\<= 0.\n.   -   `C=` - No special defined behaviour.\n.   @param nthreads Number of threads used by OpenCV.\n.   @sa getNumThreads, getThreadNum"
    ...

def setRNGSeed(seed) -> typing.Any:
    'setRNGSeed(seed) -> None\n.   @brief Sets state of default random number generator.\n.   \n.   The function cv::setRNGSeed sets state of default random number generator to custom value.\n.   @param seed new state for default random number generator\n.   @sa RNG, randu, randn'
    ...

def setTrackbarMax(trackbarname, winname, maxval) -> typing.Any:
    'setTrackbarMax(trackbarname, winname, maxval) -> None\n.   @brief Sets the trackbar maximum position.\n.   \n.   The function sets the maximum position of the specified trackbar in the specified window.\n.   \n.   @note\n.   \n.   [__Qt Backend Only__] winname can be empty if the trackbar is attached to the control\n.   panel.\n.   \n.   @param trackbarname Name of the trackbar.\n.   @param winname Name of the window that is the parent of trackbar.\n.   @param maxval New maximum position.'
    ...

def setTrackbarMin(trackbarname, winname, minval) -> typing.Any:
    'setTrackbarMin(trackbarname, winname, minval) -> None\n.   @brief Sets the trackbar minimum position.\n.   \n.   The function sets the minimum position of the specified trackbar in the specified window.\n.   \n.   @note\n.   \n.   [__Qt Backend Only__] winname can be empty if the trackbar is attached to the control\n.   panel.\n.   \n.   @param trackbarname Name of the trackbar.\n.   @param winname Name of the window that is the parent of trackbar.\n.   @param minval New minimum position.'
    ...

def setTrackbarPos(trackbarname, winname, pos) -> typing.Any:
    'setTrackbarPos(trackbarname, winname, pos) -> None\n.   @brief Sets the trackbar position.\n.   \n.   The function sets the position of the specified trackbar in the specified window.\n.   \n.   @note\n.   \n.   [__Qt Backend Only__] winname can be empty if the trackbar is attached to the control\n.   panel.\n.   \n.   @param trackbarname Name of the trackbar.\n.   @param winname Name of the window that is the parent of trackbar.\n.   @param pos New position.'
    ...

def setUseOpenVX(flag) -> typing.Any:
    'setUseOpenVX(flag) -> None\n.'
    ...

def setUseOptimized(onoff) -> typing.Any:
    'setUseOptimized(onoff) -> None\n.   @brief Enables or disables the optimized code.\n.   \n.   The function can be used to dynamically turn on and off optimized dispatched code (code that uses SSE4.2, AVX/AVX2,\n.   and other instructions on the platforms that support it). It sets a global flag that is further\n.   checked by OpenCV functions. Since the flag is not checked in the inner OpenCV loops, it is only\n.   safe to call the function on the very top level in your application where you can be sure that no\n.   other OpenCV function is currently executed.\n.   \n.   By default, the optimized code is enabled unless you disable it in CMake. The current status can be\n.   retrieved using useOptimized.\n.   @param onoff The boolean flag specifying whether the optimized code should be used (onoff=true)\n.   or not (onoff=false).'
    ...

def setWindowProperty(winname, prop_id, prop_value) -> typing.Any:
    'setWindowProperty(winname, prop_id, prop_value) -> None\n.   @brief Changes parameters of a window dynamically.\n.   \n.   The function setWindowProperty enables changing properties of a window.\n.   \n.   @param winname Name of the window.\n.   @param prop_id Window property to edit. The supported operation flags are: (cv::WindowPropertyFlags)\n.   @param prop_value New value of the window property. The supported flags are: (cv::WindowFlags)'
    ...

def setWindowTitle(winname, title) -> typing.Any:
    'setWindowTitle(winname, title) -> None\n.   @brief Updates window title\n.   @param winname Name of the window.\n.   @param title New title.'
    ...

def solve(src1: Mat, src2: Mat, dts: Mat = ..., flags: int = ...) -> typing.Any:
    'solve(src1, src2[, dst[, flags]]) -> retval, dst\n.   @brief Solves one or more linear systems or least-squares problems.\n.   \n.   The function cv::solve solves a linear system or least-squares problem (the\n.   latter is possible with SVD or QR methods, or by specifying the flag\n.   #DECOMP_NORMAL ):\n.   \\f[\\texttt{dst} =  \\arg \\min _X \\| \\texttt{src1} \\cdot \\texttt{X} -  \\texttt{src2} \\|\\f]\n.   \n.   If #DECOMP_LU or #DECOMP_CHOLESKY method is used, the function returns 1\n.   if src1 (or \\f$\\texttt{src1}^T\\texttt{src1}\\f$ ) is non-singular. Otherwise,\n.   it returns 0. In the latter case, dst is not valid. Other methods find a\n.   pseudo-solution in case of a singular left-hand side part.\n.   \n.   @note If you want to find a unity-norm solution of an under-defined\n.   singular system \\f$\\texttt{src1}\\cdot\\texttt{dst}=0\\f$ , the function solve\n.   will not do the work. Use SVD::solveZ instead.\n.   \n.   @param src1 input matrix on the left-hand side of the system.\n.   @param src2 input matrix on the right-hand side of the system.\n.   @param dst output solution.\n.   @param flags solution (matrix inversion) method (#DecompTypes)\n.   @sa invert, SVD, eigen'
    ...

def solveCubic(coeffs, roots=...) -> typing.Any:
    'solveCubic(coeffs[, roots]) -> retval, roots\n.   @brief Finds the real roots of a cubic equation.\n.   \n.   The function solveCubic finds the real roots of a cubic equation:\n.   -   if coeffs is a 4-element vector:\n.   \\f[\\texttt{coeffs} [0] x^3 +  \\texttt{coeffs} [1] x^2 +  \\texttt{coeffs} [2] x +  \\texttt{coeffs} [3] = 0\\f]\n.   -   if coeffs is a 3-element vector:\n.   \\f[x^3 +  \\texttt{coeffs} [0] x^2 +  \\texttt{coeffs} [1] x +  \\texttt{coeffs} [2] = 0\\f]\n.   \n.   The roots are stored in the roots array.\n.   @param coeffs equation coefficients, an array of 3 or 4 elements.\n.   @param roots output array of real roots that has 1 or 3 elements.\n.   @return number of real roots. It can be 0, 1 or 2.'
    ...

def solveLP(Func, Constr, z=...) -> typing.Any:
    'solveLP(Func, Constr[, z]) -> retval, z\n.   @brief Solve given (non-integer) linear programming problem using the Simplex Algorithm (Simplex Method).\n.   \n.   What we mean here by "linear programming problem" (or LP problem, for short) can be formulated as:\n.   \n.   \\f[\\mbox{Maximize } c\\cdot x\\\\\n.    \\mbox{Subject to:}\\\\\n.    Ax\\leq b\\\\\n.    x\\geq 0\\f]\n.   \n.   Where \\f$c\\f$ is fixed `1`-by-`n` row-vector, \\f$A\\f$ is fixed `m`-by-`n` matrix, \\f$b\\f$ is fixed `m`-by-`1`\n.   column vector and \\f$x\\f$ is an arbitrary `n`-by-`1` column vector, which satisfies the constraints.\n.   \n.   Simplex algorithm is one of many algorithms that are designed to handle this sort of problems\n.   efficiently. Although it is not optimal in theoretical sense (there exist algorithms that can solve\n.   any problem written as above in polynomial time, while simplex method degenerates to exponential\n.   time for some special cases), it is well-studied, easy to implement and is shown to work well for\n.   real-life purposes.\n.   \n.   The particular implementation is taken almost verbatim from **Introduction to Algorithms, third\n.   edition** by T. H. Cormen, C. E. Leiserson, R. L. Rivest and Clifford Stein. In particular, the\n.   Bland\'s rule <http://en.wikipedia.org/wiki/Bland%27s_rule> is used to prevent cycling.\n.   \n.   @param Func This row-vector corresponds to \\f$c\\f$ in the LP problem formulation (see above). It should\n.   contain 32- or 64-bit floating point numbers. As a convenience, column-vector may be also submitted,\n.   in the latter case it is understood to correspond to \\f$c^T\\f$.\n.   @param Constr `m`-by-`n+1` matrix, whose rightmost column corresponds to \\f$b\\f$ in formulation above\n.   and the remaining to \\f$A\\f$. It should contain 32- or 64-bit floating point numbers.\n.   @param z The solution will be returned here as a column-vector - it corresponds to \\f$c\\f$ in the\n.   formulation above. It will contain 64-bit floating point numbers.\n.   @return One of cv::SolveLPResult'
    ...

def solveP3P(objectPoints, imagePoints, cameraMatrix, distCoeffs, flags: int, rvecs=..., tvecs=...) -> typing.Any:
    'solveP3P(objectPoints, imagePoints, cameraMatrix, distCoeffs, flags[, rvecs[, tvecs]]) -> retval, rvecs, tvecs\n.   @brief Finds an object pose from 3 3D-2D point correspondences.\n.   \n.   @param objectPoints Array of object points in the object coordinate space, 3x3 1-channel or\n.   1x3/3x1 3-channel. vector\\<Point3f\\> can be also passed here.\n.   @param imagePoints Array of corresponding image points, 3x2 1-channel or 1x3/3x1 2-channel.\n.    vector\\<Point2f\\> can be also passed here.\n.   @param cameraMatrix Input camera matrix \\f$A = \\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\\f$ .\n.   @param distCoeffs Input vector of distortion coefficients\n.   \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6 [, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$ of\n.   4, 5, 8, 12 or 14 elements. If the vector is NULL/empty, the zero distortion coefficients are\n.   assumed.\n.   @param rvecs Output rotation vectors (see @ref Rodrigues ) that, together with tvecs, brings points from\n.   the model coordinate system to the camera coordinate system. A P3P problem has up to 4 solutions.\n.   @param tvecs Output translation vectors.\n.   @param flags Method for solving a P3P problem:\n.   -   **SOLVEPNP_P3P** Method is based on the paper of X.S. Gao, X.-R. Hou, J. Tang, H.-F. Chang\n.   "Complete Solution Classification for the Perspective-Three-Point Problem" (@cite gao2003complete).\n.   -   **SOLVEPNP_AP3P** Method is based on the paper of T. Ke and S. Roumeliotis.\n.   "An Efficient Algebraic Solution to the Perspective-Three-Point Problem" (@cite Ke17).\n.   \n.   The function estimates the object pose given 3 object points, their corresponding image\n.   projections, as well as the camera matrix and the distortion coefficients.\n.   \n.   @note\n.   The solutions are sorted by reprojection errors (lowest to highest).'
    ...

def solvePnP(objectPoints, imagePoints, cameraMatrix, distCoeffs, rvec=..., tvec=..., useExtrinsicGuess=..., flags: int = ...) -> typing.Any:
    'solvePnP(objectPoints, imagePoints, cameraMatrix, distCoeffs[, rvec[, tvec[, useExtrinsicGuess[, flags]]]]) -> retval, rvec, tvec\n.   @brief Finds an object pose from 3D-2D point correspondences.\n.   This function returns the rotation and the translation vectors that transform a 3D point expressed in the object\n.   coordinate frame to the camera coordinate frame, using different methods:\n.   - P3P methods (@ref SOLVEPNP_P3P, @ref SOLVEPNP_AP3P): need 4 input points to return a unique solution.\n.   - @ref SOLVEPNP_IPPE Input points must be >= 4 and object points must be coplanar.\n.   - @ref SOLVEPNP_IPPE_SQUARE Special case suitable for marker pose estimation.\n.   Number of input points must be 4. Object points must be defined in the following order:\n.     - point 0: [-squareLength / 2,  squareLength / 2, 0]\n.     - point 1: [ squareLength / 2,  squareLength / 2, 0]\n.     - point 2: [ squareLength / 2, -squareLength / 2, 0]\n.     - point 3: [-squareLength / 2, -squareLength / 2, 0]\n.   - for all the other flags, number of input points must be >= 4 and object points can be in any configuration.\n.   \n.   @param objectPoints Array of object points in the object coordinate space, Nx3 1-channel or\n.   1xN/Nx1 3-channel, where N is the number of points. vector\\<Point3d\\> can be also passed here.\n.   @param imagePoints Array of corresponding image points, Nx2 1-channel or 1xN/Nx1 2-channel,\n.   where N is the number of points. vector\\<Point2d\\> can be also passed here.\n.   @param cameraMatrix Input camera matrix \\f$A = \\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\\f$ .\n.   @param distCoeffs Input vector of distortion coefficients\n.   \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6 [, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$ of\n.   4, 5, 8, 12 or 14 elements. If the vector is NULL/empty, the zero distortion coefficients are\n.   assumed.\n.   @param rvec Output rotation vector (see @ref Rodrigues ) that, together with tvec, brings points from\n.   the model coordinate system to the camera coordinate system.\n.   @param tvec Output translation vector.\n.   @param useExtrinsicGuess Parameter used for #SOLVEPNP_ITERATIVE. If true (1), the function uses\n.   the provided rvec and tvec values as initial approximations of the rotation and translation\n.   vectors, respectively, and further optimizes them.\n.   @param flags Method for solving a PnP problem:\n.   -   **SOLVEPNP_ITERATIVE** Iterative method is based on a Levenberg-Marquardt optimization. In\n.   this case the function finds such a pose that minimizes reprojection error, that is the sum\n.   of squared distances between the observed projections imagePoints and the projected (using\n.   projectPoints ) objectPoints .\n.   -   **SOLVEPNP_P3P** Method is based on the paper of X.S. Gao, X.-R. Hou, J. Tang, H.-F. Chang\n.   "Complete Solution Classification for the Perspective-Three-Point Problem" (@cite gao2003complete).\n.   In this case the function requires exactly four object and image points.\n.   -   **SOLVEPNP_AP3P** Method is based on the paper of T. Ke, S. Roumeliotis\n.   "An Efficient Algebraic Solution to the Perspective-Three-Point Problem" (@cite Ke17).\n.   In this case the function requires exactly four object and image points.\n.   -   **SOLVEPNP_EPNP** Method has been introduced by F. Moreno-Noguer, V. Lepetit and P. Fua in the\n.   paper "EPnP: Efficient Perspective-n-Point Camera Pose Estimation" (@cite lepetit2009epnp).\n.   -   **SOLVEPNP_DLS** Method is based on the paper of J. Hesch and S. Roumeliotis.\n.   "A Direct Least-Squares (DLS) Method for PnP" (@cite hesch2011direct).\n.   -   **SOLVEPNP_UPNP** Method is based on the paper of A. Penate-Sanchez, J. Andrade-Cetto,\n.   F. Moreno-Noguer. "Exhaustive Linearization for Robust Camera Pose and Focal Length\n.   Estimation" (@cite penate2013exhaustive). In this case the function also estimates the parameters \\f$f_x\\f$ and \\f$f_y\\f$\n.   assuming that both have the same value. Then the cameraMatrix is updated with the estimated\n.   focal length.\n.   -   **SOLVEPNP_IPPE** Method is based on the paper of T. Collins and A. Bartoli.\n.   "Infinitesimal Plane-Based Pose Estimation" (@cite Collins14). This method requires coplanar object points.\n.   -   **SOLVEPNP_IPPE_SQUARE** Method is based on the paper of Toby Collins and Adrien Bartoli.\n.   "Infinitesimal Plane-Based Pose Estimation" (@cite Collins14). This method is suitable for marker pose estimation.\n.   It requires 4 coplanar object points defined in the following order:\n.     - point 0: [-squareLength / 2,  squareLength / 2, 0]\n.     - point 1: [ squareLength / 2,  squareLength / 2, 0]\n.     - point 2: [ squareLength / 2, -squareLength / 2, 0]\n.     - point 3: [-squareLength / 2, -squareLength / 2, 0]\n.   \n.   The function estimates the object pose given a set of object points, their corresponding image\n.   projections, as well as the camera matrix and the distortion coefficients, see the figure below\n.   (more precisely, the X-axis of the camera frame is pointing to the right, the Y-axis downward\n.   and the Z-axis forward).\n.   \n.   ![](pnp.jpg)\n.   \n.   Points expressed in the world frame \\f$ \\bf{X}_w \\f$ are projected into the image plane \\f$ \\left[ u, v \\right] \\f$\n.   using the perspective projection model \\f$ \\Pi \\f$ and the camera intrinsic parameters matrix \\f$ \\bf{A} \\f$:\n.   \n.   \\f[\n.     \\begin{align*}\n.     \\begin{bmatrix}\n.     u \\\\\n.     v \\\\\n.     1\n.     \\end{bmatrix} &=\n.     \\bf{A} \\hspace{0.1em} \\Pi \\hspace{0.2em} ^{c}\\bf{T}_w\n.     \\begin{bmatrix}\n.     X_{w} \\\\\n.     Y_{w} \\\\\n.     Z_{w} \\\\\n.     1\n.     \\end{bmatrix} \\\\\n.     \\begin{bmatrix}\n.     u \\\\\n.     v \\\\\n.     1\n.     \\end{bmatrix} &=\n.     \\begin{bmatrix}\n.     f_x & 0 & c_x \\\\\n.     0 & f_y & c_y \\\\\n.     0 & 0 & 1\n.     \\end{bmatrix}\n.     \\begin{bmatrix}\n.     1 & 0 & 0 & 0 \\\\\n.     0 & 1 & 0 & 0 \\\\\n.     0 & 0 & 1 & 0\n.     \\end{bmatrix}\n.     \\begin{bmatrix}\n.     r_{11} & r_{12} & r_{13} & t_x \\\\\n.     r_{21} & r_{22} & r_{23} & t_y \\\\\n.     r_{31} & r_{32} & r_{33} & t_z \\\\\n.     0 & 0 & 0 & 1\n.     \\end{bmatrix}\n.     \\begin{bmatrix}\n.     X_{w} \\\\\n.     Y_{w} \\\\\n.     Z_{w} \\\\\n.     1\n.     \\end{bmatrix}\n.     \\end{align*}\n.   \\f]\n.   \n.   The estimated pose is thus the rotation (`rvec`) and the translation (`tvec`) vectors that allow transforming\n.   a 3D point expressed in the world frame into the camera frame:\n.   \n.   \\f[\n.     \\begin{align*}\n.     \\begin{bmatrix}\n.     X_c \\\\\n.     Y_c \\\\\n.     Z_c \\\\\n.     1\n.     \\end{bmatrix} &=\n.     \\hspace{0.2em} ^{c}\\bf{T}_w\n.     \\begin{bmatrix}\n.     X_{w} \\\\\n.     Y_{w} \\\\\n.     Z_{w} \\\\\n.     1\n.     \\end{bmatrix} \\\\\n.     \\begin{bmatrix}\n.     X_c \\\\\n.     Y_c \\\\\n.     Z_c \\\\\n.     1\n.     \\end{bmatrix} &=\n.     \\begin{bmatrix}\n.     r_{11} & r_{12} & r_{13} & t_x \\\\\n.     r_{21} & r_{22} & r_{23} & t_y \\\\\n.     r_{31} & r_{32} & r_{33} & t_z \\\\\n.     0 & 0 & 0 & 1\n.     \\end{bmatrix}\n.     \\begin{bmatrix}\n.     X_{w} \\\\\n.     Y_{w} \\\\\n.     Z_{w} \\\\\n.     1\n.     \\end{bmatrix}\n.     \\end{align*}\n.   \\f]\n.   \n.   @note\n.      -   An example of how to use solvePnP for planar augmented reality can be found at\n.           opencv_source_code/samples/python/plane_ar.py\n.      -   If you are using Python:\n.           - Numpy array slices won\'t work as input because solvePnP requires contiguous\n.           arrays (enforced by the assertion using cv::Mat::checkVector() around line 55 of\n.           modules/calib3d/src/solvepnp.cpp version 2.4.9)\n.           - The P3P algorithm requires image points to be in an array of shape (N,1,2) due\n.           to its calling of cv::undistortPoints (around line 75 of modules/calib3d/src/solvepnp.cpp version 2.4.9)\n.           which requires 2-channel information.\n.           - Thus, given some data D = np.array(...) where D.shape = (N,M), in order to use a subset of\n.           it as, e.g., imagePoints, one must effectively copy it into a new array: imagePoints =\n.           np.ascontiguousarray(D[:,:2]).reshape((N,1,2))\n.      -   The methods **SOLVEPNP_DLS** and **SOLVEPNP_UPNP** cannot be used as the current implementations are\n.          unstable and sometimes give completely wrong results. If you pass one of these two\n.          flags, **SOLVEPNP_EPNP** method will be used instead.\n.      -   The minimum number of points is 4 in the general case. In the case of **SOLVEPNP_P3P** and **SOLVEPNP_AP3P**\n.          methods, it is required to use exactly 4 points (the first 3 points are used to estimate all the solutions\n.          of the P3P problem, the last one is used to retain the best solution that minimizes the reprojection error).\n.      -   With **SOLVEPNP_ITERATIVE** method and `useExtrinsicGuess=true`, the minimum number of points is 3 (3 points\n.          are sufficient to compute a pose but there are up to 4 solutions). The initial solution should be close to the\n.          global solution to converge.\n.      -   With **SOLVEPNP_IPPE** input points must be >= 4 and object points must be coplanar.\n.      -   With **SOLVEPNP_IPPE_SQUARE** this is a special case suitable for marker pose estimation.\n.          Number of input points must be 4. Object points must be defined in the following order:\n.            - point 0: [-squareLength / 2,  squareLength / 2, 0]\n.            - point 1: [ squareLength / 2,  squareLength / 2, 0]\n.            - point 2: [ squareLength / 2, -squareLength / 2, 0]\n.            - point 3: [-squareLength / 2, -squareLength / 2, 0]'
    ...

def solvePnPGeneric(objectPoints, imagePoints, cameraMatrix, distCoeffs, rvecs=..., tvecs=..., useExtrinsicGuess=..., flags: int = ..., rvec=..., tvec=..., reprojectionError=...) -> typing.Any:
    'solvePnPGeneric(objectPoints, imagePoints, cameraMatrix, distCoeffs[, rvecs[, tvecs[, useExtrinsicGuess[, flags[, rvec[, tvec[, reprojectionError]]]]]]]) -> retval, rvecs, tvecs, reprojectionError\n.   @brief Finds an object pose from 3D-2D point correspondences.\n.   This function returns a list of all the possible solutions (a solution is a <rotation vector, translation vector>\n.   couple), depending on the number of input points and the chosen method:\n.   - P3P methods (@ref SOLVEPNP_P3P, @ref SOLVEPNP_AP3P): 3 or 4 input points. Number of returned solutions can be between 0 and 4 with 3 input points.\n.   - @ref SOLVEPNP_IPPE Input points must be >= 4 and object points must be coplanar. Returns 2 solutions.\n.   - @ref SOLVEPNP_IPPE_SQUARE Special case suitable for marker pose estimation.\n.   Number of input points must be 4 and 2 solutions are returned. Object points must be defined in the following order:\n.     - point 0: [-squareLength / 2,  squareLength / 2, 0]\n.     - point 1: [ squareLength / 2,  squareLength / 2, 0]\n.     - point 2: [ squareLength / 2, -squareLength / 2, 0]\n.     - point 3: [-squareLength / 2, -squareLength / 2, 0]\n.   - for all the other flags, number of input points must be >= 4 and object points can be in any configuration.\n.   Only 1 solution is returned.\n.   \n.   @param objectPoints Array of object points in the object coordinate space, Nx3 1-channel or\n.   1xN/Nx1 3-channel, where N is the number of points. vector\\<Point3d\\> can be also passed here.\n.   @param imagePoints Array of corresponding image points, Nx2 1-channel or 1xN/Nx1 2-channel,\n.   where N is the number of points. vector\\<Point2d\\> can be also passed here.\n.   @param cameraMatrix Input camera matrix \\f$A = \\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\\f$ .\n.   @param distCoeffs Input vector of distortion coefficients\n.   \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6 [, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$ of\n.   4, 5, 8, 12 or 14 elements. If the vector is NULL/empty, the zero distortion coefficients are\n.   assumed.\n.   @param rvecs Vector of output rotation vectors (see @ref Rodrigues ) that, together with tvecs, brings points from\n.   the model coordinate system to the camera coordinate system.\n.   @param tvecs Vector of output translation vectors.\n.   @param useExtrinsicGuess Parameter used for #SOLVEPNP_ITERATIVE. If true (1), the function uses\n.   the provided rvec and tvec values as initial approximations of the rotation and translation\n.   vectors, respectively, and further optimizes them.\n.   @param flags Method for solving a PnP problem:\n.   -   **SOLVEPNP_ITERATIVE** Iterative method is based on a Levenberg-Marquardt optimization. In\n.   this case the function finds such a pose that minimizes reprojection error, that is the sum\n.   of squared distances between the observed projections imagePoints and the projected (using\n.   projectPoints ) objectPoints .\n.   -   **SOLVEPNP_P3P** Method is based on the paper of X.S. Gao, X.-R. Hou, J. Tang, H.-F. Chang\n.   "Complete Solution Classification for the Perspective-Three-Point Problem" (@cite gao2003complete).\n.   In this case the function requires exactly four object and image points.\n.   -   **SOLVEPNP_AP3P** Method is based on the paper of T. Ke, S. Roumeliotis\n.   "An Efficient Algebraic Solution to the Perspective-Three-Point Problem" (@cite Ke17).\n.   In this case the function requires exactly four object and image points.\n.   -   **SOLVEPNP_EPNP** Method has been introduced by F.Moreno-Noguer, V.Lepetit and P.Fua in the\n.   paper "EPnP: Efficient Perspective-n-Point Camera Pose Estimation" (@cite lepetit2009epnp).\n.   -   **SOLVEPNP_DLS** Method is based on the paper of Joel A. Hesch and Stergios I. Roumeliotis.\n.   "A Direct Least-Squares (DLS) Method for PnP" (@cite hesch2011direct).\n.   -   **SOLVEPNP_UPNP** Method is based on the paper of A.Penate-Sanchez, J.Andrade-Cetto,\n.   F.Moreno-Noguer. "Exhaustive Linearization for Robust Camera Pose and Focal Length\n.   Estimation" (@cite penate2013exhaustive). In this case the function also estimates the parameters \\f$f_x\\f$ and \\f$f_y\\f$\n.   assuming that both have the same value. Then the cameraMatrix is updated with the estimated\n.   focal length.\n.   -   **SOLVEPNP_IPPE** Method is based on the paper of T. Collins and A. Bartoli.\n.   "Infinitesimal Plane-Based Pose Estimation" (@cite Collins14). This method requires coplanar object points.\n.   -   **SOLVEPNP_IPPE_SQUARE** Method is based on the paper of Toby Collins and Adrien Bartoli.\n.   "Infinitesimal Plane-Based Pose Estimation" (@cite Collins14). This method is suitable for marker pose estimation.\n.   It requires 4 coplanar object points defined in the following order:\n.     - point 0: [-squareLength / 2,  squareLength / 2, 0]\n.     - point 1: [ squareLength / 2,  squareLength / 2, 0]\n.     - point 2: [ squareLength / 2, -squareLength / 2, 0]\n.     - point 3: [-squareLength / 2, -squareLength / 2, 0]\n.   @param rvec Rotation vector used to initialize an iterative PnP refinement algorithm, when flag is SOLVEPNP_ITERATIVE\n.   and useExtrinsicGuess is set to true.\n.   @param tvec Translation vector used to initialize an iterative PnP refinement algorithm, when flag is SOLVEPNP_ITERATIVE\n.   and useExtrinsicGuess is set to true.\n.   @param reprojectionError Optional vector of reprojection error, that is the RMS error\n.   (\\f$ \\text{RMSE} = \\sqrt{\\frac{\\sum_{i}^{N} \\left ( \\hat{y_i} - y_i \\right )^2}{N}} \\f$) between the input image points\n.   and the 3D object points projected with the estimated pose.\n.   \n.   The function estimates the object pose given a set of object points, their corresponding image\n.   projections, as well as the camera matrix and the distortion coefficients, see the figure below\n.   (more precisely, the X-axis of the camera frame is pointing to the right, the Y-axis downward\n.   and the Z-axis forward).\n.   \n.   ![](pnp.jpg)\n.   \n.   Points expressed in the world frame \\f$ \\bf{X}_w \\f$ are projected into the image plane \\f$ \\left[ u, v \\right] \\f$\n.   using the perspective projection model \\f$ \\Pi \\f$ and the camera intrinsic parameters matrix \\f$ \\bf{A} \\f$:\n.   \n.   \\f[\n.     \\begin{align*}\n.     \\begin{bmatrix}\n.     u \\\\\n.     v \\\\\n.     1\n.     \\end{bmatrix} &=\n.     \\bf{A} \\hspace{0.1em} \\Pi \\hspace{0.2em} ^{c}\\bf{T}_w\n.     \\begin{bmatrix}\n.     X_{w} \\\\\n.     Y_{w} \\\\\n.     Z_{w} \\\\\n.     1\n.     \\end{bmatrix} \\\\\n.     \\begin{bmatrix}\n.     u \\\\\n.     v \\\\\n.     1\n.     \\end{bmatrix} &=\n.     \\begin{bmatrix}\n.     f_x & 0 & c_x \\\\\n.     0 & f_y & c_y \\\\\n.     0 & 0 & 1\n.     \\end{bmatrix}\n.     \\begin{bmatrix}\n.     1 & 0 & 0 & 0 \\\\\n.     0 & 1 & 0 & 0 \\\\\n.     0 & 0 & 1 & 0\n.     \\end{bmatrix}\n.     \\begin{bmatrix}\n.     r_{11} & r_{12} & r_{13} & t_x \\\\\n.     r_{21} & r_{22} & r_{23} & t_y \\\\\n.     r_{31} & r_{32} & r_{33} & t_z \\\\\n.     0 & 0 & 0 & 1\n.     \\end{bmatrix}\n.     \\begin{bmatrix}\n.     X_{w} \\\\\n.     Y_{w} \\\\\n.     Z_{w} \\\\\n.     1\n.     \\end{bmatrix}\n.     \\end{align*}\n.   \\f]\n.   \n.   The estimated pose is thus the rotation (`rvec`) and the translation (`tvec`) vectors that allow transforming\n.   a 3D point expressed in the world frame into the camera frame:\n.   \n.   \\f[\n.     \\begin{align*}\n.     \\begin{bmatrix}\n.     X_c \\\\\n.     Y_c \\\\\n.     Z_c \\\\\n.     1\n.     \\end{bmatrix} &=\n.     \\hspace{0.2em} ^{c}\\bf{T}_w\n.     \\begin{bmatrix}\n.     X_{w} \\\\\n.     Y_{w} \\\\\n.     Z_{w} \\\\\n.     1\n.     \\end{bmatrix} \\\\\n.     \\begin{bmatrix}\n.     X_c \\\\\n.     Y_c \\\\\n.     Z_c \\\\\n.     1\n.     \\end{bmatrix} &=\n.     \\begin{bmatrix}\n.     r_{11} & r_{12} & r_{13} & t_x \\\\\n.     r_{21} & r_{22} & r_{23} & t_y \\\\\n.     r_{31} & r_{32} & r_{33} & t_z \\\\\n.     0 & 0 & 0 & 1\n.     \\end{bmatrix}\n.     \\begin{bmatrix}\n.     X_{w} \\\\\n.     Y_{w} \\\\\n.     Z_{w} \\\\\n.     1\n.     \\end{bmatrix}\n.     \\end{align*}\n.   \\f]\n.   \n.   @note\n.      -   An example of how to use solvePnP for planar augmented reality can be found at\n.           opencv_source_code/samples/python/plane_ar.py\n.      -   If you are using Python:\n.           - Numpy array slices won\'t work as input because solvePnP requires contiguous\n.           arrays (enforced by the assertion using cv::Mat::checkVector() around line 55 of\n.           modules/calib3d/src/solvepnp.cpp version 2.4.9)\n.           - The P3P algorithm requires image points to be in an array of shape (N,1,2) due\n.           to its calling of cv::undistortPoints (around line 75 of modules/calib3d/src/solvepnp.cpp version 2.4.9)\n.           which requires 2-channel information.\n.           - Thus, given some data D = np.array(...) where D.shape = (N,M), in order to use a subset of\n.           it as, e.g., imagePoints, one must effectively copy it into a new array: imagePoints =\n.           np.ascontiguousarray(D[:,:2]).reshape((N,1,2))\n.      -   The methods **SOLVEPNP_DLS** and **SOLVEPNP_UPNP** cannot be used as the current implementations are\n.          unstable and sometimes give completely wrong results. If you pass one of these two\n.          flags, **SOLVEPNP_EPNP** method will be used instead.\n.      -   The minimum number of points is 4 in the general case. In the case of **SOLVEPNP_P3P** and **SOLVEPNP_AP3P**\n.          methods, it is required to use exactly 4 points (the first 3 points are used to estimate all the solutions\n.          of the P3P problem, the last one is used to retain the best solution that minimizes the reprojection error).\n.      -   With **SOLVEPNP_ITERATIVE** method and `useExtrinsicGuess=true`, the minimum number of points is 3 (3 points\n.          are sufficient to compute a pose but there are up to 4 solutions). The initial solution should be close to the\n.          global solution to converge.\n.      -   With **SOLVEPNP_IPPE** input points must be >= 4 and object points must be coplanar.\n.      -   With **SOLVEPNP_IPPE_SQUARE** this is a special case suitable for marker pose estimation.\n.          Number of input points must be 4. Object points must be defined in the following order:\n.            - point 0: [-squareLength / 2,  squareLength / 2, 0]\n.            - point 1: [ squareLength / 2,  squareLength / 2, 0]\n.            - point 2: [ squareLength / 2, -squareLength / 2, 0]\n.            - point 3: [-squareLength / 2, -squareLength / 2, 0]'
    ...

def solvePnPRansac(objectPoints, imagePoints, cameraMatrix, distCoeffs, rvec=..., tvec=..., useExtrinsicGuess=..., iterationsCount=..., reprojectionError=..., confidence=..., inliers=..., flags: int = ...) -> typing.Any:
    'solvePnPRansac(objectPoints, imagePoints, cameraMatrix, distCoeffs[, rvec[, tvec[, useExtrinsicGuess[, iterationsCount[, reprojectionError[, confidence[, inliers[, flags]]]]]]]]) -> retval, rvec, tvec, inliers\n.   @brief Finds an object pose from 3D-2D point correspondences using the RANSAC scheme.\n.   \n.   @param objectPoints Array of object points in the object coordinate space, Nx3 1-channel or\n.   1xN/Nx1 3-channel, where N is the number of points. vector\\<Point3d\\> can be also passed here.\n.   @param imagePoints Array of corresponding image points, Nx2 1-channel or 1xN/Nx1 2-channel,\n.   where N is the number of points. vector\\<Point2d\\> can be also passed here.\n.   @param cameraMatrix Input camera matrix \\f$A = \\vecthreethree{fx}{0}{cx}{0}{fy}{cy}{0}{0}{1}\\f$ .\n.   @param distCoeffs Input vector of distortion coefficients\n.   \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6 [, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$ of\n.   4, 5, 8, 12 or 14 elements. If the vector is NULL/empty, the zero distortion coefficients are\n.   assumed.\n.   @param rvec Output rotation vector (see @ref Rodrigues ) that, together with tvec, brings points from\n.   the model coordinate system to the camera coordinate system.\n.   @param tvec Output translation vector.\n.   @param useExtrinsicGuess Parameter used for @ref SOLVEPNP_ITERATIVE. If true (1), the function uses\n.   the provided rvec and tvec values as initial approximations of the rotation and translation\n.   vectors, respectively, and further optimizes them.\n.   @param iterationsCount Number of iterations.\n.   @param reprojectionError Inlier threshold value used by the RANSAC procedure. The parameter value\n.   is the maximum allowed distance between the observed and computed point projections to consider it\n.   an inlier.\n.   @param confidence The probability that the algorithm produces a useful result.\n.   @param inliers Output vector that contains indices of inliers in objectPoints and imagePoints .\n.   @param flags Method for solving a PnP problem (see @ref solvePnP ).\n.   \n.   The function estimates an object pose given a set of object points, their corresponding image\n.   projections, as well as the camera matrix and the distortion coefficients. This function finds such\n.   a pose that minimizes reprojection error, that is, the sum of squared distances between the observed\n.   projections imagePoints and the projected (using @ref projectPoints ) objectPoints. The use of RANSAC\n.   makes the function resistant to outliers.\n.   \n.   @note\n.      -   An example of how to use solvePNPRansac for object detection can be found at\n.           opencv_source_code/samples/cpp/tutorial_code/calib3d/real_time_pose_estimation/\n.      -   The default method used to estimate the camera pose for the Minimal Sample Sets step\n.          is #SOLVEPNP_EPNP. Exceptions are:\n.            - if you choose #SOLVEPNP_P3P or #SOLVEPNP_AP3P, these methods will be used.\n.            - if the number of input points is equal to 4, #SOLVEPNP_P3P is used.\n.      -   The method used to estimate the camera pose using all the inliers is defined by the\n.          flags parameters unless it is equal to #SOLVEPNP_P3P or #SOLVEPNP_AP3P. In this case,\n.          the method #SOLVEPNP_EPNP will be used instead.'
    ...

def solvePnPRefineLM(objectPoints, imagePoints, cameraMatrix, distCoeffs, rvec, tvec, criteria=...) -> typing.Any:
    'solvePnPRefineLM(objectPoints, imagePoints, cameraMatrix, distCoeffs, rvec, tvec[, criteria]) -> rvec, tvec\n.   @brief Refine a pose (the translation and the rotation that transform a 3D point expressed in the object coordinate frame\n.   to the camera coordinate frame) from a 3D-2D point correspondences and starting from an initial solution.\n.   \n.   @param objectPoints Array of object points in the object coordinate space, Nx3 1-channel or 1xN/Nx1 3-channel,\n.   where N is the number of points. vector\\<Point3d\\> can also be passed here.\n.   @param imagePoints Array of corresponding image points, Nx2 1-channel or 1xN/Nx1 2-channel,\n.   where N is the number of points. vector\\<Point2d\\> can also be passed here.\n.   @param cameraMatrix Input camera matrix \\f$A = \\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\\f$ .\n.   @param distCoeffs Input vector of distortion coefficients\n.   \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6 [, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$ of\n.   4, 5, 8, 12 or 14 elements. If the vector is NULL/empty, the zero distortion coefficients are\n.   assumed.\n.   @param rvec Input/Output rotation vector (see @ref Rodrigues ) that, together with tvec, brings points from\n.   the model coordinate system to the camera coordinate system. Input values are used as an initial solution.\n.   @param tvec Input/Output translation vector. Input values are used as an initial solution.\n.   @param criteria Criteria when to stop the Levenberg-Marquard iterative algorithm.\n.   \n.   The function refines the object pose given at least 3 object points, their corresponding image\n.   projections, an initial solution for the rotation and translation vector,\n.   as well as the camera matrix and the distortion coefficients.\n.   The function minimizes the projection error with respect to the rotation and the translation vectors, according\n.   to a Levenberg-Marquardt iterative minimization @cite Madsen04 @cite Eade13 process.'
    ...

def solvePnPRefineVVS(objectPoints, imagePoints, cameraMatrix, distCoeffs, rvec, tvec, criteria=..., VVSlambda=...) -> typing.Any:
    'solvePnPRefineVVS(objectPoints, imagePoints, cameraMatrix, distCoeffs, rvec, tvec[, criteria[, VVSlambda]]) -> rvec, tvec\n.   @brief Refine a pose (the translation and the rotation that transform a 3D point expressed in the object coordinate frame\n.   to the camera coordinate frame) from a 3D-2D point correspondences and starting from an initial solution.\n.   \n.   @param objectPoints Array of object points in the object coordinate space, Nx3 1-channel or 1xN/Nx1 3-channel,\n.   where N is the number of points. vector\\<Point3d\\> can also be passed here.\n.   @param imagePoints Array of corresponding image points, Nx2 1-channel or 1xN/Nx1 2-channel,\n.   where N is the number of points. vector\\<Point2d\\> can also be passed here.\n.   @param cameraMatrix Input camera matrix \\f$A = \\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\\f$ .\n.   @param distCoeffs Input vector of distortion coefficients\n.   \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6 [, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$ of\n.   4, 5, 8, 12 or 14 elements. If the vector is NULL/empty, the zero distortion coefficients are\n.   assumed.\n.   @param rvec Input/Output rotation vector (see @ref Rodrigues ) that, together with tvec, brings points from\n.   the model coordinate system to the camera coordinate system. Input values are used as an initial solution.\n.   @param tvec Input/Output translation vector. Input values are used as an initial solution.\n.   @param criteria Criteria when to stop the Levenberg-Marquard iterative algorithm.\n.   @param VVSlambda Gain for the virtual visual servoing control law, equivalent to the \\f$\\alpha\\f$\n.   gain in the Damped Gauss-Newton formulation.\n.   \n.   The function refines the object pose given at least 3 object points, their corresponding image\n.   projections, an initial solution for the rotation and translation vector,\n.   as well as the camera matrix and the distortion coefficients.\n.   The function minimizes the projection error with respect to the rotation and the translation vectors, using a\n.   virtual visual servoing (VVS) @cite Chaumette06 @cite Marchand16 scheme.'
    ...

def solvePoly(coeffs, roots=..., maxIters=...) -> typing.Any:
    'solvePoly(coeffs[, roots[, maxIters]]) -> retval, roots\n.   @brief Finds the real or complex roots of a polynomial equation.\n.   \n.   The function cv::solvePoly finds real and complex roots of a polynomial equation:\n.   \\f[\\texttt{coeffs} [n] x^{n} +  \\texttt{coeffs} [n-1] x^{n-1} + ... +  \\texttt{coeffs} [1] x +  \\texttt{coeffs} [0] = 0\\f]\n.   @param coeffs array of polynomial coefficients.\n.   @param roots output (complex) array of roots.\n.   @param maxIters maximum number of iterations the algorithm does.'
    ...

def sort(src: Mat, flags: int, dts: Mat = ...) -> typing.Any:
    'sort(src, flags[, dst]) -> dst\n.   @brief Sorts each row or each column of a matrix.\n.   \n.   The function cv::sort sorts each matrix row or each matrix column in\n.   ascending or descending order. So you should pass two operation flags to\n.   get desired behaviour. If you want to sort matrix rows or columns\n.   lexicographically, you can use STL std::sort generic function with the\n.   proper comparison predicate.\n.   \n.   @param src input single-channel array.\n.   @param dst output array of the same size and type as src.\n.   @param flags operation flags, a combination of #SortFlags\n.   @sa sortIdx, randShuffle'
    ...

def sortIdx(src: Mat, flags: int, dts: Mat = ...) -> typing.Any:
    'sortIdx(src, flags[, dst]) -> dst\n.   @brief Sorts each row or each column of a matrix.\n.   \n.   The function cv::sortIdx sorts each matrix row or each matrix column in the\n.   ascending or descending order. So you should pass two operation flags to\n.   get desired behaviour. Instead of reordering the elements themselves, it\n.   stores the indices of sorted elements in the output array. For example:\n.   @code\n.       Mat A = Mat::eye(3,3,CV_32F), B;\n.       sortIdx(A, B, SORT_EVERY_ROW + SORT_ASCENDING);\n.       // B will probably contain\n.       // (because of equal elements in A some permutations are possible):\n.       // [[1, 2, 0], [0, 2, 1], [0, 1, 2]]\n.   @endcode\n.   @param src input single-channel array.\n.   @param dst output integer array of the same size as src.\n.   @param flags operation flags that could be a combination of cv::SortFlags\n.   @sa sort, randShuffle'
    ...

def spatialGradient(src: Mat, dx=..., dy=..., ksize=..., borderType=...) -> typing.Any:
    'spatialGradient(src[, dx[, dy[, ksize[, borderType]]]]) -> dx, dy\n.   @brief Calculates the first order image derivative in both x and y using a Sobel operator\n.   \n.   Equivalent to calling:\n.   \n.   @code\n.   Sobel( src, dx, CV_16SC1, 1, 0, 3 );\n.   Sobel( src, dy, CV_16SC1, 0, 1, 3 );\n.   @endcode\n.   \n.   @param src input image.\n.   @param dx output image with first-order derivative in x.\n.   @param dy output image with first-order derivative in y.\n.   @param ksize size of Sobel kernel. It must be 3.\n.   @param borderType pixel extrapolation method, see #BorderTypes.\n.                     Only #BORDER_DEFAULT=#BORDER_REFLECT_101 and #BORDER_REPLICATE are supported.\n.   \n.   @sa Sobel'
    ...

def split(m, mv=...) -> typing.Any:
    'split(m[, mv]) -> mv\n.   @overload\n.   @param m input multi-channel array.\n.   @param mv output vector of arrays; the arrays themselves are reallocated, if needed.'
    ...

def sqrBoxFilter(src: Mat, ddepth, ksize, dts: Mat = ..., anchor=..., normalize=..., borderType=...) -> typing.Any:
    "sqrBoxFilter(src, ddepth, ksize[, dst[, anchor[, normalize[, borderType]]]]) -> dst\n.   @brief Calculates the normalized sum of squares of the pixel values overlapping the filter.\n.   \n.   For every pixel \\f$ (x, y) \\f$ in the source image, the function calculates the sum of squares of those neighboring\n.   pixel values which overlap the filter placed over the pixel \\f$ (x, y) \\f$.\n.   \n.   The unnormalized square box filter can be useful in computing local image statistics such as the the local\n.   variance and standard deviation around the neighborhood of a pixel.\n.   \n.   @param src input image\n.   @param dst output image of the same size and type as _src\n.   @param ddepth the output image depth (-1 to use src.depth())\n.   @param ksize kernel size\n.   @param anchor kernel anchor point. The default value of Point(-1, -1) denotes that the anchor is at the kernel\n.   center.\n.   @param normalize flag, specifying whether the kernel is to be normalized by it's area or not.\n.   @param borderType border mode used to extrapolate pixels outside of the image, see #BorderTypes. #BORDER_WRAP is not supported.\n.   @sa boxFilter"
    ...

def sqrt(src: Mat, dts: Mat = ...) -> typing.Any:
    'sqrt(src[, dst]) -> dst\n.   @brief Calculates a square root of array elements.\n.   \n.   The function cv::sqrt calculates a square root of each input array element.\n.   In case of multi-channel arrays, each channel is processed\n.   independently. The accuracy is approximately the same as of the built-in\n.   std::sqrt .\n.   @param src input floating-point array.\n.   @param dst output array of the same size and type as src.'
    ...

def startWindowThread() -> typing.Any:
    'startWindowThread() -> retval\n.'
    ...

def stereoCalibrate(objectPoints, imagePoints1, imagePoints2, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, imageSize, R=..., T=..., E=..., F=..., flags: int = ..., criteria=...) -> typing.Any:
    'stereoCalibrate(objectPoints, imagePoints1, imagePoints2, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, imageSize[, R[, T[, E[, F[, flags[, criteria]]]]]]) -> retval, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, R, T, E, F\n.'
    ...

def stereoCalibrateExtended(objectPoints, imagePoints1, imagePoints2, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, imageSize, R, T, E=..., F=..., perViewErrors=..., flags: int = ..., criteria=...) -> typing.Any:
    "stereoCalibrateExtended(objectPoints, imagePoints1, imagePoints2, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, imageSize, R, T[, E[, F[, perViewErrors[, flags[, criteria]]]]]) -> retval, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, R, T, E, F, perViewErrors\n.   @brief Calibrates a stereo camera set up. This function finds the intrinsic parameters\n.   for each of the two cameras and the extrinsic parameters between the two cameras.\n.   \n.   @param objectPoints Vector of vectors of the calibration pattern points. The same structure as\n.   in @ref calibrateCamera. For each pattern view, both cameras need to see the same object\n.   points. Therefore, objectPoints.size(), imagePoints1.size(), and imagePoints2.size() need to be\n.   equal as well as objectPoints[i].size(), imagePoints1[i].size(), and imagePoints2[i].size() need to\n.   be equal for each i.\n.   @param imagePoints1 Vector of vectors of the projections of the calibration pattern points,\n.   observed by the first camera. The same structure as in @ref calibrateCamera.\n.   @param imagePoints2 Vector of vectors of the projections of the calibration pattern points,\n.   observed by the second camera. The same structure as in @ref calibrateCamera.\n.   @param cameraMatrix1 Input/output camera matrix for the first camera, the same as in\n.   @ref calibrateCamera. Furthermore, for the stereo case, additional flags may be used, see below.\n.   @param distCoeffs1 Input/output vector of distortion coefficients, the same as in\n.   @ref calibrateCamera.\n.   @param cameraMatrix2 Input/output second camera matrix for the second camera. See description for\n.   cameraMatrix1.\n.   @param distCoeffs2 Input/output lens distortion coefficients for the second camera. See\n.   description for distCoeffs1.\n.   @param imageSize Size of the image used only to initialize the intrinsic camera matrices.\n.   @param R Output rotation matrix. Together with the translation vector T, this matrix brings\n.   points given in the first camera's coordinate system to points in the second camera's\n.   coordinate system. In more technical terms, the tuple of R and T performs a change of basis\n.   from the first camera's coordinate system to the second camera's coordinate system. Due to its\n.   duality, this tuple is equivalent to the position of the first camera with respect to the\n.   second camera coordinate system.\n.   @param T Output translation vector, see description above.\n.   @param E Output essential matrix.\n.   @param F Output fundamental matrix.\n.   @param perViewErrors Output vector of the RMS re-projection error estimated for each pattern view.\n.   @param flags Different flags that may be zero or a combination of the following values:\n.   -   **CALIB_FIX_INTRINSIC** Fix cameraMatrix? and distCoeffs? so that only R, T, E, and F\n.   matrices are estimated.\n.   -   **CALIB_USE_INTRINSIC_GUESS** Optimize some or all of the intrinsic parameters\n.   according to the specified flags. Initial values are provided by the user.\n.   -   **CALIB_USE_EXTRINSIC_GUESS** R and T contain valid initial values that are optimized further.\n.   Otherwise R and T are initialized to the median value of the pattern views (each dimension separately).\n.   -   **CALIB_FIX_PRINCIPAL_POINT** Fix the principal points during the optimization.\n.   -   **CALIB_FIX_FOCAL_LENGTH** Fix \\f$f^{(j)}_x\\f$ and \\f$f^{(j)}_y\\f$ .\n.   -   **CALIB_FIX_ASPECT_RATIO** Optimize \\f$f^{(j)}_y\\f$ . Fix the ratio \\f$f^{(j)}_x/f^{(j)}_y\\f$\n.   .\n.   -   **CALIB_SAME_FOCAL_LENGTH** Enforce \\f$f^{(0)}_x=f^{(1)}_x\\f$ and \\f$f^{(0)}_y=f^{(1)}_y\\f$ .\n.   -   **CALIB_ZERO_TANGENT_DIST** Set tangential distortion coefficients for each camera to\n.   zeros and fix there.\n.   -   **CALIB_FIX_K1,...,CALIB_FIX_K6** Do not change the corresponding radial\n.   distortion coefficient during the optimization. If CALIB_USE_INTRINSIC_GUESS is set,\n.   the coefficient from the supplied distCoeffs matrix is used. Otherwise, it is set to 0.\n.   -   **CALIB_RATIONAL_MODEL** Enable coefficients k4, k5, and k6. To provide the backward\n.   compatibility, this extra flag should be explicitly specified to make the calibration\n.   function use the rational model and return 8 coefficients. If the flag is not set, the\n.   function computes and returns only 5 distortion coefficients.\n.   -   **CALIB_THIN_PRISM_MODEL** Coefficients s1, s2, s3 and s4 are enabled. To provide the\n.   backward compatibility, this extra flag should be explicitly specified to make the\n.   calibration function use the thin prism model and return 12 coefficients. If the flag is not\n.   set, the function computes and returns only 5 distortion coefficients.\n.   -   **CALIB_FIX_S1_S2_S3_S4** The thin prism distortion coefficients are not changed during\n.   the optimization. If CALIB_USE_INTRINSIC_GUESS is set, the coefficient from the\n.   supplied distCoeffs matrix is used. Otherwise, it is set to 0.\n.   -   **CALIB_TILTED_MODEL** Coefficients tauX and tauY are enabled. To provide the\n.   backward compatibility, this extra flag should be explicitly specified to make the\n.   calibration function use the tilted sensor model and return 14 coefficients. If the flag is not\n.   set, the function computes and returns only 5 distortion coefficients.\n.   -   **CALIB_FIX_TAUX_TAUY** The coefficients of the tilted sensor model are not changed during\n.   the optimization. If CALIB_USE_INTRINSIC_GUESS is set, the coefficient from the\n.   supplied distCoeffs matrix is used. Otherwise, it is set to 0.\n.   @param criteria Termination criteria for the iterative optimization algorithm.\n.   \n.   The function estimates the transformation between two cameras making a stereo pair. If one computes\n.   the poses of an object relative to the first camera and to the second camera,\n.   ( \\f$R_1\\f$,\\f$T_1\\f$ ) and (\\f$R_2\\f$,\\f$T_2\\f$), respectively, for a stereo camera where the\n.   relative position and orientation between the two cameras are fixed, then those poses definitely\n.   relate to each other. This means, if the relative position and orientation (\\f$R\\f$,\\f$T\\f$) of the\n.   two cameras is known, it is possible to compute (\\f$R_2\\f$,\\f$T_2\\f$) when (\\f$R_1\\f$,\\f$T_1\\f$) is\n.   given. This is what the described function does. It computes (\\f$R\\f$,\\f$T\\f$) such that:\n.   \n.   \\f[R_2=R R_1\\f]\n.   \\f[T_2=R T_1 + T.\\f]\n.   \n.   Therefore, one can compute the coordinate representation of a 3D point for the second camera's\n.   coordinate system when given the point's coordinate representation in the first camera's coordinate\n.   system:\n.   \n.   \\f[\\begin{bmatrix}\n.   X_2 \\\\\n.   Y_2 \\\\\n.   Z_2 \\\\\n.   1\n.   \\end{bmatrix} = \\begin{bmatrix}\n.   R & T \\\\\n.   0 & 1\n.   \\end{bmatrix} \\begin{bmatrix}\n.   X_1 \\\\\n.   Y_1 \\\\\n.   Z_1 \\\\\n.   1\n.   \\end{bmatrix}.\\f]\n.   \n.   \n.   Optionally, it computes the essential matrix E:\n.   \n.   \\f[E= \\vecthreethree{0}{-T_2}{T_1}{T_2}{0}{-T_0}{-T_1}{T_0}{0} R\\f]\n.   \n.   where \\f$T_i\\f$ are components of the translation vector \\f$T\\f$ : \\f$T=[T_0, T_1, T_2]^T\\f$ .\n.   And the function can also compute the fundamental matrix F:\n.   \n.   \\f[F = cameraMatrix2^{-T}\\cdot E \\cdot cameraMatrix1^{-1}\\f]\n.   \n.   Besides the stereo-related information, the function can also perform a full calibration of each of\n.   the two cameras. However, due to the high dimensionality of the parameter space and noise in the\n.   input data, the function can diverge from the correct solution. If the intrinsic parameters can be\n.   estimated with high accuracy for each of the cameras individually (for example, using\n.   calibrateCamera ), you are recommended to do so and then pass CALIB_FIX_INTRINSIC flag to the\n.   function along with the computed intrinsic parameters. Otherwise, if all the parameters are\n.   estimated at once, it makes sense to restrict some parameters, for example, pass\n.   CALIB_SAME_FOCAL_LENGTH and CALIB_ZERO_TANGENT_DIST flags, which is usually a\n.   reasonable assumption.\n.   \n.   Similarly to calibrateCamera, the function minimizes the total re-projection error for all the\n.   points in all the available views from both cameras. The function returns the final value of the\n.   re-projection error."
    ...

def stereoRectify(cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, imageSize, R, T, R1=..., R2=..., P1=..., P2=..., Q=..., flags: int = ..., alpha=..., newImageSize=...) -> typing.Any:
    'stereoRectify(cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, imageSize, R, T[, R1[, R2[, P1[, P2[, Q[, flags[, alpha[, newImageSize]]]]]]]]) -> R1, R2, P1, P2, Q, validPixROI1, validPixROI2\n.   @brief Computes rectification transforms for each head of a calibrated stereo camera.\n.   \n.   @param cameraMatrix1 First camera matrix.\n.   @param distCoeffs1 First camera distortion parameters.\n.   @param cameraMatrix2 Second camera matrix.\n.   @param distCoeffs2 Second camera distortion parameters.\n.   @param imageSize Size of the image used for stereo calibration.\n.   @param R Rotation matrix from the coordinate system of the first camera to the second camera,\n.   see @ref stereoCalibrate.\n.   @param T Translation vector from the coordinate system of the first camera to the second camera,\n.   see @ref stereoCalibrate.\n.   @param R1 Output 3x3 rectification transform (rotation matrix) for the first camera. This matrix\n.   brings points given in the unrectified first camera\'s coordinate system to points in the rectified\n.   first camera\'s coordinate system. In more technical terms, it performs a change of basis from the\n.   unrectified first camera\'s coordinate system to the rectified first camera\'s coordinate system.\n.   @param R2 Output 3x3 rectification transform (rotation matrix) for the second camera. This matrix\n.   brings points given in the unrectified second camera\'s coordinate system to points in the rectified\n.   second camera\'s coordinate system. In more technical terms, it performs a change of basis from the\n.   unrectified second camera\'s coordinate system to the rectified second camera\'s coordinate system.\n.   @param P1 Output 3x4 projection matrix in the new (rectified) coordinate systems for the first\n.   camera, i.e. it projects points given in the rectified first camera coordinate system into the\n.   rectified first camera\'s image.\n.   @param P2 Output 3x4 projection matrix in the new (rectified) coordinate systems for the second\n.   camera, i.e. it projects points given in the rectified first camera coordinate system into the\n.   rectified second camera\'s image.\n.   @param Q Output \\f$4 \\times 4\\f$ disparity-to-depth mapping matrix (see @ref reprojectImageTo3D).\n.   @param flags Operation flags that may be zero or CALIB_ZERO_DISPARITY . If the flag is set,\n.   the function makes the principal points of each camera have the same pixel coordinates in the\n.   rectified views. And if the flag is not set, the function may still shift the images in the\n.   horizontal or vertical direction (depending on the orientation of epipolar lines) to maximize the\n.   useful image area.\n.   @param alpha Free scaling parameter. If it is -1 or absent, the function performs the default\n.   scaling. Otherwise, the parameter should be between 0 and 1. alpha=0 means that the rectified\n.   images are zoomed and shifted so that only valid pixels are visible (no black areas after\n.   rectification). alpha=1 means that the rectified image is decimated and shifted so that all the\n.   pixels from the original images from the cameras are retained in the rectified images (no source\n.   image pixels are lost). Any intermediate value yields an intermediate result between\n.   those two extreme cases.\n.   @param newImageSize New image resolution after rectification. The same size should be passed to\n.   initUndistortRectifyMap (see the stereo_calib.cpp sample in OpenCV samples directory). When (0,0)\n.   is passed (default), it is set to the original imageSize . Setting it to a larger value can help you\n.   preserve details in the original image, especially when there is a big radial distortion.\n.   @param validPixROI1 Optional output rectangles inside the rectified images where all the pixels\n.   are valid. If alpha=0 , the ROIs cover the whole images. Otherwise, they are likely to be smaller\n.   (see the picture below).\n.   @param validPixROI2 Optional output rectangles inside the rectified images where all the pixels\n.   are valid. If alpha=0 , the ROIs cover the whole images. Otherwise, they are likely to be smaller\n.   (see the picture below).\n.   \n.   The function computes the rotation matrices for each camera that (virtually) make both camera image\n.   planes the same plane. Consequently, this makes all the epipolar lines parallel and thus simplifies\n.   the dense stereo correspondence problem. The function takes the matrices computed by stereoCalibrate\n.   as input. As output, it provides two rotation matrices and also two projection matrices in the new\n.   coordinates. The function distinguishes the following two cases:\n.   \n.   -   **Horizontal stereo**: the first and the second camera views are shifted relative to each other\n.       mainly along the x-axis (with possible small vertical shift). In the rectified images, the\n.       corresponding epipolar lines in the left and right cameras are horizontal and have the same\n.       y-coordinate. P1 and P2 look like:\n.   \n.       \\f[\\texttt{P1} = \\begin{bmatrix}\n.                           f & 0 & cx_1 & 0 \\\\\n.                           0 & f & cy & 0 \\\\\n.                           0 & 0 & 1 & 0\n.                        \\end{bmatrix}\\f]\n.   \n.       \\f[\\texttt{P2} = \\begin{bmatrix}\n.                           f & 0 & cx_2 & T_x*f \\\\\n.                           0 & f & cy & 0 \\\\\n.                           0 & 0 & 1 & 0\n.                        \\end{bmatrix} ,\\f]\n.   \n.       where \\f$T_x\\f$ is a horizontal shift between the cameras and \\f$cx_1=cx_2\\f$ if\n.       CALIB_ZERO_DISPARITY is set.\n.   \n.   -   **Vertical stereo**: the first and the second camera views are shifted relative to each other\n.       mainly in the vertical direction (and probably a bit in the horizontal direction too). The epipolar\n.       lines in the rectified images are vertical and have the same x-coordinate. P1 and P2 look like:\n.   \n.       \\f[\\texttt{P1} = \\begin{bmatrix}\n.                           f & 0 & cx & 0 \\\\\n.                           0 & f & cy_1 & 0 \\\\\n.                           0 & 0 & 1 & 0\n.                        \\end{bmatrix}\\f]\n.   \n.       \\f[\\texttt{P2} = \\begin{bmatrix}\n.                           f & 0 & cx & 0 \\\\\n.                           0 & f & cy_2 & T_y*f \\\\\n.                           0 & 0 & 1 & 0\n.                        \\end{bmatrix},\\f]\n.   \n.       where \\f$T_y\\f$ is a vertical shift between the cameras and \\f$cy_1=cy_2\\f$ if\n.       CALIB_ZERO_DISPARITY is set.\n.   \n.   As you can see, the first three columns of P1 and P2 will effectively be the new "rectified" camera\n.   matrices. The matrices, together with R1 and R2 , can then be passed to initUndistortRectifyMap to\n.   initialize the rectification map for each camera.\n.   \n.   See below the screenshot from the stereo_calib.cpp sample. Some red horizontal lines pass through\n.   the corresponding image regions. This means that the images are well rectified, which is what most\n.   stereo correspondence algorithms rely on. The green rectangles are roi1 and roi2 . You see that\n.   their interiors are all valid pixels.\n.   \n.   ![image](pics/stereo_undistort.jpg)'
    ...

def stereoRectifyUncalibrated(points1, points2, F, imgSize, H1=..., H2=..., threshold=...) -> typing.Any:
    'stereoRectifyUncalibrated(points1, points2, F, imgSize[, H1[, H2[, threshold]]]) -> retval, H1, H2\n.   @brief Computes a rectification transform for an uncalibrated stereo camera.\n.   \n.   @param points1 Array of feature points in the first image.\n.   @param points2 The corresponding points in the second image. The same formats as in\n.   findFundamentalMat are supported.\n.   @param F Input fundamental matrix. It can be computed from the same set of point pairs using\n.   findFundamentalMat .\n.   @param imgSize Size of the image.\n.   @param H1 Output rectification homography matrix for the first image.\n.   @param H2 Output rectification homography matrix for the second image.\n.   @param threshold Optional threshold used to filter out the outliers. If the parameter is greater\n.   than zero, all the point pairs that do not comply with the epipolar geometry (that is, the points\n.   for which \\f$|\\texttt{points2[i]}^T*\\texttt{F}*\\texttt{points1[i]}|>\\texttt{threshold}\\f$ ) are\n.   rejected prior to computing the homographies. Otherwise, all the points are considered inliers.\n.   \n.   The function computes the rectification transformations without knowing intrinsic parameters of the\n.   cameras and their relative position in the space, which explains the suffix "uncalibrated". Another\n.   related difference from stereoRectify is that the function outputs not the rectification\n.   transformations in the object (3D) space, but the planar perspective transformations encoded by the\n.   homography matrices H1 and H2 . The function implements the algorithm @cite Hartley99 .\n.   \n.   @note\n.      While the algorithm does not need to know the intrinsic parameters of the cameras, it heavily\n.       depends on the epipolar geometry. Therefore, if the camera lenses have a significant distortion,\n.       it would be better to correct it before computing the fundamental matrix and calling this\n.       function. For example, distortion coefficients can be estimated for each head of stereo camera\n.       separately by using calibrateCamera . Then, the images can be corrected using undistort , or\n.       just the point coordinates can be corrected with undistortPoints .'
    ...

def stylization(src: Mat, dts: Mat = ..., sigma_s=..., sigma_r=...) -> typing.Any:
    'stylization(src[, dst[, sigma_s[, sigma_r]]]) -> dst\n.   @brief Stylization aims to produce digital imagery with a wide variety of effects not focused on\n.   photorealism. Edge-aware filters are ideal for stylization, as they can abstract regions of low\n.   contrast while preserving, or enhancing, high-contrast features.\n.   \n.   @param src Input 8-bit 3-channel image.\n.   @param dst Output image with the same size and type as src.\n.   @param sigma_s %Range between 0 to 200.\n.   @param sigma_r %Range between 0 to 1.'
    ...

def subtract(src1: Mat, src2: Mat, dts: Mat = ..., mask: Mat = ..., dtype=...) -> typing.Any:
    'subtract(src1, src2[, dst[, mask[, dtype]]]) -> dst\n.   @brief Calculates the per-element difference between two arrays or array and a scalar.\n.   \n.   The function subtract calculates:\n.   - Difference between two arrays, when both input arrays have the same size and the same number of\n.   channels:\n.       \\f[\\texttt{dst}(I) =  \\texttt{saturate} ( \\texttt{src1}(I) -  \\texttt{src2}(I)) \\quad \\texttt{if mask}(I) \\ne0\\f]\n.   - Difference between an array and a scalar, when src2 is constructed from Scalar or has the same\n.   number of elements as `src1.channels()`:\n.       \\f[\\texttt{dst}(I) =  \\texttt{saturate} ( \\texttt{src1}(I) -  \\texttt{src2} ) \\quad \\texttt{if mask}(I) \\ne0\\f]\n.   - Difference between a scalar and an array, when src1 is constructed from Scalar or has the same\n.   number of elements as `src2.channels()`:\n.       \\f[\\texttt{dst}(I) =  \\texttt{saturate} ( \\texttt{src1} -  \\texttt{src2}(I) ) \\quad \\texttt{if mask}(I) \\ne0\\f]\n.   - The reverse difference between a scalar and an array in the case of `SubRS`:\n.       \\f[\\texttt{dst}(I) =  \\texttt{saturate} ( \\texttt{src2} -  \\texttt{src1}(I) ) \\quad \\texttt{if mask}(I) \\ne0\\f]\n.   where I is a multi-dimensional index of array elements. In case of multi-channel arrays, each\n.   channel is processed independently.\n.   \n.   The first function in the list above can be replaced with matrix expressions:\n.   @code{.cpp}\n.       dst = src1 - src2;\n.       dst -= src1; // equivalent to subtract(dst, src1, dst);\n.   @endcode\n.   The input arrays and the output array can all have the same or different depths. For example, you\n.   can subtract to 8-bit unsigned arrays and store the difference in a 16-bit signed array. Depth of\n.   the output array is determined by dtype parameter. In the second and third cases above, as well as\n.   in the first case, when src1.depth() == src2.depth(), dtype can be set to the default -1. In this\n.   case the output array will have the same depth as the input array, be it src1, src2 or both.\n.   @note Saturation is not applied when the output array has the depth CV_32S. You may even get\n.   result of an incorrect sign in the case of overflow.\n.   @param src1 first input array or a scalar.\n.   @param src2 second input array or a scalar.\n.   @param dst output array of the same size and the same number of channels as the input array.\n.   @param mask optional operation mask; this is an 8-bit single channel array that specifies elements\n.   of the output array to be changed.\n.   @param dtype optional depth of the output array\n.   @sa  add, addWeighted, scaleAdd, Mat::convertTo'
    ...

def sumElems(src) -> typing.Any:
    'sumElems(src) -> retval\n.   @brief Calculates the sum of array elements.\n.   \n.   The function cv::sum calculates and returns the sum of array elements,\n.   independently for each channel.\n.   @param src input array that must have from 1 to 4 channels.\n.   @sa  countNonZero, mean, meanStdDev, norm, minMaxLoc, reduce'
    ...

def textureFlattening(src: Mat, mask: Mat, dts: Mat = ..., low_threshold=..., high_threshold=..., kernel_size=...) -> typing.Any:
    "textureFlattening(src, mask[, dst[, low_threshold[, high_threshold[, kernel_size]]]]) -> dst\n.   @brief By retaining only the gradients at edge locations, before integrating with the Poisson solver, one\n.   washes out the texture of the selected region, giving its contents a flat aspect. Here Canny Edge %Detector is used.\n.   \n.   @param src Input 8-bit 3-channel image.\n.   @param mask Input 8-bit 1 or 3-channel image.\n.   @param dst Output image with the same size and type as src.\n.   @param low_threshold %Range from 0 to 100.\n.   @param high_threshold Value \\> 100.\n.   @param kernel_size The size of the Sobel kernel to be used.\n.   \n.   @note\n.   The algorithm assumes that the color of the source image is close to that of the destination. This\n.   assumption means that when the colors don't match, the source image color gets tinted toward the\n.   color of the destination image."
    ...

def threshold(src: Mat, thresh, maxval, type, dts: Mat = ...) -> typing.Any:
    "threshold(src, thresh, maxval, type[, dst]) -> retval, dst\n.   @brief Applies a fixed-level threshold to each array element.\n.   \n.   The function applies fixed-level thresholding to a multiple-channel array. The function is typically\n.   used to get a bi-level (binary) image out of a grayscale image ( #compare could be also used for\n.   this purpose) or for removing a noise, that is, filtering out pixels with too small or too large\n.   values. There are several types of thresholding supported by the function. They are determined by\n.   type parameter.\n.   \n.   Also, the special values #THRESH_OTSU or #THRESH_TRIANGLE may be combined with one of the\n.   above values. In these cases, the function determines the optimal threshold value using the Otsu's\n.   or Triangle algorithm and uses it instead of the specified thresh.\n.   \n.   @note Currently, the Otsu's and Triangle methods are implemented only for 8-bit single-channel images.\n.   \n.   @param src input array (multiple-channel, 8-bit or 32-bit floating point).\n.   @param dst output array of the same size  and type and the same number of channels as src.\n.   @param thresh threshold value.\n.   @param maxval maximum value to use with the #THRESH_BINARY and #THRESH_BINARY_INV thresholding\n.   types.\n.   @param type thresholding type (see #ThresholdTypes).\n.   @return the computed threshold value if Otsu's or Triangle methods used.\n.   \n.   @sa  adaptiveThreshold, findContours, compare, min, max"
    ...

def trace(mtx) -> typing.Any:
    'trace(mtx) -> retval\n.   @brief Returns the trace of a matrix.\n.   \n.   The function cv::trace returns the sum of the diagonal elements of the\n.   matrix mtx .\n.   \\f[\\mathrm{tr} ( \\texttt{mtx} ) =  \\sum _i  \\texttt{mtx} (i,i)\\f]\n.   @param mtx input matrix.'
    ...

def transform(src: Mat, m, dts: Mat = ...) -> typing.Any:
    'transform(src, m[, dst]) -> dst\n.   @brief Performs the matrix transformation of every array element.\n.   \n.   The function cv::transform performs the matrix transformation of every\n.   element of the array src and stores the results in dst :\n.   \\f[\\texttt{dst} (I) =  \\texttt{m} \\cdot \\texttt{src} (I)\\f]\n.   (when m.cols=src.channels() ), or\n.   \\f[\\texttt{dst} (I) =  \\texttt{m} \\cdot [ \\texttt{src} (I); 1]\\f]\n.   (when m.cols=src.channels()+1 )\n.   \n.   Every element of the N -channel array src is interpreted as N -element\n.   vector that is transformed using the M x N or M x (N+1) matrix m to\n.   M-element vector - the corresponding element of the output array dst .\n.   \n.   The function may be used for geometrical transformation of\n.   N -dimensional points, arbitrary linear color space transformation (such\n.   as various kinds of RGB to YUV transforms), shuffling the image\n.   channels, and so forth.\n.   @param src input array that must have as many channels (1 to 4) as\n.   m.cols or m.cols-1.\n.   @param dst output array of the same size and depth as src; it has as\n.   many channels as m.rows.\n.   @param m transformation 2x2 or 2x3 floating-point matrix.\n.   @sa perspectiveTransform, getAffineTransform, estimateAffine2D, warpAffine, warpPerspective'
    ...

def transpose(src: Mat, dts: Mat = ...) -> typing.Any:
    'transpose(src[, dst]) -> dst\n.   @brief Transposes a matrix.\n.   \n.   The function cv::transpose transposes the matrix src :\n.   \\f[\\texttt{dst} (i,j) =  \\texttt{src} (j,i)\\f]\n.   @note No complex conjugation is done in case of a complex matrix. It\n.   should be done separately if needed.\n.   @param src input array.\n.   @param dst output array of the same type as src.'
    ...

def triangulatePoints(projMatr1, projMatr2, projPoints1, projPoints2, points4D=...) -> typing.Any:
    "triangulatePoints(projMatr1, projMatr2, projPoints1, projPoints2[, points4D]) -> points4D\n.   @brief This function reconstructs 3-dimensional points (in homogeneous coordinates) by using\n.   their observations with a stereo camera.\n.   \n.   @param projMatr1 3x4 projection matrix of the first camera, i.e. this matrix projects 3D points\n.   given in the world's coordinate system into the first image.\n.   @param projMatr2 3x4 projection matrix of the second camera, i.e. this matrix projects 3D points\n.   given in the world's coordinate system into the second image.\n.   @param projPoints1 2xN array of feature points in the first image. In the case of the c++ version,\n.   it can be also a vector of feature points or two-channel matrix of size 1xN or Nx1.\n.   @param projPoints2 2xN array of corresponding points in the second image. In the case of the c++\n.   version, it can be also a vector of feature points or two-channel matrix of size 1xN or Nx1.\n.   @param points4D 4xN array of reconstructed points in homogeneous coordinates. These points are\n.   returned in the world's coordinate system.\n.   \n.   @note\n.      Keep in mind that all input data should be of float type in order for this function to work.\n.   \n.   @note\n.      If the projection matrices from @ref stereoRectify are used, then the returned points are\n.      represented in the first camera's rectified coordinate system.\n.   \n.   @sa\n.      reprojectImageTo3D"
    ...

def undistort(src: Mat, cameraMatrix, distCoeffs, dts: Mat = ..., newCameraMatrix=...) -> typing.Any:
    'undistort(src, cameraMatrix, distCoeffs[, dst[, newCameraMatrix]]) -> dst\n.   @brief Transforms an image to compensate for lens distortion.\n.   \n.   The function transforms an image to compensate radial and tangential lens distortion.\n.   \n.   The function is simply a combination of #initUndistortRectifyMap (with unity R ) and #remap\n.   (with bilinear interpolation). See the former function for details of the transformation being\n.   performed.\n.   \n.   Those pixels in the destination image, for which there is no correspondent pixels in the source\n.   image, are filled with zeros (black color).\n.   \n.   A particular subset of the source image that will be visible in the corrected image can be regulated\n.   by newCameraMatrix. You can use #getOptimalNewCameraMatrix to compute the appropriate\n.   newCameraMatrix depending on your requirements.\n.   \n.   The camera matrix and the distortion parameters can be determined using #calibrateCamera. If\n.   the resolution of images is different from the resolution used at the calibration stage, \\f$f_x,\n.   f_y, c_x\\f$ and \\f$c_y\\f$ need to be scaled accordingly, while the distortion coefficients remain\n.   the same.\n.   \n.   @param src Input (distorted) image.\n.   @param dst Output (corrected) image that has the same size and type as src .\n.   @param cameraMatrix Input camera matrix \\f$A = \\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\\f$ .\n.   @param distCoeffs Input vector of distortion coefficients\n.   \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6[, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$\n.   of 4, 5, 8, 12 or 14 elements. If the vector is NULL/empty, the zero distortion coefficients are assumed.\n.   @param newCameraMatrix Camera matrix of the distorted image. By default, it is the same as\n.   cameraMatrix but you may additionally scale and shift the result by using a different matrix.'
    ...

def undistortPoints(src: Mat, cameraMatrix, distCoeffs, dts: Mat = ..., R=..., P=...) -> typing.Any:
    'undistortPoints(src, cameraMatrix, distCoeffs[, dst[, R[, P]]]) -> dst\n.   @brief Computes the ideal point coordinates from the observed point coordinates.\n.   \n.   The function is similar to #undistort and #initUndistortRectifyMap but it operates on a\n.   sparse set of points instead of a raster image. Also the function performs a reverse transformation\n.   to projectPoints. In case of a 3D object, it does not reconstruct its 3D coordinates, but for a\n.   planar object, it does, up to a translation vector, if the proper R is specified.\n.   \n.   For each observed point coordinate \\f$(u, v)\\f$ the function computes:\n.   \\f[\n.   \\begin{array}{l}\n.   x^{"}  \\leftarrow (u - c_x)/f_x  \\\\\n.   y^{"}  \\leftarrow (v - c_y)/f_y  \\\\\n.   (x\',y\') = undistort(x^{"},y^{"}, \\texttt{distCoeffs}) \\\\\n.   {[X\\,Y\\,W]} ^T  \\leftarrow R*[x\' \\, y\' \\, 1]^T  \\\\\n.   x  \\leftarrow X/W  \\\\\n.   y  \\leftarrow Y/W  \\\\\n.   \\text{only performed if P is specified:} \\\\\n.   u\'  \\leftarrow x {f\'}_x + {c\'}_x  \\\\\n.   v\'  \\leftarrow y {f\'}_y + {c\'}_y\n.   \\end{array}\n.   \\f]\n.   \n.   where *undistort* is an approximate iterative algorithm that estimates the normalized original\n.   point coordinates out of the normalized distorted point coordinates ("normalized" means that the\n.   coordinates do not depend on the camera matrix).\n.   \n.   The function can be used for both a stereo camera head or a monocular camera (when R is empty).\n.   @param src Observed point coordinates, 2xN/Nx2 1-channel or 1xN/Nx1 2-channel (CV_32FC2 or CV_64FC2) (or\n.   vector\\<Point2f\\> ).\n.   @param dst Output ideal point coordinates (1xN/Nx1 2-channel or vector\\<Point2f\\> ) after undistortion and reverse perspective\n.   transformation. If matrix P is identity or omitted, dst will contain normalized point coordinates.\n.   @param cameraMatrix Camera matrix \\f$\\vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\\f$ .\n.   @param distCoeffs Input vector of distortion coefficients\n.   \\f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6[, s_1, s_2, s_3, s_4[, \\tau_x, \\tau_y]]]])\\f$\n.   of 4, 5, 8, 12 or 14 elements. If the vector is NULL/empty, the zero distortion coefficients are assumed.\n.   @param R Rectification transformation in the object space (3x3 matrix). R1 or R2 computed by\n.   #stereoRectify can be passed here. If the matrix is empty, the identity transformation is used.\n.   @param P New camera matrix (3x3) or new projection matrix (3x4) \\f$\\begin{bmatrix} {f\'}_x & 0 & {c\'}_x & t_x \\\\ 0 & {f\'}_y & {c\'}_y & t_y \\\\ 0 & 0 & 1 & t_z \\end{bmatrix}\\f$. P1 or P2 computed by\n.   #stereoRectify can be passed here. If the matrix is empty, the identity new camera matrix is used.'
    ...

def undistortPointsIter(src: Mat, cameraMatrix, distCoeffs, R, P, criteria, dts: Mat = ...) -> typing.Any:
    'undistortPointsIter(src, cameraMatrix, distCoeffs, R, P, criteria[, dst]) -> dst\n.   @overload\n.       @note Default version of #undistortPoints does 5 iterations to compute undistorted points.'
    ...

def useOpenVX() -> typing.Any:
    'useOpenVX() -> retval\n.'
    ...

def useOptimized() -> typing.Any:
    'useOptimized() -> retval\n.   @brief Returns the status of optimized code usage.\n.   \n.   The function returns true if the optimized code is enabled. Otherwise, it returns false.'
    ...

def validateDisparity(disparity, cost, minDisparity, numberOfDisparities, disp12MaxDisp=...) -> typing.Any:
    'validateDisparity(disparity, cost, minDisparity, numberOfDisparities[, disp12MaxDisp]) -> disparity\n.'
    ...

def vconcat(src: Mat, dts: Mat = ...) -> typing.Any:
    'vconcat(src[, dst]) -> dst\n.   @overload\n.    @code{.cpp}\n.       std::vector<cv::Mat> matrices = { cv::Mat(1, 4, CV_8UC1, cv::Scalar(1)),\n.                                         cv::Mat(1, 4, CV_8UC1, cv::Scalar(2)),\n.                                         cv::Mat(1, 4, CV_8UC1, cv::Scalar(3)),};\n.   \n.       cv::Mat out;\n.       cv::vconcat( matrices, out );\n.       //out:\n.       //[1,   1,   1,   1;\n.       // 2,   2,   2,   2;\n.       // 3,   3,   3,   3]\n.    @endcode\n.    @param src input array or vector of matrices. all of the matrices must have the same number of cols and the same depth\n.    @param dst output array. It has the same number of cols and depth as the src, and the sum of rows of the src.\n.   same depth.'
    ...

def waitKey(delay=...) -> typing.Any:
    'waitKey([, delay]) -> retval\n.   @brief Waits for a pressed key.\n.   \n.   The function waitKey waits for a key event infinitely (when \\f$\\texttt{delay}\\leq 0\\f$ ) or for delay\n.   milliseconds, when it is positive. Since the OS has a minimum time between switching threads, the\n.   function will not wait exactly delay ms, it will wait at least delay ms, depending on what else is\n.   running on your computer at that time. It returns the code of the pressed key or -1 if no key was\n.   pressed before the specified time had elapsed.\n.   \n.   @note\n.   \n.   This function is the only method in HighGUI that can fetch and handle events, so it needs to be\n.   called periodically for normal event processing unless HighGUI is used within an environment that\n.   takes care of event processing.\n.   \n.   @note\n.   \n.   The function only works if there is at least one HighGUI window created and the window is active.\n.   If there are several HighGUI windows, any of them can be active.\n.   \n.   @param delay Delay in milliseconds. 0 is the special value that means "forever".'
    ...

def waitKeyEx(delay=...) -> typing.Any:
    'waitKeyEx([, delay]) -> retval\n.   @brief Similar to #waitKey, but returns full key code.\n.   \n.   @note\n.   \n.   Key code is implementation specific and depends on used backend: QT/GTK/Win32/etc'
    ...

def warpAffine(src: Mat, M, dsize: typing.Tuple[int, int], dts: Mat = ..., flags: int = ..., borderMode=..., borderValue=...) -> typing.Any:
    'warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) -> dst\n.   @brief Applies an affine transformation to an image.\n.   \n.   The function warpAffine transforms the source image using the specified matrix:\n.   \n.   \\f[\\texttt{dst} (x,y) =  \\texttt{src} ( \\texttt{M} _{11} x +  \\texttt{M} _{12} y +  \\texttt{M} _{13}, \\texttt{M} _{21} x +  \\texttt{M} _{22} y +  \\texttt{M} _{23})\\f]\n.   \n.   when the flag #WARP_INVERSE_MAP is set. Otherwise, the transformation is first inverted\n.   with #invertAffineTransform and then put in the formula above instead of M. The function cannot\n.   operate in-place.\n.   \n.   @param src input image.\n.   @param dst output image that has the size dsize and the same type as src .\n.   @param M \\f$2\\times 3\\f$ transformation matrix.\n.   @param dsize size of the output image.\n.   @param flags combination of interpolation methods (see #InterpolationFlags) and the optional\n.   flag #WARP_INVERSE_MAP that means that M is the inverse transformation (\n.   \\f$\\texttt{dst}\\rightarrow\\texttt{src}\\f$ ).\n.   @param borderMode pixel extrapolation method (see #BorderTypes); when\n.   borderMode=#BORDER_TRANSPARENT, it means that the pixels in the destination image corresponding to\n.   the "outliers" in the source image are not modified by the function.\n.   @param borderValue value used in case of a constant border; by default, it is 0.\n.   \n.   @sa  warpPerspective, resize, remap, getRectSubPix, transform'
    ...

def warpPerspective(src: Mat, M, dsize: typing.Tuple[int, int], dts: Mat = ..., flags: int = ..., borderMode=..., borderValue=...) -> typing.Any:
    'warpPerspective(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) -> dst\n.   @brief Applies a perspective transformation to an image.\n.   \n.   The function warpPerspective transforms the source image using the specified matrix:\n.   \n.   \\f[\\texttt{dst} (x,y) =  \\texttt{src} \\left ( \\frac{M_{11} x + M_{12} y + M_{13}}{M_{31} x + M_{32} y + M_{33}} ,\n.        \\frac{M_{21} x + M_{22} y + M_{23}}{M_{31} x + M_{32} y + M_{33}} \\right )\\f]\n.   \n.   when the flag #WARP_INVERSE_MAP is set. Otherwise, the transformation is first inverted with invert\n.   and then put in the formula above instead of M. The function cannot operate in-place.\n.   \n.   @param src input image.\n.   @param dst output image that has the size dsize and the same type as src .\n.   @param M \\f$3\\times 3\\f$ transformation matrix.\n.   @param dsize size of the output image.\n.   @param flags combination of interpolation methods (#INTER_LINEAR or #INTER_NEAREST) and the\n.   optional flag #WARP_INVERSE_MAP, that sets M as the inverse transformation (\n.   \\f$\\texttt{dst}\\rightarrow\\texttt{src}\\f$ ).\n.   @param borderMode pixel extrapolation method (#BORDER_CONSTANT or #BORDER_REPLICATE).\n.   @param borderValue value used in case of a constant border; by default, it equals 0.\n.   \n.   @sa  warpAffine, resize, remap, getRectSubPix, perspectiveTransform'
    ...

def warpPolar(src: Mat, dsize: typing.Tuple[int, int], center, maxRadius, flags: int, dts: Mat = ...) -> typing.Any:
    'warpPolar(src, dsize: typing.Tuple[int, int], center, maxRadius, flags[, dst]) -> dst\n.   \\brief Remaps an image to polar or semilog-polar coordinates space\n.   \n.   @anchor polar_remaps_reference_image\n.   ![Polar remaps reference](pics/polar_remap_doc.png)\n.   \n.   Transform the source image using the following transformation:\n.   \\f[\n.   dst(\\rho , \\phi ) = src(x,y)\n.   \\f]\n.   \n.   where\n.   \\f[\n.   \\begin{array}{l}\n.   \\vec{I} = (x - center.x, \\;y - center.y) \\\\\n.   \\phi = Kangle \\cdot \\texttt{angle} (\\vec{I}) \\\\\n.   \\rho = \\left\\{\\begin{matrix}\n.   Klin \\cdot \\texttt{magnitude} (\\vec{I}) & default \\\\\n.   Klog \\cdot log_e(\\texttt{magnitude} (\\vec{I})) & if \\; semilog \\\\\n.   \\end{matrix}\\right.\n.   \\end{array}\n.   \\f]\n.   \n.   and\n.   \\f[\n.   \\begin{array}{l}\n.   Kangle = dsize.height / 2\\Pi \\\\\n.   Klin = dsize.width / maxRadius \\\\\n.   Klog = dsize.width / log_e(maxRadius) \\\\\n.   \\end{array}\n.   \\f]\n.   \n.   \n.   \\par Linear vs semilog mapping\n.   \n.   Polar mapping can be linear or semi-log. Add one of #WarpPolarMode to `flags` to specify the polar mapping mode.\n.   \n.   Linear is the default mode.\n.   \n.   The semilog mapping emulates the human "foveal" vision that permit very high acuity on the line of sight (central vision)\n.   in contrast to peripheral vision where acuity is minor.\n.   \n.   \\par Option on `dsize`:\n.   \n.   - if both values in `dsize <=0 ` (default),\n.   the destination image will have (almost) same area of source bounding circle:\n.   \\f[\\begin{array}{l}\n.   dsize.area  \\leftarrow (maxRadius^2 \\cdot \\Pi) \\\\\n.   dsize.width = \\texttt{cvRound}(maxRadius) \\\\\n.   dsize.height = \\texttt{cvRound}(maxRadius \\cdot \\Pi) \\\\\n.   \\end{array}\\f]\n.   \n.   \n.   - if only `dsize.height <= 0`,\n.   the destination image area will be proportional to the bounding circle area but scaled by `Kx * Kx`:\n.   \\f[\\begin{array}{l}\n.   dsize.height = \\texttt{cvRound}(dsize.width \\cdot \\Pi) \\\\\n.   \\end{array}\n.   \\f]\n.   \n.   - if both values in `dsize > 0 `,\n.   the destination image will have the given size therefore the area of the bounding circle will be scaled to `dsize`.\n.   \n.   \n.   \\par Reverse mapping\n.   \n.   You can get reverse mapping adding #WARP_INVERSE_MAP to `flags`\n.   \\snippet polar_transforms.cpp InverseMap\n.   \n.   In addiction, to calculate the original coordinate from a polar mapped coordinate \\f$(rho, phi)->(x, y)\\f$:\n.   \\snippet polar_transforms.cpp InverseCoordinate\n.   \n.   @param src Source image.\n.   @param dst Destination image. It will have same type as src.\n.   @param dsize The destination image size (see description for valid options).\n.   @param center The transformation center.\n.   @param maxRadius The radius of the bounding circle to transform. It determines the inverse magnitude scale parameter too.\n.   @param flags A combination of interpolation methods, #InterpolationFlags + #WarpPolarMode.\n.               - Add #WARP_POLAR_LINEAR to select linear polar mapping (default)\n.               - Add #WARP_POLAR_LOG to select semilog polar mapping\n.               - Add #WARP_INVERSE_MAP for reverse mapping.\n.   @note\n.   -  The function can not operate in-place.\n.   -  To calculate magnitude and angle in degrees #cartToPolar is used internally thus angles are measured from 0 to 360 with accuracy about 0.3 degrees.\n.   -  This function uses #remap. Due to current implementation limitations the size of an input and output images should be less than 32767x32767.\n.   \n.   @sa cv::remap'
    ...

def watershed(image: Mat, markers) -> typing.Any:
    'watershed(image, markers) -> markers\n.   @brief Performs a marker-based image segmentation using the watershed algorithm.\n.   \n.   The function implements one of the variants of watershed, non-parametric marker-based segmentation\n.   algorithm, described in @cite Meyer92 .\n.   \n.   Before passing the image to the function, you have to roughly outline the desired regions in the\n.   image markers with positive (\\>0) indices. So, every region is represented as one or more connected\n.   components with the pixel values 1, 2, 3, and so on. Such markers can be retrieved from a binary\n.   mask using #findContours and #drawContours (see the watershed.cpp demo). The markers are "seeds" of\n.   the future image regions. All the other pixels in markers , whose relation to the outlined regions\n.   is not known and should be defined by the algorithm, should be set to 0\'s. In the function output,\n.   each pixel in markers is set to a value of the "seed" components or to -1 at boundaries between the\n.   regions.\n.   \n.   @note Any two neighbor connected components are not necessarily separated by a watershed boundary\n.   (-1\'s pixels); for example, they can touch each other in the initial marker image passed to the\n.   function.\n.   \n.   @param image Input 8-bit 3-channel image.\n.   @param markers Input/output 32-bit single-channel image (map) of markers. It should have the same\n.   size as image .\n.   \n.   @sa findContours\n.   \n.   @ingroup imgproc_misc'
    ...

def writeOpticalFlow(path, flow) -> typing.Any:
    'writeOpticalFlow(path, flow) -> retval\n.   @brief Write a .flo to disk\n.   \n.    @param path Path to the file to be written\n.    @param flow Flow field to be stored\n.   \n.    The function stores a flow field in a file, returns true on success, false otherwise.\n.    The flow field must be a 2-channel, floating-point matrix (CV_32FC2). First channel corresponds\n.    to the flow in the horizontal direction (u), second - vertical (v).'
    ...

def __getattr__(name) -> typing.Any: ... #incomplete