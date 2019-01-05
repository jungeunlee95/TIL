package kr.co.mlec.day08.homework;

/**
 * 원의 넓이를 구하는 클래스 SquareArea를 상속 받음 => 다른점 : area*3.14
 * 
 * @author BIT
 *
 */
public class CircleArea extends Area {

	public CircleArea(int height) {
		super(height);
	}

	@Override
	public int area() {
		return 0;
	}

	@Override
	public double cArea() {
		return height*width*3.14;
	}



}
