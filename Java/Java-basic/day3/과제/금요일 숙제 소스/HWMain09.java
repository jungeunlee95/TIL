package kr.co.mlec.day04.homework;

import java.util.Random;

/*
9. 0 - 99������ ������ 5�� �����Ƿ� �����Ͽ� ������ ���� ����ϴ� �ڵ� �ۼ�

  < PRINT >
  8  63  90  7  52
  
  < REVERSE >
  25  70  9  36  80   

*/

public class HWMain09 {

	public static void main(String[] args) {

		int[] num = new int[5];
		Random rand = new Random();

		System.out.println("< PRINT >");
		for (int i = 0; i < num.length; i++) {
			num[i] = rand.nextInt(100);
			System.out.print(num[i] + "  ");
		}
		System.out.println();
		
		int front, end;
		System.out.println("< REVERSE >");
		for (int i = num.length-1; i >= 0; i--) {
			front = num[i] / 10;
			end = num[i] % 10;

			System.out.print(end * 10 + front + "  ");
		}

	}

}
