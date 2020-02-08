

<http://webatoz.com:9090/job/jelee03-test/>



```
chmod +x ./gradlew 
./gradlew clean 
./gradlew build
docker login -u webatoz -p *****
docker build --build-arg JAR_FILE=build/libs/*.jar -t jelee03/springboot-docker-test .
docker tag jelee03/springboot-docker-test webatoz/spring-docker:latest
docker push webatoz/spring-docker:latest
```



<https://hub.docker.com/repository/docker/webatoz/spring-docker>

