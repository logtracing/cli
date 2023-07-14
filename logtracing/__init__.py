__app_name__ = "LogTracing CLI App"
__version__ = "0.0.1"

(
    SUCCESS,
    CONFIG_DIR_ERROR,
    CONFIG_FILE_ERROR,
    ERROR,
) = range(4)

ERRORS = {
    CONFIG_DIR_ERROR: "config directory error",
    CONFIG_FILE_ERROR: "config file error",
}
