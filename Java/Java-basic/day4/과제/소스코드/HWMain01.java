package kr.co.mlec.day05.homework;

import java.util.Scanner;

/*
 아이스크림 몇개 구입할래? => 4(키보드 입력)

*** 1번째 아이스크림 정보 입력 ***
아이스크림명 : 비비빅(키보드)
아이스크림가격 : 1200(키보드)

*** 2번째 아이스크림 정보 입력 ***
아이스크림명 : 월드콘
아이스크림가격 : 1500

*** 3번째 아이스크림 정보 입력 ***
아이스크림명 : 메로나
아이스크림가격 : 1000

*** 4번째 아이스크림 정보 입력 ***
아이스크림명 : 죠스바
아이스크림가격 : 1200

 < 아이스크림 구매 정보 >
번호   아이스크림명   아이스크림가격
1         비비빅         1200원
2
3
4
 */
public class HWMain01 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		Icecream ic = new Icecream();

		System.out.print("아이스크림 구매 개수 :");
		int num = scan.nextInt();
		ic.name = new String[num];
		ic.price = new int[num];

		for (int i = 0; i < num; i++) {
			System.out.println("*** " + (i + 1) + "번째 아이스크림 정보 입력 ***");
			System.out.print("아이스크림명 : ");
			ic.name[i] = scan.next();
			System.out.print("아이스크림 가격 : ");
			ic.price[i] = scan.nextInt();
		}
		scan.close();

		System.out.println("번호\t이름\t가격");
		for (int i = 0; i < num; i++) {
			System.out.println((i + 1) + "\t" + ic.name[i] + "\t" + ic.price[i] + "원");
		}

	}

}

class Icecream {
	String name[];
	int price[];
}
