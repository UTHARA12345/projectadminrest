from rest_framework import serializers
from .models import EmployerTask

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = EmployerTask
		fields ='__all__'