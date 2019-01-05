package kr.co.mlec.day06.homework;
/*
 사칙연산을 수행하는 Calculate 클래스 작성

  정수 입력 : 12 (키보드)
  정수 입력 : 5 (키보드)

   12 + 5 = 17
   12 - 5 = 7
   12 * 5 = 60
   12 / 5 = 2.4

   12의 소수체크 : false
   5의 소수체크 : true

 */

import java.util.Scanner;

class Calculate{
	
	Scanner scan = new Scanner(System.in);
	
	int getNum() {
		System.out.print("정수 입력 : ");
		return scan.nextInt();
	}

	void add(int a, int b) {
		System.out.printf("%d + %d = %d\n", a, b, a + b);
	}

	void sub(int a, int b) {
		System.out.printf("%d - %d = %d\n", a, b, a - b);
	}

	void mul(int a, int b) {
		System.out.printf("%d * %d = %d\n", a, b, a * b);
	}

	void div(int a, int b) {
		System.out.println(a + " / " + b + " = " + (double) a / b);
	}
	void pNum(int a) {
		if (a == 2 || a == 3 || a == 5 || a == 7) {
			System.out.println(a + "의 소수체크 : true");
		} else if (a % 2 == 0 || a % 3 == 0 || a % 5 == 0 || a % 7 == 0) {
			System.out.println(a + "의 소수체크 : false");
		} else {
			System.out.println(a + "의 소수체크 : true");
		}
	}
}
public class HWMain01 {

	public static void main(String[] args) {
		Calculate cal = new Calculate();
		int num1 = cal.getNum();
		int num2 = cal.getNum();
		
		cal.add(num1, num2);
		cal.sub(num1, num2);
		cal.div(num1, num2);
		cal.mul(num1, num2);
		cal.pNum(num1);
		cal.pNum(num2);

	}

}

