
/**
 * ServiceSubtractExceptionException.java
 *
 * This file was auto-generated from WSDL
 * by the Apache Axis2 version: 1.7.9  Built on : Nov 16, 2018 (12:05:37 GMT)
 */

package com.javahelps.servicesubtract;

public class ServiceSubtractExceptionException extends java.lang.Exception{

    private static final long serialVersionUID = 1545206888149L;
    
    private com.javahelps.servicesubtract.ServiceSubtractStub.ServiceSubtractException faultMessage;

    
        public ServiceSubtractExceptionException() {
            super("ServiceSubtractExceptionException");
        }

        public ServiceSubtractExceptionException(java.lang.String s) {
           super(s);
        }

        public ServiceSubtractExceptionException(java.lang.String s, java.lang.Throwable ex) {
          super(s, ex);
        }

        public ServiceSubtractExceptionException(java.lang.Throwable cause) {
            super(cause);
        }
    

    public void setFaultMessage(com.javahelps.servicesubtract.ServiceSubtractStub.ServiceSubtractException msg){
       faultMessage = msg;
    }
    
    public com.javahelps.servicesubtract.ServiceSubtractStub.ServiceSubtractException getFaultMessage(){
       return faultMessage;
    }
}
    