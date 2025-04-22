Commands to run the Project

1. git clone https://github.com/anilramasita/cloud-native-monitoring-k8s.git
2. pip install -r requirements.txt

To Run locally in our system
3. python app.py

To Make Our Project as Docker Container
4. docker build -t <image_name> .
5. docker run -p 5000:5000 <image_name>

Run ecr.py to create ecr repository or create the ecr repo in aws console directly
6. python ecr.py

Run eks.py with changing the image uri
7. python eks.py

8. kubectl get deployment -n default (check deployments)
9. kubectl get service -n default (check service)
10. kubectl get pods -n default (to check the pods)

Once your pod is up and running, run the port-forward to expose the service

11. kubectl port-forward service/<service_name> 5000:5000 (service name from 9th command)
