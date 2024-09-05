# 🌟 Data Structures and Algorithms 🌟

## 📚 What is a Data Structure?

A **data structure** is a way to organize and store data efficiently, enabling effective access and modification. 

### 🗂️ Examples of Common Data Structures:
- **Arrays**
- **Hash Tables**
- **Hash Sets**
- **Linked Lists**

## 🔍 What is an Algorithm?

An **algorithm** is a step-by-step procedure or formula for solving a problem. Algorithms interact with data structures to perform various operations, like searching, sorting, or modifying data.

---

## 📦 Arrays

Arrays are used to organize collections of values. They come in two main types:

- **Static Arrays**: A true array with a fixed size, defined at creation.
- **Dynamic Arrays**: Arrays that can change in size, allowing more flexibility in data storage.

### Array Operations
| Operation                    | Time Complexity | Description                                                                 |
|------------------------------|-----------------|-----------------------------------------------------------------------------|
| **Read/Write ith element**   | O(1)            | Direct access to any element by index.                                      |
| **Insert/Remove at End**     | O(1)            | Efficient insertion or removal at the end of the array.                     |
| **Insert at Middle/Beginning** | O(n)            | Involves shifting elements due to reassignment of indices.                  |
| **Remove at Middle/Beginning** | O(n)            | Involves shifting elements due to reassignment of indices.                  |

### 📚 Stacks
- **Definition**: Stacks are **Last-In-First-Out (LIFO)** data structures.
- **Efficiency**: Arrays are highly efficient when implemented as stacks.
- **Practical Example**: Check out the [Baseball Game Problem](https://leetcode.com/problems/baseball-game/description/) for a stack-based solution!

## 🤔 When to Use a Stack?

- **Ensuring Order of Operations:** 
  Used when tasks must be completed in a specific order, such as function calls or parsing expressions.
  
- **Reversing Data:** 
  Useful for operations that require reversing, like reversing strings or lists.

- **Undo/Redo Functionality:** 
  Commonly used in applications (e.g., text editors) to implement **Undo/Redo** functionalities.

## 🤔 When to Use a Queue?
- **First-In-First-Out (FIFO) Processing:**
  Ideal for scenarios where the first element added needs to be the first processed.
  
  - **Task Scheduling:**  
    Managing tasks in an order where the first task added should be the first executed (e.g., print queues, process scheduling in operating systems).
  
  - **Breadth-First Search (BFS):**  
    Used to explore nodes in a graph level by level.
  
  - **Real-Time Systems:**  
    Handling events or messages in the order they occur, such as incoming network requests or event handling in games or user interfaces.