package kr.co.mlec.day07.homework;

/**
 * 원의 넓이를 구하는 클래스 SquareArea를 상속 받음 => 다른점 : area*3.14
 * 
 * @author BIT
 *
 */
public class CircleArea extends SquareArea {

	public CircleArea(int height) {
		super(height);
	}

	public int area() {
		int area = super.area() * 3;
		return area;
	}

}
