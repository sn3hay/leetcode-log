import unittest
class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for i in s:
            if i == '*' and result:
                result.pop()
            elif i == '*':
                continue
            elif i == '#':
                result.extend(result)
            elif i == '%':
                result.reverse()
            else:
                result.append(i)
        # print(result)
        return ''.join(result)

        
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_processStr(self):
        self.assertEqual(self.solution.processStr("a#b%*"), "ba")
        self.assertEqual(self.solution.processStr("*%"), "")
    
if __name__ == '__main__':
    unittest.main()
        
        
    
        


            
        
        
        
        
