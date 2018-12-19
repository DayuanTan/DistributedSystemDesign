package com.javahelps.loadBaln2;

import javax.swing.JOptionPane;
import javax.xml.namespace.QName;
import org.apache.axis2.addressing.EndpointReference;
import org.apache.axis2.client.Options;
import org.apache.axis2.rpc.client.RPCServiceClient;
import java.sql.*;
import java.util.Properties;
 

public class LoadBaln2 {
	public float getServicesResult(String serviceName, float a, float b) {
		String methodPara = "", wsdl = "", namespace = "";
		Connection c;
		float r=0 ;
		
		if (serviceName.equals("sum")){
			methodPara = "getSum";
		}else if (serviceName.equals("subtract")){
			methodPara = "getDiff";
		}else if (serviceName.equals("multiply")){
			methodPara = "getProduct";
		}
		
		//find service WSDL form table
		//the JDBC connector class
		final String dbClassName = "com.mysql.cj.jdbc.Driver";
		//connection string
		final String CONNECTION = "jdbc:mysql://127.0.0.1/distributedSystemDesign";
		try {
			//load JDBC class
			Class.forName(dbClassName).newInstance();
			Properties p = new Properties();
			p.put("user", "dayuan");
			p.put("password", "1111");
			//connect
			c = DriverManager.getConnection(CONNECTION, p);
			//sql query 
			String sql = "Select wsdl,namespace,method,ipv4,port from distributedSystemDesign.servicesStatus where method = ? and active=1 and busy=0 limit 1";
		
			PreparedStatement pst = c.prepareStatement(sql);
			pst.setString(1, methodPara);
			//exe the query and get result
			ResultSet rs = pst.executeQuery();
			//iterate through the sql result
			while(rs.next()) {
				wsdl = rs.getString("wsdl");
				namespace = rs.getString("namespace");
			}

			System.out.println("The return wsdl is:"  + wsdl);	

			
			//call webService using RPC
			RPCServiceClient serviceClient = new RPCServiceClient();
			Options options = serviceClient.getOptions();
			//Call webService URL
			EndpointReference targetEPR = new EndpointReference(wsdl);
			options.setTo(targetEPR);
		
			//set parameters
			Object[] opAddEntryArgs	= new Object[] {a,b};
			//set return's type's class object
			Class[] classes = new Class[] {float.class,float.class};
			//set method we want to call, parameters are (targetNamespace, targetMethod)
			QName opAddEntry = new QName(namespace,methodPara);
			//call
			r = (float)(serviceClient.invokeBlocking(opAddEntry,opAddEntryArgs,classes)[0]);
			System.out.println(r);
			
			c.close();
		}
		catch (Exception e) {
			JOptionPane.showMessageDialog(null, e);
		} 
		
		
		
		return r;
	}
}