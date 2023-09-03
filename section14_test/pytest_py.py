import pytest

import calculation



class TestCal(object):
    
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()
        
    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal
        
    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        #self.cal = calculation.Cal()
    
    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        #del self.cal
        
    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4
        
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
    
    
    
#     #@unittest.skip('skip!')
#     @unittest.skipIf(release_name=='lesson', 'skip!!')
#     def test_add_num_and_double(self):
#         self.assertEqual(self.cal.add_num_and_double(1, 1), 4)
   

