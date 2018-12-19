package com.javahelps.servicemultiply;


public class Client {
	public static void main(String[] args) throws Exception{
		//Create the stub object
		ServiceMulStub stub = new ServiceMulStub();
		
		//Create the request
		ServiceMulStub.GetProduct request = new ServiceMulStub.GetProduct();
		
		for (float i = 10; i >0; i--) {
			//Set the parameters
			float a = i;
			float b = i - 1;
			request.setA(a);
			request.setB(b);
			
			//Invoke the service
			ServiceMulStub.GetProductResponse response = stub.getProduct(request);
			float res = response.get_return();
			System.out.println("The diffrence of " + a +" and " + b + " is :" + res);	
		}
	}
}
