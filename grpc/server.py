from concurrent import futures
import grpc
import firebase_admin
from firebase_admin import credentials, firestore
import equipment_pb2
import equipment_pb2_grpc


# Inisialisasi Firebase
cred = credentials.Certificate("C:/Users/USER/Documents/PEI/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

class EquipmentService(equipment_pb2_grpc.EquipmentServiceServicer):
    def CreateEquipment(self, request, context):
        data = {
            "name": request.name,
            "type": request.type,
            "quantity": request.quantity,
        }
        doc_ref = db.collection("equipment").document(request.name)
        doc_ref.set(data)
        return request
    

    def ReadEquipment(self, request, context):
        doc_ref = db.collection("equipment").document(request.name)
        doc = doc_ref.get()
        if doc.exists:
            data = doc.to_dict()
            return equipment_pb2.Equipment(name=data["name"], type=data["type"], quantity=data["quantity"])
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Equipment not found")
            return equipment_pb2.Equipment()

    def UpdateEquipment(self, request, context):
        data = {
            "name": request.name,
            "type": request.type,
            "quantity": request.quantity,
        }
        doc_ref = db.collection("equipment").document(request.name)
        doc_ref.set(data)
        return request

    def DeleteEquipment(self, request, context):
        doc_ref = db.collection("equipment").document(request.name)
        doc_ref.delete()
        return request

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    equipment_pb2_grpc.add_EquipmentServiceServicer_to_server(EquipmentService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
    