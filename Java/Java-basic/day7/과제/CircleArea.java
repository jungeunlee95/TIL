package kr.co.mlec.day08.homework;

/**
 * ���� ���̸� ���ϴ� Ŭ���� SquareArea�� ��� ���� => �ٸ��� : area*3.14
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
