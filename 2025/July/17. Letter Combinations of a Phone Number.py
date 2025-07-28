import unittest
class Solution:
    def backtrack(self, path, level, digits, mapping, res):
        if level == len(digits):
            res.append(''.join(path))
            return 

        curr_level_map = mapping[digits[level]]
        for i in curr_level_map:
            path.append(i)
            self.backtrack(path, level + 1, digits, mapping, res)
            path.pop()

    def letterCombinations(self, digits):
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs', 
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        if not digits:
            return []
        self.backtrack([], 0, digits, mapping, res)
        return res

        
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_backtrack(self):
        digits = '23'
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        expected = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        res = []
        self.solution.backtrack([], 0, digits, mapping, res)
        self.assertEqual(sorted(res), sorted(expected))
        
        
    def test_letterCombinations(self):
        self.assertEqual(
            sorted(self.solution.letterCombinations('23')),
            sorted(['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
        )
        self.assertEqual(
            sorted(self.solution.letterCombinations('')),
            sorted([])
        )
if __name__ == '__main__':
    unittest.main()
        
        
    
        


            
        
        
        
        
