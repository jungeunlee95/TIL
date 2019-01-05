package kr.co.mlec.day07.homework;

/**
 * 삼각형의 넓이를 계산하기 위한 Area를 상속받는 클래스 => Area와 다른 점 : 넓이를 반으로 나눔
 * 
 * @author BIT
 *
 */
public class TriArea extends Area {

	public TriArea(int height, int width) {
		super(height, width);
	}

	public int area() {
		int area = super.area() / 2;
		return area;
	}

}
