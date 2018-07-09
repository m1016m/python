public class Ex02_02 {

	
	public static void main(String[] args) {
	  
	  int i;
	  
	  int sum = 0;
	  
	  for (i = 1; i <= 10; i++) {
	      
	      sum += i;
	  }
	  
	  
	  System.out.println("從1加到10的總和是: " + sum);	
	  
	  
	  System.out.println("最後 i 值為: " + i);		
	  
	  int j=1,sumA=0;
	  
	  while(j <= 10){
	  	
	  	sumA += j;
	  	
	  	j++;
	  	
	  }  
	  
	  System.out.println("從1加到10的總和是: " + sumA);	
	  
	  
	  System.out.println("最後 j 值為: " + j);	
	}
}