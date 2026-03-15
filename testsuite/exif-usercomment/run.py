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
# testwrite=False skips the pixel diff; we only care that metadata survives.

# ASCII JPEG
command += rw_command("src", "usercomment-ascii.jpg", use_oiiotool=1,
                      output_filename="rt-ascii.jpg", safematch=True,
                      testwrite=False)
command += info_command("rt-ascii.jpg", safematch=True)

# Unicode JPEG
command += rw_command("src", "usercomment-unicode.jpg", use_oiiotool=1,
                      output_filename="rt-unicode.jpg", safematch=True,
                      testwrite=False)
command += info_command("rt-unicode.jpg", safematch=True)

# ASCII PNG
command += rw_command("src", "usercomment-ascii.png", use_oiiotool=1,
                      output_filename="rt-ascii.png", safematch=True,
                      testwrite=False)
command += info_command("rt-ascii.png", safematch=True)

# Unicode PNG
command += rw_command("src", "usercomment-unicode.png", use_oiiotool=1,
                      output_filename="rt-unicode.png", safematch=True,
                      testwrite=False)
command += info_command("rt-unicode.png", safematch=True)
