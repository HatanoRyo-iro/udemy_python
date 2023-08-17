import glob
import zipfile

with zipfile.ZipFile('section8/test.zip', 'w') as z:
    # z.write('testzip_dir')
    # z.write('testzip_dir/test.txt')
    for f in glob.glob('section8/test_dir/**', recursive=True):
        print(f)
        z.write(f)
        
with zipfile.ZipFile('section8/test.zip', 'r') as z:
    z.extractall('test.zip')