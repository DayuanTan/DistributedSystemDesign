package com.javahelps.loadbaln2;

public class Client {
	public static void main(String[] args) throws Exception{
		//Create the stub object
		LoadBaln2Stub stub = new LoadBaln2Stub();
		
		
		//Create the request
		LoadBaln2Stub.GetServicesResult request = new LoadBaln2Stub.GetServicesResult();
		
		for (float i = 1; i < 10; i++) {
			//Set the parameters
			float a = i;
			float b = i + 1;
			request.setA(a);
			request.setB(b);
			String serviceName="sum";
			request.setServiceName(serviceName);
			
			//Invoke the service
			LoadBaln2Stub.GetServicesResultResponse response = stub.getServicesResult(request);
			float result = response.get_return();
			System.out.println("The " + serviceName + " of " + a +" and " + b + " is :" + result);	
		}
		
	
		
		
	}
}
