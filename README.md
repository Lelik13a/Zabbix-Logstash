# Description
Check Logstash 7.x status and LLD pipelines.  
Check JVM memory.  
Check pipelines events.

It is assumed that the Logstash is listening on a localhost 9600 port.

# Dependencies
python, curl, zabbix-agent.

Installation
============
1. copy logstash_pipelines_lld.py to /etc/zabbix/
2. copy zabbix_agentd.d/logstash.conf to /etc/zabbix/zabbix_agentd.d/
3. chmod 755 /etc/zabbix/logstash_pipelines_lld.py
4. if needed, change in logstash.conf and logstash_pipelines_lld.py host and port.
5. restart zabbix-agent daemon.
6. import "zbx_templates/Template Logstash.xml" into your templates.
7. apply template "Template Logstash" to Logstash node.
9. enjoy.


PS
===========
You can easily change the settings for monitoring a remote Logstash node.

