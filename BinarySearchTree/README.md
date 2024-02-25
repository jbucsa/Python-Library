[![LinkedIn][linkedin-shield]][linkedin-url-Bucsa]

# PPP-Create-a-BST

## Description

When creating a BST, we are going to follow a similar process. We will first create a BSTNode class, and then we will create our BST class using BSTNodes. However, there are some key differences. Let's review the structure of a linked list and of a BST.

A linked list can be thought of as looking like this:

![Image description](img/HeadToTailsLinks.png style="max-height: 70px;" )

Each box is a node, and each node has two parts: the data, and the "next", or pointer to the next node.

On the other hand, a BST may look like this:

![Image description](img/BTSDataTree.png style="max-height: 70px;" )

There are two key differences here between a linked list and a BST. First, each node of a BST has up to two children, not just one. Because there can never be more than two children, we often denote them as "left" and "right", rather than "next".

The second key difference has to do with the order in which elements are stored in a BST. To simplify our understanding, we will only deal with numerical data in this activity, but the same principle applies to any type of data.

In a BST, the data is kept "balanced" by enforcing certain rules.

If the tree is empty (root points to None), put the new node at the top of the tree
If the tree is not empty, start at the root. Compare the new node's value to the current node's value. If the new node is bigger, move to the right. If the new node's value is smaller, move to the left. When there is no node at the current position, put the new node there.


[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url-Bucsa]: https://www.linkedin.com/in/justin-bucsa