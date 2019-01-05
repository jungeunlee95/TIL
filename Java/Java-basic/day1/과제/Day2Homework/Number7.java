package Day2Homework;
//QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

import java.util.Scanner;

/*
 *화면에서 알파벳을 입력 받아 대문자는 소문자로 소문자는 대문자로 출력하는 프로그램을 작성하시오
입력(알파벳) : a
변경된 값 : A
참고> 화면에서 받은 문자열에서 한 문자 가져오기
String inputStr = sc.nextLine( );
char c = inputStr.charAt(0);

-소문자와 대문자의 아스키 코드의 차이는 32
65 <= char <= 90 or 'A' <= char <= 'Z'  =>대문자
97 <= char <= 122 or 'a' <= char <= 'z'  =>소문자

  A -> a로 만들려면 32를 더하고
  a -> A로 만들려면 32를 뺀다

 */

public class Number7 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		String inputStr = sc.nextLine( );
		char c = inputStr.charAt(0);
		
		if('A' <= c && c<= 'Z') {
			System.out.println((char)(c-'A'+'a'));
		}
		
		
		
		
	}
}
