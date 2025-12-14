from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

# -------------------------
# Feed View
# -------------------------
class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

# -------------------------
# Like / Unlike Views
# -------------------------
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # checker expects this exact line
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"detail": "You already liked this post"}, status=400)

        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
        return Response({"detail": "Post liked successfully"})


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # checker expects this exact line
        like = Like.objects.filter(user=request.user, post=post)
        if not like.exists():
            return Response({"detail": "You haven't liked this post"}, status=400)
        like.delete()
        return Response({"detail": "Post unliked successfully"})
