#!/bin/bash

# Import colors
source colors.sh
header()
{
    if [ "$#" -eq 2 ]; then
        COLOR="$2"
    else
        COLOR="${UWhi}"
    fi
    echo -e "$COLOR$1${RCol}"
}

fail()
{
    echo "${BRed}$1${RCol}" | exit 1
}

header "Creating binary..."
INSTALLERPATH=$(which pyinstaller)
eval "$INSTALLERPATH -F golatex.py" || fail "Failed to run command 'eval $INSTALLER_PATH golatex.py'"
echo

header "Packing release..."
ARCHIVE=golatex.tar.gz
rm -f "$ARCHIVE"
mv dist/golatex golatex
tar -czf "$ARCHIVE" golatex LICENSE.txt LICENSE-3RD-PARTY.txt PYGMENTS_AUTHORS
header "${UGre}" "Created release archive: golatex.tar.gz"
echo

header "Cleaning up..."
rm -rf build dist golatex.spec golatex
header "${UGre}Done."

