package kr.co.mlec.day08.homework;

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

	@Override
	public int area() {
		return height*width/2;
	}

	@Override
	public double cArea() {
		return 0;
	}



}
