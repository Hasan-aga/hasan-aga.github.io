---
layout: post
title: Comparing procedural and functional java
date: 2024-07-28
category: [programming]
---

<img src="/assets/2024-07-28-comparing-procedural-and-functional-java/code.jpg" alt="code.jpg"/>

I was watching a Youtube video [about how java is good for everything](https://youtu.be/2fopl7-2wT0?si=-t59AO_ct9pKenbi) when in the video a code snippet was reviewd. The code was a simple algorithm called "FizzBuzz" but the implementation in java used the beautiful functional stream API:

```java
public static String fizzBuzz(int[] arr) {
    var preds = new HashMap<Predicate<Integer>, String>();
    preds.put(x -> x % 3 == 0, "Fizz");
    preds.put(x -> x % 5 == 0, "Buzz");
    return Arrays.stream(arr)
            .mapToObj(x -> preds.entrySet().stream()
                    .filter(entry -> entry.getKey().test(x))
                    .map(Map.Entry::getValue)
                    .reduce(String::concat)
                    .orElse(String.valueOf(x)))
            .collect(Collectors.joining("\n"));
}
```

As you can see the code is very concise and if you are familiar with the functional programming concepts you can easily understand the code. I wanted to implement the same code using procedural programming and I ended up with this:

```java
public static String proceduralFizzBuzz(int[] arr) {
    List<String> result = new ArrayList<>();
    for (var x : arr) {
        StringBuilder sb = new StringBuilder();
        if (x % 3 == 0) {
            sb.append("Fizz");
        }
        if (x % 5 == 0) {
            sb.append("Buzz");
        }
        if (sb.isEmpty()) {
            sb.append(x);
        }
        result.add(sb.toString());
    }
    return String.join("\n", result);
}
```

This code is a bit more verbose and is littered with if statements but it is It is more readable. The problem with this code is that it goes against some "good practices", for example, we have multiple if statements and the function is rather large. But the story is not over, I decided to benchmark both functions so I quickly did some research and found that the standard way to benchmark java code is to use the JMH library, here is my benchmark code:

```java
@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Benchmark)
@Fork(value = 1, warmups = 1)
@Warmup(iterations = 1, time = 1)
@Measurement(iterations = 3, time = 1)
public class FizzBuzzBenchmark {
    @Param({"1000", "10000", "100000"})
    private int length;

    int[] data;

    @Setup
    public void setup() {
        data = new int[length];
        for (int i = 0; i < length; i++) {
            data[i] = i;
        }
    }

    @Benchmark
    public void functionalFizzBuzz() {
        FizzBuzz.fizzBuzz(data);
    }

    @Benchmark
    public void proceduralFizzBuzz() {
        FizzBuzz.proceduralFizzBuzz(data);
    }

    public static void main(String[] args) throws RunnerException {
        Options opt = new OptionsBuilder()
                .include(FizzBuzzBenchmark.class.getSimpleName())
                .build();

        new Runner(opt).run();
    }
}

```

## The result

The results were these:

```
Benchmark                                      (length)  Mode  Cnt   Score    Error  Units
fizzBuzz.FizzBuzzBenchmark.functionalFizzBuzz      1000  avgt    3   0.283 ±  1.034  ms/op
fizzBuzz.FizzBuzzBenchmark.functionalFizzBuzz     10000  avgt    3   2.974 ±  5.636  ms/op
fizzBuzz.FizzBuzzBenchmark.functionalFizzBuzz    100000  avgt    3  46.900 ± 42.673  ms/op

fizzBuzz.FizzBuzzBenchmark.proceduralFizzBuzz      1000  avgt    3   0.073 ±  0.119  ms/op
fizzBuzz.FizzBuzzBenchmark.proceduralFizzBuzz     10000  avgt    3   0.815 ±  0.705  ms/op
fizzBuzz.FizzBuzzBenchmark.proceduralFizzBuzz    100000  avgt    3   9.903 ±  5.446  ms/op
```

As you can see, the cleaner, smaller functional code is much slower than the procedural code (almost 5 times slower)!! This was not surprising to me and it reminded me of a demo made on youtube: ["Clean" Code, Horrible Performance](https://youtu.be/tD5NrevFtbU?si=miRTsfxfUsHI1voC)
The reason why clean code is slower than procedural is because clean code prioritizes readability and maintainability. Clean code is meant for humans, CPUs don't care about that, procedural code is faster because it is arranged in a way to suits the CPU.
