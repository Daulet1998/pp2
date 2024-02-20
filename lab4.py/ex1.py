#Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.
'''Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 '''

import json 
f1 = open('sample.json', 'r') 
f2 = open('output_json.txt', 'w') 
 
Dict = json.loads(f1.read()) 
 
f2.write('Interface Status\n') 
f2.write('================================================================================\n') 
f2.write('DN                                                 Description           Speed    MTU\n') 
f2.write('-------------------------------------------------- --------------------  ------  ------\n') 
 
cnt = 1 
 
for i in Dict['imdata']: 
    if cnt == 4: 
        break 
    f2.write(json.dumps(i["l1PhysIf"]["attributes"]["dn"])) 
    f2.write('                            ') 
    f2.write(json.dumps(i["l1PhysIf"]["attributes"]["speed"])) 
    f2.write(' ') 
    f2.write(json.dumps(i["l1PhysIf"]["attributes"]["mtu"])) 
    f2.write('\n') 
    cnt+=1