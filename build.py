import setup
import os, subprocess

asm_bin = "nasm"
asm_flag = "-fwin32"

cython_bin = "cython"

c_src = "src"
inc_dir = c_src
pyx_src = c_src
asm_src = os.path.join(c_src,"asm")



def search_src_file(src, ext, recursion=False):
    ret_files = []
    for root, dirs, files in os.walk(src):
        for fname in files:
            if fname.endswith(ext):
                ret_files.append(os.path.join(root, fname))
        if not recursion:
            break
    return ret_files


def gen_pyx2c(files):
    for f in files:
        args = [cython_bin,f]
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        p.wait()
        #print p.stdout.read()
        print "[PYX]:"+" ".join(args)
    return files

def gen_objs(asm_list):
    obj_list = [f.replace(".asm", ".obj") for f in asm_list]
    for idx in xrange(len(obj_list)):
        in_f, out_f = asm_list[idx], obj_list[idx]
        args=[asm_bin, asm_flag, "%s"%in_f, "-o %s"%out_f]
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        p.wait()
        print "[ASM]:"+" ".join(args)
        #print p.stdout.read()
    return obj_list


def build():
    #gen .pyx to .c first.
    pyx_files = search_src_file(pyx_src, ".pyx")
    print "gen pyx to c files....."
    gen_pyx2c(pyx_files)

    c_files = search_src_file(c_src, ".c")

    print "gen objs files...."
    asm_files = search_src_file(asm_src, ".asm")
    asm_objs = gen_objs(asm_files)

    setup.sources = c_files
    setup.objs = asm_objs
    setup.inc_dirs = [inc_dir,]
    print "build python ext lib."
    setup.do_setup(["build_ext", "--inplace"])

def clean():
    # clean obj
    objs = search_src_file(asm_src,".obj",True)
    for obj_file in objs:
        if os.path.exists(obj_file):
            os.remove(obj_file)
            print "remove:%s"%obj_file
    pyxs = search_src_file(pyx_src,".pyx")
    for pyx in pyxs:
        c_file = pyx.replace(".pyx",".c")
        if os.path.exists(c_file):
            os.remove(c_file)
            print "remove:%s"%c_file


if __name__ == "__main__":
    import sys
    usage = '''build:build.py
clean:build.py clean
    '''
    if len(sys.argv) > 1:
        if sys.argv[1] == "clean":
            clean()
        elif sys.argv[1] == "help":
            print usage
        else:
            print "unknow args!"
            print usage
    else:
        build()

