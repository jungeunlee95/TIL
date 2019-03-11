# python file - csv

영진위

https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do





numpy, 다중행렬, 하나의행렬을 이루는 벡터

벡터 하나의 값 - 텐서

머신러닝 프레임워크 텐서들이 움직여 -> tensorflow!

**csv_pratice.py**

```python
lunch = {
    '김밥' : '02-123-4565',
    '양자강' : '02-345-3525',
    '순남시래기' : '02-567-8653'
}

f = open('lunch.csv','w')

# for name, phone in lunch.items():
#     f.write(name+ ", "+ phone+"\n")
for name in lunch:
    f.write("{}, {}\n".format(name,lunch[name]))
    #f.write(", ".join((name,lunch[name])) + '\n')
f.close()
```

**lunch.csv**

```
김밥, 02-123-4565
양자강, 02-345-3525
순남시래기, 02-567-8653
```



### file.close() 를 알아서 날려주는 것

```python
lunch = {
    '김밥' : '02-123-4565',
    '양자강' : '02-345-3525',
    '순남시래기' : '02-567-8653'
}
with open('lunch.csv','w') as f:
    for name in lunch:
        f.write("{}, {}\n".format(name,lunch[name]))
```



### import csv

**csv_pratice.py** --  리스트

```python
import csv

lunch = {
    '김밥' : '02-123-4565',
    '양자강' : '02-345-3525',
    '순남시래기' : '02-567-8653'
}
menu = ['김밥', '탕슉', '시래기']

with open('lunch.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(menu)
    
lunch.cvs 
김밥,탕슉,시래기
```



**csv_pratice.py** --  딕셔너리

```python
import csv

lunch2 = {
    '상호명' : '양자강',
    '전화번호' : "020-333-444"
}
with open('lunch.csv','w') as f:
    # writer = csv.Dictwriter(f, 필드네임(튜플형태))
    field = ('상호명', '전화번호')
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()
    writer.writerow(lunch2)
    
lunch.cvs 
상호명,전화번호
양자강,020-333-444

```

**csv_pratice.py** --  딕셔너리 리스트

```python
import csv

lunch2 = [
    {
    '상호명' : '양자강',
    '전화번호' : "020-333-444"
    },
    {
    '상호명' : '김밥',
    '전화번호' : "111-333-444"
    },
    {
    '상호명' : '순시',
    '전화번호' : "222-333-444"
    }
]

with open('lunch.csv','w') as f:
    field = ('상호명', '전화번호')
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()
    
    for l in lunch2:
        writer.writerow(l)
    
    
lunch.cvs 
상호명,전화번호
양자강,020-333-444
김밥,111-333-444
순시,222-333-444

```



**csv파일 가져와서 읽기**

```python
with open('lunch.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            
## 출력
['상호명', '전화번호']
['양자강', '020-333-444']
['김밥', '111-333-444']
['순시', '222-333-444']

with open('lunch.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0])
            
## 출력
상호명
양자강
김밥
순시
```



































