package Day2Homework;

import java.util.Scanner;

/*
 *정수 4개를 입력받아 가장 큰수를 출력하는 코드를 작성
정수 4개 입력 : 12 56 8 34
가장 큰수 : 56

 */
public class Number911 {

	public static void main(String[] args) {
		
		int a, b, c, d;
		
		Scanner sc = new Scanner(System.in);
	    System.out.print("서로 다른 정수 4개를 입력하세요 : ");
	    a = sc.nextInt();
	    b = sc.nextInt();
	    c = sc.nextInt();
	    d = sc.nextInt();
	    
	    if(a>b & a>c & a>d) {
	    	System.out.println("가장 큰 수 : " + a);
	    } else if (b>a & b>c & b>d) {
	    	System.out.println("가장 큰 수 : " + b);
	    } else if (c>a & c>b & c>d) {
	    	System.out.println("가장 큰 수 : " + c);
	    } else {
	    	System.out.println("가장 큰 수 : " + d);
	    }
	    
	    }
	    
		    		
	

	
  }

