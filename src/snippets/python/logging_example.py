import logging
import logging.config
import json

JSON_CONFIG_FILENAME = "basic-logging-config.json"

with open(JSON_CONFIG_FILENAME, "r") as f:
    config_dict = json.load(f)
    logging.config.dictConfig(config_dict)

logger = logging.getLogger("")

print("\n--- Sending Log Messages ---")
logger.debug("This is a DEBUG message. It should appear ONLY in the log file.")
logger.info(
    "This is an INFO message. It should appear in the console AND the log file."
)
logger.warning(
    "This is a WARNING message. It should appear in the console AND the log file."
)
logger.error("This is an ERROR message. It indicates a significant problem.")

print("\n--- Raise an Exception ---")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    logger.critical(f"A CRITICAL error occurred: Division by zero! {e}", exc_info=True)
    # The exc_info=True argument is key for logging the full traceback
