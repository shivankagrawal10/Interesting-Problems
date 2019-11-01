package prime;

public class checker {
	private int num;
	public checker(int n){
		num=n;
	}
	public boolean isprime(){
		
		for (int i=2;i<num;i++){
			if (num%i==0){
				return false;
			}
		}
		return true;
	}
	public int getnum(){
		return num;
	}
}
