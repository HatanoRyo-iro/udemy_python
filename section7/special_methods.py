class Word(object):
    
    """
    前後にアンダースコアが2個あるのが特殊メソッド
    """
    
    # これも特殊メソッド
    def __init__(self, text):
        self.text = text
        
    def __str__(self):
        return 'Word!!!!!'
    
    def __len__(self):
        return len(self.text)
    
    def __add__(self, word):
        return self.text.lower() + word.text.lower()
    
    # 普通はidが一緒ならTrueを出すけど、このequalの特殊メソッドは値が同じならTrueを返す
    def __eq__(self, word):
        return self.text.lower() == word.text.lower()
        
    
w = Word('test')
print(len(w))   # 本来は len(w.text)

w2 = Word('####')
print(w + w2)

print(w == w2)


"""
良く使われる特殊メソッドは
def __str__(self):
    return ~~
"""