<!-- TOC
# Ray Introduction
## Quick intro
## 基础概念
## Examples Using Ray
## Others
-->

<!-- links are based on ray v2.3.1 -->

<!-- see this repo at https://github.com/gglin001/ray_intro -->

# Ray Introduction

> from GH:

Ray is a unified framework for scaling AI and Python applications. Ray consists of a core distributed runtime and a toolkit of libraries (Ray AIR) for simplifying ML compute:

[what-is-ray](imgs/what-is-ray-padded.svg)

https://github.com/ray-project/ray
https://www.ray.io/
https://docs.ray.io/en/latest/

Ray v2 Architecture
https://docs.google.com/document/d/1tBw9A4j62ruI5omIJbMxly-la5w4q_TjyJgJL_jN2fI/preview#

Ray AIR Technical Whitepaper
https://docs.google.com/document/d/1bYL-638GN6EeJ45dPuLiPImA8msojEDDKiBx3YzB4_s/preview

## Quick intro

https://github.com/ray-project/ray-educational-materials/blob/main/Introductory_modules/Overview-of-Ray.pdf

https://towardsdatascience.com/modern-parallel-and-distributed-python-a-quick-tutorial-on-ray-99f8d70369b8

## 基础概念

Tasks, Actors, Objects(ray-core)
https://docs.ray.io/en/latest/ray-core/key-concepts.html
Other misc
https://docs.ray.io/en/latest/ray-core/handling-dependencies.html
https://docs.ray.io/en/latest/ray-core/scheduling/resources.html
Design Patterns & Anti-patterns
https://docs.ray.io/en/latest/ray-core/patterns/index.html

Ray Cluster Key Concepts
https://docs.ray.io/en/latest/cluster/key-concepts.html
launching-clusters on-premises
https://docs.ray.io/en/latest/cluster/vms/user-guides/launching-clusters/on-premises.html

Ray AI Runtime (AIR)
https://docs.ray.io/en/latest/ray-air/getting-started.html

ML workloads with Ray(common usage of ray)
https://docs.ray.io/en/latest/ray-overview/use-cases.html

Ray dashboard(monitoring and debugging tools)
https://docs.ray.io/en/latest/ray-observability/overview.html

more materials at ray-educational-materials
https://github.com/ray-project/ray-educational-materials

## Examples Using Ray

Configuring Ray

https://docs.ray.io/en/latest/ray-core/configure.html

### a tiny python demo

[O1_tiny_demo](O1_tiny_demo.py)
[O2_actors](O2_actors.py)
[O3_data](O3_data.py)
[O4_serve](O4_serve.py)

### a demo using pytorch

[serve_torchvision](serve_torchvision.py)
[serve_transformers](serve_transformers.py)

### a demo on ipu

TODO

## Others

Spark, Dask, Ray
https://discuss.ray.io/t/what-is-the-difference-between-ray-and-spark/1578
https://c-nemri.medium.com/spark-dask-ray-choose-the-right-distributed-computing-framework-6b766e177728
https://www.datarevenue.com/en-blog/pandas-vs-dask-vs-vaex-vs-modin-vs-rapids-vs-ray
https://docs.ray.io/en/latest/data/integrations.html
https://github.com/ray-project/ray/issues/642

see also "Ray v2 Architecture" & "Ray AIR Technical Whitepaper"

ray-serve and TFServing like tools
https://docs.ray.io/en/latest/serve/index.html

ray also support c++/java/etc

## Q&A

> 对于 `O1_tiny_demo.py`, ray 会自动的将 操作拆分并分布到多个 node 中运行吗?

no, ray 不会自动的做并行处理.
由于 X.remote() 函数是异步的, 一些 job 可以通过并行化的方式(多个 subjob 放到多个 node 上)来提高效率.
比如这里的例子: https://docs.ray.io/en/latest/ray-core/examples/highly_parallel.html

> ray 的优点/为什么选择 ray?

也许需要对类似的工具做一些比较(实践)才能说明, 以及这些 link 作为参考

https://www.anyscale.com/blog/why-you-should-build-your-ai-applications-with-ray

TODO: add more links

> ray 如何与 其他并行方法的结合使用

一个例子 [alpa](https://github.com/alpa-projects/alpa) + Ray

https://www.anyscale.com/blog/training-175b-parameter-language-models-at-1000-gpu-scale-with-alpa-and-ray
