package kr.co.mlec.day07.homework;

/**
 * ���� ���̸� ���ϴ� Ŭ���� SquareArea�� ��� ���� => �ٸ��� : area*3.14
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
