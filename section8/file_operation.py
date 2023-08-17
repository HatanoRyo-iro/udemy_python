import os
import pathlib
import glob
import shutil


# 指定したものが存在するか
print(os.path.exists('section8/test.txt'))

# ファイルか
print(os.path.isfile('section8/test.txt'))

# ディレクトリか
print(os.path.isdir('section8'))

# # ファイル名の書き換え
# os.rename('section8/test.txt', 'section8/renamed.txt')

# # symlink
# os.symlink('section8/renamed.txt', 'section8/symlinked.txt')


# os.mkdir('section8/test_dir')
# os.rmdir('section8/test_dir')   # test_dir下に何もなかったら削除できる

# pathlib.Path('section8/empty.txt').touch()
# os.remove('section8/empty.txt')


# os.mkdir('section8/test_dir')
# os.mkdir('section8/test_dir/test_dir2')
# print(os.listdir('section8/test_dir'))
# pathlib.Path('section8/test_dir/test_dir2/empty.txt').touch()
# print(glob.glob('section8/test_dir/test_dir2/*'))

# shutil.copy('section8/test_dir/test_dir2/empty.txt',
#             'section8/test_dir/test_dir2/empty2.txt')
# print(glob.glob('section8/test_dir/test_dir2/*'))


#! これ使うには要注意 全部消える
# shutil.rmtree('section8/test_dir')

print(os.getcwd())