### package-lock.json ?

```
package-lock.json 파일은 npm을 사용해서 node_modules 트리나 package.json 파일을 수정하게 되면 자동으로 생성되는 파일
이 파일은 파일이 생성되는 시점의 의존성 트리에 대한 정확한 정보를 가지고 있음
```



---

### package-lock.json push

- package.json 파일에는 버전이 아니라 버전 범위를 갖고있어서 동일한 파일로 npm install을 해도 버전 오류가 발생할수도 있음

- 그래서 pacakge-lock.json은 의존성 트리에 대한 정보도 가지고 있어서 package.json의 변화 당시 의존성에 대한 모든 버전 정보를 갖고있다고해서 `node_modules/` 없이 배포하는 경우 필요함!

- -lock.json이 있으면 lock 내용을 우선순위로 생성

<br>

#### [ 요약 ]

1. `package-lock.json` 파일은 의존성 트리에 대한 정보를 가지고 있으며, 작성된 시점의 의존성 트리가 다시 생성될 수 있도록 보장해준다.
2. `package-lock.json` 파일은 저장소에 꼭 같이 커밋해야 한다. 
3. `package-lock.json` 파일은 `node_modules` 없이 배포하는 경우 반드시 필요하다.

------



<br>

---

혹시라도 이미 `node_modules/` 의 의존성 패키지들이 꼬인경우

1. npm/node 버전 확인 : `node -v`, `npm -v`
2. node_modules/삭제 `rm -rf node_modules/`
3. npm cache 삭제: `npm cache clean --force`
4. 의존성 패키지 다운: `npm install`

<br>

---

### 충돌

TODO 더 공부 필요: 둘 다 npm install로 무언가를 받아서.. package-lock.json을 둘 다 수정하게되면,, 충돌나는 부분은 , , ,, , , , , , , , , ,, , , , ,, , ,, , ,,



<br>

<br>

### 참고

https://medium.com/@han7096/package-lock-json-%EC%97%90-%EA%B4%80%ED%95%98%EC%97%AC-5652f90b734c

https://hyunjun19.github.io/2018/03/23/package-lock-why-need/