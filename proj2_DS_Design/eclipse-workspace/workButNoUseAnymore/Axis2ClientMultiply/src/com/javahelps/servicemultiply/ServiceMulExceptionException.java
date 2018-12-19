
/**
 * ServiceMulExceptionException.java
 *
 * This file was auto-generated from WSDL
 * by the Apache Axis2 version: 1.7.9  Built on : Nov 16, 2018 (12:05:37 GMT)
 */

package com.javahelps.servicemultiply;

public class ServiceMulExceptionException extends java.lang.Exception{

    private static final long serialVersionUID = 1545205900587L;
    
    private com.javahelps.servicemultiply.ServiceMulStub.ServiceMulException faultMessage;

    
        public ServiceMulExceptionException() {
            super("ServiceMulExceptionException");
        }

        public ServiceMulExceptionException(java.lang.String s) {
           super(s);
        }

        public ServiceMulExceptionException(java.lang.String s, java.lang.Throwable ex) {
          super(s, ex);
        }

        public ServiceMulExceptionException(java.lang.Throwable cause) {
            super(cause);
        }
    

    public void setFaultMessage(com.javahelps.servicemultiply.ServiceMulStub.ServiceMulException msg){
       faultMessage = msg;
    }
    
    public com.javahelps.servicemultiply.ServiceMulStub.ServiceMulException getFaultMessage(){
       return faultMessage;
    }
}
    