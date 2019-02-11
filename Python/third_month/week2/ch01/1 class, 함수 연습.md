## 1번 - My dict

```python
class Word:
    def __init__(self):
        self.wordbook = {}
    def add(self, en, ko):
        #self.wordbook[en] = ko
        self.wordbook.update({en:ko})
    def delete(self, en):
        if en in self.wordbook:
            self.wordbook.pop(en)
            return True
        else:
            return False
    def print(self):
        for en, ko in self.wordbook.items():
            print(f'{en} : {ko}')
if __name__=="__main__":
    mybook = Word()
    mybook.add("apple", "사과")
    mybook.add("banana", "바나나")
    mybook.add("grape", "포도")
    mybook.print()
    print(mybook.delete("apple"))
    mybook.print()
    
# apple : 사과
# banana : 바나나
# grape : 포도
# True
# banana : 바나나
# grape : 포도
```





## 2 번 - 사각형

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def get_area(self):
        return (self.p2.x - self.p1.x) * (self.p1.y -  self.p2.y)
    
    def get_perimeter(self):
        return  ( (self.p2.x - self.p1.x) + (self.p1.y -  self.p2.y) ) * 2
    
    def is_square(self):
        return (self.p2.x - self.p1.x) == (self.p1.y -  self.p2.y)
#         if (self.p2.x - self.p1.x) == (self.p1.y -  self.p2.y):
#             return True
#         else:
#             return False
        
    
if __name__ == "__main__" :
    p1 = Point(1, 3)
    p2 = Point(3, 1)
    r1 = Rectangle(p1, p2)
    print(r1.get_area())
    print(r1.get_perimeter())
    print(r1.is_square())
    
#4
#8
#True
```





## 3번 - 글자 count	

```python
def alphabet_count(word):
    result = {}
    for c in word:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result
def maxcnt(word):
    result = {}
    for c in word:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return max(result.items(), key=lambda x : x[1])[0]
#     max_cnt = max(result.values())
#     for char, count in result.items():
#         if count == max_cnt:
#             return char

            
if __name__ == "__main__":
    print(alphabet_count("hello"))
    print(maxcnt("heeello"))
    
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# e
```





## 4번 - 아스키코드

```python
def cipher(word, n):
    result = ""
    
    n = n % 26
    
    for c in word:
#         w = ord(c) + n 
        
#         if w > 122:
#             w = w - 26
#         result += chr(w)
        result += chr((ord(c) - 97 + n) % 26 + 97)
    return result

if __name__ == "__main__":
    print(cipher("apple", 1))
    print(cipher("apple", 27))
    print(cipher("zoo", 2))
```























