# Dependencies - python (obviously), inkscape, imagemagick
# Usage:
# python svg2ico.py <svg filename> 
# e.g.:
# python svg2ico.py test.svg

import os, sys, shutil

def main():
  if len(sys.argv) > 1:
    if os.path.exists(os.getcwd() + sys.argv[1]):
      filename, ext = os.path.splitext(os.path.abspath(os.getcwd() + sys.argv[1]))
      filepath = filename + ext
      if ext == '.svg':
        create_tmp()
        tmpdir = os.path.normpath(os.path.join(os.getcwd() + "/tmp"))
        svg_to_png(filepath, tmpdir)
        png_to_ico(filename)
        rmtmp = input("Do you want to remove the tmp (temporary) directory? (Y/n): ")
        if rmtmp.capitalize() != 'N':
          remove_tmp()
  else:
    print("Usage: python SVG2ICO.py file.svg")

def create_tmp():
  tmpdir = os.path.normpath(os.path.join(os.getcwd() + "/tmp"))
  if os.path.exists(tmpdir):
    print(f"{tmpdir} directory already exists.")
    delch = input("Do you want to delete it and continue? (y/N): ")
    if delch.capitalize() == "Y":
      shutil.rmtree(tmpdir)
      os.mkdir(tmpdir)
    else:
      exit(1)
  else:
    os.mkdir(tmpdir)

def svg_to_png(filepath, tmpdir):
  tmpfile = os.path.normpath(os.path.join(tmpdir, "tmp.svg" ))
  shutil.copyfile(filepath, tmpfile)
  os.chdir(tmpdir)
  for i in 16, 32, 48, 64, 128, 256:
    os.system(f'inkscape --export-type="png" --export-filename="{i}x{i}.png" -w {i} {tmpfile}')

def png_to_ico(filename):
  os.system(f'convert 16x16.png 32x32.png 48x48.png 64x64.png 128x128.png 256x256.png tmp.ico')
  tmpout = os.path.normpath(os.path.join(os.getcwd(), "tmp.ico" ))
  shutil.copyfile(tmpout, (filename + ".ico"))

def remove_tmp():
  os.chdir("..")
  tmpdir = os.path.normpath(os.path.join(os.getcwd() + "/tmp"))
  shutil.rmtree(tmpdir)

if __name__ == '__main__':
  main()