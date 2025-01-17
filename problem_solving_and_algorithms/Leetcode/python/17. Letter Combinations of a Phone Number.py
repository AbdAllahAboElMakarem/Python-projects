class Solution(object):
    def letterCombinations(self, digits):
       
    
        if(len(digits) == 0):
            return []

        digit2char = {'1': '',     '2': 'abc', '3': 'def',
                      '4': 'ghi',  '5': 'jkl', '6': 'mno',
                      '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ''}

        resus = ['']

        for d in digits:
            tem = []
            for c in digit2char[d]:
                tem = tem + [r + c for r in resus]

            resus = tem

        return resus
