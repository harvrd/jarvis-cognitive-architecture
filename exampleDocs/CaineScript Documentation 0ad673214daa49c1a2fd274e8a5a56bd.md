# CaineScript Documentation

# Introduction

Hello! CaineScript is a programming language that makes creating experiences in augmented reality simple and fun.

This documentation describes all of the available functions and listeners in CaineScript, as well as example games and a Hello World. If you have any questions, please reach out to Caine!

# Getting Started

## Hello World in CaineScript

There are a few fundamental concepts in CaineScript:

1. `Listener` A set of built-in listeners like `onCollision`, `onButtonPress`, `onStart`, and `forever`, that can take in 0 or several parameters.
2. `Function` A set of built-in utilities that allow you to interact with your game. These include `PlaySound`, `Rotate`, `Move`, and many more.
3. `Variable` A variable allows you to create state in your CaineScript. For example, you can declare `numCollisions = 0` and increment `numCollisions` every time a player collides with a coin.

With that in mind, the first step in a HelloWorld program is to use an `onStart` listener to be ran right when your experience starts. To actually write to the console, we’ll use the `Write` function:

```fortran
onStart {
	Write('Hello World');
}
```

## More examples of CaineScript

`HelloWorld` is a great starting point, but what more is CaineScript capable of? View the [examples page](https://www.notion.so/Example-Games-ad26722a76d5443aaa63dffe275ff1fb) to see examples of what CaineScript can do. 

## CaineScript Basic Conventions

If you’re coming from other programming languages, you may be wondering how CaineScript compares.

Similar to Python, Javascript, and other high level languages, both single and double quotes are acceptable. This means that the following code runs as expected

```jsx
Write('Hello');
Write("World");
```

# Listener Reference

## forever

Runs every frame

**Example Code**

```
forever {}
```

---

## onStart

Runs on start

**Example Code**

```
onStart {}
```

---

## onCollision

Runs when two objects collide

**Example Code**

```
onCollision<"obj1", "obj2"> {}
```

---

## onButtonPress

Runs when a button is pressed

**Example Code**

```
onButtonPress<"button1"> {}
```

---

## if-statements

Runs when a button is pressed

**Example Code**

```
onStart {
	numCollisions = 0;
}
forever {
	if (TimeSinceStart() > 5) && (numCollisions >== 2) {
		Disappear("box1");
	}
}
```

# Manual

## Creating game objects

There are many functions to create an object in CaineScript:

[Create](CaineScript%20Documentation%200ad673214daa49c1a2fd274e8a5a56bd.md) 

[CreateCollection](CaineScript%20Documentation%200ad673214daa49c1a2fd274e8a5a56bd.md) 

In creating a game object, you have several parameters, including the type, color, size, position, and source.

1. `Source` can be `built-in`, `primitive`, or `prefab`
    1. If you select built-in, your type must be button
    2. If you select prefab, your type must be one of the prefabs in the `Assets/Resources` (e.g. `LunarModule` or `GoldCoin`)
    3. If you select primitive, you must select `sphere` or `cube` as your type
2. `Color`
3. `Size`
4. `Position`
5. `Type` is determined by `Source` and is of type `resource-name`

**Examples**

```fortran
Create('my_id', 'cube', '1,0.5,1', '0,0,0', '0,0,0', 'primitive');
```

## Error Handling in CaineScript

**Example 1**

```csharp
forever {
	Move('cube1', 'slow', [1,2.0,3]);
	ASDFMove('cube2', 'slow', [1,2.0,3]);
	Move('cube2', 'slow', [1,2.0,3]);
} 
forever {
	Move('lunar1', 'slow', [1.0,2.0,3.0]);
}
```

This will only move the lunar module

**Example 2**

```jsx
asdfMove('cube1', 'slow', [1,2,3]);
onStart {
	PlaySound('bg_piano');
}
```

This will not run the sound

**Example 3**

```jsx
onStart {
	asdfMove('cube1', 'slow', [1,2,3]);
}
onStart {
	PlaySound('bg_piano');
}
```

This will run the sound

So errors that you get will kill that thread of code. On the backend, each of the event handlers  creates a new “IEnumerator,” which is basically a separate thread of code that runs apart from the main thread. 

# Type Reference

[Untitled](CaineScript%20Documentation%200ad673214daa49c1a2fd274e8a5a56bd/Untitled%20Database%20c069cbf5d144464891b67d6d68a083a7.csv)

# Function Reference

## PlaySound

Plays a sound clip

**Arguments**

[Untitled](CaineScript%20Documentation%200ad673214daa49c1a2fd274e8a5a56bd/Untitled%20Database%203703f14ffb694a9a8cff9fda6fa2bc97.csv)

**Example Code**

```
PlaySound("bg_piano");
```

---

## Create

Creates a game object

[Untitled](CaineScript%20Documentation%200ad673214daa49c1a2fd274e8a5a56bd/Untitled%20Database%20379151f7558c456689b50437696433e9.csv)

**Example Code**

```fortran
Create('unique_id_1', 'cube', [0.1,.3,1], [2,2,2], [3,3,3], 'primitive')
```

---

## ChangeColor

Changes the color

[Untitled](CaineScript%20Documentation%200ad673214daa49c1a2fd274e8a5a56bd/Untitled%20Database%208f1c36f246aa4e79936ac4e438fe3418.csv)

**Example Code**

```fortran
ChangeColor('unique_id_1', [1,0.5,1])
```

---

## Write

Writes to the console

**Example Code**

```fortran
Write("Hello World!", "It's CaineScript")
```

---

## TimeSinceStart

Gets the time in seconds since the game started as a `float`

**Example Code**

```fortran
TimeSinceStart()
```

---

## Disappear

Makes the game object disappear

[Untitled](CaineScript%20Documentation%200ad673214daa49c1a2fd274e8a5a56bd/Untitled%20Database%204013566a4cf74b16855fd0d329ae20d1.csv)

**Example Code**

```fortran
Disappear('unique_id_1')
```

---

## Pass

It does nothing

**Example Code**

```fortran
Pass()
```

---

## Move

Moves the game object in `direction` at `speed`

[Untitled](CaineScript%20Documentation%200ad673214daa49c1a2fd274e8a5a56bd/Untitled%20Database%202324add06aaf43f2bafb5f8a9d8a2e57.csv)

**Example Code**

```fortran
forever {
	Move('cube2', 'slow',  GetPosition('Player') - GetPosition('cube2'));
}
```

---

## MoveTo

Moves the game object to `position`

[Untitled](CaineScript%20Documentation%200ad673214daa49c1a2fd274e8a5a56bd/Untitled%20Database%20365f8f2253c54ff9a1cf6bd63796c42a.csv)

**Example Code**

```fortran
MoveTo('cube2',  GetPosition('Player') + [1, 0, 0]);
```

---

## Rotate

Rotates a game object by n degrees every second

[Untitled](CaineScript%20Documentation%200ad673214daa49c1a2fd274e8a5a56bd/Untitled%20Database%20e97a45913fdc4eaa8f787305c98ff33b.csv)

**Example Code**

```fortran
forever {	
	Rotate('lunar1', 0, 10, 10);
}
```

---

## GetPosition

Gets the position of a game object and returns a float vector

[Untitled](CaineScript%20Documentation%200ad673214daa49c1a2fd274e8a5a56bd/Untitled%20Database%200992a6e7ac5d415eb528ca4481236cd1.csv)

**Example Code**

```fortran
GetPosition('Player') - GetPosition('cube2')
```

---

## CreateCollection

Creates a set of game objects

[Untitled](CaineScript%20Documentation%200ad673214daa49c1a2fd274e8a5a56bd/Untitled%20Database%201d4e506e82824e849f953eb2c67f7b9c.csv)

**Example Code**

```fortran
CreateCollection('unique_id_1', 7, 'cube', '1,0.5,1', '1,1,1', [0,0,0], 'primitive')
```