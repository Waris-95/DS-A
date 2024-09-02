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

### 🤔 When to Use a Stack?
- Ensuring that a system completes tasks in a specific order (e.g., function calls, parsing expressions).
- Reversing operations or data (e.g., reversing strings).
- Implementing **Undo/Redo** functionality (e.g., in text editors or applications).