package Day2Homework;

import java.util.Scanner;

/*
 *정수 3개를 입력받아 큰수에서 작은수 순으로 출력하는 코드를 작성
첫번째 정수 : 12
두번째 정수 : 26
세번째 정수 : 16
26  16  12

 */
public class Number910 {
public static void main(String[] args) {
		
		int a, b, c ;
		
		Scanner sc = new Scanner(System.in);
	    System.out.print("첫번째 정수를 입력하세요 : ");
	    a = sc.nextInt();
	    System.out.print("두번째 정수를 입력하세요 : ");
	    b = sc.nextInt();
	    System.out.print("세번째 정수를 입력하세요 : ");
	    c = sc.nextInt();
	    /*
	     * a>b>c
	     * a>c>b
	     * b>a>c
	     * b>c>a
	     * c>a>b
	     * c>b>a
	     */
	    
	    if(a>b & b>c) {
	    	System.out.printf("큰수 순으로 정렬 결과 : %d %d %d\n", a,b,c);
	    } else if (a>c & c>b) {
	    	System.out.printf("큰수 순으로 정렬 결과 : %d %d %d\n", a,c,b);
	    } else if (b>a & a>c) {
	    	System.out.printf("큰수 순으로 정렬 결과 : %d %d %d\n", b,a,c);
	    } else if (b>c & b>a) {
	    	System.out.printf("큰수 순으로 정렬 결과 : %d %d %d\n", b,c,a);
	    } else if (c>a & a>b) {
	    	System.out.printf("큰수 순으로 정렬 결과 : %d %d %d\n", c,a,b);
	    } else {
	    	System.out.printf("큰수 순으로 정렬 결과 : %d %d %d\n", c,b,a);
	    }
	    
	    }

}
