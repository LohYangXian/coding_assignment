import os
import re
import logging 


def update_sconstruct():
    """
    Updates the 'point=' line in the SConstruct file with the new build number

    How it looks 
    config.version = Version(
        major=15,
        minor=0,
        point=6,
        patch=0
    )
    """
    _update_file(
        file_path=os.environ["SourcePath"] + "/develop/global/src/SConstruct",
        replacement=os.environ["SConstructPattern"],
        build_num=os.environ["BuildNum"]
    )

def update_version():
    """
    Updates the 'ADLMSDK_VERSION_POINT=' line in the VERSION file with the new build number

    How it looks 
    ADLMSDK_VERSION_POINT=6
    """
    _update_file(
        file_path=os.environ["SourcePath"] + "/develop/global/src/VERSION",
        pattern=os.environ["VersionPattern"],
        build_num=os.environ["BuildNum"]
    )

def _update_file(file_path, pattern, build_num):
    """
    Generic function to update a file with a new build number
    """

    logging.info(f"Updating {file_path} with Regex pattern {pattern} and build number {build_num}")

    temp_file_path = file_path + ".tmp"
    try:
        with open(file_path, "r") as fin, open(temp_file_path, "w") as fout:
            for line in fin:
                line = re.sub(pattern+"[\d]+", pattern+build_num, line)
                fout.write(line)
    
        os.replace(temp_file_path, file_path)
        logging.info(f"Successfully updated {file_path} with build number {build_num}")

    except Exception as e:
        logging.error(f"Failed to update {file_path} with build number {build_num}: {e}")
        raise

    
def _validate_env_vars(required_vars):
    """
    Validates that all required environment variables are set
    """
    missing = []
    for var in required_vars:
        val = os.environ.get(var)
        if val is None or val.strip() == "":
            missing.append(var)
    
    if missing:
        raise ValueError(f"Missing or empty required environment variables: {', '.join(missing)}")

    if not os.environ["BuildNum"].isdigit():
        raise ValueError("BuildNum must be a valid integer")

    logging.info("All required environment variables are present and valid.")


def main():
    _validate_env_vars(["SourcePath", "SConstructPattern", "VersionPattern", "BuildNum"])
    update_sconstruct()
    update_version()

if __name__ == "__main__":
    try:
        main()
        logging.info("Version update completed successfully.")
    except Exception as e:
        logging.error(f"Version update failed: {e}")
        exit(1)