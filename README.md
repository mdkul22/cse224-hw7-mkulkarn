# cse224-hw7-mkulkarn
# HW 7 
Read this paper about Akamai:

Erik Nygren, Ramesh K. Sitaraman, and Jennifer Sun. 2010. The Akamai network: a platform for high-performance internet applications. SIGOPS Oper. Syst. Rev. 44, 3 (August 2010), 2-19. DOI: https://doi.org/10.1145/1842733.1842736

What are some of the challenges to delivering content over the Internet?
Why isn’t a simple web server model sufficient to efficiently deliver content? (In other words, what need or gap does Akamai address?)
Briefly describe how Akamai enables distribution of live and streaming content?
What information does the Akamai CDN use to map requests to resources? How (briefly) does it implement that mapping?

# Overview
In HW5, you built a DropBox-like file service called SurfStore. In this project, 
you’re going to experiment with block placement policies and their impact on storage performance.
You're going to test two methods of storing blocks either in the random fashion or by finding the least
RTT server and storing it on that blockstore

# Experiments
On AWS, run a BlockStore in these datacenters:

Seoul, Korea
Dublin, Ireland
Sao Paulo, Brazil
Mumbai, India
On the US West (Oregon) datacenter, run your Metadata Store and your client. Do not run a BlockStore instance in the US West datacenter!

# Conclusions
Write 2-3 sentences on your conclusions. Does file size matter? 
How does the average download time using the hash algorithm compare to the average round trip time to the other data centers?
