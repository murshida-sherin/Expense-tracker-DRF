from django.shortcuts import render
from ExpenseApp.serializer import UserSerializer,ExpenseSerializer
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from ExpenseApp.models import Expense
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.
class CreateUserView(CreateAPIView):
    serializer_class=UserSerializer
    
    def perform_create(self, serializer):
        return User.objects.create_user(**serializer.validated_data)

class CreateListView(CreateAPIView,ListAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ExpenseSerializer
    
    def perform_create(self, serializer):
        user=self.request.user
        return serializer.save(owner=user)
    
    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)
    
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    
    filterset_fields=['payment','category']
    search_fields=['title']
    ordering_fields=['amount','created_at']
   
    
class UpdateRetrieveDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ExpenseSerializer
    
    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)
        
    