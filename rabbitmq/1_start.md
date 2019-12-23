[TOC]

---

ref: [rabbitmq docker hub](https://hub.docker.com/_/rabbitmq?tab=description)

---

## 1. 이미지 다운

```powershell
D:>docker image pull rabbitmq:3.8.0-management
```





------

## 2. 이미지 확인

```powershell
D:>docker images
```





------

## 3. RabbitMQ 도커 컨테이너 띄우기

```powershell
D:>docker run -d --hostname test-rabbit --name some-rabbit -p 15672:15672 rabbitmq:3.8.0-management
126bfab692ba2f57d8325098b8aa7df22575b6a51e5e1bd646e53db375484ded
```







------

## 4. RabbitMQ 도커 로그 확인

```powershell
D:>docker logs test-rabbit
 
...

 * rabbitmq_management
 * rabbitmq_web_dispatch
 * rabbitmq_management_agent
```



------

## 5. Docker RabbitMQ 프로세스 확인

```powershell
D:>docker ps --all
CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS                      PORTS                                                                                        NAMES
8ba1ec682be6        rabbitmq:3.8.0-management   "docker-entrypoint.s…"   3 minutes ago       Up 3 minutes                4369/tcp, 5671/tcp, 0.0.0.0:5672->5672/tcp, 15671/tcp, 25672/tcp, 0.0.0.0:15672->15672/tcp   test-rabbit
```



------

## 6. RabbitMQ 관리자 페이지 접속

```powershell
URL : http://localhost:15672
ID / Password : guest/guest
```

<br>

------

## etc..

#### RabbitMQ가 설치된 컨테이너에 접속하기

```powershell
docker exec -it {{container id}} /bin/bash
```

<br>

#### RabbitMQ 프로세스 Stop

```powershell
docker stop {{container id}}
```

<br>

#### RabbitMQ 프로세스 시작

```powershell
docker start {{container id}}
```

<br>

#### docker stop` <container id>` 명령어로 중지 후 삭제

```powershell
docker rm {{container id}}
```

<br>

####  docker images 명령어로 image id 확인 후 삭제 : docker rmi `<image id>`

```powershell
docker rmi {{container id}}
```

<br>

#### RabbitMQ가 설치된 컨테이너에 접속하기

```powershell
docker exec -it {{container id}} /bin/bash
```

<br>

#### RabbitMQ가 설치된 컨테이너에 접속하기

```powershell
docker exec -it {{container id}} /bin/bash
```

