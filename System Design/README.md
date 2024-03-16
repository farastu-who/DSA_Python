1. Understand the functional and non-functional requirements before designing.
2. Clearly define the use cases and constraints of the system.
3. There is no perfect solution. It’s all about tradeoffs.
4. Assume requirements will change and design the system to be flexible.
5. Assume everything can and will fail. Make it fault tolerant.
6. Don't add functionality until it's necessary. Avoid over-engineering.
7. Design your system for scalability from the ground up.
8. Prefer horizontal scaling over vertical scaling for scalability.
9. Add Load Balancers to ensure high availability and distribute traffic.
10. Consider using SQL Databases for structured data and ACID transactions.
11. Opt for NoSQL Databases when dealing with unstructured data.
12. Use Database Sharding to scale SQL databases horizontally.
13. Use Database Indexing and search engines for efficient data retrievals.
14. Use Rate Limiting to prevent system overload and DOS attacks.
15. Use WebSockets for real-time communication.
16. Employ Heartbeat Mechanisms for failure detection.
17. Consider using a message queue for asynchronous communication.
18. Implement data partitioning and sharding for large datasets.
19. Consider denormalizing databases for read-heavy workloads.
20. Consider using event-driven architecture for decoupled systems.
21. Use CDNs to reduce latency for a global user base.
22. Use write-through cache for write-heavy applications.
23. Use read-through cache for read-heavy applications.
24. Use blob/object storage for storing media files like files, videos etc..
25. Implement Data Replication and Redundancy to avoid single point of failure.
26. Implement Autoscaling to handle traffic spikes smoothly.
27. Use Asynchronous processing to run background tasks.
28. Make operations idempotent where possible to simplify retry logic and error handling.
29. When appropriate, use microservices for flexibility, scalability, and maintainability.
30. Consider using a data lake or data warehouse for analytics and reporting.
