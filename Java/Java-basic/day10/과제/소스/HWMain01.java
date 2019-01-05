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
		
		list.add(new UserVO("ȫ�浿", "010-1111-2222", "����� ���ʱ�"));
		list.add(new UserVO("��浿", "010-3333-4444", "��⵵ ������ �д籸"));
		list.add(new UserVO("�ֱ浿", "010-5555-6666", "����� ������ �б�����"));
		list.add(new UserVO("�ڱ浿", "010-7777-8888", "����� ���ϱ�"));
		
		FileOutputStream fos = null;
		ObjectOutputStream oos = null;
		
		try {
			fos = new FileOutputStream("iotest/userVO.txt");
			oos = new ObjectOutputStream(fos);
			
			for(int i = 0; i<list.size(); i++) {
				oos.writeObject(list.get(i));
			}
			
			System.out.println("����Ϸ�");
			
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

			System.out.println("���� �б� �Ϸ�");
			
			while(true) {
				try{
					UserVO user = (UserVO)ois.readObject();
					System.out.println(user);
				}catch(Exception e) {     // ���̻� �о�� Object�� ���� Exception�� �߻��ϸ� break;
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
