package kr.co.mlec.day11.homework;


import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.List;

import kr.co.mlec.util.FileClose;

public class HWMain01 {

	public static void write() {
		List<UserVO> list = new ArrayList<>();
		
		list.add(new UserVO("홍길동", "010-1111-2222", "서울시 서초구"));
		list.add(new UserVO("고길동", "010-3333-4444", "경기도 성남시 분당구"));
		list.add(new UserVO("최길동", "010-5555-6666", "서울시 강남구 압구정동"));
		list.add(new UserVO("박길동", "010-7777-8888", "서울시 성북구"));
		
		FileOutputStream fos = null;
		ObjectOutputStream oos = null;
		
		try {
			fos = new FileOutputStream("iotest/userVO.txt");
			oos = new ObjectOutputStream(fos);
			
			for(int i = 0; i<list.size(); i++) {
				oos.writeObject(list.get(i));
			}
			
			System.out.println("저장완료");
			
		}catch (Exception e) {
			e.printStackTrace();
		}finally {
			FileClose.close(oos);
			FileClose.close(fos);
		}
		
	}
	
	public static void read() {
		
		FileInputStream fis = null;
		ObjectInputStream ois = null;
		
		try {
			fis = new FileInputStream("iotest/userVO.txt");
			ois = new ObjectInputStream(fis);

			System.out.println("파일 읽기 완료");
			
			while(true) {
				try{
					UserVO user = (UserVO)ois.readObject();
					System.out.println(user);
				}catch(Exception e) {     // 더이상 읽어올 Object가 없어 Exception이 발생하면 break;
					break;
				}
			}
		
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			FileClose.close(ois);
			FileClose.close(fis);
		}
	}
	
	public static void main(String[] args) {
		
//		write();
		read();

	}

}
