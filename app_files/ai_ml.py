import numpy as np
from sklearn.cluster import KMeans

class Compress:
    def __init__(self, image):
        self.img = image.copy()
        self.h = image.shape[0]
        self.w = image.shape[1]
    
    def params(self, clusters):
        self.clusters = clusters
        self.seed = np.random.randint(1, 50)
        self.kmeans = KMeans(n_clusters = clusters, max_iter=300, init='k-means++', n_init='auto', random_state=self.seed)
    
    def preprocess(self):
        self.img = self.img.reshape(-1, 3)
    
    def get_output(self, blobs):
        self.preprocess()
        
        self.params(blobs)
        self.kmeans.fit(self.img)
        centroids = self.kmeans.cluster_centers_
        predictions = self.kmeans.predict(self.img)
        dummy_img = self.img
        for i in range(dummy_img.shape[0]):
            dummy_img[i] = centroids[int(predictions[i])]
        dummy_img = dummy_img.reshape(self.h, self.w, 3)
        return dummy_img