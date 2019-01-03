# 2019-01-03 1-git

**git 강의**

https://www.udacity.com/course/how-to-use-git-and-github--ud775

**gitignore 목록**

https://github.com/github/gitignore

**sublime text 다운**

https://www.sublimetext.com/



- ### .gitignore

**.gitignore** 파일 안에 설정하면 됨

![1546476350294](..\typora-user-images\1546476350294.png)

​					**--> vscode 폴더 아래 모든 파일은 git이 무시함**

- **git bash chrome 시작 default**

제어판 -> 시스템 및 보안 -> 관리도구 - > 서비스-> crytographic service 클릭 -> 로그온 ->로컬 시스템 계정



- ### git clone

**git bash**

```
$ git clone 복사주소
```

**수정 후 push**

```
< Home Computer >

$ cd git_practice/
$ git status
$ git add .
$ git status
$ git commit -m "Edit browser.py"
$ git log 							// 커밋 로그 확인
$ git push -u origin master
```

**수정 파일 pull**

```
< SSAFY Computer >

$ git pull origin master
$ git log

```

**pull안하고 같은 파일 수정했을때 Error** 

![1546489860144](..\typora-user-images\1546489860144.png)

![1546489869091](..\typora-user-images\1546489869091.png)

```
선택 후 다시 
$ git add README.md
$ git commit -m "메세지"
$ git push origin master
```



- ### git branch

```
-보기
$ git branch		// 모든 branch를 보여줌 
-생성
$ git branch [브랜치 이름]    // <이름>의 새 브랜치를 만듦
-이동(브랜치 간 이동, 커밋 간 이동)
$ git checkout [브랜치 이름] 	// 해당 브랜치로 이동
```

![1546494292378](..\typora-user-images\1546494292378.png)

​						... 코드 수정...

![1546493083531](..\typora-user-images\1546493083531.png)





### 다른 branch 합치기

- **git merge**

```
$ git merge [브랜치 이름]
```





























