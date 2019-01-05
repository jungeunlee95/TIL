package kr.co.mlec.day07.homework;

import java.util.Random;

/*
 * - 면적을 구할 도형의 종류를 표현할 랜덤한 숫자를 생성합니다.(1 ~ 4)  => Random
 *    예> 1-정사각형, 2-직사각형, 3-삼각형, 4-원 
 * - 생성된 숫자에 따라서  
 * 	1, 4번일 경우는 도형의 면적을 구할 랜덤 숫자를 1개 생성합니다. 
 *  2, 3번일 경우는 도형의 면적을 구할 랜덤 숫자를 2개 생성합니다.   
 *  => Random & switch
 *  
 *  면적을 구할 랜덤 숫자까지 생성되었다면 각각의 도형의 면적을 구하는 클래스를 호출합니다
 */
public class AreaMain {

	public static void main(String[] args) {
		Random rand = new Random();
		int num = rand.nextInt(4) + 1;
		int num2 = rand.nextInt(10) + 1;
		int num3;
		
		System.out.println(num + "  " + num2);
		
		switch (num) {
		case 1:
			SquareArea s = new SquareArea(num2);
			System.out.println("정사각형의 면적 : " + s.area());
			break;
		case 2:
			num3 = rand.nextInt(10) + 1;
			System.out.println(num3);
			Area a = new Area(num2, num3);
			System.out.println("직사각형의 면적 : " + a.area());
			break;
		case 3:
			num3 = rand.nextInt(10) + 1;
			TriArea t = new TriArea(num2, num3);
			System.out.println("삼각형의 면적 : " + t.area());
			break;
		case 4:
			CircleArea c = new CircleArea(num2);
			System.out.println("원의 면적 : " + c.area());
			break;

		default:

		}

	}

}
