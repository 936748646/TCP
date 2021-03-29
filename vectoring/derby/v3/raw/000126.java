/*

   Derby - Class org.apache.derbyTesting.functionTests.tests.derbynet.maxthreads

   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

 */
package org.apache.derbyTesting.functionTests.tests.derbynet;

import java.sql.*;
import java.util.Vector;
import java.util.Properties;
import java.io.File;
import java.io.FileOutputStream;
import java.io.BufferedOutputStream;

import org.apache.derby.iapi.reference.Property;
import org.apache.derby.drda.NetworkServerControl;
import org.apache.derbyTesting.functionTests.harness.jvm;
import org.apache.derbyTesting.functionTests.util.TestUtil;
import org.apache.derbyTesting.functionTests.util.ExecProcUtil;
import org.apache.derby.tools.ij;

/**
	This tests the maxthreads command
*/

public class maxthreads
{
	private static Properties properties = new java.util.Properties();
	private static jvm jvm;
	private static Vector vCmd;
	private static String[] maxthreadsCmd1 = new String[] {"org.apache.derby.drda.NetworkServerControl",
		"maxthreads", "0"};
	private static String[] maxthreadsCmd2 = new String[] {"org.apache.derby.drda.NetworkServerControl",
		"maxthreads","-1", "-h", "localhost", "-p", "1527"};
	private static String[] maxthreadsCmd3 = new String[] {"org.apache.derby.drda.NetworkServerControl",
		"maxthreads", "-12"};
	private static String[] maxthreadsCmd4 = new String[] {"org.apache.derby.drda.NetworkServerControl",
		"maxthreads", "2147483647"};
	private static String[] maxthreadsCmd5 = new String[] {"org.apache.derby.drda.NetworkServerControl",
		"maxthreads", "9000"};
	private static String[] maxthreadsCmd6 = new String[] {"org.apache.derby.drda.NetworkServerControl",
			"maxthreads", "a"};
    private static  BufferedOutputStream bos = null;
	private static  NetworkServerControl server;
	private static String host;
	private static int port = 1527;
   
	private static void checkMaxThreads( int value)
		throws Exception
	{
		int maxValue = server.getMaxThreads();
		if (maxValue == value)
			System.out.println("PASS - max threads value, "+ value +" is correct");
		else
			System.out.println("FAIL - max threads value is " + maxValue + " should be "
				+ value);
	}


	public static void main (String args[]) throws Exception
	{
		host = TestUtil.getHostName();
		maxthreadsCmd2[4] = host;
		
		if ((System.getProperty("java.vm.name") != null) && System.getProperty("java.vm.name").equals("J9"))
			jvm = jvm.getJvm("j9_13");
		else
			jvm = jvm.getJvm("currentjvm");		// ensure compatibility
		vCmd = jvm.getCommandLine();
		try
		{
			ij.getPropertyArg(args); 
			Connection conn1 = ij.startJBMS();

        	bos = new BufferedOutputStream(System.out, 1024);

			server = new NetworkServerControl();
			/************************************************************
			 *  Test max threads
			 ************************************************************/
			System.out.println("Testing maxthreads");
			//test maxthreads 0
			ExecProcUtil.execCmdDumpResults(maxthreadsCmd1,vCmd,bos);	
			checkMaxThreads(0);
			//test maxthreads -1 
			ExecProcUtil.execCmdDumpResults(maxthreadsCmd2,vCmd,bos);	
			checkMaxThreads(0);	//default is currently 0
			//test maxthreads -12 - should error
			ExecProcUtil.execCmdDumpResults(maxthreadsCmd3,vCmd,bos);	
			checkMaxThreads(0);
			//test maxthreads 2147483647 - should work
			ExecProcUtil.execCmdDumpResults(maxthreadsCmd4,vCmd,bos);	
			checkMaxThreads(2147483647);
			//test maxthreads 9000 - should work
			ExecProcUtil.execCmdDumpResults(maxthreadsCmd5,vCmd,bos);	
			checkMaxThreads(9000);
			//test maxthreads with invalid value (NumberFormatException)
			ExecProcUtil.execCmdDumpResults(maxthreadsCmd6,vCmd,bos);	
			// try the same values using the callable interface
			//test maxthreads 0
			server.setMaxThreads(0);
			checkMaxThreads(0);
			//test maxthreads -1 
			server.setMaxThreads(-1);
			checkMaxThreads(0);
			//test maxthreads -2 - should error
			try {
				server.setMaxThreads(-2);
			} catch (Exception e) {
				System.out.println (e.getMessage());
			}
			//test maxthreads 2147483647 - should work
			server.setMaxThreads(2147483647);
			checkMaxThreads(2147483647);
			//test maxthreads 9000 - should work
			server.setMaxThreads(9000);
			checkMaxThreads(9000);
			System.out.println("End test");
			bos.close();
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
	}
}
