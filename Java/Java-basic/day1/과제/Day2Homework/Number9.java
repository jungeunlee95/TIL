package Day2Homework;
/*
 *다음의 결과를 보이는 프로그램을 작성
보유하고 있는 책권수 : -34
잘못입력했습니다

보유하고 있는 책권수 : 0
보유하고 있는 책 없음

보유하고 있는 책권수 : 1
1 book

보유하고 있는 책권수 : 12
12 books

 */

import java.util.Scanner;

public class Number9 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
	    System.out.print("보유하고 있는 책 권수 입력 : ");
	    int book = sc.nextInt();
		
	    if(book == 0) {
	    	System.out.println("보유하고 있는 책 없음");
	    } else if (book == 1) {
	    	System.out.println(book + " book");
        } else if (book >0){
        	System.out.println(book + " books");
        } else {
        	System.out.println("잘못 입력 했습니다.");
        }
		
	 
	    
	}

}
