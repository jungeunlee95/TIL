package kr.co.mlec.day04.homework;

import java.util.Scanner;

/*
10. 5���� ������ ������ ���� �Է¹޾� ������� �ڵ带 �ۼ�
 
    num1 : 6
    num2 : 12
    num3 : 9
      6, 12���� ū������ �մϴ�
    num3 : 25
    num4 : 9
      6, 12, 25���� ū������ �մϴ�
    num4 : 22
      6, 12, 25���� ū������ �մϴ�
    num4 : 40
    num5 : 77
    
    < PRINT >
    6  12  25  40  77 
 */

public class HWMain10 {

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		int[] num = new int[5];
		int cnt = 0;
		do {
			System.out.print("num" + (cnt + 1) + " : ");
			num[cnt] = scan.nextInt();
			if (cnt == 4)
				break;
			else if (cnt == 0) {
				cnt++;
				continue;
			}
			if (cnt != 0 && num[cnt] > num[cnt - 1]) {
				cnt++;
			}else {
				for (int i = 0; i < cnt; i++) {
					System.out.print(num[i] + " ");
				}
				System.out.println("���� ū ������ �մϴ�.");
			}

		} while (true);
		scan.close();
		System.out.println("< PRINT >");
		for (int i = 0; i < num.length; i++) {
			System.out.print(num[i] + "  ");
		}
	}

}

