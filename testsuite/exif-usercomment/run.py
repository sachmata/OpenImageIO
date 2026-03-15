#!/usr/bin/env python

# Copyright Contributors to the OpenImageIO project.
# SPDX-License-Identifier: Apache-2.0
# https://github.com/AcademySoftwareFoundation/OpenImageIO

# Tests for Exif UserComment tag support (ASCII and Unicode/UCS-2 encodings)
# in both JPEG (little-endian EXIF) and PNG (big-endian EXIF) formats.

redirect = ' >> out.txt 2>&1 '

# -- Read tests ----------------------------------------------------------------

# ASCII UserComment in JPEG (little-endian EXIF stream)
command += info_command("src/usercomment-ascii.jpg", safematch=True)

# Unicode (UCS-2 LE) UserComment in JPEG
command += info_command("src/usercomment-unicode.jpg", safematch=True)

# ASCII UserComment in PNG (big-endian EXIF stream)
command += info_command("src/usercomment-ascii.png", safematch=True)

# Unicode (UCS-2 BE) UserComment in PNG
command += info_command("src/usercomment-unicode.png", safematch=True)

# -- Round-trip write tests ---------------------------------------------------
# Copy each file with oiiotool and read the copy back, to verify that the
# UserComment survives being re-encoded. We deliberately don't use rw_command
# here: its pixel-comparison step is meaningless for a lossy JPEG re-encode,
# and disabling that step would also suppress the write itself.

# ASCII JPEG (little-endian Exif stream)
command += oiiotool("src/usercomment-ascii.jpg -o rt-ascii.jpg")
command += info_command("rt-ascii.jpg", safematch=True)

# Unicode JPEG (UCS-2 LE)
command += oiiotool("src/usercomment-unicode.jpg -o rt-unicode.jpg")
command += info_command("rt-unicode.jpg", safematch=True)

# ASCII PNG (big-endian Exif stream)
command += oiiotool("src/usercomment-ascii.png -o rt-ascii.png")
command += info_command("rt-ascii.png", safematch=True)

# Unicode PNG (UCS-2 BE)
command += oiiotool("src/usercomment-unicode.png -o rt-unicode.png")
command += info_command("rt-unicode.png", safematch=True)
