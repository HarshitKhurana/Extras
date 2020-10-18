
### [\*] Un-Supervised Learning Algos

**1. K-Means Clustering:**
  * In this the model tries to classify the objects into fixed number of pre-defined groups such that the objects ar as much similar as possible within the group, but as much dissimilar in different groups.
  * **K** = number of clusters.
  * Steps:
    1. Decide K, i.e number of clusters.
    2. Provide centroid of 3 clusters (random but far from each other covering entire sample space)
    3. The algo will calculate the euclidean distance of point from centroid and assign point to closest cluster.
    4. Next, the centroids are re-calculated(by taking mean of euclidean distance from all points) as we have added new point
    5. Step 4 is repeated untill the position of centrod no longer changes.
  * **Elbow Method**: It is used to find the optimum K value for particular dataset. 
    * Compute SSE (sum of squared error) i.e sum of squared distance b/w each point of the cluster and it's centroid.
    * As K increases SSE decreases, pick the value of K at which the SSe saturates.
  * Eg: Application - Image compression, object detection

