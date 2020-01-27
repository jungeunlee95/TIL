## 로컬에 있는 git 브랜치 전체 삭제

이유: 브랜치 하나 이름을 잘못 생성했는데 삭제가 안됨 ,,, 

![1578642600347](assets/1578642600347.png)

<br>

### 해결

>  명령어: git branch -D `git branch --merged | grep -v \* | xargs`

```powershell
# 브랜치 확인
$ git branch -v
  jungeun_2020_01_10   1c1f920 fix bug & add VueX
* master               1e7a85a fix bug & add VueX
  tab-sample           bb8b0c9 fix permission bug
  <C3><A3>backup       474b73f FIX BUG

# 브랜치 삭제 실패
$ git branch -D <C3><A3>backup
bash: syntax error near unexpected token `<'

# 브랜치 전체 삭제
$ git branch -D `git branch --merged | grep -v \* | xargs`
Deleted branch jungeun_2020_01_10 (was 1c1f920).
Deleted branch tab-sample (was bb8b0c9).
Deleted branch ãbackup (was 474b73f).

# 브랜치 삭제 성공
$ git branch -v
* master 1e7a85a fix bug & add VueX
```