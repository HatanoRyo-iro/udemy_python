import tarfile

# ファイルの圧縮方法

with tarfile.open('section8/test.tar.gz', 'w:gz') as tr:
    tr.add('section8/test_dir')
    
with tarfile.open('section8/test.tar.gz', 'r:gz') as tr:
    tr.extractall(path='sectiton8/test_tar')
    with tr.extractfile('sectiton8/test_tar/section8/test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())