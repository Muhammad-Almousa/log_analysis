# Log-Analysis-Project

In this project, I stretched my SQL database skills. I practiced interacting with a live database both from the command line and from my code.
I explored a large database with over a million rows, and I built and refined complex queries and used them to draw business conclusions from data.


## What is the Out output of this project?

After running this project, it will answer these three questions:

### 1. What are the most popular three articles of all time?

### 2. Who are the most popular article authors of all time?

### 3. On which days did more than 1% of requests lead to errors?


## What is inside my `log_analysis` file?
* 1 - A function to connect the database.
* 2 - Three queries to answer the required questions.
* 3 - Functions to save and print out the result of the queries. 




## Instructions on how to run it:
* <h4>Install <a href="https://www.vagrantup.com/">Vagrant</a> and <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox.</a></h4>
* <h4>Clone the repository to your local machine</h4>
  <pre> git clone https://github.com/Muhammad-Almousa/log_analysis.git</pre>
* <h4>Start the virtual machine</h4>
  From your terminal, inside the project directory, run the command  `vagrant up` . This will cause Vagrant to download the Linux      
  operating   system and install it.
  When vagrant up is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your  
  newly installed Linux VM!
* <h4>Download the <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">data</a></h4>
  You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant     
  directory, which is shared with your virtual machine.
* <h4>Setup Database</h4>
  To load the database use the following command:
  <pre>psql -d news -f newsdata.sql;</pre>
* <h4>Make Views</h4>
  Make views by running respective queries on command line or uncomment code written in python module.
* <h4>Run Module</h4>
  <pre>python log.py</pre>
