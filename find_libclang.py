##-----------------------------------------------------------------------------##
## find_libclang.py                                                            ##
##                                                                             ##
## This file is distributed under the MIT License. See LICENSE.txt for details.##
## Copyright (C) Tran Tuan Nghia <trantuannghia95@gmail.com> 2018              ##
##-----------------------------------------------------------------------------##
import os
import sys


def get_usr_lib(target_cpu):
    if target_cpu == "x86":
        usr_lib = "/usr/lib32"
    elif target_cpu == "x64":
        usr_lib = "/usr/lib64"
    if not os.path.exists(usr_lib):
        # fallback directory
        usr_lib = "/usr/lib"
    return usr_lib


# Debian based distros have weird install location for clang.
# /usr/lib/llvm-x.x/lib/libclang.so
# /usr/lib/llvm-x.x/include
def find_in_usr_lib_llvm(target_cpu):
    usr_lib = get_usr_lib(target_cpu)
    for dir in os.listdir(usr_lib):
        if dir.startswith("llvm"):
            llvm_dir = os.path.join(usr_lib, dir)
            print("""
            include_dir = "%s"
            lib = "%s"
            """ % (os.path.join(llvm_dir, "include/"),
                   os.path.join(llvm_dir, "lib", "libclang.so")))
            return True
    return False


# Arch based distros
# /usr/lib/libclang.so
# /usr/include
def find_in_usr_lib(target_cpu):
    usr_lib = get_usr_lib(target_cpu)
    so_file = os.path.join(usr_lib, "libclang.so")
    if os.path.exists(so_file) and os.path.exists("/usr/include/clang-c"):
        print("""
        include_dir = "/usr/include"
        lib = "%s"
        """ % (so_file))
        return True
    return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)
    target_cpu = sys.argv[1]
    if target_cpu != "x86" and target_cpu != "x64":
        exit(1)
    if find_in_usr_lib_llvm(target_cpu) or find_in_usr_lib(target_cpu):
        exit(0)
    exit(1)
