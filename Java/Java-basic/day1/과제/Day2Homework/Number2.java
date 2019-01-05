package Day2Homework;
//QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
import java.util.Scanner;

/*
 *2. 3661초가 몇 시간 몇 분 몇 초인지 환산해서 출력하시오 
결과출력 : 1시간 1분 1초
초를 입력하시오. 0000초
=00시간 00분 00초

{{{{{{{{해야할 일}}}}}}}}
1. 사용자 입력 받기 : Scanner함수 사용 "초를 입력하시오" 
2.초 = "입력된 값"을 60으로 나눈 나머지
    분 = ("입력된 값"을 60으로 나눈 나머지)를 60으로 나눈 나머지 
  시간 = ("입력된 값"을 60으로 나눈 몫)을 60으로 나눈 몫
3."입력된 초의 시간은~ 입니다"    
 */
public class Number2 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("초를 입력하세요.");
		
		int num =  sc.nextInt();
		int second = num % 60;
		int minute = second % 60;
		int hour = (num / 60 ) / 60;
		
		System.out.println("총 초의 시간은 : " + hour + "시간" + minute + "분" + second + "초" + "입니다.");
		
/*추과 과제
ex) 2889초  -0시간 48분 32초  -> 이럴때는 시간 생략하고 분 초만 뜨게
ex) 12초면 -> 초만뜨게
 
 만약 값이 0 이면 표시하지마. 
 
*/
//		if(second == 0) {
//			System.out.println("총 초의 시간은 : " + hour + "시간" + minute + "분" + "입니다.");
//	    }  else if(minute == 0) { 
//	    	System.out.println("총 초의 시간은 : " + hour + "시간" + second + "초" + "입니다.");
//	    }  else if(hour == 0 ){
//	    	System.out.println("총 초의 시간은 : " + minute + "분" + second + "초" + "입니다.");
//        }  else {
//        	System.out.println("총 초의 시간은 : " + hour + "시간" + minute + "분" + second + "초" + "입니다.");
//        }
		
	}

}
		
