# Understanding Array Indexes, Memory Addresses, and Base Addresses

## Question

While learning arrays, I had a doubt.

Arrays normally take `0` as their first index.

Suppose:

```text
myArray = [1, 3, 5]
```

and it starts at some memory address.

Now let's say there is another array:

```text
newArray = [10, 20, 30]
```

which also has index `0`.

If both arrays have a `0th` index, how does the computer know which memory address to access when I write:

```python
myArray[0]
```

or

```python
newArray[0]
```

How does the system differentiate between them?

Please explain with a real-world analogy.

---

# Answer

This is actually a very good question.

The key idea is:

> The index alone is NEVER enough.
>
> The computer always uses:
>
> **Array Base Address + Index**

---

## Real-World Analogy: Streets and House Numbers

Imagine two streets:

```text
Apple Street
House 0
House 1
House 2
```

and

```text
Orange Street
House 0
House 1
House 2
```

If someone tells you:

```text
Go to House 0
```

you would immediately ask:

```text
Which street?
```

because both streets have a House 0.

Similarly, arrays can both have index 0.

The index is not enough by itself.

The computer also needs to know which array is being referenced.

---

## Arrays in Memory

Suppose:

```python
myArray = [1, 3, 5]
newArray = [10, 20, 30]
```

In memory, they may look like:

```text
myArray

Address 1000 -> 1
Address 1004 -> 3
Address 1008 -> 5
```

```text
newArray

Address 5000 -> 10
Address 5004 -> 20
Address 5008 -> 30
```

Notice:

```text
Both arrays have:
Index 0
Index 1
Index 2
```

but their memory locations are completely different.

---

## What Does the Array Variable Store?

This is the most important concept.

The variable:

```python
myArray
```

does not store all the elements.

Instead, it stores the **base address** (the address of the first element).

For example:

```text
myArray = 1000
newArray = 5000
```

These are the starting points of the arrays.

---

## How Array Access Works

When you write:

```python
myArray[2]
```

the CPU calculates:

```text
Address = Base Address + (Index × Element Size)
```

For integers that occupy 4 bytes:

```text
1000 + (2 × 4)
```

```text
= 1008
```

At address 1008, the value is:

```text
5
```

So:

```python
myArray[2] == 5
```

---

For:

```python
newArray[2]
```

the CPU calculates:

```text
5000 + (2 × 4)
```

```text
= 5008
```

At address 5008:

```text
30
```

So:

```python
newArray[2] == 30
```

---

## Why Do Array Indexes Start at 0?

Because the address calculation becomes simpler.

For the first element:

```text
Address = Base Address + (0 × Size)
```

```text
Address = Base Address
```

No extra adjustments are required.

This makes memory access efficient.

---

## Another Real-World Analogy: Hotels

Imagine:

### Hotel A

```text
Room 0
Room 1
Room 2
```

### Hotel B

```text
Room 0
Room 1
Room 2
```

If someone says:

```text
Go to Room 2
```

you would ask:

```text
Which hotel?
```

The hotel identifies the location.

The room number identifies the room inside that location.

Similarly:

```python
array[2]
```

means:

```text
(Base Address of Array) + Room Number
```

The array variable tells the computer which hotel.

The index tells it which room.

---

## Why Array Access Is O(1)

When accessing:

```python
arr[i]
```

the CPU directly computes:

```text
Base Address + (i × Element Size)
```

It does not need to search through the array.

Therefore:

```text
Time Complexity = O(1)
```

---

## Practice Question

Suppose an integer array starts at address:

```text
2000
```

and each integer occupies:

```text
4 bytes
```

What address will contain:

```python
arr[5]
```

### Solution

```text
Address = Base Address + (Index × Element Size)
```

```text
Address = 2000 + (5 × 4)
```

```text
Address = 2020
```

Therefore:

```python
arr[5]
```

is stored at:

```text
Address 2020
```
