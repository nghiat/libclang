##----------------------------------------------------------------------------##
## DEPS                                                                       ##
##                                                                            ##
## This file is distributed under the MIT License.                            ##
## See LICENSE.txt for details.                                               ##
## Copyright (C) Tran Tuan Nghia <trantuannghia95@gmail.com> 2018             ##
##----------------------------------------------------------------------------##

import _config

deps = []

if _config.is_win:
    deps.extend([
        {
	    "file": "libclang-win-6.0.0.tar.xz",
            "url": "https://media.githubusercontent.com/media/nghiat/binaries/392238e7d558e3d1e32f31b64a558bed7952f226/libclang-win/libclang-win-6.0.0.tar.xz",
            "sha1": "1dc5b443311d27d8006bf4772d89d5cf2f573657"
        }
    ])
