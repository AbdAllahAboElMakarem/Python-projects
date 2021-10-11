class Solution(object):
    def intToRoman(self, num):
        
             
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD"}
        keyset, result = sorted(numeral_map.keys()), ""
        
        while num > 0:
            for key in reversed(keyset):
                while num / key > 0:
                    num -= key
                    result += numeral_map[key]
                    
        return result
