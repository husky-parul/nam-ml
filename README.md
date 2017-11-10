Problem description: 

With the advent of PCI and HIPAA, all organisations are logging network activities. These log files are growing within the organisation but very little is done about the valuable information contained in these logs. Most of the times, it is only when an organisation realises that the network has been compromised that these logs are analysed. Given the gargantuan size of these log files it is very difficult to narrow down relevant information when a security incident occur. Although there are numerous log analysing tool and SIEM solutions, but there are based on deterministic and constant rules. What is needed is a self evolving engine that would narrow the quantity of information for the SOC team of organisations or Security Analyst. 

The idea is to introduce machine learning to mine relevant information from ocean of log files and enable organisations to make informed decisions. What we are trying to achieve is classify potential malicious activities logged in the network. This would not only reduce tiresome hours spent by human resources but also help organisation to speed up their mitigation and response when a breach has occurred.

Nevertheless a learning algorithm would need massive dataset. The input to the algorithm is pre-processed datasets from firewall and network logs. The source of data is DShield API from SANS[1]. An example is as below
<data>
<ip>183.060.048.025</ip>
<attacks>54045</attacks>
<count>650544</count>
<firstseen>2015-10-08</firstseen>
<lastseen>2017-03-14</lastseen>
</data>

IP: IP address of the attacker
attacks: targets/number of unique destination IP addresses for these packets
Count: total number of packets blocked from this IP
Firstseen: date of first logged attack
lastSeen: date of last logged attack


Algorithms: 
The classification algorithm that we would be using is Support Vector Machines. This algorithm seems most appropriate because it efficiently separates non-linear groups when the features are numeric. The essence of our learning algorithm is based on the property called Internet Bad Neighbourhood, inspired from PhD Thesis paper by Moura called "Internet Bad Neighborhoods"[2]. It implies that if a machine is engaged in a specific (in our case malicious), it is very likely that it’s neighbors will also be engaged in similar activities given the nature of topology of the internet. SVM is a discriminative classifier formally defined by a separating hyperplane. Given labeled training data (supervised learning), the algorithm outputs an optimal hyperplane which categorizes new examples[3]. To use SVM in our project, first we gather cluster of events based on their behavior, like blocked attempts on ports. Then we assign a rank to these data based on how recent they have been noticed. Then we will group them using Bad Behavior property. Obviously we need to have some benign data for cross validating. Once the training data is constructed and the model is trained we use SVM to classify new samples. It would predict if a certain IP would be malicious or not.

References
[1]DShield API - SANS Internet Storm Center - https://isc.sans.edu/api/
[2]Internet Bad Neighborhoods – G. Moura http://www.utwente.nl/en/archive/2013/03/bad_neighbourhoods_on_the_inte rnet_are_a_real_nuisance.doc
[3]SVM-http://docs.opencv.org/2.4/doc/tutorials/ml/introduction_to_svm/introduction_to_svm.html
[4]Implementing paper - https://www.defcon.org/images/defcon-21/dc-21-presentations/Pinto/DEFCON-21-Pinto-Defending-Networks-Machine-Learning-WP-Updated.pdf
