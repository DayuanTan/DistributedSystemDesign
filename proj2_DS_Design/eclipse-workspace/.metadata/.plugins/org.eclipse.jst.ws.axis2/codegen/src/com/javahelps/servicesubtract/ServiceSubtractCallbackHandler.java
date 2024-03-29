
/**
 * ServiceSubtractCallbackHandler.java
 *
 * This file was auto-generated from WSDL
 * by the Apache Axis2 version: 1.7.9  Built on : Nov 16, 2018 (12:05:37 GMT)
 */

    package com.javahelps.servicesubtract;

    /**
     *  ServiceSubtractCallbackHandler Callback class, Users can extend this class and implement
     *  their own receiveResult and receiveError methods.
     */
    public abstract class ServiceSubtractCallbackHandler{



    protected Object clientData;

    /**
    * User can pass in any object that needs to be accessed once the NonBlocking
    * Web service call is finished and appropriate method of this CallBack is called.
    * @param clientData Object mechanism by which the user can pass in user data
    * that will be avilable at the time this callback is called.
    */
    public ServiceSubtractCallbackHandler(Object clientData){
        this.clientData = clientData;
    }

    /**
    * Please use this constructor if you don't want to set any clientData
    */
    public ServiceSubtractCallbackHandler(){
        this.clientData = null;
    }

    /**
     * Get the client data
     */

     public Object getClientData() {
        return clientData;
     }

        
           /**
            * auto generated Axis2 call back method for active method
            * override this method for handling normal response from active operation
            */
           public void receiveResultactive(
                    com.javahelps.servicesubtract.ServiceSubtractStub.ActiveResponse result
                        ) {
           }

          /**
           * auto generated Axis2 Error handler
           * override this method for handling error response from active operation
           */
            public void receiveErroractive(java.lang.Exception e) {
            }
                
           /**
            * auto generated Axis2 call back method for getDiff method
            * override this method for handling normal response from getDiff operation
            */
           public void receiveResultgetDiff(
                    com.javahelps.servicesubtract.ServiceSubtractStub.GetDiffResponse result
                        ) {
           }

          /**
           * auto generated Axis2 Error handler
           * override this method for handling error response from getDiff operation
           */
            public void receiveErrorgetDiff(java.lang.Exception e) {
            }
                


    }
    