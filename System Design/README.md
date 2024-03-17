

1. Understand the functional and non-functional requirements before designing.
- Before starting the design, it's essential to understand what the system needs to do (functional requirements, like features and operations) and how it should perform (non-functional requirements, like performance, reliability, and usability). For instance, designing an e-commerce website involves functional requirements such as displaying products and processing payments, and non-functional requirements like loading time under 3 seconds and 99.9% uptime.

### Functional Requirements:

Functional requirements describe what the system should do. They define specific behaviors or functions. For an e-commerce website, these include:

Product Display: Showing products with images, prices, and descriptions.
Search and Filter: Allowing users to search for products and apply filters based on category, price, brand, etc.
Shopping Cart: Enabling users to add and remove products from a shopping cart.
Checkout Process: Processing payments, applying discounts, calculating taxes, and capturing shipping information.
User Account Management: Allowing users to register, log in, manage their profiles, view order history, and track current orders.
Product Reviews and Ratings: Enabling users to rate products and write reviews.

### Non-Functional Requirements:

Non-functional requirements, on the other hand, describe how the system performs a particular function. They are crucial for the system's reliability, efficiency, and overall user satisfaction. For the same e-commerce website, non-functional requirements might include:

Performance: Ensuring the website loads quickly (e.g., in under 3 seconds) to prevent user drop-off.
Scalability: Being able to handle increases in traffic, especially during peak shopping times, without degradation of performance.
Availability and Reliability: Achieving high uptime (e.g., 99.9%) to ensure the website is always accessible to users. This might involve using redundant systems and failover mechanisms.
Security: Protecting sensitive user information, such as credit card details and personal information, against breaches and ensuring compliance with data protection regulations (e.g., GDPR).
Usability: Designing an intuitive and easy-to-navigate user interface that works well on both desktop and mobile devices.
Maintainability: Ensuring that the website can be easily updated or modified without significant downtime or bugs

2. Clearly define the use cases and constraints of the system.
- Identifying the specific scenarios in which the system will be used (use cases) and its limitations (constraints like technology, budget, and regulatory compliance) helps in tailoring the design appropriately. For example, a mobile payment app's use cases include transferring money and paying bills, with constraints like secure transactions and regulatory compliance.

3. There is no perfect solution. It’s all about tradeoffs.
- Every design decision involves trade-offs in terms of cost, performance, scalability, etc. Choosing the right database might mean balancing between consistency and availability. For example, using a SQL database ensures consistency but might limit scalability compared to NoSQL databases.

4. Assume requirements will change and design the system to be flexible.
- Systems should be designed with modularity and flexibility to accommodate future changes in requirements without significant rework. Using microservices architecture can allow for easier updates and adding new features without affecting the entire system.

5. Assume everything can and will fail. Make it fault tolerant.
-  Designing with redundancy, failover mechanisms, and graceful degradation in mind ensures the system remains operational even when components fail. For example, replicating databases across different geographical locations can prevent downtime if one location experiences an outage.

6. Don't add functionality until it's necessary. Avoid over-engineering.
- Implement features as they become necessary rather than anticipating future needs which might not materialize. This approach, known as YAGNI (You Aren’t Gonna Need It), saves resources and simplifies the system.
7. Design your system for scalability from the ground up.
- Consider how the system can handle growth in users, data volume, and transaction frequency. Scalability can be built into the system through techniques like caching, load balancing, and microservices.

### Caching
Caching involves storing copies of data in temporary storage locations (caches) for quick access upon future requests. This reduces the number of direct access requests to the primary data storage, thereby reducing load and improving response times.

Example: An e-commerce platform might cache popular products' details on a front-end server. When a customer requests the details of a popular product, the system retrieves the information from the cache rather than the database, significantly speeding up the response time.
Techniques
In-memory Caches: Tools like Redis or Memcached store data in RAM, offering extremely fast data retrieval.
Content Delivery Networks (CDNs): These are geographically distributed networks of proxy servers that deliver content more rapidly to users based on their geographic location.
Database Caching: Some systems cache query results so that identical future requests can be served directly from the cache.

### Load Balancing
Load balancing distributes incoming network traffic across multiple servers to ensure no single server bears too much demand. By spreading the load, the system can serve more requests simultaneously, enhancing the overall capacity and reliability of the system.

Example: A video streaming service uses a load balancer to distribute user requests to watch videos across a pool of servers, ensuring that no single server is overwhelmed, which could potentially degrade the quality of video streaming for users.
Techniques
Round Robin: Distributing requests sequentially across a group of servers.
Least Connections: Directing new requests to the server with the fewest active connections.
IP Hashing: Assigning users to specific servers based on their IP address, ensuring a user always connects to the same server.

### Microservices
Microservices architecture breaks down a system into a collection of smaller, independent services that perform specific functions. This modular structure allows for easier scaling of individual components as needed, rather than scaling the entire application.

Example: A social media platform uses microservices for different functionalities such as posting updates, messaging, and notifications. As the platform grows, each service can be scaled independently. For instance, if the messaging feature sees a surge in usage, only the messaging service needs to be scaled up without affecting other parts of the system.
Benefits
Flexibility in Scaling: Services can be scaled independently based on demand.
Improved Fault Isolation: Issues in one service do not necessarily impact others.
Technology Diversity: Each microservice can be built using the best technology stack for its specific requirements.

