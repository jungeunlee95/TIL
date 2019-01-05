package kr.co.mlec.day08.homework;

/**
 * 정사각형과 같이 하나의 정수로 넓이를 구할 수 있는 모양들을 위한 클래스 => Area 상속, 다른점 : height == width
 * 
 * @author BIT
 *
 */
public class SquareArea extends Area {

	public SquareArea(int height) {
		super(height);
	}
	public SquareArea(int height, int width) {
		super(height, width);
	}
	
	@Override
	public int area() {
		
		return height * width;
	}
	@Override
	public double cArea() {
		return 0;
	}

}
