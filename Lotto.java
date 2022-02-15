package zenna;

import java.util.Arrays;
import java.util.Scanner;

public class Lotto {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("금액을 입력하세요 : ");
		int money = input.nextInt();
		if (money < 1000) {
			System.out.println("돈 없으면 집에 가세요");
			System.out.println(money + "원을 뱉었습니다");
		} else if (money > 5000) {
			System.out.println("로또는 5회만 되는거 아시잖아요..");
			System.out.println(money - 5000 + "원을 반환합니다");
			money = 5000;
		} else {
			int tries = money / 1000;
			System.out.println(money - tries * 1000 + "원을 반환합니다");
			System.out.println(tries + "회를 출력합니다");
			System.out.println("===================");

			int[] lotto = new int[6];
			for (int i = 0; i < 50; i++) {

				for (int ii = 0; ii < 6; ii++) {
					lotto[ii] = (int) (Math.random() * 45 + 1);
					for (int j = 0; j < ii; j++) {
						if (lotto[j] == lotto[ii]) {
							ii--;
						}
					}
				}
				Arrays.sort(lotto);
				System.out.println(i + 1 + "회 : " + Arrays.toString(lotto));
			}
		}
	}
}