8. Prefer horizontal scaling over vertical scaling for scalability.
- Horizontal scaling (adding more machines) is generally more flexible and cost-effective than vertical scaling (upgrading to more powerful machines). It allows for on-demand scaling without major disruptions.
9. Add Load Balancers to ensure high availability and distribute traffic.
- Load balancers distribute incoming traffic across multiple servers to prevent any single server from becoming a bottleneck, improving performance and availability. For instance, a load balancer can route user requests to the least busy server in a web application cluster.
10.  Consider using SQL Databases for structured data and ACID transactions.
- SQL databases are ideal for scenarios requiring structured data storage, complex queries, and transactions that follow ACID properties (Atomicity, Consistency, Isolation, Durability). An example would be an online banking system that requires transaction integrity.
11.  Opt for NoSQL Databases when dealing with unstructured data.
- NoSQL databases like MongoDB or Cassandra are suitable for unstructured or semi-structured data, offering flexibility, scalability, and high performance. They're often used in big data applications and real-time web apps.
12.  Use Database Sharding to scale SQL databases horizontally.
- Sharding involves dividing a database into smaller, more manageable pieces called shards, distributed across multiple servers. This can significantly improve performance and scalability for large databases.
13.  Use Database Indexing and search engines for efficient data retrievals.
- Indexes speed up data retrieval without scanning the entire database. Search engines like Elasticsearch can provide fast, scalable search capabilities for large datasets.
14.  Use Rate Limiting to prevent system overload and DOS attacks.
15.  Use WebSockets for real-time communication.
16.  Employ Heartbeat Mechanisms for failure detection.
17.  Consider using a message queue for asynchronous communication.
18. Implement data partitioning and sharding for large datasets.
11. Consider denormalizing databases for read-heavy workloads.
12. Consider using event-driven architecture for decoupled systems.
13. Use CDNs to reduce latency for a global user base.
14. Use write-through cache for write-heavy applications.
15. Use read-through cache for read-heavy applications.
16. Use blob/object storage for storing media files like files, videos etc..
17. Implement Data Replication and Redundancy to avoid single point of failure.
18. Implement Autoscaling to handle traffic spikes smoothly.
19. Use Asynchronous processing to run background tasks.
20. Make operations idempotent where possible to simplify retry logic and error handling.
21. When appropriate, use microservices for flexibility, scalability, and maintainability.
22. Consider using a data lake or data warehouse for analytics and reporting.


a. How I would learn System Design (If I could start over)

1. Harvard Scalability lecture: https://lnkd.in/gCE5-2Uy

2. CAP theorem: https://lnkd.in/gBK3Yr-k

3. Load Balancing: https://lnkd.in/gKmiBGMY

4. SQL vs NoSQL: https://lnkd.in/gTwWGgRW

5. Database Sharding: https://lnkd.in/gge-HFki

6. Caching: https://lnkd.in/gcEenvvY

7. What is a CDN: https://lnkd.in/g2v99kw4

8. 10 popular System Design problems: https://lnkd.in/gtw7H378

9. Grokking the System Design Interview (Paid): https://lnkd.in/g3i2Jzsd

10. Designing Data-Intensive Applications: https://lnkd.in/ghVWhgAb


b. If I had to start learning System Design from scratch, I would begin with these 25 articles to get a head start:

1) Scalability: https://lnkd.in/gx-sPXZm

2) Horizontal vs Vertical Scaling: https://lnkd.in/gAH2e9du

3) Latency vs Throughput: https://lnkd.in/g_amhAtN

4) Load Balancing: https://lnkd.in/gQaa8sXK

5) Caching: https://lnkd.in/gC9piQbJ

6) ACID Transactions: https://lnkd.in/gMe2JqaF

7) SQL vs NoSQL: https://lnkd.in/g3WC_yxn

8) Database Indexes: https://lnkd.in/gCeshYVt

9) Database Sharding: https://lnkd.in/gMqqc6x9

10) Content Delivery Network (CDN): https://lnkd.in/gjJrEJeH

11) Strong vs Eventual Consistency: https://lnkd.in/gJ-uXQXZ

12) Batch Processing vs Stream Processing: https://lnkd.in/g4_MzM4s

13) Concurrency vs Parallelism: https://lnkd.in/gSKUm2Nh

14) Synchronous vs. asynchronous communications: https://lnkd.in/gC3F2nvr

15) Rest vs RPC: https://lnkd.in/gN__zcAB

16) CAP Theorem: https://lnkd.in/g3hmVamx

17) Reverse Proxy: https://lnkd.in/gFwWFDu8

18) Domain Name System (DNS): https://lnkd.in/gkMcZW8V

19) Rate Limiting: https://lnkd.in/gWsTDR3m

20) Redundancy and Replication: https://lnkd.in/gvwQGEiP

21) Fault Tolerance: https://lnkd.in/dVJ6n3wA

22) Failover: https://lnkd.in/dihZ-cEG

23) WebSockets: https://lnkd.in/g76Gv2KQ

24) Microservices Architecture: https://lnkd.in/gFXUrz_T

25) API Design: https://lnkd.in/ghYzrr8q

c. SD Github Repo for revision:

https://github.com/karanpratapsingh/system-design#what-is-system-design