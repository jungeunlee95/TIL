package kr.co.mlec.day04.homework;

import java.util.Scanner;

/*
10. 5개의 정수를 다음과 같이 입력받아 출력한은 코드를 작성
 
    num1 : 6
    num2 : 12
    num3 : 9
      6, 12보다 큰수여야 합니다
    num3 : 25
    num4 : 9
      6, 12, 25보다 큰수여야 합니다
    num4 : 22
      6, 12, 25보다 큰수여야 합니다
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
				System.out.println("보다 큰 수여야 합니다.");
			}

		} while (true);
		scan.close();
		System.out.println("< PRINT >");
		for (int i = 0; i < num.length; i++) {
			System.out.print(num[i] + "  ");
		}
	}

}

