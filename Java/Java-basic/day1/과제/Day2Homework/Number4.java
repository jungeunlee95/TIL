package Day2Homework;

import java.util.Scanner;

/*
 *4. 화면에서 하나의 정수를 입력 받고 정수를 나눌 수를 입력 받은 다음 몫과 나머지를 화면에 출력하시오
정수를 입력하세요  :  10
나눌 수를 입력하세요  :  7
몫 : 1
나머지 : 


 */
public class Number4 {
        public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.print("정수를 입력하세요 : ");
		int num = sc.nextInt();
		
		System.out.print("나눌 수를 입력하세요 : ");
		int num2 = sc.nextInt();
		
		//System.out.println("몫 : " + (num/num2) + ", 나머지 : " + (num%num2));
		 if(num2 == 0) {
		    	System.out.println("0으로 나눌 수 없습니다.");
		    }  else if(num == 0) { 
		    	System.out.println("0은 나눌 수 없습니다.");
		    }  else {
		    	System.out.println("몫 : " + (num/num2) + ", 나머지 : " + (num%num2));
	        } 
		 
       }
}
