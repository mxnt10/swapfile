#!/bin/bash

pkgver='1.0'
install_root=${install_root:-""}

set -e
# shellcheck disable=SC2015
[ "$install_root" != "" ] && mkdir -p "$install_root"/usr/{bin,share/{applications,pixmaps,swapfile/utils},doc/swapfile-"$pkgver"} || mkdir -p /usr/{share/swapfile/utils,doc/swapfile-"$pkgver"}

install -Dm 0644 appdata/swapfile.png "$install_root"/usr/share/pixmaps
install -Dm 0644 appdata/swapfile.desktop "$install_root"/usr/share/applications

install -Dm 0755 utils/* "$install_root"/usr/share/swapfile/utils

cp -a ChangeLog LICENSE README.md "$install_root"/usr/doc/swapfile-"$pkgver"
cp -Tr src "$install_root"/usr/share/swapfile

echo "#!/bin/bash
cd /usr/share/swapfile
python3 swapfile.py" > "$install_root"/usr/bin/swapfile

chmod 755 "$install_root"/usr/bin/swapfile
exit 0
