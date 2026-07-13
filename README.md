# Cloud-Network-Security-Design                                                                                          Design and Implementation of an Automated Threat Detection and Response System in AWS


Cloud infrastructures are increasingly vulnerable to complex and rapidly evolving cyber threats, making automated security systems crucial for maintaining resilience and reducing incident response times. This project demonstrates the design and implementation of an automated threat detection and response system within an Amazon Web Services (AWS) environment. The seamless integration of three essential AWS
EventBridge then executes a custom Lambda function that provides quick remediation, including isolating the compromised EC2 instance by deleting its public IP, adding a quarantine security group, and flagging the resource for further investigation.
The speed and consistency of incident response are significantly enhanced by this automated approach, which also minimises human involvement. Supporting components, such as VPC Flow Logs, CloudTrail, Security Hub, and IAM policies, enable additional layers of monitoring, auditing, and compliance, thereby improving the overall security posture. The system serves as an example of how cloud-native services can be combined to build an autonomous, scalable, and adaptable defence system. The resulting architecture lays the groundwork for further predictive research and provides a viable solution for businesses seeking to enhance cloud security through automation.

1.	Introduction
 Cloud computing has quickly become a central part of how organisations build and deliver digital services, offering the ability to scale quickly and operate more efficiently than ever before. However, as businesses move more of their critical systems into the cloud, the security risks they face have also evolved. Cyberattacks are becoming more sophisticated, and even small misconfigurations can expose systems to serious threats. This growing complexity means that relying only on manual security processes is no longer enough to keep cloud environments safe.
This project explores how a secure cloud network can be designed in Amazon Web Services (AWS) and strengthened through automated threat detection and response. The aim is not just to build a secure network, but to show how AWS-native security tools can work together to respond to threats instantly and without human intervention. Using services such as Amazon GuardDuty, VPC Flow Logs, CloudTrail, and Security Hub for visibility, and integrating EventBridge with AWS Lambda for automation, the project demonstrates how cloud environments can actively defend themselves. This approach reflects a modern shift towards intelligent, self-healing security systems in the cloud.

1.1 Research Motivations
•	Increasing cloud adoption and expanding attack surfaces, which require organisations to deploy secure, resilient, and self-defending cloud infrastructures. 
•	The growing sophistication of cyberattacks, where misconfigurations, weak visibility, and slow response times remain leading causes of cloud compromises. 
•	The need for automated security operations, reducing reliance on manual processes by integrating threat detection, monitoring, and remediation within AWS-native services. 
•	The opportunity to demonstrate cloud-native tools such as GuardDuty, CloudTrail, VPC Flow Logs, and EventBridge can be orchestrated to form an autonomous incident-response workflow. 
•	The growing business requirement for intelligent defence mechanisms, enabling systems to isolate threats rapidly, minimise human intervention, and maintain operational continuity. 

1.2 Research Contributions
This project contributes to cloud security research by demonstrating how AWS-native services can be combined to create a secure, intelligent, and automated defence system. While secure cloud architectures are widely discussed, there is still a gap in practical implementations that integrate detection, monitoring, and automated response into a single, cohesive workflow. This project addresses that gap by showing how AWS tools can be orchestrated to improve visibility, reduce human dependency, and enhance real-time protection. The contributions of this work are summarised below as three key achievements:
• A secure multi-tier AWS network architecture using VPC segmentation, controlled access, and defence-in-depth principles.
• An integrated monitoring and threat-visibility layer using VPC Flow Logs, CloudTrail, GuardDuty, and Security Hub.
• An automated threat detection and response workflow using GuardDuty, EventBridge, and Lambda to isolate compromised EC2 instances in real time.
Together, these contributions show how cloud-native security features can be used not only to detect threats but also to respond automatically, reducing risk exposure and strengthening overall cloud resilience.

