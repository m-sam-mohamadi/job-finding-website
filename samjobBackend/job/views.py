from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,authentication,permissions

from .forms import JobForm
from .models import Job,Category
from .serializer import JobSerializer,JobDetailSerializer,CategSerializer


class NewJobsView(APIView):
    def get(self,request,format=None):
        jobs = Job.objects.all()[0:4]
        serializer = JobSerializer(jobs,many=True)
        return Response(serializer.data)
    
class MyJobsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]
        
    def get(self,request,format=None):
        if request.user.is_authenticated:
            jobs = Job.objects.filter(created_by=request.user)
            serializer = JobSerializer(jobs,many=True)
            return Response(serializer.data)
        else: 
            return Response(None)
class CreateJobView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]
    def post(self,request):
        form = JobForm(request.data)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            
            return Response({'status':'created'})
        else:
            return Response({'status':'errors','errors':form.errors})
    def delete(self,request,pk):
        job = Job.objects.get(pk=pk,created_by=request.user)
        job.delete()
        return Response({'status':'deleted'})
    def put(self,request,pk):
        job = Job.objects.get(pk=pk,created_by=request.user)
        form = JobForm(request.data,instance=job)
        form.save()
        return Response({'status':'updated'})
        
        
        
class BrowseJobsView(APIView):
    def get(self,request,format=None):
        jobs = Job.objects.all() 
        categories = request.GET.get('categories','')
        query = request.GET.get('query','')
        if query:
            jobs = jobs.filter(title__icontains=query)
        if categories:
            jobs = jobs.filter(category_id__in=categories.split(','))
        serializer = JobSerializer(jobs,many=True)
        return Response(serializer.data)
    
class JobsDetailView(APIView):
    def get(self,request,pk,format=None):
        jobs = Job.objects.get(pk=pk)
        serializer = JobDetailSerializer(jobs )
        return Response(serializer.data)

class CategoryView(APIView):
    def get(self,request,format=None):
        cat = Category.objects.all()
        serializer = CategSerializer(cat,many=True)
        return Response(serializer.data) 