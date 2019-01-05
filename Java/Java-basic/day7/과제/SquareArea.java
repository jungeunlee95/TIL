package kr.co.mlec.day08.homework;

/**
 * ���簢���� ���� �ϳ��� ������ ���̸� ���� �� �ִ� ������ ���� Ŭ���� => Area ���, �ٸ��� : height == width
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
