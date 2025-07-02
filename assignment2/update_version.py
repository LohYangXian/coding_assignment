import os
import re

# SCONSTRUCT file interesting lines
# config.version = Version(
# major=15,
# minor=0,
# point=6,
# patch=0
#)

def updateSconstruct():
    # Update the build number in the SConstruct file
    file_path = os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct")
    temp_file_path = file_path + ".tmp"

    with open(file_path, 'r') as fin, open(temp_file_path, 'w') as fout:
        for line in fin:
            line = re.sub("point\=[\d]+","point="+os.environ["BuildNum"],line)
            fout.write(line)
    
    os.replace(temp_file_path, file_path)

# VERSION file interesting line
# ADLMSDK_VERSION_POINT=6

def updateVersion():
    # "Update the build number in the VERSION file"
    file_path = os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION")
    temp_file_path = file_path + ".tmp"

    with open(file_path, 'r') as fin, open(temp_file_path, 'w') as fout:
        for line in fin:
            line = re.sub("ADLMSDK_VERSION_POINT=[\d]+","ADLMSDK_VERSION_POINT="+os.environ["BuildNum"],line)
            fout.write(line)
    
    os.replace(temp_file_path, file_path)

def main():
    updateSconstruct()
    updateVersion()
    main()