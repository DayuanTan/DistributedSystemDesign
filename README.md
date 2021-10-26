# CMSC621_OS

This is a repostory for UMBC CMSC621 Operating System class projects.

## Project 1
Socket. Create a new thread for each client connection.

Requirement is [here](Project1.pdf)

My report is [here](DayuanTan_proj1.pdf)

## Project 2

Requirement is [here](project2_ds.pdf)

My report is [here](DayuanTan_proj2.pdf)

Design a distributed system. 

I used ubuntu 16.04 in virtual box. Download both form offical website and create virtual machince.

|Steps |Reference links|Back-up web-page PDF|
|:-|:-:|-|
|**Step 1: Install tomcat.** <br> I choice Tomcat 8.5.35, since I'm afarid new version may have conflict because this manual chose v8.|https://www.digitalocean.com/community/tutorials/how-to-install-apache-tomcat-8-on-ubuntu-16-04.|<a href="proj2_DS_Design/r1.pdf">Install tomcat.</a>|
|**Step 2: Install Axis2.** <br> Do everythin before "Installing Axis2 in a Servlet Container" part, we don't need servlet here.|https://axis.apache.org/axis2/java/core/docs/installationguide.html# | <a href="proj2_DS_Design/r2.pdf">Axis2</a>|
|**Step 3: Install Eclipse.** <br> Choose old version. Lastest version is not a good chocie. I chose Oxygen.|https://www.javahelps.com/2015/03/install-latest-eclipse-in-ubuntu.html | <a href="proj2_DS_Design/r3.pdf">Eclipse</a>|
|**Step 4: Integrate Axis2 with Eclipse.** <br> Just do "Integrate Axis2 with Eclipse" and below part.|https://www.javahelps.com/2016/04/setup-apache-axis2-on-ubuntu.html | <a href="proj2_DS_Design/r4.pdf">Integrate Axis2 with Eclipse.</a>|
|**Step 5: Setup a Hello service and client.** <br> Totally we need to mannually import 3 libs, which are under <a href="proj2_DS_Design/eclipse-workspace/libNeededToEclipseDynamicWS/">`libNeededToEclipseDynamicWS`</a>. |https://www.javahelps.com/2016/04/apache-axis2-hello-world-using-eclipse.html| <a href="proj2_DS_Design/r5.pdf">Hello World.</a>|
|**Maybe meet some issue** like "Can not find the tag library descriptor for 'http://java.sun.com/jsp/jstl/core' "|https://stackoverflow.com/questions/13285826/can-not-find-the-tag-library-descriptor-for-http-java-sun-com-jsp-jstl-core |<a href="proj2_DS_Design/r6.pdf">Maybe-Issue Solutions.</a>|
|**Step 6: Load balancer:**|||
|**Create Multi Tomcat instances.** <br> Note: should also cp whole webapps into /var/lib/tomcat7-a_or_b_or_c/webapps|https://madurad.wordpress.com/2014/07/17/installing-and-configuring-multiple-tomcat-server-instances/|<a href="proj2_DS_Design/r7.pdf">Create Multi Tomcat instances.</a>|
|**Doesn't Work!!! Skip this one!** ~~**Load balancing (mod_jk)**~~ <br> ~~Note: In step 4 should be ```sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/loadbalance.conf```~~ <br> ~~and in step 5~~ ~~`sudo a2ensiteloadbalance.com` should be `sudo a2ensite loadbalance.conf`, enabled site should be listed in /etc/apache2/sites-enabled~~|~~https://madurad.wordpress.com/2014/08/27/tomcat-server-loab-balancing-using-multiple-tomcat-server-instances-in-ubuntu/~~|<a href="proj2_DS_Design/r8.pdf">~~Load balancing.~~ </a> |
|**Call wsdl in web service.** <br> I used only section 3.|https://clq9761.iteye.com/blog/976029|<a href="proj2_DS_Design/r9.pdf">Call wsdl in service.</a>|
|**Step 7: Setup Database MySQL.** <br>Setup Mysql on Ubuntu and in Java. <br> Setup database and table. <br> Install MySQL workbench: `sudo apt-get install mysql-workbench`|https://help.ubuntu.com/community/JDBCAndMySQL|<a href="proj2_DS_Design/r10.pdf">MySQL;</a> <br> <a href="proj2_DS_Design/mysql.log">sql log.</a>|
|Download MySQL Connector/J and put it into `WebContent/WEB_INF/lib`|https://stackoverflow.com/questions/17484764/java-lang-classnotfoundexception-com-mysql-jdbc-driver-in-eclipse <br> https://mvnrepository.com/artifact/mysql/mysql-connector-java/8.0.13|<a href="proj2_DS_Design/eclipse-workspace/libNeededToEclipseDynamicWS/">The jar file.</a>|
|**Connect MySQL form java.** <br> **For `Eclipse` part, don't do that**, put the jar into `lib`. <bar> And need use this class **`com.mysql.cj.jdbc.Driver`** to replace `com.mysql.jdbc.Drive`.|https://help.ubuntu.com/community/JDBCAndMySQL|<a href="proj2_DS_Design/r11.pdf">Connect MySQL form java.</a> |
|Improve LoadBalancer. Check wsdl for each request form Client. Client update Busy when uses one service and release it after usage. Seperate application run every half minutes to check whether services are active or not and update Status Table.|Some useful link for using mysql in java:<br> https://stackoverflow.com/questions/13973958/creating-a-login-form-with-java-connected-to-mysql <br> https://alvinalexander.com/java/java-mysql-select-query-example <br> https://stackoverflow.com/questions/1905607/cannot-issue-data-manipulation-statements-with-executequery||
||||







