from ..models import Post
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
#from skimage import io

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    # print(args)
    #resp = urllib.urlopen(Post.objects.image_url)
    # image = np.asarray(bytearray(resp.read()), dtype="uint8")
    # image = cv2.imdecode(image, cv2.IMREAD_COLOR)

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def create(self, request, *args, **kwargs):
        super(PostCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        # Create image from image_url
        # print(args)
        # resp = urllib.urlopen(args)
    	# image = np.asarray(bytearray(resp.read()), dtype="uint8")
    	# image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        return Response(response)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def retrieve(self, request, *args, **kwargs):
        super(PostDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(PostDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(PostDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)
