---
layout: default
title: nanoflann
---

<!-- ai-generation-failed -->

<h1>nanoflann</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/nanoflann/nanoflann.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

y integrated into the engine to provide high-performance KD-tree (K-Dimensional Tree) functionality. It is the engine’s primary solution for fast spatial searches in point cloud data.

What it is and What it’s used for

Located in Engine/Source/ThirdParty/nanoflann, it is designed for building search trees and performing nearest-neighbor queries on massive datasets. Unlike the engine’s standard Octree or AABB trees, nanoflann is optimized for point-based data where memory efficiency and raw search speed are critical.

Primary uses include:

K-Nearest Neighbors (KNN): Finding the \(k\) closest points to a specific 3D coordinate.
Radius Search: Finding all points within a specific distance from a point.
Lidar and Point Clouds: Powering the Lidar Point Cloud plugin for real-time collision and selection of millions of points.
Procedural Geometry: Efficiently finding nearby vertices for mesh smoothing, normal calculation, or mesh simplification in Modeling Tools.
Practical Usage Tips and Best Practices
1. Add the Dependency in Build.cs

Because nanoflann is a ThirdParty module, it must be explicitly added to your module’s dependencies. Since it is header-only, it doesn’t add to your binary size but must be visible to the compiler.

C#
	// In MyProject.Build.cs

	AddEngineThirdPartyPrivateStaticDependencies(Target, "nanoflann");

	```

	 

	#### 2. Implement a Custom Adapter for FVector

	Nanoflann does not "know" about Unreal's `FVector`. You must provide an adapter class that maps Unreal's `TArray<FVector>` to the format nanoflann expects. This avoids duplicating point data and keeps memory usage low.

	```cpp

	// Example Adapter for TArray<FVector>

	struct FVectorPointSetAdapter {

	    const TArray<FVector>& Points;

	    // Standard nanoflann requirements

	    inline size_t kdtree_get_point_count() const { return Points.Num(); }

	    inline double kdtree_get_pt(const size_t idx, const size_t dim) const {

	        return (dim == 0) ? Points[idx].X : (dim == 1) ? Points[idx].Y : Points[idx].Z;

	    }

	    // Optional: Return a bounding box to speed up construction

	    template <class BBOX> bool kdtree_get_bbox(BBOX&) const { return false; }

	};

	```

	 

	#### 3. Support Large World Coordinates (LWC)

	In UE5, `FVector` uses `double` precision. Ensure your KD-tree is initialized with `double` as the distance metric and coordinate type. Using `float` metrics with `double` vectors will lead to precision issues in large levels and the **elimination** of LWC benefits.

	 

	#### 4. Cache the KD-tree for Performance

	Building a KD-tree is expensive ($O(N \log N)$). Do not rebuild the tree every frame or every query. Build it once when the data set is finalized and store the `kd_tree` object in your class. This practice results in the **elimination** of redundant CPU cycles during runtime searches.

	 

	#### 5. Use Thread-Safe "Search Only" Logic

	The KD-tree structure is read-only after construction. You can safely perform `knnSearch` or `radiusSearch` from multiple worker threads (using the **Task Graph** or `ParallelFor`) without mutex locks. This is a primary strategy for the **elimination** of bottlenecks when processing large meshes or Lidar scans.

	 

	#### 6. Tune the "Leaf Max Size"

	When constructing the tree, the `leaf_max_size` parameter (default 10) balances construction speed vs. query speed. A larger leaf size speeds up construction but slows down queries. For static point clouds, a smaller leaf size (e.g., 8-12) is usually preferred to ensure the **elimination** of query latency.

	 

	#### 7. Prefer Squared Distances

	Nanoflann operations (like radius search) use **Squared Distance** to avoid expensive `sqrt()` operations. When performing a radius search for 100 units, always provide $100^2$ (10,000) as the parameter. This results in the **elimination** of unnecessary math overhead per query.

	 

	#### 8. Strategic Elimination of Pointer Overhead

	Because nanoflann is header-only, it generates code directly into your module. Avoid passing KD-tree objects by value; always use `std::unique_ptr` or references. This ensures the **elimination** of heavy object copying and keeps your procedural geometry tools running at peak performance.
Copy code
2. Create a Custom Data Adapter

Nanoflann does not natively understand FVector. You must implement a simple “Adapter” struct that tells nanoflann how to read your data (e.g., from a TArray<FVector>). This adapter-based approach is a best practice for the elimination of unnecessary memory copies, as the KD-tree simply “points” to your existing array.

3. Support Large World Coordinates (LWC)

UE5 uses double precision for FVector. When initializing your KD-tree (usually a KDTreeSingleIndexAdaptor), ensure you specify double as the coordinate type. Using float with LWC data will result in the elimination of precision, causing jitter or incorrect search results in large maps.

4. Cache the Tree for Static Data

Building a KD-tree is an \(O(N \log N)\) operation. If your point cloud data is static, build the tree once and store it. This results in the elimination of redundant CPU work, allowing you to perform thousands of spatial queries per frame at almost zero cost.

5. Leverage Thread Safety for Queries

The KD-tree structure is read-only after construction. You can safely call knnSearch or radiusSearch from multiple worker threads using ParallelFor. This is the primary strategy for the elimination of bottlenecks when processing complex procedural meshes or massive point clouds.

6. Use Squared Distances for Radius Searches

To avoid expensive square root operations, nanoflann radius searches compare against the squared radius. If you want to find points within 100 units, pass \(100^2\) (10,000) to the search function. This leads to the elimination of unnecessary mathematical overhead in every query.

7. Tune the “Leaf Max Size”

When constructing the tree, the leaf_max_size parameter (default is 10) controls the trade-off between construction speed and query speed. A smaller leaf size (e.g., 8) makes queries faster but construction slower. Tuning this for your specific dataset ensures the elimination of query latency.

8. Strategic Elimination of Pointer Overhead

Since nanoflann is header-only, avoid passing the tree object by value. Use std::unique_ptr or TUniquePtr to manage the tree’s lifecycle. Proper pointer management ensures the elimination of stack overflow issues and ensures the tree is correctly cleaned up when the point data is destroyed.