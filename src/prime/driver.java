package prime;

public class driver {
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for (int i=1;i<100;i++){
			int[]primes=new int[10*i];
			int counter=0,n=2;
			long startTime = System.nanoTime();
			while (counter<primes.length){
			checker first= new checker(n);
			if (first.isprime()==true){
				primes[counter]=first.getnum();
				counter++;
			}
			//System.out.println(first.isprime());
			n++;
			if (counter==10001){
				System.out.println("\n");
			}
			}
			long endTime = System.nanoTime();
	
			//System.out.println(primes[primes.length-1]+" time:"+(endTime - startTime)/Math.pow(10, 9) + " s ");
			System.out.println((endTime - startTime)/Math.pow(10, 9));
		}
	}
}
