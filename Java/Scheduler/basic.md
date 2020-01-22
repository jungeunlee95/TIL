참고: http://jmlim.github.io/spring/2018/11/27/spring-boot-schedule/

---

### Scheduler

어노테이션 추가

Class: `@EnableScheduling` 

method: `@Scheduled`

> 실행 주기 속성 : cron, fixedDelay, fixedRate
>
> - cron (6자리로 설정가능)
>
>   ```
>   *           *　　　　　　*　　　　　　*　　　　　　*　　　　　　*
>   초(0-59)   분(0-59)　　시간(0-23)　　일(1-31)　　월(1-12)　　요일(0-7) 
>   각 별 위치에 따라 주기를 다르게 설정 할 수 있다.
>   순서대로 초-분-시간-일-월-요일 순이다. 
>   그리고 괄호 안의 숫자 범위 내로 별 대신 입력 할 수도 있다.
>   요일에서 0과 7은 일요일이며, 1부터 월요일이고 6이 토요일이다.
>   ```
>
>   ```java
>   @Component
>   @EnableScheduling
>   public class TestScheduler {
>   
>       @Autowired
>       private final TestService testService;
>   	
>       // 매분(정분? 00분마다) 실행
>       @Scheduled(cron = "0/60 * * * * *")
>       public void Test() {
>           testService.doingSomething();
>       }
>   
>   }
>   ```
>
> - fixedDelay 고정된 시간 - 이 시간은 이전 호출이 완료된 시점부터 계산
>
>   ```java
>   // 1초에 한번 실행
>   @Scheduled(fixedDelay  = 1000)
>   public void Test() {
>       testService.doingSomething();
>   }
>   ```
>
> - fixedRate 연속적인 시작 시각 간격으로
>
>   ```java
>   // 1초에 한번 실행
>   @Scheduled(fixedRate   = 1000)
>   public void Test() {
>       testService.doingSomething();
>   }
>   ```
>
> ```
> [fixedDelay,fixedRate 차이점]
> fixedDelay - 이전 수행이 종료된 시점부터 delay 후에 재 호출
> fixedRate - 이전 수행이 시작된 시점부터 delay 후에 재 호출 
> > 그러므로 fixedRate 로 지정 시 동시에 여러개가 돌 가능성이 존재한다.
> ```



