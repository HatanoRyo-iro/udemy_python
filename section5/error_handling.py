l = [1, 2, 3]
i = 5
del l


try:
    l[0]
except IndexError as e:
    print("Don't worry: {}".format(e))
except NameError as e:
    print(e)
except Exception as e:   # 全てのエラーをキャッチするのはあんまり良くない
    print('other:{}'.format(e))
else:   # エラーが発生しなかった場合のみ実行される
    print('done')
finally:   # エラーの有無に関わらず実行される
    print('clean up')
