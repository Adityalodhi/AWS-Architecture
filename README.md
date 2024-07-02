#AWS High Availability, Secure, and Scalable Deployment Architecture

Introduction

To learn the core functionality of AWS, I have created a project showcasing a deployment model which is reliable, secure, and scalable. This project demonstrates the following AWS services and features:

    Auto Scaling Group
    Application Load Balancer
    Private Subnets
    NAT Gateway
    Bastion Host

# Diagram


# Viedo 
working Project Video

# Architecture Overview

The architecture is designed to ensure high availability, security, and scalability using the following components:

1. High Availability: Servers are deployed across two Availability Zones using an Auto Scaling group. This setup ensures that even if one zone goes down, services remain available.

2. Load Balancing: An Application Load Balancer (ALB) distributes incoming requests to the servers efficiently, improving performance and ensuring no single server is overwhelmed.
3. Enhanced Security: Servers are deployed in private subnets, adding an extra layer of security by not exposing them directly to the internet.
4. Internet Access via NAT Gateway: Servers can connect to the internet for updates and external API calls using a NAT gateway. The NAT gateway is deployed in both Availability Zones for high availability.
5. Scalability: The Auto Scaling group automatically adjusts the number of running instances based on demand, allowing seamless handling of traffic spikes and maintaining optimal performance.
Secure Access via Bastion Host: A Bastion Host is deployed in the public subnet, providing secure administrative access to servers in private subnets.


# Prerequisites

    An AWS account
    AWS CLI configured
    Basic knowledge of AWS services



# Steps to Create the Architecture
1. Set Up VPC and Subnets

    a.Create a VPC with a CIDR block (e.g., 10.0.0.0/16).

    b.Create two public subnets (one in each Availability Zone).

    c.Create two private subnets (one in each Availability Zone).

2. Set Up Internet Gateway and NAT Gateway

Attach an Internet Gateway to the VPC.

Create NAT Gateways in each public subnet.


3. Set Up Route Tables

    a.Create a route table for the public subnets and add a route to the Internet Gateway.

    b.Create a route table for the private subnets and add a route to the NAT Gateway.

4. Set Up Security Groups

    a.Create a security group for the ALB allowing inbound traffic on port 80 (HTTP) and 443 (HTTPS).

    b.Create a security group for the EC2 instances allowing inbound traffic from the ALB security group.

    c.Create a security group for the Bastion Host allowing SSH access from your IP address.
5. Launch EC2 Instances

    a.Launch EC2 instances in the private subnets using the Auto Scaling group.

    b.Ensure the instances are associated with the appropriate security group.

6. Set Up Application Load Balancer

    a.Create an Application Load Balancer in the public subnets.
    b.Configure the ALB to forward traffic to the EC2 instances in the private subnets.
7. Set Up Auto Scaling Group

    a.Create a launch configuration or launch template for the EC2 instances.

    b.Create an Auto Scaling group and specify the private subnets.
    
    c.Attach the ALB to the Auto Scaling group.
8. Set Up Bastion Host

    a.Launch an EC2 instance in a public subnet to act as a Bastion Host.

    b.Associate the Bastion Host with the security group allowing SSH access from your IP address.



# Conclusion
This project demonstrates a highly available, secure, and scalable architecture using AWS services. It has been a fantastic learning experience and a testament to my commitment to mastering cloud architecture and best practices.

