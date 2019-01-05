package kr.co.mlec.day04.homework;

/*
  7. 다음의 글을 보면서 코드를 작성하시오.
 
   달팽이가 100M깊이의 우물에 빠졌습니다
   달팽이는 한시간에 5M속도로 우물을 기어오릅니다
   올라간 높이가 50M미만일 때는 한시간에 1M씩 미끌어지고,
   올라간 높이가 50M이상일 때는 한시간에 2M씩 미끌어집니다
   달팽이가 몇시간 만에 우물을 탈출하는지 코드를 작성
   
   < 출력결과 >
   [1시간후] 달팽이가 올라간 총 높이 : 4M
   [2시간후] 달팽이가 올라간 총 높이 : 8M
   ...
   [XX시간후] 달팽이가 올라간 총 높이 : 100M, 101M, 102M
 */

public class HWMain07 {

	public static void main(String[] args) {

		int height = 0, time = 0;
		int move= 5;
		System.out.println("< 출력결과 >");
		while(true) {
			time++;
			height +=move;
			if(height<50) {
				height--;
			}else {
				height-=2;
			}
			
			System.out.println("[ "+time+"시간 후 ] 달팽이가 올라간 총 높이 : "+ height +"M");
			if(height>100) break;
		}
		

	}

}






