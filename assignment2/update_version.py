import os
import re

# SCONSTRUCT file interesting lines
# config.version = Version(
# major=15,
# minor=0,
# point=6,
# patch=0
#)

def update_sconstruct():
    # Update the build number in the SConstruct file
    _update_file(
        file_path=os.environ["SourcePath"] + "/develop/global/src/SConstruct",
        replacement=os.environ["SConstructPattern"] + os.environ["BuildNum"],
        pattern=os.environ["SConstructPattern"] + "[\d]+"
    )

# VERSION file interesting line
# ADLMSDK_VERSION_POINT=6
def update_version():
    # "Update the build number in the VERSION file"
    _update_file(
        file_path=os.environ["SourcePath"] + "/develop/global/src/VERSION",
        replacement=os.environ["VersionPattern"] + os.environ["BuildNum"],
        pattern=os.environ["VersionPattern"] + "[\d]+"
    )

def _update_file(file_path, replacement, pattern):
    # Update the build number in the file
    temp_file_path = file_path + ".tmp"
    with open(file_path, "r") as fin, open(temp_file_path, "w") as fout:
        for line in fin:
            line = re.sub(pattern, replacement, line)
            fout.write(line)
    
    os.replace(temp_file_path, file_path)
    


def main():
    update_sconstruct()
    update_version()
    main()