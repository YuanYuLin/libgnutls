import ops
import iopc

pkg_path = ""
output_dir = ""
arch = ""
src_usr_lib_dir = ""
dst_lib_dir = ""
src_include_dir = ""
dst_include_dir = ""

def set_global(args):
    global pkg_path
    global output_dir
    global arch
    global src_usr_lib_dir
    global dst_lib_dir
    global src_include_dir
    global dst_include_dir
    global tmp_include_dir
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    arch = ops.getEnv("ARCH_ALT")
    if arch == "armhf":
        src_usr_lib_dir = iopc.getBaseRootFile("usr/lib/arm-linux-gnueabihf")
    elif arch == "armel":
        src_usr_lib_dir = iopc.getBaseRootFile("usr/lib/arm-linux-gnueabi")
    elif arch == "x86_64":
        src_usr_lib_dir = iopc.getBaseRootFile("usr/lib/x86_64-linux-gnu")
    else:
        sys.exit(1)
    dst_lib_dir = ops.path_join(output_dir, "lib")

    src_include_dir = iopc.getBaseRootFile("usr/include")
    tmp_include_dir = ops.path_join(output_dir, ops.path_join("include",args["pkg_name"]))
    dst_include_dir = ops.path_join("include",args["pkg_name"])


def MAIN_ENV(args):
    set_global(args)
    return False

def MAIN_EXTRACT(args):
    set_global(args)

    ops.mkdir(dst_lib_dir)

    lib_so = "libgnutls-deb0.so.28.41.0"
    ops.copyto(ops.path_join(src_usr_lib_dir, lib_so), dst_lib_dir)
    ops.ln(dst_lib_dir, lib_so, "libgnutls-deb0.so.28.41")
    ops.ln(dst_lib_dir, lib_so, "libgnutls-deb0.so.28")
    ops.ln(dst_lib_dir, lib_so, "libgnutls-deb0.so")

    ops.ln(dst_lib_dir, lib_so, "libgnutls.so")

    lib_so = "libgnutls-openssl.so.27.0.2"
    ops.copyto(ops.path_join(src_usr_lib_dir, lib_so), dst_lib_dir)
    ops.ln(dst_lib_dir, lib_so, "libgnutls-openssl.so.27.0")
    ops.ln(dst_lib_dir, lib_so, "libgnutls-openssl.so.27")
    ops.ln(dst_lib_dir, lib_so, "libgnutls-openssl.so")

    lib_so = "libgnutlsxx.so.28.1.0"
    ops.copyto(ops.path_join(src_usr_lib_dir, lib_so), dst_lib_dir)
    ops.ln(dst_lib_dir, lib_so, "libgnutlsxx.so.28.1")
    ops.ln(dst_lib_dir, lib_so, "libgnutlsxx.so.28")
    ops.ln(dst_lib_dir, lib_so, "libgnutlsxx.so")

    lib_so = "libssl.so.1.0.0"
    ops.copyto(ops.path_join(src_usr_lib_dir, lib_so), dst_lib_dir)
    ops.ln(dst_lib_dir, lib_so, "libssl.so.1.0")
    ops.ln(dst_lib_dir, lib_so, "libssl.so.1")
    ops.ln(dst_lib_dir, lib_so, "libssl.so")

    lib_so = "libcrypto.so.1.0.0"
    ops.copyto(ops.path_join(src_usr_lib_dir, lib_so), dst_lib_dir)
    ops.ln(dst_lib_dir, lib_so, "libcrypto.so.1.0")
    ops.ln(dst_lib_dir, lib_so, "libcrypto.so.1")
    ops.ln(dst_lib_dir, lib_so, "libcrypto.so")

    ops.mkdir(tmp_include_dir)
    ops.copyto(ops.path_join(src_include_dir, 'gnutls'), tmp_include_dir)

    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(build_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)
    return False

def MAIN_BUILD(args):
    set_global(args)
    return False

def MAIN_INSTALL(args):
    set_global(args)
    '''
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "abstract.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "compat.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "crypto.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "dane.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "dtls.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "gnutls.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "gnutlsxx.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "ocsp.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "openpgp.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "openssl.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "pkcs11.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "pkcs12.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "pkcs7.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "self-test.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "socket.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "system-keys.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "tpm.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "urls.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "x509-ext.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "x509.h"), dst_include_dir)
    '''
    iopc.installBin(args["pkg_name"], ops.path_join(tmp_include_dir, "."), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(dst_lib_dir, "."), "lib") 
    return False

def MAIN_SDKENV(args):
    set_global(args)

    sdkinclude_dir = ops.path_join(iopc.getSdkPath(), 'usr/include/' + args["pkg_name"])
    cflags = ""
    cflags += " -I" + sdkinclude_dir
    cflags += " -I" + ops.path_join(sdkinclude_dir, "gnutls")
    iopc.add_includes(cflags)

    libs = ""
    libs += " -lgnutls-openssl -lgnutls -lgnutlsxx -lssl -lcrypto"
    iopc.add_libs(libs)

    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)
    return False

def MAIN(args):
    set_global(args)

