__app_name__ = "logtracing"
__version__ = "0.0.1"

(
    SUCCESS,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
) = range(3)

ERRORS = {
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
}
