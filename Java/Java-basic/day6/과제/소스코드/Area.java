package kr.co.mlec.day07.homework;

/**
 * 밑변과 높이가 다른 직사각형의 넓이를 구하기 위한 클래스
 * 
 * @author BIT
 *
 */
public class Area {

	private int height;
	private int width;

	public Area(int height) {
		this.height = height;
		this.width = height;
	}

	public Area(int height, int width) {
		this.height = height;
		this.width = width;
	}

	public int area() {
		return height * width;
	}

}
